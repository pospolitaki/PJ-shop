from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.db.models import Prefetch

from shopping_cart.models import Order, OrderItem
from .models import Profile

@login_required()
def my_profile(request):
	if request.user.is_authenticated:
		my_user_profile = Profile.objects.filter(user=request.user).first()
		# my_orders = Order.objects.prefetch_related('items').filter(is_ordered=True, owner=my_user_profile)
		my_orders = Order.objects.prefetch_related(Prefetch('items', queryset=OrderItem.objects.select_related('product'))).filter(is_ordered=True, owner=my_user_profile)
		
		context = {
			'my_orders': my_orders
		}

		return render(request, "accounts/profile.html", context)
	else:
		return redirect(reverse('landing:home'))