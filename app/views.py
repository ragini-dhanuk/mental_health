from django.shortcuts import render
from .models import Feedback
from .models import Message
# Create your views here.
def landing(request):
    return render(request, 'landing.html')

def feedback(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message'] 
        rating = request.POST['rating']
        feedback = Feedback(name=name, email=email, message=message, rating=rating)
        feedback.save()
        return render(request, 'feedback.html')
    else:
        return render(request, 'feedback.html')
    
def message(request):
    if request.method == 'POST':
        client = request.POST['client']
        psychiatrist = request.POST['psychiatrist']
        Message = request.POST['Message']
        message = Message(client=client, psychiatrist=psychiatrist, Message=Message)
        message.save()
        return render(request, 'message.html')
    else:
        return render(request, 'message.html')