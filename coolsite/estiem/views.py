# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, FormView, TemplateView

from .forms import *
from .models import *
from .utils import *


class EstiemHome(DataMixin, ListView):
    model = Estiem
    template_name = 'estiem/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Главная страница", cat_selected=0)
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Estiem.objects.filter(is_published=True).select_related('cat')


# def index(request):  # HttpRequest
#     # return HttpResponse("Страница приложения estiem.")
#     posts = Estiem.objects.all()
#
#     context = {
#         'posts': posts,
#         'menu': menu,
#         'title': 'Главная страница',
#         'cat_selected': 0
#     }
#
#     return render(request, 'estiem/index.html', context=context)


class About(DataMixin, TemplateView):
    model = Estiem
    template_name = 'estiem/about.html'
    # context_object_name = 'about'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="О сайте")
        return dict(list(context.items()) + list(c_def.items()))


class AddPage(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'estiem/addpage.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('home')
    raise_exception = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Добавление события")
        return dict(list(context.items()) + list(c_def.items()))


# def addpage(request):
#     if request.method == 'POST':
#         form = AddPostForm(request.POST, request.FILES)
#         if form.is_valid():
#             # print(form.cleaned_data)
#             # try:
#             #     Estiem.objects.create(**form.cleaned_data)
#             #     return redirect('home')
#             # except:
#             #     form.add_error(None, 'Ошибка добавления поста')
#             form.save()
#             return redirect('home')
#     else:
#         form = AddPostForm()
#     return render(request, 'estiem/addpage.html', {'form': form, 'menu': menu, 'title': 'Add Page'})


# @login_required
# def contact(request):
#     return HttpResponse("<h1>Обратная связь</h1>")


class ContactFormView(DataMixin, FormView):
    form_class = ContactForm
    template_name = 'estiem/contact.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Обратная связь")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        print(form.cleaned_data)
        return redirect('home')


# def login(request):
#     return HttpResponse("<h1>Войти</h1>")


class ShowPost(DataMixin, DetailView):
    model = Estiem
    template_name = 'estiem/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['cat_number'] = context['post'].cat_id
        if context['post'].kind_id:
            k = Kind.objects.get(id=context['post'].kind_id)
            kind_name = k.name
            kind_content = k.content
        else:
            kind_name = None
            kind_content = None
        c_def = self.get_user_context(title=context['post'], kind_name=kind_name, kind_content=kind_content)
        return dict(list(context.items()) + list(c_def.items()))


# def show_post(request, post_slug):
#     # return HttpResponse(f"<h1>Отображение статьи с id = {post_id}</h1>")
#     post = get_object_or_404(Estiem, slug=post_slug)
#
#     context = {
#         'post': post,
#         'menu': menu,
#         'title': post.title,
#         'cat_selected': post.cat_id
#     }
#
#     return render(request, 'estiem/post.html', context=context)


class EstiemCategory(DataMixin, ListView):
    model = Estiem
    template_name = 'estiem/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c = Category.objects.get(slug=self.kwargs['cat_slug'])
        c_def = self.get_user_context(title=str(c.name) + ' events', cat_selected=c.pk)
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Estiem.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True).select_related('cat')


# def show_category(request, cat_id):
#     # return HttpResponse(f"<h1>Отображение категории с id = {cat_id}</h1>")
#     posts = Estiem.objects.filter(cat_id=cat_id)
#
#     if len(posts) == 0:
#         raise Http404()
#
#     context = {
#         'posts': posts,
#         'menu': menu,
#         'title': 'Отображение по рубрикам',
#         'cat_selected': cat_id
#     }
#
#     return render(request, 'estiem/index.html', context=context)


# def categories(request, catid):
#     return HttpResponse(f"<h1>Статьи по категориям</h1><p>{catid}</p>")


def archive(request, year):
    if int(year) > 2023:
        # raise Http404()
        return redirect('home', permanent=True)

    return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")


def pageNotFound(request, exeption):
    return HttpResponseNotFound('<h1>Сори страница не найдена</h1>')


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'estiem/register.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'estiem/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')
