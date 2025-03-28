from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
import threading

@receiver(post_save, sender=User)
def my_signal_receiver(sender, instance, created, **kwargs):
    receiver_thread_id = threading.current_thread().ident
    print(f"Receiver running in thread ID: {receiver_thread_id}")
    