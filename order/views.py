from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.utils import timezone

from store.models import Product
from order.models import Cart, Order, Wish, OrderUpdate

# Create your views here.
def add_to_wish(request, pk):
    if request.user.is_authenticated:
        item = get_object_or_404(Product, pk=pk)
        wish_item = Wish.objects.get_or_create(item=item, user=request.user)
        return redirect('store:index')
    else:
        return redirect('account:login')

def wish_view(request):
    if request.user.is_authenticated:
        wish_list = Wish.objects.filter(user=request.user)
        if wish_list.exists():
            context = {
                'wish_list':wish_list
            }
            return render(request, 'store/wishlist.html', context)
        else:
            return redirect('store:index')
    else:
        return redirect('account:login')