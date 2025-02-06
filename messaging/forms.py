from django import forms

from .models import Conversation, ConversationMessage

class ConversationForm(forms.ModelForm):
    class Meta:
        model = Conversation
        fields = ['sender', 'reciever', 'product']

class ConversationMessageForm(forms.ModelForm):
    class Meta:
        model = ConversationMessage
        fields = ['message']
        widgets = {
            'message': forms.TextInput(attrs={
                'class': 'w-full h-10 rounded-full border-black/30 bg-white',
                'placeholder': 'Write Your Message',
                # 'id': 'message',
                # 'name': 'message',
            })
        }