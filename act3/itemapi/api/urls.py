from django.urls import path
from .views import get_items, get_item, add_item, update_item, delete_item

urlpatterns = [
    path('items/', get_items, name='get_items'),
    path('items/<int:item_id>/', get_item, name='get_item'),
    path('items/add/', add_item, name='add_item'),
    path('items/update/<int:item_id>/', update_item, name='update_item'),
    path('items/delete/<int:item_id>/', delete_item, name='delete_item'),
]
