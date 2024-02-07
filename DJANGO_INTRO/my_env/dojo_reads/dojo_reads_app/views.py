from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from dojo_reads_app.models import Author
from dojo_reads_app.models import Book

def show_author(request, author_id):
  context = {
    'this_author': Author.objects.get(id=author_id)
  }
  return render(request, "display.html", context)

def add_book(request):
  if request.method == "GET":
    print(request.GET)
    # print(request)
    context = {
      'current_user' : "Morgan",
      'all_authors': Author.objects.all(),
      'all_books' : Book.objects.all()
    }
    return render(request, "index.html", context)
  if request.method == "POST":
    print(request)
    print(request.POST)
    # print("a POST request is being made to this route")
    Book.objects.create(
      title = request.POST["title"],
      author = Author.objects.get(id=request.POST["author_id"]),
      review = request.POST["review"],
      rating = request.POST["rating"],
    )
    # title = request.POST["title"]
    # author = request.POST["author_id"]
    # review = request.POST["review"]
    # rating = request.POST["rating"]
    # print(title)
    # print(author_id)
    # print(review)
    # print(rating)
    # request.session['title'] = title
    return redirect("/")
  

