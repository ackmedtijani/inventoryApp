from django.shortcuts import render , redirect
from .models import Product , Purchase
from .forms import ProductForm , PurchaseForm
from django.http.response import JsonResponse , HttpResponseRedirect , HttpResponse

# Create your views here.


def home(request):
    context = {}
    template = 'base.html'
    product_form , purchase_form = ProductForm() , PurchaseForm()
    if request.method == 'GET':
        product , purchase = Product.objects.all() , Purchase.objects.all()
        context['product_object'] , context['purchase_object'] = Product , Purchase 
        context['products'] , context['purchases']=  product , purchase
        context['product_addform'] , context['purchase_addform'] = product_form , purchase_form

    if request.method == 'POST':
        pass
        
    return render(request, template , context)


def add(request , params):
    template = 'base.html'
    if request.method == 'POST':
        if params == 'product':
            print('Product')
            form = ProductForm(request.POST)
            print(request.POST)
            if form.is_valid():
                form.save()
        else:
            form = PurchaseForm(request.POST)
            if form.is_valid():
                form.save()
                
        return redirect('home')
        
        
def edit(request , params , name):
    if request.method == 'GET':
        print(params , name)
        if params == 'product':
            object = Product.objects.get(name = name)
            form = ProductForm(instance=object)
        else:
            product = Product.objects.get(name = name)
            object = Purchase.objects.get(product = product)
            form = PurchaseForm(instance=object)
        
            
        return HttpResponse(form.as_p())
            
        
    if request.method == 'POST':
        print(params , name)
        if params == 'product':
            object = Product.objects.get(name = name)
            form = ProductForm(request.POST , instance=object)
            if form.is_valid():
                form.save()
        else:
            product = Product.objects.get(name = name)
            object = Purchase.objects.get(product = product)
            form = PurchaseForm(request.POST , instance=object)
        
        return redirect('home')
                        
            

def delete(request):
    pass

def search(request):
    pass

def filter(request , params , filter):
    if request.method == 'GET':
        if params == 'product':
            pass
        

def sort(request):
    pass