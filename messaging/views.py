from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from product.models import Product
from .models import Conversation, ConversationMessage
from .forms import ConversationMessageForm
# Create your views here.
def new_conversation(request, pk, sender, reciever):
    conversations = Conversation.objects.filter(sender=request.user)
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
        'form': form,
        'messages': messages,
        'sender': sender,
        'reciever': reciever,
        'conversations': conversations,
    }
    return render(request, 'pages/inbox.html', context)