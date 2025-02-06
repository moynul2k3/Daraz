from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from mainapp.models import Category

from product.models import Product
from messaging.models import Conversation, ConversationMessage
from messaging.forms import ConversationMessageForm

# Create your views here.
# global variables................
categories = Category.objects.all()
context = {
    'categories': categories,
}


@login_required
def manage_ac(request):
    return render(request, 'pages/manage_account.html', context)

@login_required
def my_profile(request):
    return render(request, 'pages/my_profile.html', context)

@login_required
def inbox(request, pk):
    categories = Category.objects.all()
    sender=request.user
    conversations = Conversation.objects.filter(sender=request.user)
    if pk>0:
        this_conversation = Conversation.objects.get(id=pk)
    else:
        this_conversation = Conversation.objects.none()
    messages = ConversationMessage.objects.filter(conversation_id=pk)
    form = ConversationMessageForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save(commit=False) 
            form.instance.conversation=get_object_or_404(Conversation, pk=pk)
            form.instance.created_by=request.user
            form.save()
            return redirect('.')
    else:
        form = ConversationMessageForm()
        
    context={
        'categories': categories,
        'form': form,
        'messages': messages,
        'pk': pk,
        'sender': sender,
        'conversations': conversations,
        'this_conversation': this_conversation,
    }
    return render(request, 'pages/inbox.html', context)

@login_required
def address_book(request):
    return render(request, 'pages/address_book.html', context)

@login_required
def payment_options(request):
    return render(request, 'pages/my_payment_options.html', context)

@login_required
def wallet(request):
    return render(request, 'pages/daraz_wallet.html', context)

@login_required
def vouchers(request):
    return render(request, 'pages/vouchers.html', context)

@login_required
def my_orders(request):
    return render(request, 'pages/my_orders.html', context)

@login_required
def my_returns(request):
    return render(request, 'pages/my_returns.html', context)

@login_required
def my_cancellations(request):
    return render(request, 'pages/my_cancellations.html', context)

@login_required
def my_reviews(request):
    return render(request, 'pages/my_reviews.html', context)

@login_required
def wishlist(request):
    return render(request, 'pages/wishlist.html', context)

