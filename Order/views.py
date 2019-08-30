from django.shortcuts import render
from Cart.cart import Cart
from .forms import OrderCreateForm
from .models import OrderItem


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form  = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,food=item['food'],
                                        price=item['price'],quantity=item['quantity'])
            cart.clear()
            return render(request, 'Order/create_done.html', {'order':order})
    else:
        form = OrderCreateForm()

    return render(request, 'Order/create.html', {'cart':cart, 'form':form})
