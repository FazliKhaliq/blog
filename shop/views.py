from django.shortcuts import render

from .models import Product, Contact, Orders

from math import ceil

# Create your views here.
def index(request):

    allProds= []
    catprods= Product.objects.values('category', 'id')
    cats= {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])
    params = {'allProds': allProds}
    return render(request, 'shop/index.html', params)


def about(request):
    return render(request, 'shop/about.html')


def home(request):
    return render(request, 'shop/home.html')

def productsview(request, myid):
    # Fetch product using id
    product = Product.objects.filter(id=myid)
    return render(request, 'shop/productsview.html', {'product':product[0]})


def search(request):
    allProds= []
    catprods= Product.objects.values('category', 'id')
    cats= {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])
    params = {'allProds': allProds}

    return render(request, 'shop/index.html')


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc,)
        contact.save()
    return render(request, 'shop/contact.html')



def tracker(request):
    return render(request, 'shop/tracker.html')

def checkout(request):
    if request.method == "POST":
        items_json = request.POST.get('itemsJson', '')
        amount = request.POST.get('amount', '')
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        address = request.POST.get('address', '') + "" + request.POST.get('address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        order = Orders(items_json=items_json, amount=amount, name=name, email=email, phone=phone, address=address, city=city, state=state, zip_code=zip_code)
        order.save()

    return render(request, 'shop/checkout.html')


def privacy(request):
    return render(request, 'shop/privacy.html')
def termsandcondition(request):
    return render(request, 'shop/termsandcondition.html')