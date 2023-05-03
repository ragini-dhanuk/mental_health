from django.shortcuts import render, redirect
from .models import Client
# Create your views here.

def add_client(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone_number = request.POST['phone_number'] 
        password = request.POST['password']
        client = Client(name=name, email=email, phone_number=phone_number, password=password)
        client.save()
        return redirect('/clients')
    else:
        return render(request, 'client/add.html')

def all_clients(request):
    clients = Client.objects.all()
    ctx = {
        'clients':clients
    }
    return render(request, 'client/all.html', ctx)

def view_client(request,id):
    client = Client.objects.get(id=id)
    context = {'client':client}
    return render(request, 'client/view.html', context)