from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .forms import MessageForm
from .models import Message

#Display messages
@login_required
def inbox(request):
    received_messages = Message.objects.filter(
        recipient=request.user,
        is_archived=False
    )
    return render(request, 'inbox/inbox.html', {"received_messages": received_messages})


#Sent messages
@login_required
def sent_messages(request):

    sent = Message.objects.filter(sender=request.user)

    return render(request, "inbox/sent.html", {"sent_messages": sent})


#Archived messages view
@login_required
def archived_messages(request):

    archived = Message.objects.filter(
        recipient=request.user,
        is_archived=True,
    )

    return render(request, 'inbox/archived.html', {"archived_messages": archived})

#Compose messages logic and direct
@login_required
def compose_message(request):
    if request.method == "POST":
         form = MessageForm(request.POST)

         if form.is_valid():
              message = form.save(commit=False)
              message.sender = request.user
              message.save()

              messages.success(request, "Message sent successfully.")
              return redirect("inbox")
         
    else:
        form = MessageForm()

    return render(request, 'inbox/compose.html', {"form":form})

# Message details
@login_required
def message_detail(request, pk): 
    message = get_object_or_404(
        Message,
        pk=pk,
    )

    if message.sender != request.user and message.recipient != request.user:
        messages.error(request, "You do not have permissions to view that message.")
        return redirect("inbox")
    
    if message.recipient == request.user and not message.is_read:
        message.is_read = True
        message.save()
    
    return render(request, 'inbox/message_detail.html', {"message":message},)

#Reply message function - repurposing the existing compose template
@login_required
def reply_message(request, pk):

    original = get_object_or_404(
        Message, 
        pk=pk,
    )

    if original.sender !=request.user and original.recipient != request.user:
        messages.error(request, "You do not have permission to reply.")
        return redirect("inbox")
    

    
    subject = original.subject

    if not subject.startswith("Re:"):
        subject = f"Re: {subject}"
    
    if request.method == "POST":

        form = MessageForm(request.POST)

        if form.is_valid():

            reply = form.save(commit=False)
            reply.sender = request.user
            reply.save()

            messages.success(request, "Reply sent successfully.")
            return redirect("inbox")
        
    else:

        form = MessageForm(
        initial={
            "recipient": original.sender,
            "subject": subject,
            "body": (
                "\n\n"
                "--------------------------------------\n"
                f"On {original.sent_at:%d %b %Y %H %M}, "
                f"{original.sender.username} wrote:\n\n"
                f"{original.body}"
            ),
                }
            )

    return render(
        request, "inbox/compose.html", {"form": form, },
    )



 #When archiving messages
@login_required
def archive_message(request, pk):
     
     message = get_object_or_404(
         Message,
         pk=pk,
         recipient=request.user,
     )

     if request.method == "POST":
         message.is_archived = True
         message.save()

         messages.success(request, "Message archived.")
         return redirect("inbox")


     return redirect("message_detail", pk=message.pk)