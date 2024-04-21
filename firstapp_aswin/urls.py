from django.urls import path
from firstapp_aswin import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", views.home, name="home"),
    path("home", views.home, name="home"),
    path("sign_up", views.sign_up, name="sign_up"),
    path("sign_in", views.sign_in, name="sign_in"),
    path("sign_up_form", views.sign_up_form, name="sign_up_form"),
    path("profile", views.profile_page, name="profile"),
    path("healthdatapage", views.healthshowdetails, name="heathshowdetails"),
    path("financialdatapage", views.financialdatadetails, name="financialdatadetails"),
    path("educationaldatapage", views.edcationaldatadetails, name="educationaldatadetails"),
    path("login_form", views.login_form, name="login_form"),
    path("logout", views.lout, name="lout"),
    path("user_data", views.profile_data, name="profile_data"),
    path("health", views.health_form, name="health_form"),
    path("healthformdata", views.health_formdata, name="health_formdata"),
    path("education", views.edu_form, name="edu_form"),
    path("educationalformdata", views.educational_formdata, name="educational_formdata"),
    path("financial", views.financial_form, name="financial_form"),
    path("financialformdata", views.financial_formdata, name="financial_formdata"),
    path("success", views.success_page, name="success_page"),


    

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

