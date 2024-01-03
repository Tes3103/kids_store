from django.contrib import admin
from .models import WishItem, WishitemProduct

# Register your models here.
admin.site.register(WishItem)
admin.site.register(WishitemProduct)