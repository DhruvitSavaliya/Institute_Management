from django.contrib import admin
from .models import Student,Teacher,Department,Campus,Club,Parent,LibraryBook,Routine,Event

# Register your models here.

admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Department)
admin.site.register(Campus)
admin.site.register(Club)
admin.site.register(Parent)
admin.site.register(LibraryBook)
admin.site.register(Routine)
admin.site.register(Event)