
from django.urls import path
from . import views

urlpatterns = [
    path('',views.test, name="test"),
    path('sendmail/',views.send_emails_view,name="sendmail")
]
