import profile
from turtle import title
from django.shortcuts import redirect, render
from django.http  import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm,UploadImageForm, EditBioForm, CommentForm


from .models import Image, Profile, Comments
# from django.contrib.auth.mixins import LoginRequiredMixin




# Create your views here.
# def index(request):
#     return render(request, 'index.html')


@login_required(login_url='/accounts/login/')
def index(request):
    title= "Instagram"
    current_user = request.user
    images = Image.objects.all()
    comments = Comments.objects.all()
    profile = Profile.objects.all()
    
    
    return render(request, 'index.html', locals())


@login_required(login_url='/accounts/login/')
def upload_image(request):
    title = "Instagram | Upload image"
    current_user = request.user
    try:
        profile = Profile.objects.get(user = current_user)
    except Profile.DoesNotExist:
        raise Http404()
    if request.method == "POST":
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.profile = profile
            image.save()
        return redirect('index')
    else:
        form = UploadImageForm()
    return render(request, 'upload_image.html', {'form': form, 'title': title})
    
    
