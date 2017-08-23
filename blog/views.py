from django.shortcuts import render, get_object_or_404, render_to_response
from django.utils import timezone
from .models import Post
from .forms import PostForm
from django.shortcuts import redirect
from .models import BooksModel
from .models import *

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def post_new(request):
    form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})
# Create your views here.
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

def books_list(request):
    booksModel = BooksModel()
    books = [
        Book(author='Tolstoy', title='Voina i mir', description='nice book', rating=3, imageUrl="https://www.asme.org/getmedia/c2c8ea5a-b690-4ba7-92bb-34bd1432862b/book_guide_hero_books.aspx"),
        Book(author='Tolstoy2', title='Voina i mir2', description='nice book very', rating=10, imageUrl="https://www.asme.org/getmedia/c2c8ea5a-b690-4ba7-92bb-34bd1432862b/book_guide_hero_books.aspx"),
        Book(author='Tolstoy3', title='Voina i mir3', description='nice book bad', rating=9, imageUrl="https://www.asme.org/getmedia/c2c8ea5a-b690-4ba7-92bb-34bd1432862b/book_guide_hero_books.aspx")
    ]
    booksModel.books = books
    return render_to_response('blog/json_html.html', {'booksModel': booksModel})