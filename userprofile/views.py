from django.shortcuts import render, redirect
from .forms import UserRegisterForm, LoginForm, PostForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from blog.models import Post
from .models import UserProfile

@login_required
def user_profile(request,post_id = None):
    user = request.user
    user_posts = Post.objects.filter(author=user)
    post_edit = None

    if post_id: #проверка на передачу пост айди
        post_edit = Post.objects.get(pk=post_id) # если айди передан, сохранаяем пост в переменную едит пост 
        if post_edit.author != user:
            return HttpResponseForbidden("У вас нет прав для редактирования данного поста.")

    if request.method == 'POST':
        if post_edit: # если переменная пост эдит заполненна тогда возвращаем  форму с данными поста.
            post_form = PostForm(request.POST, request.FILES, instance=post_edit)
        else:
            post_form = PostForm(request.POST, request.FILES)
        print(post_form.is_valid())

        if post_form.is_valid():   # что бы загружалась картинка через форму нужно указать request.FILES и шаблоне формы добавить enctype="multipart/form-data"
            new_post = post_form.save(commit=False)
            new_post.author = request.user
            new_post.save()

            if post_id:
                return redirect('blog:show_single_post', post_id)
            else:
                return redirect('blog:show_all_categories')
    else:# опять же проверка на значение постэдит если есть, возвращаем заполненную форму если нет то пустую.
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
    print(request.session.items())
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data.get('password'))
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                    return redirect('userprofile:user_profile')
            else:
                return redirect('userprofile:user_login')
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
            new_user.set_password(user_form.cleaned_data.get('password'))
            new_user.save()
            UserProfile.objects.create(
                user=new_user, 
                first_name=new_user.first_name,
                e_mail = new_user.email
                )
   
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
    user_posts = Post.objects.get(pk=post_id)
    
    if request.user == user_posts.author:
        user_posts.delete()
    else:
        return HttpResponseForbidden("У вас нет прав для удаления данного поста.")
    
    
    return redirect('userprofile:user_profile')
