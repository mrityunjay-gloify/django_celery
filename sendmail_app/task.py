from celery import shared_task
from celery import Task
from celery.utils.log import get_task_logger
from django.core.mail import send_mail
from django_celery_project import settings
import logging

logger = get_task_logger(__name__)

class BatchTask(Task):
    ignore_result = True
    acks_late = True

    def run(self, email_batches, **kwargs):
        email_subject = "Hi! Celery Testing"
        message = "Testing celery send email"
        for email in email_batches:
            to_email = email
            try:
                send_mail(
                    subject=email_subject,
                    message=message,
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[to_email],
                    fail_silently=True,
                )
                logger.info(f"Email sent to {email}")
            except Exception as e:
                logger.error(f"Error sending email to {email}: {str(e)}")

@shared_task(base=BatchTask)
def send_mail_batch(emails):
    return emails