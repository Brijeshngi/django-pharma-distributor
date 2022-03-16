from django.shortcuts import render, HttpResponseRedirect, redirect

from django.http import HttpResponse

from .models import product,product_category

from django.core.paginator import Paginator

from django.db.models import Count

from django.db.models import Q

from django.contrib.auth.forms import UserCreationForm

from .form import registerform

from django.contrib import messages


from django.contrib.auth import login, authenticate,logout,update_session_auth_hash

from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm

from django.contrib.auth.models import User



# Create your views here.

def productlist(request):
    productlist = product.objects.all()
    items = product_category.objects.annotate(total_products= Count('product'))

    kategorie = product.objects.filter().order_by('product_category')


    search_query = request.GET.get('q')
    if search_query :
        productlist = productlist.filter(
            Q(product_name__icontains = search_query)
        )


    paginator = Paginator(productlist, 3)  # Show 3 items per page.

    page_number = request.GET.get('page')
    productlist = paginator.get_page(page_number)



    context = {'product_list': productlist , 'category_list': items,'kategorie': kategorie }

    template = 'product/product_list.html'

    return render(request, template, context)




def productdetails(request,post_id):

    productdetails = product.objects.get(id=post_id)

    context = {'product_detail': productdetails}
    template = 'product/product_detail.html'


    return render(request, template, context)

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def index(request):
    return render(request, "index.html")




def abc(request):
	pass




'''
def register(request):
    if request.method == 'POST':
        fm = UserCreationForm(request.POST)
        if fm.is_valid():
            fm.save()

    else:        
        fm = UserCreationForm()
    return render(request, 'product/register.html', {'register_form':fm})

'''
def register(request):
    if request.method == 'POST':        #request comes with post method checks here
        fm = registerform(request.POST)
        if fm.is_valid():               #checks if all the data comes here are valid or not
            fm.save()                   #saved to database
    else:        
        fm = registerform()             #if request come swith get method will be rejected here
    return render(request, 'product/register.html', {'register_form':fm})



 # started login here...after importing authenticationform ...
def user_login(request):
    if not request.user.is_authenticated:           #checks is user is logged in and trying to login again
        if request.method == "POST":
            fm = AuthenticationForm(request=request, data=request.POST) #inbuilt form to take data from login page
            if fm.is_valid():
                uname = fm.cleaned_data['username']     
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname, password=upass) #inbuilt key to take data from login form pass to user variable
                if user is not None:
                    login(request, user)
                    fname = user.first_name
                    lname = user.last_name
                    return render(request, 'product/profile.html', {'fname':fname,'lname':lname})
        else:            
            fm = AuthenticationForm()           #get request rejected and redirected to login page
        return render(request, 'product/login.html', {'login_form':fm}) 
    else:
        return render(request, 'product/profile.html')    #if user is already logged in

def profile(request):
    if request.user.is_authenticated:           #if user authenticated and again trying to log in
        return render(request, 'product/profile.html')
    else:
        return render(request, 'product/login.html') #if not logged in then redirect to login page





def signout(request):
    logout(request)             #login logout inbuilt function are imported
    
    return render(request, 'product/index.html')


def changepass(request):
    if request.user.is_authenticated:
        if request.method == "POST": #here POST request comes
            fm = PasswordChangeForm(user = request.user, data=request.POST) #inbuilt form takes data via post
            if fm.is_valid():                       #validation
                fm.save()                       #save data in password field for current profile
                update_session_auth_hash(request, fm.user)   # to store session on the same profile
                return render(request, 'product/profile.html')
        else:
            fm = PasswordChangeForm(user= request.user) #rejected when request comes with get 
        return render(request, 'product/changepass.html', {'fm':fm})
    else:
        return render(request, 'product/login.html')