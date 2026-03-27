from django.shortcuts import render, redirect
from APP.models import review, registr
from django.conf import settings
from django.contrib import messages
import re
from random import randint
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse


@csrf_exempt
def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        return JsonResponse({"status": "success"})


def otp_verify(request):
    return render(request, "otp.html")


def index(request):
    if request.method == "POST":
        val = request.POST.get("log")

        if val == "reg":
            if registr.objects.filter(email=request.POST.get("gmaill")).exists():
                return render(request, "index.html", {"e_msg": 1})
            else:
                name = request.POST.get("namee")
                email = request.POST.get("gmaill")
                password = request.POST.get("password")
                cpassword = request.POST.get("cpassword")
                pin = request.POST.get("spin")

                if name == "":
                    return render(request, "index.html", {"name_empty": 3})
                if email == "":
                    return render(request, "index.html", {"email_empty": 4})
                if password == "":
                    return render(request, "index.html", {"password_empty": 5})
                if cpassword == "":
                    return render(request, "index.html", {"cpassword_empty": 6})
                if pin == "":
                    return render(request, "index.html", {"pin_empty": 10})
                if not re.search("[0-9]", pin):
                    return render(request, "index.html", {"pin_int": 12})
                if len(str(pin)) < 4 or len(str(pin)) > 4:
                    return render(request, "index.html", {"pin_length": 11})

                if password == cpassword:
                    x = registr()
                    x.name = name
                    x.email = email
                    x.password = password
                    x.status = "activate"
                    x.pin = pin
                    x.save()
                    messages.success(request, "Successfully Registered. Please Login !!!")
                    return redirect("/login/")
                else:
                    return render(request, "index.html", {"pass_invalid": 7})

        elif val == "log":
            user = registr.objects.filter(
                email=request.POST.get("login_mail"),
                password=request.POST.get("login_password"),
            )
            if len(user) > 0:
                request.session['l_user'] = request.POST.get("login_mail")
                return redirect("/pin/")
            else:
                return render(request, "index.html", {"invalid_user": 9})
    else:
        return render(request, "index.html")


def dashboard(request):
    return render(request, 'dashboard.html')


def dashboard_s(request):
    return render(request, 'dashboard_s.html')


def pin(request):
    if request.method == "POST":
        user = registr.objects.filter(
            email=request.session["l_user"], pin=request.POST.get("pin")
        )
        if len(user) > 0:
            return redirect("/dashboard_s/")
        else:
            messages.error(request, "Invalid Security PIN !!!")
            return render(request, "pin.html")
    else:
        return render(request, "pin.html")


def logout(request):
    del request.session['l_user']
    return redirect('/')


def login_page(request):
    if request.method == "POST":
        user = registr.objects.filter(
            email=request.POST.get("login_email"),
            password=request.POST.get("login_pass"),
        )
        if len(user) > 0:
            request.session["l_user"] = request.POST.get("login_email")
            return redirect("/pin/")
        else:
            messages.error(request, "Invalid Email or Password")
            return render(request, "loginpage.html")
    else:
        return render(request, "loginpage.html")


def email_enter(request):
    return render(request, "enteremail.html")


def user_profile(request):
    user = registr.objects.get(email=request.session['l_user'])
    u_name = user.name
    u_email = user.email
    return render(request, 'userprofile.html', {'name': u_name, 'email': u_email})


def tesla(request):
    if not request.session.has_key('l_user'):
        return redirect('/')
    return render(request, 'tesla.html')


def apple(request):
    if not request.session.has_key('l_user'):
        return redirect('/')
    return render(request, 'apple.html')


def microsoft(request):
    if not request.session.has_key('l_user'):
        return redirect('/')
    return render(request, 'microsoft.html')


def visa(request):
    if not request.session.has_key('l_user'):
        return redirect('/')
    return render(request, 'visa.html')


def unitedhealth(request):
    if not request.session.has_key('l_user'):
        return redirect('/')
    return render(request, 'unitedhealth.html')


def cocacola(request):
    if not request.session.has_key('l_user'):
        return redirect('/')
    return render(request, 'cocacola.html')


def pg(request):
    if not request.session.has_key('l_user'):
        return redirect('/')
    return render(request, 'pg.html')


def chevron(request):
    if not request.session.has_key('l_user'):
        return redirect('/')
    return render(request, 'chevron.html')


def cisco(request):
    if not request.session.has_key('l_user'):
        return redirect('/')
    return render(request, 'cisco.html')


def intel(request):
    if not request.session.has_key('l_user'):
        return redirect('/')
    return render(request, 'intel.html')


def disney(request):
    if not request.session.has_key('l_user'):
        return redirect('/')
    return render(request, 'disney.html')


def jpmorgan(request):
    if not request.session.has_key('l_user'):
        return redirect('/')
    return render(request, 'jpmorgan.html')


def mastercard(request):
    if not request.session.has_key('l_user'):
        return redirect('/')
    return render(request, 'mastercard.html')


def adeia(request):
    if not request.session.has_key('l_user'):
        return redirect('/')
    return render(request, 'adeia.html')


def albertsons(request):
    if not request.session.has_key('l_user'):
        return redirect('/')
    return render(request, 'albertsons.html')


def aceglobal(request):
    if not request.session.has_key('l_user'):
        return redirect('/')
    return render(request, 'aceglobal.html')


def d3system(request):
    if not request.session.has_key('l_user'):
        return redirect('/')
    return render(request, 'd3system.html')


def google(request):
    if not request.session.has_key('l_user'):
        return redirect('/')
    return render(request, 'google.html')


def a10(request):
    if not request.session.has_key('l_user'):
        return redirect('/')
    return render(request, 'a10.html')


def amazon(request):
    if not request.session.has_key('l_user'):
        return redirect('/')
    return render(request, 'amazon.html')