from django.shortcuts import render
from django.http import HttpResponse
from .tasks import *
from sendmail_app.task import *
# Create your views here.

def test(request):
    test_func.delay()
    return HttpResponse("Done")

def send_emails_view(request):
    emails = [f"user{i}@example.com" for i in range(1, 10001)]
    batch_size = 1000
    num_batches = (len(emails) + batch_size - 1) // batch_size  # Calculate the number of batches

    for i in range(num_batches):
        batch = emails[i*batch_size:(i+1)*batch_size]
        send_mail_batch.apply_async(args=[batch], countdown=10 * (i + 1))

    return HttpResponse("Email Sent")


