from django.shortcuts import render
from django.http  import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

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



