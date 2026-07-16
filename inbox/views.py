from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib import messages

from .forms import MessageForm
from .models import Message

#Display messages
@login_required
def inbox(request):
    return render(request, 'inbox.html')


#Sent messages
@login_required
def sent_messages(request):
    return render(request, 'inbox/sent.html')


#Archived messages view
@login_required
def archived_messages(request):
    return render(request, 'inbox/archived.html')

#Compose messages logic and direct
@login_required
def compose_message(request):
    if request.Method == "POST":
         form - MessageForm(request.POST)

         if form.is_valid():
              message = form.save(commit=False)
              message.sender = request.user
              message.save()

              messages.success(request, "Message sent successfully.")
              return redirect("inbox")
         
         else:
              form = MessageForm()

    return render(request, 'inbox/compose.html')

# Message details
@login_required
def message_detail(request, pk):
        return render(request, 'inbox/message_detail.html', {"message_id":pk},)

 #When archiving messages
@login_required
def archive_message(request, pk):
     return render(request, "inbox/message_detail.html", {"message_id":pk},)