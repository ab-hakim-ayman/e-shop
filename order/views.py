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
    
def remove_item_from_wish(request, pk):
    item = get_object_or_404(Product, pk=pk)
    wish_list = Wish.objects.filter(user=request.user, item=item)
    if wish_list.exists():
        wish_list.delete()
        return redirect('order:wish')
    
def add_to_cart(request, pk):
    if request.user.is_authenticated:
        item = get_object_or_404(Product, pk=pk)
        order_item = Cart.objects.get_or_create(item=item, user=request.user, purchased=False)
        order_qs = Order.objects.filter(user=request.user, ordered=False)
        if order_qs.exists():
            order = order_qs[0]
            if order.orderitems.filter(item=item).exists():
                size = request.POST.get('size')
                color = request.POST.get('color')
                quantity = request.POST.get('quantity')
                if quantity:
                    order_item[0].quantity += int(quantity)
                else:
                    order_item[0].quantity += 1
                order_item[0].size = size
                order_item[0].color = color
                order_item[0].save()
                message = f"Quantity updated"
                # SendNotification(request.user, message)
                return redirect('store:index')
            else:
                size = request.POST.get('size')
                color = request.POST.get('color')
                quantity = request.POST.get('quantity')
                order_item[0].size = size
                order_item[0].color = color
                if quantity:
                    order_item[0].quantity = int(quantity)
                else:
                    order_item[0].quantity = 1
                order_item[0].save()
                order.orderitems.add(order_item[0])
                order.save()
                return redirect('store:index')
        else:
            order = Order(user=request.user)
            order.save()
            order.orderitems.add(order_item[0])
            message = f"Product added to your cart"
            # SendNotification(request.user, message)
            return redirect('store:index')
    else:
        return redirect('account:login')