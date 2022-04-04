

from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.http  import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .forms import ProfileForm,UploadImageForm, CommentForm
from .models import Image, Profile, Comments



def index(request):
    return render(request, 'index.html')


@login_required(login_url='/accounts/login/')
def home(request):
    title= "Instagram"
    current_user = request.user
    images = Image.objects.all()
    comments = Comments.objects.all()
    profile = Profile.objects.all()
    
    
    return render(request, 'home.html', {'title':title, 'current_user':current_user, 'images':images, 'comments': comments, 'profile':profile})


@login_required(login_url='/accounts/login/')
def upload_image(request):
    title = "Instagram | Upload image"
    current_user = request.user
    if request.method == "POST":
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.profile = current_user
            image.save()
        return redirect('home', {'title':title})
    else:
        form = UploadImageForm()
    return render(request, 'upload_image.html', {'form': form })
    
    
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
            
        return render (request, 'profile.html')
    

@login_required(login_url='/accounts/login/')
def search(request):
    Profile = User.objects.all()

    if 'name' in request.GET and request.GET['name']:
        searched_name = request.GET.get('name')
        results = User.objects.filter(username__icontains=searched_name)
        print(results)

        return render(request,'results.html',{'Profile':Profile})

def comments(request,image_id):
    current_user=request.user
    image = Image.objects.get(id=image_id)
    user= User.objects.get(user=current_user)
    comments = Comments.objects.all()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comments = form.save(commit=False)
            comments.image = image
            comments.comments_user = current_user
            comments.save()
        return redirect('home')
    else:
        form = CommentForm()
    return render(request, 'comment.html',{'current_user':current_user, 'image':image, 'user':user, 'comments': comments})



def like_image(request,image_id):
    image = Image.objects.get(pk=image_id)
    liked = False
    current_user = request.user
    try:
        profile = Profile.objects.get(user = current_user)
    except Profile.DoesNotExist:
        raise Http404()
    if image.likes.filter(id=profile.id).exists():
        image.likes.remove(profile)
        liked = False
    else:
        image.likes.add(profile)
        liked = True
    return HttpResponseRedirect(reverse('home', {'liked':liked}))