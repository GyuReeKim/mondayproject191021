from django.shortcuts import render, redirect, get_object_or_404
from .forms import DcinsideForm, CommentForm
from .models import Dcinside, Comment
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    # dcinsides = request.user.dcinside_set.all()
    dcinsides = Dcinside.objects.all()
    context = {
        'dcinsides' : dcinsides
    }
    return render(request, 'dcinside/index.html', context)

def create(request):
    if request.method == "POST":
        form = DcinsideForm(request.POST)
        if form.is_valid():
            dcinside = form.save(commit=False)
            dcinside.user = request.user
            dcinside.save()
            return redirect('dcinside:index')
    else:
        form = DcinsideForm()
    context = {
        'form': form
    }
    return render(request, 'dcinside/form.html', context)

def detail(request, id):
    dcinside = get_object_or_404(Dcinside, id=id)
    form = CommentForm()
    #comments = get_object_or_404(Comment, id=id)
    context = {
        'dcinside' : dcinside,
        'form' : form,
        #'comments' : comments,
    }
    return render(request, 'dcinside/detail.html', context)



@login_required
def update(request, id):
    dcinside = get_object_or_404(Dcinside, id=id)
    if request.method == "POST":
        form = DcinsideForm(request.POST, instance=dcinside)
        if form.is_valid():
            dcinside = form.save(commit=False)
            dcinside.user = request.user
            dcinside.save()
            return redirect('dcinside:detail', id)
    else:
        form = DcinsideForm(instance=dcinside)
    context = {
        'form': form
    }
    return render(request, 'dcinside/form.html', context)

@login_required
def delete(request, id):
    dcinside = get_object_or_404(Dcinside, id=id)
    if request.method == "POST":
        dcinside.delete()
        return redirect('dcinside:index')
    else:
        return redirect('dcinside:detail', id)

@login_required
def comment_create(request, id):
    dcinside = get_object_or_404(Dcinside, id=id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.dcinside = dcinside
            comment.c_user = request.user
            comment.save()
            return redirect('dcinside:detail', id)

@login_required
def comment_delete(request, id, c_id):
    dcinside = get_object_or_404(Dcinside, id=id)
    if request.method == "POST":
        comment = get_object_or_404(Comment, id=c_id)
        comment.delete()
        return redirect('dcinside:detail', id)