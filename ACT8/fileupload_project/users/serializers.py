from rest_framework import serializers
from .models import CustomUser
from django.core.files.base import ContentFile
from PIL import Image
from io import BytesIO

class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('username', 'password', 'photo')
        extra_kwargs = {'password': {'write_only': True}}

    def validate_photo(self, value):
        if value is None:
            raise serializers.ValidationError("No file was uploaded.")

        # ✅ Size check
        if value.size > 2 * 1024 * 1024:
            raise serializers.ValidationError("Image size should not exceed 2MB.")

        # ✅ Format check
        valid_types = ['image/jpeg', 'image/png', 'image/webp']
        if value.content_type not in valid_types:
            raise serializers.ValidationError("Only JPEG, PNG, and WebP images are allowed.")

        return value

    def create(self, validated_data):
        photo = validated_data.get('photo')

        if photo:
            image = Image.open(photo)
            width, height = image.size

            # ✅ Crop image to 1:1 aspect ratio (center crop)
            min_dim = min(width, height)
            left = (width - min_dim) // 2
            top = (height - min_dim) // 2
            right = left + min_dim
            bottom = top + min_dim
            cropped_image = image.crop((left, top, right, bottom))

            # Save to buffer and convert back to file
            buffer = BytesIO()
            cropped_image.save(buffer, format=image.format)
            buffer.seek(0)
            validated_data['photo'] = ContentFile(buffer.read(), name=photo.name)

        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            photo=validated_data.get('photo')
        )
        return user
