from django.shortcuts import render ,redirect
from django.views.generic import View
from mobile.forms import MobileForm,RegistrationForm,LoginForm

from mobile.models import Mobiles
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.utils.decorators import method_decorator

def signin_required(fn):
    def wrapper(request,*args,**kwargs):
        if not request.user.is_authenticated:
            return redirect("signin")
        else:
            return fn(request,*args,**kwargs)    
    return wrapper  
@method_decorator(signin_required,name="dispatch")          
class MobileListView(View):
    def get(self,request,*args,**kwargs):
        qs=Mobiles.objects.all()
        #filter using brand
        if "brand"in request.GET:
            brand=request.GET.get("brand")
            qs=qs.filter(brand__iexact=brand)
        #filter using display    
        if "display" in request.GET: 
            display=request.GET.get("display")   
            qs=qs.filter(display__iexact=display)
            #iexact for removing casematching
            #filtering using price
        if "price_lt" in request.GET:
            amount=request.GET.get("price_lt")
            qs=qs.filter(price__lte=amount)
        if "price_gt" in request.GET:
            amount=request.GET.get("price_gt")
            qs=qs.filter(price__gte=amount)    
        return render(request,"mob_list.html",{"data":qs}) 


        
#localhost:8000/mobiles/{id}
@method_decorator(signin_required,name="dispatch")
class MobileDetailsView(View):
    def get(self,request,*args,**kwargs):
        # if not request.user.is_authenticated:
        #     return redirect("signin")
            id=kwargs.get('pk')
            qs=Mobiles.objects.get(id=id)
            return render(request,"mob_detail.html",{"data":qs})
#localhost:8000/mobiles/{id}/remove
@method_decorator(signin_required,name="dispatch")
class MobileDeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        Mobiles.objects.get(id=id).delete()
        messages.success(request,"mobile has been removed")
        return redirect("mobile-all")
    
#localhost:8000/mobiles/add    
#get -mobile_add.html
#post-save form data
@method_decorator(signin_required,name="dispatch")
class MobileCreateView(View):
    def get(self,request,*args,**kwargs):
        form=MobileForm()
        return render(request,"mobile_add.html",{"form":form})
                                   
    def post(self,request,*args,**kwargs):
        form=MobileForm(request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,"mobile has been added")
            return redirect("mobile-all")
        else:
            messages.error(request,"failed to add mobile")
            return render(request,"mobile_add.html",{"form":form})
@method_decorator(signin_required,name="dispatch")    
class MobileUpdateView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        obj=Mobiles.objects.get(id=id)
        form=MobileForm(instance=obj)
        return render(request,"mobile_change.html",{"form":form}) 
    def post(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        obj=Mobiles.objects.get(id=id)
        form=MobileForm(request.POST,instance=obj,files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,"mobile details changed")
            return redirect("mobile-all")
        else:
            messages.error(request,"faled to change the mobile details")
            return render(request,"mobile_change.html",{"form":form})


class SignUpView(View):
    def get(self,request,*args,**kwargs):
        form=RegistrationForm()
        return render(request,"register.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form=RegistrationForm(request.POST)
        if form.is_valid():
            #form.save()
            User.objects.create_user(**form.cleaned_data)
            messages.success(request,"account has been created successfully")
            return render(request,"register.html",{"form":form})
        else:
            messages.error(request,"failed to create the account")
            return render(request,"register.html",{"form":form})
        

class SignInView(View):
    def get(self,request,*args,**kwargs) :
        form=LoginForm()
        return render(request,"login.html",{"form":form})       
    
    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            print(uname,pwd)
            user_object=authenticate(request,username=uname,password=pwd)
            if user_object:
                print("valid credentials")
                login(request,user_object)
                print(request.user)
                return redirect("mobile-all")
            else:
                print("invalid credentials")    
            return render(request,"login.html",{"form":form})   
        else:
            return render(request,"login.html",{"form":form})   
@method_decorator(signin_required,name="dispatch")
class SignOutView(View):
    def get(self,request,*args,**kwargs) :
          form=logout(request) 
          return redirect("signin")     

