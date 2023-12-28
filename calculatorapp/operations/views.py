from django.shortcuts import render
from django.views.generic import View
class HelloWorldView(View):
    def get(self, request,*args,**kwargs):
        print("indise helloworld")
        return render(request,"helloworld.html")    


class GoodMorningView(View):
    def get(self,request,*args,**kwargs):
        print("good morning")
        return render(request,"gm.html")    
class AdditionView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"add.html")  
    def post(self,request,*args,**kwargs):
        n1=request.POST.get("num1")
        n2=request.POST.get("num2")
        result=int(n1)+int(n2)
        print(result)
        return render(request,"add.html",{"output":result})  
        
class MultiplicationView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"mul.html")  
    def post(self,request,*args,**kwargs):
        n1=request.POST.get("num1")  
        n2=request.POST.get("num2")
        result=int(n1)*int(n2)
        print(result)
        return render(request,"mul.html",{"output":result})

class DivisionView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"div.html") 
    def post(self,request,*args,**kwargs):
        n1=request.POST.get("num1")  
        n2=request.POST.get("num2") 
        result=int(n1)/int(n2)
        print(result)
        return render(request,"div.html",{"output":result})
class SubtractionView(View): 
    def get(self,request,*args,**kwargs):
        return render(request,"sub.html")
    def post(self,request,*args,**kwargs):
        n1=request.POST.get("num1")
        n2=request.POST.get("num2")
        result=int(n1)-int(n2)
        print(result)
        return render(request,"sub.html",{"output":result})
class FactorialView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"fact.html")    
    def post(self,request,*args,**kwargs):
        n=request.POST.get("num")
        fact=1
        for i in range(1,int(n)+1):
            fact=fact*i
        print(fact)
        return render(request,"fact.html",{"output":fact})

class LeapyearView(View):
    def get(self,request,*args,**kwargs) :
        return render(request,"leap.html")   
    def post(self,request,*args,**kwargs):
        n=request.POST.get("year")
        if (int(n)%100==0 and int(n)%400==0):
            result=(f"{n} is a leap year")
        elif(int(n)%100!=0 and int(n)%4==0):
            result=(f"{n} is a leap year")    
        else:
            result=("not a leap year")    
        return render(request,"leap.html",{"output":result})    
class EvennumberView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"even.html")
    def post(self,request,*args,**kwargs):
        n=request.POST.get("num")
        if int(n)%2==0:
            print(f"{n} is even")
        else:
            print(f"{n} is odd")    
        return render(request,"even.html")    
class PrimenumberView(View):
    def  get(self,request,*args,**kwargs):
        return render(request,"prime.html")
    def post(self,request,*args,**kwargs):
        n=request.POST.get("num")
        n=int(n)
        if (n)>1:
            for i in range(2,n):
                if n%i==0:
                    print(f"{n} is not prime")
                    break
                else:
                    print(f"{n} is prime no" )
                    break
                    
        else:
            print(f"{n} not prime")

        return render(request,"prime.html")     
class IndexView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"index.html")     
class BmiView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"bmi.html")      
    def post(self,request,*args,**kwargs):
        n1=request.POST.get("weight") 
        n2=request.POST.get("height")
        n1=int(n1)
        n2=int(n2)
        n2=n2/100
        result=(n1)/(n2)**2 
        return render(request,"bmi.html",{"out":result})  
class EmiView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"emi.html")   
    def post(self,request,*args,**kwargs):
        p=request.POST.get("amount")
        n=request.POST.get("year")
        r=request.POST.get("rate")
        p=int(p)
        n=int(n)
        r=int(r)
        r=r/12
        i=r/100
        n=n*12
        result=(p*i*(i+1)**n)/((1+i)**n-1)
        emi=round(result,0)
        total_payable_amount=emi*n
        total_interest_payable=total_payable_amount-p
        print(total_payable_amount)
        print(total_interest_payable)
        return render(request,"emi.html",{"out":result,
                                          "total_amount":total_payable_amount,
                                          "interest_amount":total_interest_payable})
    
    
