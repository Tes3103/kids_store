from django.shortcuts import render

# Create your views here.

def view_wishitem(request):
    """ A view that renders the wishitem contents page """

    return render(request, 'wishitem/wishitem.html')