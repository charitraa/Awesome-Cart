from django.shortcuts import render
# from django.http import HttpResponse
from .models import Product , Contact , CheckOut,OrderUpdate
from math import ceil
def index(request):

    allProds =[]
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n//4 + ceil((n/4)-(n//4))
        allProds.append([prod, range(1,nSlides), nSlides])
    params =  {'allProds':allProds}
    return render(request,"shop/index.html", params)

def about(request): 
    return render(request,"shop/about.html")


def tracker(request):
    if request.method == 'POST':
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        phone = request.POST.get('phone','')
        desc = request.POST.get('desc','')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()

    return render(request,"shop/tracker.html")

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        phone = request.POST.get('phone','')
        desc = request.POST.get('desc','')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
    return render(request,"shop/contact.html")


def search(request):
    return render(request,"shop/search.html")

def productview(request,myid):
    # fetch the product using id
    product = Product.objects.filter(id=myid)
    return render(request,"shop/productview.html",{'product':product[0]})

def checkout(request):

    if request.method == 'POST':
        # print(request)
        items_json = request.POST.get('itemsJson','')
        fname = request.POST.get('fname','')
        lname = request.POST.get('lname','')
        email = request.POST.get('email','')
        phone = request.POST.get('phone','')
        city = request.POST.get('city','')
        province = request.POST.get('province','')
        zip = request.POST.get('zip','')
        # print(desc)
        checkout = CheckOut(items_json= items_json,fname=fname,lname=lname, email=email, phone=phone, city= city, province= province, zip=zip )
        checkout.save()
        thank = True
        id = checkout.check_out_id
        update = OrderUpdate(update_desc = "Check out has been placed")
        update.save()
        return render(request,"shop/checkout.html", {'thank':thank ,'id':id})
    return render(request,"shop/checkout.html")
