from django.shortcuts import render, redirect
from .forms import UserRegisterForm, LoginForm, PostForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from blog.models import Posts

@login_required
def user_profile(request,post_id = None):
    user = request.user
    user_posts = Posts.objects.filter(author=user)
    post_edit = None

    if post_id:
        post_edit = Posts.objects.get(pk=post_id)
        if post_edit.author != user:
            return HttpResponseForbidden("У вас нет прав для редактирования данного поста.")

    if request.method == 'POST':
        if post_edit:
            post_form = PostForm(request.POST, instance=post_edit)
        else:
            post_form = PostForm(request.POST)

        if post_form.is_valid():
            new_post = post_form.save(commit=False)
            new_post.author = request.user
            new_post.save()

            return redirect('userprofile:user_profile')
    else:
        if post_edit:
            post_form = PostForm(instance=post_edit)
        else:
            post_form = PostForm()

    content = {
        'user':user,
        'user_posts':user_posts,
        'post_form':post_form,
    }

    return render(request, 'userprofile/profile.html', content)

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated secsessfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()

    content = {
        'form': form,
    }

    return render(request, 'userprofile/login.html', content)


def register(request):
    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
   
            content = {
                'new_user': new_user,
            }
    
            return render(request, 'userprofile/register_done.html', content)
    else:
        user_form = UserRegisterForm() 

    content = {
            'user_form': user_form,
        }
    
    return render(request, 'userprofile/register.html', content)

@login_required
def del_post(request, post_id):
    user_posts = Posts.objects.get(pk=post_id)
    if request.user == user_posts.author:
        user_posts.delete()
    else:
        return HttpResponseForbidden("У вас нет прав для удаления данного поста.")
    
    return redirect('userprofile:user_profile')