from django.shortcuts import render,redirect

# Create your views here.
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import ProfileForm

@login_required
def index(request):
    try:
        profile = Profile.objects.get(user=request.user)
        ctx = {'profile': profile}
        return render(request, 'accounts/view_profile.html', ctx)
    except Profile.DoesNotExist:
        return redirect('/accounts/profile/create')
    

@login_required
def create_profile(request):
    form = ProfileForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('/accounts/profile/update')
    ctx = {'form': form}
    return render(request, 'accounts/create_profile.html', ctx)


@login_required
def update_profile(request):
    try:
        profile = Profile.objects.get(user=request.user)
        form = ProfileForm(request.POST or None, request.FILES or None, instance=profile)
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                return redirect('/accounts/profile/')
        ctx = {'form': form}
        return render(request, 'accounts/update_profile.html', ctx)
    except Profile.DoesNotExist:
        return redirect('/accounts/profile/create')