from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from products.models import Product
from .models import WishItem


@login_required
def view_wishlist(request):
    '''
    A view to return to the wishitem list
    '''
    wishitem = None
    try:
        wishitem = WishItem.objects.get(user=request.user)
    except WishItem.DoesNotExist:
        pass

    context = {
        'wishitem': wishitem,
    }

    return render(request, 'wishitem.html', context)


@login_required
def add_to_wishitem(request, item_id):
    '''
    Add an item to the wishitem list
    '''
    product = get_object_or_404(Product, pk=item_id)
    redirect_url = request.POST.get('redirect_url')

    wish, _ = Wishlist.objects.get_or_create(user=request.user)

    wish.products.add(product)
    messages.info(request, f'{product.name} was added to your wishitem list')

    return redirect(redirect_url)


@login_required
def remove_from_wishitem(request, item_id):
    '''
    Removes the item from the wishitem list
    '''
    wish = Wishlist.objects.get(user=request.user)
    product = get_object_or_404(Product, pk=item_id)

    # Remove wish from the wishlist
    wish.products.remove(product)
    messages.info(request, f'{product.name} was removed from your wishitem list')

    return redirect(reverse('wishitem'))