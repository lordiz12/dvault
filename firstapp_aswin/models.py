from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Sign_in(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    def __str__(self):
        return self.username

class Sign_up(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    mobile = models.IntegerField()
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=255)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    def __str__(self):
        return self.first_name


class HealthRecord(models.Model):
    foreignkey = models.ForeignKey(Sign_in, on_delete=models.CASCADE,blank=True,null=True)
    fullname = models.CharField(max_length=100)
    dob = models.DateField()
    age = models.IntegerField()
    gender = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')])
    conditions = models.TextField(blank=True)
    allergies = models.TextField(blank=True)
    medications = models.TextField(blank=True)
    surgeries = models.TextField(blank=True)
    family_history = models.TextField(blank=True)
    symptoms = models.TextField(blank=True)
    symptoms_duration = models.CharField(max_length=100, blank=True)
    symptoms_severity = models.CharField(max_length=100, blank=True)
    diet = models.TextField(blank=True)
    exercise = models.TextField(blank=True)
    insurance_provider = models.CharField(max_length=100, blank=True)
    policy_number = models.CharField(max_length=100, blank=True)
    emergency_name = models.CharField(max_length=100, blank=True)
    emergency_relationship = models.CharField(max_length=100, blank=True)
    emergency_phone = models.CharField(max_length=20, blank=True)
    additional_comments = models.TextField(blank=True)
    def __str__(self):
        return self.fullname

class FinancialDetails(models.Model):
    foreignkey = models.ForeignKey(Sign_in, on_delete=models.CASCADE)
    income = models.DecimalField(max_digits=15, decimal_places=2)
    savings = models.DecimalField(max_digits=15, decimal_places=2)
    assets = models.DecimalField(max_digits=15, decimal_places=2)
    debts = models.DecimalField(max_digits=15, decimal_places=2)
    expenses = models.DecimalField(max_digits=15, decimal_places=2)
    credit_score = models.CharField(max_length=20, blank=True)
    aadhar_no = models.CharField(max_length=12, blank=True)
    pan_no = models.CharField(max_length=10, blank=True)
    bank_account_no = models.CharField(max_length=20)
    credit_card_no = models.CharField(max_length=20)
    additional_info = models.TextField(blank=True)

    

class EducationalDetails(models.Model):
    foreignkey = models.ForeignKey(Sign_in, on_delete=models.CASCADE)
    degree = models.CharField(max_length=100)
    university = models.CharField(max_length=100)
    major = models.CharField(max_length=100)
    graduation_year = models.CharField(max_length=4)
    gpa = models.CharField(max_length=10, blank=True)
    twelth_marks_percentage = models.CharField(max_length=10, blank=True)
    tenth_marks_percentage = models.CharField(max_length=10, blank=True)
    certifications = models.TextField(blank=True)
    additional_info = models.TextField(blank=True)

    def __str__(self):
        return self.degree


