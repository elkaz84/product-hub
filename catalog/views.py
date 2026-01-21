from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Product, Review
from .forms import ReviewForm

def product_list(request):
    products = Product.objects.all()
    return render(request, 'catalog/product_list.html', {'products': products})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    reviews = product.reviews.all().order_by('-created_at')
    
    if request.method == 'POST':
        if not request.user.is_authenticated:
            messages.error(request, "You must be logged in to post a review.")
            return redirect('login')
            
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.user = request.user
            review.save()
            messages.success(request, "Your review has been posted!")
            return redirect('product_detail', pk=product.pk)
    else:
        form = ReviewForm()
        
    return render(request, 'catalog/product_detail.html', {
        'product': product,
        'reviews': reviews,
        'form': form
    })

@login_required
def edit_review(request, pk):
    # I fetch the review and ensure only the owner can edit it
    review = get_object_or_404(Review, pk=pk, user=request.user)
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            messages.success(request, "Review updated successfully!")
            return redirect('product_detail', pk=review.product.pk)
    else:
        form = ReviewForm(instance=review)
    return render(request, 'catalog/edit_review.html', {'form': form, 'review': review})

@login_required
def delete_review(request, pk):
    # I fetch the review and ensure only the owner can delete it
    review = get_object_or_404(Review, pk=pk, user=request.user)
    product_pk = review.product.pk
    review.delete()
    messages.success(request, "Review deleted successfully!")
    return redirect('product_detail', pk=product_pk)

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful. Welcome!")
            return redirect('product_list')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})