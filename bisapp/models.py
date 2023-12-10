from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth.models import User
from django.conf import settings
import uuid
from django.utils import timezone

from datetime import datetime

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    userID = models.CharField(max_length=20, unique=True, blank=False, null=False ,default='')  

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def save(self, *args, **kwargs):
        if not self.userID:
           
            self.userID = self.generate_unique_userid()
        super().save(*args, **kwargs)

    def generate_unique_userid(self):
       
        import uuid
        return str(uuid.uuid4())[:20]

    def __str__(self):
        return self.email

class DocumentRequest(models.Model):
    PENDING = 'Pending'
    APPROVED = 'Approved'
    REJECTED = 'Rejected'

    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (APPROVED, 'Approved'),
        (REJECTED, 'Rejected'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    document_id = models.CharField(max_length=20, unique=True, blank=False, null=True, default=None)  
    document_type = models.CharField(max_length=50, choices=[
        ('Certificate', 'Certificate'),
        ('Clearance', 'Clearance'),
        ('Indigency', 'Indigency'),
        ('BarangayID', 'BarangayID'),
    ])
    delivery_date = models.DateField()
    payment_type = models.CharField(max_length=50, choices=[
        ('credit_card', 'Credit Card'),
        ('Gcash', 'Gcash'),
        ('cash', 'Cash'),
    ])
    purpose = models.CharField(max_length=50, choices=[
        ('Business', 'Business'),
        ('Personal', 'Personal'),
        ('Others', 'Others'),
    ])
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=PENDING)

    def save(self, *args, **kwargs):
        if not self.document_id:
            self.document_id = self.generate_unique_document_id()
        super().save(*args, **kwargs)

    def generate_unique_document_id(self):
        import uuid
        return str(uuid.uuid4())[:20]

    def __str__(self):
        return f"document_id-{self.document_id}"




    


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    extension = models.CharField(max_length=100, blank=True, null=True)
    birthdate = models.DateField(null=True, blank=True)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    address = models.CharField(max_length=255)
    gender = models.CharField(max_length=10)




    
    
class IncidentReport(models.Model):
    UNDER_REVIEW = 'Under Review'
    RECORDED = 'Recorded'
    DISAPPROVED = 'Disapproved'

    STATUS_CHOICES = [
        (UNDER_REVIEW, 'Under Review'),
        (RECORDED, 'Recorded'),
        (DISAPPROVED, 'Disapproved'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    reporter_id = models.CharField(max_length=20, unique=True, blank=False, null=True, default=None)
    resident_name = models.CharField(max_length=100, null=False, default='')
    incident_date = models.DateField()
    incident_type = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default=UNDER_REVIEW)
    report_date = models.DateTimeField(default=timezone.now, blank=True)

    def save(self, *args, **kwargs):
        if not self.reporter_id:
            self.reporter_id = self.generate_unique_reporter_id()
        super().save(*args, **kwargs)

    def generate_unique_reporter_id(self):
        import uuid
        return str(uuid.uuid4())[:20]

    def __str__(self):
        return f"reporter_id-{self.reporter_id}"
    


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name