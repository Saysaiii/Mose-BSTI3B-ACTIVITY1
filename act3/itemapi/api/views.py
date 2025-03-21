from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
import json
from .models import Item

# Get all items or search items
def get_items(request):
    search_query = request.GET.get('search')
    if search_query:
        items = Item.objects.filter(name__icontains=search_query)
    else:
        items = Item.objects.all()

    data = [{"id": item.id, "name": item.name, "description": item.description} for item in items]
    return JsonResponse(data, safe=False)

# Get a single item by ID
def get_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    data = {"id": item.id, "name": item.name, "description": item.description}
    return JsonResponse(data)

# Add a new item (POST request)
@csrf_exempt
def add_item(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            item = Item.objects.create(name=data['name'], description=data.get('description', ''))
            return JsonResponse({"message": "Item added successfully", "id": item.id}, status=201)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

# Update an existing item (PUT request)
@csrf_exempt
def update_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    if request.method == "PUT":
        try:
            data = json.loads(request.body)
            item.name = data.get('name', item.name)
            item.description = data.get('description', item.description)
            item.save()
            return JsonResponse({"message": "Item updated successfully"})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

# Delete an item (DELETE request)
@csrf_exempt
def delete_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    if request.method == "DELETE":
        item.delete()
        return JsonResponse({"message": "Item deleted successfully"})
