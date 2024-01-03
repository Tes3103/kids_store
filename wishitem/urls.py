from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_wishlist, name='wishlist'),
    path('add_to_wishitem/<int:item_id>', views.add_to_wishitem, name='add_to_wishitem'),
    path('remove_from_wishitem/<int:item_id>', views.remove_from_wishitem, name='remove_from_wishitem'),
]