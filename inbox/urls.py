from django.urls import path
from . import views

urlpatterns = [
    path('', views.inbox, name='inbox'),
    path("compose/", views.compose_message, name="compose_message"),
    path("sent/", views.sent_messages, name="sent_messages"),
    path("archived/", views.archived_messages, name="archived_messages"),
    path("<int:pk>/", views.message_detail, name="message_detail"),
    path("<int:pk>/archive/", views.archive_message, name="archive_message"),
    path("<int:pk>/reply/", views.reply_message, name="reply_message",),

]