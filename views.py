from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

from shop.models import wings

# Create your views here.
def foam(request):
   return render(request,'templates\shop\index.html')

def main(request):
   if request.method=="POST":
      add=request.POST['fadd'],
      point=request.POST['fpoint'],
      description=request.POST['fdescription'],
      wings(fadd=add,fpoint=point,fdescription=description),
      wings.save(),
      
   return render(request,'templates/shop/tracker.html')
    
def handlelogin(request):
   if request.method=='POST':
      loginusername=request.POST['loginusername']
      loginpassword=request.POST['loginpassword']
      user=authenticate(username=loginusername,password=loginpassword)
      
      if user is  not None:
         login(request,user)
         messages.success(request,'Successfiully loggieni')
         return redirect('wings')
      else:
         messages.error(request,"Invalid")
         return redirect('')
      
      
      
   return HttpResponse('handlelogin')



def handlelogout(request):
   logout(request)
   messages.success(request,'logged out')
   return redirect('/')




def handlesignup(request):
   if request.method=='POST':
      username=request.POST['username']
      fname=request.POST['fname']
      lastname=request.POST['lastname']
      email=request.POST['email']
      pass1=request.POST['pass1']
      pass2=request.POST['pass2']
      
      myuser=User.objects.create_user(username,email,pass1)
      myuser.firstname=fname
      myuser.lastname=lastname
      myuser.password=pass1
      myuser.save()
      messages.success(request,'your account has crreated')
      return redirect('/wings')
   else:
      return HttpResponse('error 404s')
      
      
      
      

   
   
   
      
        