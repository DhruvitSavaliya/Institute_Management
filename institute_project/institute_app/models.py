from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)

    USERNAME_FIELD='email'
    REQUIRED_FIELDS= ['username']

    def __str__(self):
        return self.email

class Student(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    roll_no = models.CharField(max_length=20)
    department = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Teacher(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    subject = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(max_length=100,unique=True)
    code = models.CharField(max_length=10,unique=True)
    description = models.TextField(blank=True,null=True)

    def __str__(self):
        return self.name
    
class Campus(models.Model):
    name = models.CharField(max_length=100,unique=True)
    code = models.CharField(max_length=10,unique=True)
    address = models.TextField()
    city = models.CharField(max_length=50)
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=10,blank=True,null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}-{self.city}"


class Club(models.Model):
    name = models.CharField(max_length=100,unique=True)
    description = models.TextField()
    president = models.ForeignKey('Student',on_delete=models.SET_NULL,null=True,related_name='club_president')
    faculty_incharge = models.ForeignKey('Teacher',on_delete=models.SET_NULL,null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Parent(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    address = models.TextField()
    student = models.ForeignKey('Student',on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} (Parent of {self.student.name})"
    
class LibraryBook(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13, unique=True)
    published_date = models.DateField()
    available_copies = models.PositiveIntegerField(default=1)
    total_copies = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.title} by {self.author}"

class Routine(models.Model):
    class_name = models.CharField(max_length=50)
    subject = models.CharField(max_length=100)
    teacher = models.ForeignKey('Teacher', on_delete=models.CASCADE)
    day_of_week = models.CharField(max_length=10, choices=[
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
    ])
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.class_name} - {self.subject} ({self.day_of_week})"
    
class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    venue = models.CharField(max_length=100)
    organized_by = models.ForeignKey('Club', on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(upload_to='event_images/', null=True, blank=True)  # <-- image field

    def __str__(self):
        return self.title