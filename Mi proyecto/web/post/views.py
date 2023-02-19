
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Post
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse_lazy





def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post/post_list.html', {'posts': posts})



def MultipleImages(request):
    if request.method == "POST":
        fotos = request.FILES.getlist('images')

        for foto in fotos:
            Post.objects.create(foto = foto)
        return HttpResponseRedirect(reverse_lazy('post_list'))    
    return render(request, "post/upload.html")