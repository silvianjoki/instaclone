
from distutils.command.upload import upload
from django.contrib.auth.models import User
from turtle import title
from django.shortcuts import redirect, render
from django.http  import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm,UploadImageForm, CommentForm
from .models import Image, Profile, Comments





@login_required(login_url='/accounts/login/')
def index(request):
    title= "Instagram"
    current_user = request.user
    images = Image.objects.all()
    comments = Comments.objects.all()
    profile = Profile.objects.all()
    
    
    return render(request, 'index.html', {'title':title, 'current_user':current_user, 'images':images, 'comments': comments, 'profile':profile})


@login_required(login_url='/accounts/login/')
def upload_image(request):
    current_user = request.user
    if request.method == "POST":
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.profile = current_user
            image.save()
        return redirect('index')
    else:
        form = UploadImageForm()
    return render(request, 'upload_image.html', {'form': form, })
    
    
@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    if request.method == ' POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.name = current_user
            profile.save()
        else:
            form = ProfileForm()
            
        return render (request, 'profile/new_profile.html')
    

@login_required(login_url='/accounts/login/')
def search(request):
    profile_list = User.objects.all()

    if 'name' in request.GET and request.GET['name']:
        searched_name = request.GET.get('name')
        results = User.objects.filter(username__icontains=searched_name)
        print(results)

        return render(request,'results.html',locals())


    