from django.db.models.signals import pre_save, pre_delete, post_save, post_delete
from django.dispatch import receiver
from django.conf import settings
from app1.models import registration
from django.core.mail import EmailMessage
from django.core.mail import send_mail
import pudb

@receiver(post_save, sender=registration)		
def send_email(sender, instance, **kwargs):
	pudb.set_trace()
	if kwargs.get('created', None) is True:
		print ('created')
		send_mail('Registration Nofication', 'Account registered successfully',
		 settings.EMAIL_HOST_USER,[instance.email], fail_silently=False)
	else:
		pass
