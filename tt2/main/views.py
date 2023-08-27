from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, UpdateView, ListView, DeleteView, FormView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from .forms import PostForm, RegistrationForm, UserInfoForm
from .models import Post, UserInfo
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
# Create your views here.

class MainView(TemplateView):
    template_name = "main/home.html"

class AddPost(LoginRequiredMixin, CreateView):
    template_name = "main/add_post.html"
    model = Post
    success_url = '/read_posts/'
    form_class = PostForm

    # after the form is validated, we want to add the user to the post
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)




class ReadPosts(LoginRequiredMixin, CreateView, ListView):
    template_name = "main/read_posts.html"
    model = Post
    context_object_name = 'posts'
    success_url = '/read_posts/'
    form_class = PostForm


class DeletePost(DeleteView):
    model = Post
    success_url = reverse_lazy('read_posts')
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(author=self.request.user)






class RegistrationView(FormView):
    template_name = "registration/sign_up.html"
    form_class = RegistrationForm
    success_url = reverse_lazy('login')
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)





class ViewUserProfile(ListView):
    template_name = "main/view_user_profile.html"
    model = Post
    context_object_name = 'data'
    def get_queryset(self):
        try:
            author = User.objects.filter(username=self.kwargs['author'])[0]
            posts = Post.objects.filter(author=author)
            try:
                user_info = UserInfo.objects.filter(user=author)[0]
            except:
                user_info = None
            data = {'user_info': user_info, 'posts': posts, 'author': author}
            return data
        except:
            return None



class GetPost(ListView):
    template_name = "main/get_post.html"
    model = Post
    context_object_name = 'post'
    def get_queryset(self):
        try:
            post = Post.objects.filter(uuid=self.kwargs['uuid'])[0]
            return post
        except:
            return "Post not found"



class UpdateUserInfo(LoginRequiredMixin, UpdateView):
    template_name = "main/update_profile.html"
    model = UserInfo
    success_url = reverse_lazy('read_posts')
    form_class = UserInfoForm
    def get_object(self):
        user_info, created = UserInfo.objects.get_or_create(user=self.request.user)
        return user_info


