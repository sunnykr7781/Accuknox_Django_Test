from django.http import HttpResponse
from django.contrib.auth.models import User
import threading

def create_user(request):
    caller_thread_id = threading.current_thread().ident
    print(f"Caller running in thread ID: {caller_thread_id}")
    
    User.objects.create(username="testuser")
    return HttpResponse("User created, check the console!")