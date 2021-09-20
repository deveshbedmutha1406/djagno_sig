from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Person
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.

# def trial(reuest):
#     # user = User.objects.create_user(username="Devesh",password="dev123")
#     user = User.objects.get(username='django')
#     phone = Person.objects.get(user_id = user.id)
#     print(phone)
#     user.email = 'de@gmail.com'
#     user.save()
#     print(user.email)
#     return render(request, "users/signup.html",)

def check_phone(a):
    for person in Person.objects.all():
        if(person.phone_no==a):
            return True
    return False

def check_user(a):
    for user in User.objects.all():
        if a== user.username:
            
            return True
    return False

def check_email(a):
    for user in User.objects.all():
        if(a== user.email):
            return True
    return False

def check_pass(a,b):
    if len(a)<8:
        return True
    pass        

# @login_required(redirect_field_name='login')

def signup(request):

    if request.method == "POST":
        uname = request.POST['uname']
        fname = request.POST['fname']
        lname = request.POST['lname']
        emailid = request.POST['email_id']
        pass1 = request.POST['pass1']
        phone = request.POST['phone_number']
        gender1 = request.POST['gender_data']
        pass2 = request.POST['pass2']

        context = {

        }

        
        if check_user(uname):
            context['username_error'] = 'user already exits'
            print(len(context))


        if check_email(emailid):
            context['email_error'] = 'email already registered'
            print(len(context))

        if check_phone(phone):
            context['phone_error'] = 'Phone number already registered'

        if len(context) != 0:
            return render(request, 'users/signup.html', context)


        

        user = User.objects.create_user(username=uname,first_name=fname,last_name=lname,email=emailid,password=pass1)

        user1 = User.objects.get(username=uname)
        print(user1)
        user2 = Person(phone_no=phone,user_id=user1,gender=gender1)
        user2.save()
        print(user2)
        return render(request, 'users/signup.html')

    return render(request, 'users/signup.html')


def loginpage(request):

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            user1 = User.objects.get(username=username)
            print(user1.email)
   
            return render(request, 'users/home.html',{'user1':user1})

        else:
            return render(request, 'users/login.html',{'error':'invlaid username'})

    return render(request, 'users/login.html')