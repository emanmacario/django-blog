from django.shortcuts import render

# Mock DB data
posts = [
    {
        'author': 'Emmanuel Macario',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 29, 2020'
    },
    {
        'author': 'Hagrid',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'September 12, 2020'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})