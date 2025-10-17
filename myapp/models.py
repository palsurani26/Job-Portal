from arrow import now
from django import forms
from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils import timezone
from jsonschema import ValidationError

class Demo(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=15)

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("Email couldn't be fetched!")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        return self.create_user(email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=30, unique=True)
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    img = models.CharField(max_length=255, null=True)
    phone = models.CharField(
        max_length=10,
        validators=[MinLengthValidator(10), MaxLengthValidator(10)],
        unique=True
    )
    address = models.ForeignKey('FullAddress', on_delete=models.CASCADE, blank=True, null=True, related_name="user_fullAddress")
    date_joined = models.DateTimeField(auto_now_add=True)
    
    # Add is_staff and is_active fields
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['firstname', 'lastname']

    def __str__(self):
        return f"{self.firstname} {self.lastname}"

class FullAddress(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="FullAddress")
    state = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    country = models.CharField(max_length=30, null=True)
    area = models.CharField(max_length=40)
    landmark = models.CharField(max_length=40, null=True)
    residency = models.CharField(max_length=30)
    house_no = models.CharField(max_length=10)
    pincode = models.CharField(max_length=8)

    def __str__(self):
        return f"{self.house_no}, {self.residency}, {self.area}, {self.city}, {self.state}"
    
    class Meta:
        verbose_name = 'Full Address'
        verbose_name_plural = 'Full Addresses'

class Enquiry(models.Model):
    name = models.CharField(max_length=60)
    contact = models.CharField(max_length=10)
    email = models.EmailField(max_length=30, default='suranipal11@example.com')  # Default value set here

    def __str__(self):
        return self.name

class Plan(models.Model):
    name = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Record(models.Model):
    name = models.CharField(max_length=255, default='Unnamed')  # Provide a default value
    email = models.EmailField()
   

    def __str__(self):
        return self.name

class OTP(models.Model):
    email = models.EmailField()
    otp = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    is_verified = models.BooleanField(default=False)

    def is_valid(self):
        # OTP is valid for 5 minutes
        return timezone.now() <= self.created_at + timezone.timedelta(minutes=5)
    
# models.py
from django.db import models

# models.py

class Job(models.Model):
    JOB_TYPE_CHOICES = [
        ('FT', 'Full Time'),
        ('PT', 'Part Time'),
        ('CT', 'Contract'),
        ('FL', 'Freelance'),
    ]

    title = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    job_type = models.CharField(max_length=2, choices=JOB_TYPE_CHOICES)
    description = models.TextField()
    who_can_apply = models.TextField()
    posted_at = models.DateTimeField(auto_now_add=True)
    last_date_to_apply = models.DateField(null=True, blank=True)

    def clean(self):
        # Ensure `posted_at` is not None
        if not self.posted_at:
            self.posted_at = now()

        # Validate the last date to apply
        if self.last_date_to_apply:
            if self.last_date_to_apply < self.posted_at.date():
                raise ValidationError("Last date to apply must be after the posted date.")

    def __str__(self):
        return self.title

class ApplyJob(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()



class JobApplication(models.Model):
    job = models.ForeignKey(
    Job, on_delete=models.CASCADE, related_name='applications', null=True, blank=True
)

      # Link application to a specific job
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()
    highest_qualification = models.CharField(max_length=50)
    course_specialization = models.CharField(max_length=200)
    experience = models.CharField(max_length=10)
    company = models.CharField(max_length=100, blank=True, null=True)
    cv = models.FileField(upload_to='cv_uploads/')  # Upload directory for CVs
    applied_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname} applied for {self.job.title}"
from django.db import models

class ApplyJobApplication(models.Model):
    # Example fields
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField()
    company = models.CharField(max_length=100)
    location = models.CharField(max_length=100)  # Make sure this exists
    job_type = models.CharField(max_length=50)  # Make sure this exists
    job_description = models.TextField()  # Make sure this exists
    cv = models.FileField(upload_to='cvs/')  # Adjust upload path as needed

    def __str__(self):
        return f"{self.firstname} {self.lastname} - {self.company}"


    

