from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.http import HttpResponse
from .models import Blogpost, Contact, Category, Comment
from django.contrib import messages
from django.db.models import Count

from .forms import CommentForm
# Create your views here.

def get_category_count():
    queryset = Category.objects.annotate(count=Count('blogpost'))
    return queryset



def index(request):
    category_count= get_category_count()
    featured = Blogpost.objects.filter(status=1).order_by('featured')
    latest = Blogpost.objects.filter(status=1).order_by('-created_on')[0:4]

    myposts = Blogpost.objects.filter(status=1)
    paginator = Paginator(myposts, 4)
    page = request.GET.get('page')
    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)

    context = {'queryset': paginated_queryset,
    'page': page,
    'featured': featured,
    'latest': latest,
    'myposts': myposts,
    'category_count': category_count,
    }
    return render(request, 'blog/index.html', context)


def blogpost(request, post):
    category_count= get_category_count()
    latest = Blogpost.objects.order_by('-created_on')[0:4]
    post = get_object_or_404(Blogpost, slug= post)
    comments = post.comments.all().order_by('-timestamp')
    form = CommentForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.instance.user = request.user
            form.instance.post = post
            form.save()
            return redirect('.')
    context = {'post':post,
    'latest': latest,
    'category_count': category_count,
    'form': form,
    'comments': comments,
    }
    return render(request, 'blog/blogpost.html', context)


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        if len(name)<2 or len(email)<4 or len(phone)<3 or len(desc)<4:
            messages.error(request, "Please fill the form correctly")
        else:
            contact = Contact(name=name, email=email, phone=phone, desc=desc,)
            contact.save()
            messages.success(request, "Your message has been successfully sent")
    return render(request, 'blog/contact.html')


def search(request):
    myposts = Blogpost.objects.all()
    query = request.GET['search']
    print(query )
    if len(query)>78:
        myposts = Blogpost.objects.none()
    else:
        post_title = Blogpost.objects.filter(Q(title__icontains=query))
        posts_content = Blogpost.objects.filter(Q(content__icontains=query))
        posts_slug = Blogpost.objects.filter(Q(slug__icontains=query))
        myposts = post_title | posts_content | posts_slug

    if myposts.count() == 0:
        messages.warning(request, "No search results found. Please enter again.")
    context = {'myposts': myposts,'query':query}
    return render(request, 'blog/search.html', context)

