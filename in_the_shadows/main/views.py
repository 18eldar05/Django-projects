from django.shortcuts import render, redirect
from .models import Comment
from .forms import CommentForm


def index(request):
    return render(request, 'main/Django_First_Website/Main.html', {'title': 'Привет!'})


def concerts(request):
    return render(request, 'main/Django_First_Website/Concerts.html')


def contacts(request):
    error = ''
    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/info#coms')
        else:
            error = 'Ошибка! Неверная форма'

    form = CommentForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/Django_First_Website/Contacts.html', context)


def about(request):
    comments = Comment.objects.order_by('-id')
    return render(request, 'main/Django_First_Website/Bout_us.html', {'comments': comments})


def piter(request):
    return render(request, 'main/Django_First_Website/Product_page_Piter.html')
