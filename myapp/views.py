<<<<<<< HEAD
from ast import Not
import email
=======
>>>>>>> f354554 (merge conflict resolved)
from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponseRedirect


# Start of prajwal code
def user_login(request):
    if not request.user.is_authenticated:
        # get the parameter
        if request.method == "POST":
            loginusername = request.POST.get('loginusername')
            loginpass = request.POST.get('loginpass')

       

        #user

        #for login using email or username 
            try:
                user = authenticate(username=User.objects.get(email=loginusername),password=loginpass)
            except:
                user = authenticate(username=loginusername,password=loginpass)

            

            if user is not None:
                login(request,user)
                messages.success(request,"You have successfully logged in !")
                return redirect('/')

            else:
                messages.warning(request,"Invalid Credentials! Please enter correct username or password !")
                return redirect('/')
        return render(request,'login.html')
    else:
        return redirect('profile')




def user_signup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if len(username) <= 2:
            messages.warning(request,"Username must be 3 to 14 character long!")
            return redirect('signup')

        if len(username) >= 15:
            messages.warning(request,"Username must be 3 to 14 character long!")
            return redirect('signup')


        if pass1 != pass2:
            messages.warning(request,"Password's should be match!")
            return redirect('signup')

        #for unique username
        if User.objects.filter(username = username).first():
            messages.warning(request, "This username is already taken")
            return redirect('signup')

        #for unique email
        if User.objects.filter(email = email).first():
            messages.warning(request, "This email is already taken")
            return redirect('signup')

        if len(pass1 and pass2) < 8:
            messages.warning(request,"Password's should be 8 character long!")
            return redirect('signup')


        # create the user
        myuser = User.objects.create_user(username,email,pass1)
        myuser.save()     
        messages.success(request,"Your Account Has Been Created")
        # messages.success(request,"An activation mail sent to your email") #Added - 15/09/2022
        return redirect('login')
        
    
    return render(request,'signup.html')





def user_profile(request):
    if request.user.is_anonymous:
        return redirect('login')
    else:
        return render(request,'profile.html')




def user_logout(request):
    logout(request)
    messages.success(request,"You have been logged out !")

    return redirect('/')
# End of prajwal code





                                # NEwtonschool Code for Email activation

# def user_login(request):
#     if request.method == 'POST':
#         loginusername = request.POST.get('loginusername')
#         loginpass = request.POST.get('loginpass')


#         try:
#             user_obj = authenticate(username=User.objects.get(email=loginusername),password=loginpass)
#         except:
#             user_obj = authenticate(username=loginusername,password=loginpass)

#         user_obj = User.objects.filter(username = email).first()

#         # if not user_obj.exists():
#         #     messages.warning(request,"Acccount not found !")
#         #     return HttpResponseRedirect(request.path_info)

#         if not user_obj[0].profile.is_email_verified:
#             messages.warning(request,"Please verify your account")
#             return HttpResponseRedirect(request.path_info)


#         # user_obj = authenticate(username = email, password  = pass1)
#         if user_obj:
#             login(request, user_obj)
#             return redirect('/')
        
#         messages.warning(request,"Invalid credentials")
#         return HttpResponseRedirect(request.path_info)
    
#     return render(request, 'login.html')


# def user_signup(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         email = request.POST.get('email')
#         pass1 = request.POST.get('pass1')
#         pass2 = request.POST.get('pass2')

#         #for login using email or username 
        

#         user_obj = User.objects.filter(username = email)
#         if user_obj.exists():
#             messages.warning(request,"Email is already taken !")
#             return HttpResponseRedirect(request.path_info)

#         user_obj = User.objects.create(username = username, email = email)
#         user_obj.set_password(pass1)
#         user_obj.save()
#         messages.success(request,"An activation mail sent to your email")
#         return HttpResponseRedirect(request.path_info)

    

#     return render(request, 'signup.html')

                                                # End of newtonschool Code










# not using this

# def forgot_password(request):
#     if request.method == "POST":
#         username = request.POST.get('username')
#         if not User.objects.filter(username=username):
#             messages.warning(request,"No user found with this username.")
#             return redirect('forgot_password')

#         user_obj = User.objects.get(username=username)
#         token = str(uuid.uuid4())
#         send_forgot_password_mail(user_obj, token)
#         messages.warning(request,"Email has been sent to registered email.")
#         return redirect('forgot_password')

#     return render(request,'forgot_password.html')


# not using this
# def change_password(request,token):
#     context = {}
#     profile_obj = Profile.objects.get(fogot_password_token = token)
#     print(profile_obj)
#     return render(request,'change_password.html')
<<<<<<< HEAD
=======
from ast import Not
import email
from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib import messages

# from myapp.models import Profile
# from .helpers import send_forgot_password_mail
# import uuid

# Create your views here.
def user_login(request):
    if not request.user.is_authenticated:
        # get the parameter
        if request.method == "POST":
            loginusername = request.POST.get('loginusername')
            loginpass = request.POST.get('loginpass')

        #user

        #for login using email or username 
            try:
                user = authenticate(username=User.objects.get(email=loginusername),password=loginpass)
            except:
                user = authenticate(username=loginusername,password=loginpass)

            if user is not None:
                login(request,user)
                messages.success(request,"You have successfully logged in !")
                return redirect('/')

            else:
                messages.warning(request,"Invalid Credentials! Please enter correct username or password !")
                return redirect('/')

       


               



        return render(request,'login.html')
    else:
        return redirect('profile')



def user_signup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if len(username) <= 3:
            messages.warning(request,"Username must be 3 to 13 character long!")
            return redirect('signup')

        if len(username) >= 12:
            messages.warning(request,"Username must be 3 to 13 character long!")
            return redirect('signup')


        if pass1 != pass2:
            messages.warning(request,"Password's should be match!")
            return redirect('signup')

        #for unique username
        if User.objects.filter(username = username).first():
            messages.warning(request, "This username is already taken")
            return redirect('signup')

        #for unique email
        if User.objects.filter(email = email).first():
            messages.warning(request, "This email is already taken")
            return redirect('signup')

        if len(pass1 and pass2) < 8:
            messages.warning(request,"Password's should be 8 character long!")
            return redirect('signup')


        # create the user
        myuser = User.objects.create_user(username,email,pass1)
        myuser.save()     
        messages.success(request,"Your Account Has Been Created")
        return redirect('login')
        
    
    return render(request,'signup.html')





def user_profile(request):
    if request.user.is_anonymous:
        return redirect('login')
    else:
        return render(request,'profile.html')




def user_logout(request):
    logout(request)
    messages.success(request,"You have been logged out !")

    return redirect('/')



# not using this

# def forgot_password(request):
#     if request.method == "POST":
#         username = request.POST.get('username')
#         if not User.objects.filter(username=username):
#             messages.warning(request,"No user found with this username.")
#             return redirect('forgot_password')

#         user_obj = User.objects.get(username=username)
#         token = str(uuid.uuid4())
#         send_forgot_password_mail(user_obj, token)
#         messages.warning(request,"Email has been sent to registered email.")
#         return redirect('forgot_password')

#     return render(request,'forgot_password.html')

# not using this
# def change_password(request,token):
#     context = {}
#     profile_obj = Profile.objects.get(fogot_password_token = token)
#     print(profile_obj)
#     return render(request,'change_password.html')
>>>>>>> f354554 (merge conflict resolved)
