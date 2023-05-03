from django.shortcuts import render, redirect
from .models import Psychiatrist 
from .models import Prescription

# Create your views here.

def all_psychiatrists(request):
    Psychiatrists = Psychiatrist.objects.all()
    ctx = {'psychiatrists':Psychiatrists}
    return render(request, 'psychiatrist/all.html', ctx)

def view_psychiatrist(request,id):
    psy = Psychiatrist.get(id=id)
    context = {'psy':psy}
    return render(request, 'psychiatrist/view.html', context)

def make_prescription(request):
    if request.method == 'POST':
        
        return redirect('/prescriptions')
    else:
        return render(request, 'prescription/make_pres.html')
    
def all_prescriptions(request):
    prescriptions = Prescription.objects.all()
    ctx = {
         'prescriptions':prescriptions
    }
    return render(request, 'prescription/all_pres.html', ctx)
    
def view_prescription(request,id):
    pres = Prescription.get(id=id)
    context = {'prescription':pres}
    return render(request, 'psychiatrist/view_pres.html', context)



def Article(request):
    if request.method == 'POST':
        psychiatrist = request.POST['psychiatrist']
        title = request.POST['title']
        image = request.POST['image'] 
        content = request.POST['content']
        article = Article(psychiatrist=psychiatrist, title=title, image=image, content=content)
        article.save()
        return render(request, 'Article.html')
    else:
        return render(request, 'Article.html')