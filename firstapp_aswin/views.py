from django.shortcuts import render, redirect
from firstapp_aswin.models import Sign_in,Sign_up,HealthRecord,FinancialDetails,EducationalDetails
from django.contrib.auth.models import User
from django.core.exceptions import MultipleObjectsReturned
from django.http import HttpResponse
from django.contrib.auth import logout


# Create your views here.



def home(request):
    return render(request,'index.html')

def sign_up(request):
    return render(request,'signup.html')

def sign_in(request):
    return render(request,'login.html')

def health_form(request):
    return render(request,'health_form.html')

def edu_form(request):
    return render(request,'educational_form.html')


def financial_form(request):
    return render(request,'financial_form.html')

def success_page(request):
    return render(request,'success.html')

def profile_page(request):
    return render(request,"profile.html")

def healthshowdetails(request):
    return render(request,"healthdata.html")

def financialdatadetails(request):
    return render(request,"financialdata.html")

def edcationaldatadetails(request):
    return render(request,"educationaldata.html")


""" def sign_up_form(request):
    if request.method=="POST":
        a = request.POST["fname"]
        b = request.POST["lname"]
        c = request.POST["mob"]
        d = request.POST["email"]
        g = request.POST["address"]
        e = request.POST["uname"]
        f = request.POST["password"]
        
        h = Sign_in(username = e,password = f)
        h.save()
        m = Sign_up(first_name = a,last_name = b,mobile = c,email = d, address = g,username = e,password = f)
        m.save()
        return render(request,'success.html')

    return render(request, 'signup.html') """



def sign_up_form(request):
    if request.method == "POST":
        a = request.POST["fname"]
        b = request.POST["lname"]
        c = request.POST["mob"]
        d = request.POST["email"]
        g = request.POST["address"]
        e = request.POST["uname"]
        f = request.POST["password"]

        try:
       
            exist_user = Sign_in.objects.get(username=e)
            return render(request, 'error.html', {'error_message': 'Username already exists'})
        except:
            h = Sign_in(username=e, password=f)
            h.save()
            m = Sign_up(first_name=a, last_name=b, mobile=c, email=d, address=g, username=e, password=f)
            m.save()
            return render(request, 'success.html')

    return render(request, 'signup.html')



def login_form(request):
    try:
        if request.method == "POST":
            a = request.POST["user"]
            b = request.POST["pass"]

            # Using filter instead of get to handle multiple users with the same username
            users_with_username = Sign_in.objects.filter(username=a)

            if not users_with_username.exists():
                return render(request, "error.html", {'error_message': 'User not found'})

            if users_with_username.count() > 1:
                # Handle the case where multiple users have the same username
                return render(request, "error.html", {'error_message': 'Multiple users with the same username'})

            q = users_with_username.first()

            if q.password == b:
                request.session["member_id"] = q.id
                return render(request, "profile.html")
            else:
                return render(request, "error.html", {'error_message': 'Incorrect password'})
    except MultipleObjectsReturned:
        # Handle the case where multiple objects were returned unexpectedly
        return render(request, "error.html", {'error_message': 'Error: Multiple objects returned for the same username'})

""" def login_form(request):
    try:
        if request.method=="POST":
          a = request.POST["user"]
          b = request.POST["pass"]
          q = Sign_in.objects.get(username=a)
        if q.password==b:
            request.session["member_id"]=q.id
            return render(request,"profile.html")
           
        else:
            return render(request,"error.html")
    except Sign_in.DoesNotExist:
        return render(request,"error.html") """
        
def lout(request):
    logout(request)
    return redirect ("home")
  


def profile_data(request):
    data = Sign_up.objects.get(id=request.session["member_id"])
    instance = Sign_in.objects.get(id=request.session["member_id"])
    data1 = HealthRecord.objects.get(foreignkey=instance)
    instance = Sign_in.objects.get(id=request.session["member_id"])
    data2 = FinancialDetails.objects.get(foreignkey=instance)
    instance = Sign_in.objects.get(id=request.session["member_id"])
    data3 = EducationalDetails.objects.get(foreignkey=instance)
    return render(request, 'userdata.html', {'profiledata': data,'healthdata': data1,'financialdata': data2,'educationaldata': data3})


def health_formdata(request):
    if request.method=="POST":
        a = request.POST["name"]
        b = request.POST["dob"]
        c = request.POST["age"]
        d = request.POST["gender"]
        e = request.POST["conditions"]
        f = request.POST["allergies"]
        g = request.POST["medications"]
        h = request.POST["surgeries"]
        i = request.POST["family_history"]
        j = request.POST["symptoms"]
        k = request.POST["symptoms_duration"]
        l = request.POST["symptoms_severity"]
        m = request.POST["diet"]
        n = request.POST["exercise"]
        q = request.POST["insurance_provider"]
        r = request.POST["policy_number"]
        s = request.POST["emergency_name"]
        t = request.POST["emergency_relationship"]
        u = request.POST["emergency_phone"]
        v = request.POST["additional_comments"]

        foreign_key_instance = Sign_in.objects.get(pk=request.session["member_id"])


        w = HealthRecord(foreignkey=foreign_key_instance,fullname = a,dob = b,age = c,gender = d,conditions = e,allergies = f,medications = g,surgeries = h,family_history = i,symptoms = j,symptoms_duration = k,symptoms_severity = l,diet = m,exercise = n,insurance_provider = q,policy_number = r,emergency_name = s,emergency_relationship = t,emergency_phone = u,additional_comments = v)
        w.save()
        return render(request,'success.html')

    return render(request, 'health_form.html')

def financial_formdata(request):
    if request.method=="POST":
        a = request.POST["income"]
        b = request.POST["savings"]
        c = request.POST["assets"]
        d = request.POST["debts"]
        e = request.POST["expenses"]
        f = request.POST["credit_score"]
        g = request.POST["aadhar_no"]
        h = request.POST["pan_no"]
        i = request.POST["bank_account"]
        j = request.POST["credit_card"]
        k = request.POST["additional_info"]


        foreign_key_instance = Sign_in.objects.get(pk=request.session["member_id"])


        w = FinancialDetails(foreignkey=foreign_key_instance,income = a,savings = b,assets = c,debts = d,expenses = e,credit_score = f,aadhar_no = g,pan_no = h,bank_account_no = i,credit_card_no = j,additional_info = k)
        w.save()
        return render(request,'success.html')

    return render(request, 'financial_form.html')


def educational_formdata(request):
    if request.method=="POST":
        a = request.POST["degree"]
        b = request.POST["university"]
        c = request.POST["major"]
        d = request.POST["graduation_year"]
        e = request.POST["gpa"]
        f = request.POST["twelth"]
        g = request.POST["tenth"]
        h = request.POST["certifications"]
        i = request.POST["additional_info"]


        foreign_key_instance = Sign_in.objects.get(pk=request.session["member_id"])


        w = EducationalDetails(foreignkey=foreign_key_instance,degree = a,university = b,major = c,graduation_year = d,gpa = e,twelth_marks_percentage = f,tenth_marks_percentage = g,certifications = h,additional_info = i)
        w.save()
        return render(request,'success.html')

    return render(request, 'educational_form.html')


