from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,login,logout,get_user_model
from django.contrib.auth.decorators import login_required
from .models import Student,Teacher,Department,Campus,Club,Parent,LibraryBook,Routine,Event
from .forms import RegisterForm,ProfileUpdateForm,StudentForm,TeacherForm,DepartmentForm,CampusForm,ClubForm,ParentForm,LibraryBookForm,RoutineForm,EventForm
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.contrib import messages
from django.utils.crypto import get_random_string
from django.conf import settings

# Create your views here.

User = get_user_model()

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)  # type: ignore
        if user:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Invalid email or password'})
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def home_view(request):
    context = {
        'Students': Student.objects.count(),
        'Teachers': Teacher.objects.count(),
        'Departments': Department.objects.count(),
        'Campuses': Campus.objects.count(),
        'Clubs': Club.objects.count(),
        'Parents': Parent.objects.count(),
        'Books': LibraryBook.objects.count(),
        'Routines': Routine.objects.count(),
        'Events': Event.objects.count(),
        'EventsImages' : Event.objects.all(),
        'routines' : Routine.objects.all(),
    }
    return render(request, 'institute_app/dashboard.html', context)

@login_required
def manage_profile(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully!")
            return redirect('home')
    else:
        form = ProfileUpdateForm(instance=request.user)
    return render(request, 'institute_app/manage_profile.html', {'form': form})

# def forgot_password(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         try:
#             user = User.objects.get(email=email)
#             new_password = get_random_string(length=8)
#             user.set_password(new_password)
#             user.save()

#             # Send email
#             send_mail(
#                 subject='Your New Password - Institute Management System',
#                 message=f'Hello {user.username},\n\nYour new password is: {new_password}\n\nPlease change it after logging in.',
#                 from_email=settings.EMAIL_HOST_USER,
#                 recipient_list=[email],
#                 fail_silently=False,
#             )

#             messages.success(request, 'A new password has been sent to your email.')
#             return redirect('login')

#         except User.DoesNotExist:
#             messages.error(request, 'No user is associated with this email.')

#     return render(request, 'forgot_password.html')


def add_student(request):
    form = StudentForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Student added successfully!")
        return redirect('manage_student')
    return render(request,'institute_app/add_student.html', {'form':form })

def manage_student(request):
    students = Student.objects.all()
    return render(request, 'institute_app/manage_student.html', {'students': students})  

def update_student(request,id):
    if request.method=='POST':
        pi = Student.objects.get(pk=id)
        fm = StudentForm(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
            messages.success(request, "Student updated successfully!")
            return redirect('manage_student')
    else:
        pi = Student.objects.get(pk=id)
        fm = StudentForm(instance=pi)
    return render(request,'institute_app/update_student.html', {'form':fm}) 

def delete_student(request, id):
    student = get_object_or_404(Student , pk=id)

    if request.method == 'POST':
        confirm = request.POST.get('confirm')
        if confirm == 'Y':
            student.delete()
            messages.success(request, "Student deleted successfully.")
            return redirect('manage_student')  # Or your preferred URL
        else:
            messages.info(request, "Deletion cancelled.")
            return redirect('manage_student')
    return render(request, 'institute_app/confirm_delete_student.html', {'student': student})

def add_teacher(request):
    form = TeacherForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Teacher added successfully!")
        return redirect('manage_teacher')
    return render(request,'institute_app/add_teacher.html', {'form':form})

def manage_teacher(request):
    teachers = Teacher.objects.all()
    return render(request,'institute_app/manage_teacher.html', {'teachers':teachers})

def update_teacher(request,id):
    if request.method=='POST':
        pi = Teacher.objects.get(pk=id)
        fm = TeacherForm(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
            messages.success(request, "Teacher updated successfully!")
            return redirect('manage_teacher')
    else:
        pi = Teacher.objects.get(pk=id)
        fm = TeacherForm(instance=pi)
    return render(request,'institute_app/update_teacher.html', {'form':fm})

def delete_teacher(request, id):
    teacher = get_object_or_404(Teacher , pk=id)

    if request.method == 'POST':
        confirm = request.POST.get('confirm')
        if confirm == 'Y':
            teacher.delete()
            messages.success(request, "Teacher deleted successfully.")
            return redirect('manage_teacher')  # Or your preferred URL
        else:
            messages.info(request, "Deletion cancelled.")
            return redirect('manage_teacher')
    return render(request, 'institute_app/confirm_delete_teacher.html', {'teacher': teacher})

def add_department(request):
    form = DepartmentForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Department added successfully!")
        return redirect('manage_department')
    return render(request,'institute_app/add_department.html', {'form' : form })

def manage_department(request):
    department = Department.objects.all()
    return render(request,'institute_app/manage_department.html', { 'departments' : department})

def update_department(request,id):
    if request.method=='POST':
        pi = Department.objects.get(pk=id)
        fm = DepartmentForm(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
            messages.success(request,'Department updated successfully!')
            return redirect('manage_department')
    else:
        pi = Department.objects.get(pk=id)
        fm = DepartmentForm(instance=pi)
    return render(request,'institute_app/update_department.html' , {'form' : fm })

def delete_department(request, id):
    department = get_object_or_404(Department , pk=id)

    if request.method == 'POST':
        confirm = request.POST.get('confirm')
        if confirm == 'Y':
            department.delete()
            messages.success(request, "Department deleted successfully.")
            return redirect('manage_department')  # Or your preferred URL
        else:
            messages.info(request, "Deletion cancelled.")
            return redirect('manage_department')
    return render(request, 'institute_app/confirm_delete_department.html', {'department': department})

def add_campus(request):
    form = CampusForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request,'Campus added successfully!')
        return redirect('manage_campus')
    return render(request,'institute_app/add_campus.html' , {'form' : form })

def manage_campus(request):
    campus = Campus.objects.all()
    return render(request,'institute_app/manage_campus.html', {'campus' : campus })

def update_campus(request,id):
    if request.method=='POST':
        pi = Campus.objects.get(pk=id)
        fm = CampusForm(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
            messages.success(request,'Campus updated successfully!')
            return redirect('manage_campus')
    else:
        pi = Campus.objects.get(pk=id)
        fm = CampusForm(instance=pi)
    return render(request,'institute_app/update_campus.html' , {'form': fm })

def delete_campus(request, id):
    campus = get_object_or_404(Campus , pk=id)

    if request.method == 'POST':
        confirm = request.POST.get('confirm')
        if confirm == 'Y':
            campus.delete()
            messages.success(request, "Campus deleted successfully.")
            return redirect('manage_campus')  # Or your preferred URL
        else:
            messages.info(request, "Deletion cancelled.")
            return redirect('manage_campus')
    return render(request, 'institute_app/confirm_delete_campus.html', {'campus': campus })

def add_club(request):
    form = ClubForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request,'Club added successfully!')
        return redirect('manage_club')
    return render(request,'institute_app/add_club.html' , {'form' : form })

def manage_club(request):
    clubs = Club.objects.all
    return render(request,'institute_app/manage_club.html',{'clubs' : clubs})

def update_club(request,id):
    if request.method=='POST':
        pi = Club.objects.get(pk=id)
        fm = ClubForm(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
            messages.success(request,'Club updated successfully!')
            return redirect('manage_club')
    else:
        pi = Club.objects.get(pk=id)
        fm = ClubForm(instance=pi)
    return render(request,'institute_app/update_club.html', {'form' : fm})

def delete_club(request,id):
    clubs = get_object_or_404(Club , pk=id)

    if request.method == 'POST':
        confirm = request.POST.get('confirm')
        if confirm == 'Y':
            clubs.delete()
            messages.success(request, "Club deleted successfully.")
            return redirect('manage_club')  # Or your preferred URL
        else:
            messages.info(request, "Deletion cancelled.")
            return redirect('manage_club')
    return render(request, 'institute_app/confirm_delete_club.html', {'clubs': clubs })

def add_parent(request):
    form = ParentForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request,'Parent Details added successfully!')
        return redirect('manage_parent')
    return render(request,'institute_app/add_parent.html' , {'form' : form })

def manage_parent(request):
    parents = Parent.objects.all
    return render(request,'institute_app/manage_parent.html',{'parents' : parents})

def update_parent(request,id):
    if request.method=='POST':
        pi = Parent.objects.get(pk=id)
        fm = ParentForm(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
            messages.success(request,'Parent Details updated successfully!')
            return redirect('manage_parent')
    else:
        pi = Parent.objects.get(pk=id)
        fm = ParentForm(instance=pi)
    return render(request,'institute_app/update_parent.html', {'form' : fm})

def delete_parent(request,id):
    parent = get_object_or_404(Parent , pk=id)

    if request.method == 'POST':
        confirm = request.POST.get('confirm')
        if confirm == 'Y':
            parent.delete()
            messages.success(request, "Parent deleted successfully.")
            return redirect('manage_parent')  # Or your preferred URL
        else:
            messages.info(request, "Deletion cancelled.")
            return redirect('manage_parent')
    return render(request, 'institute_app/confirm_delete_parent.html', {'parents': parent })

def add_library(request):
    form = LibraryBookForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request,'Book Details added successfully!')
        return redirect('manage_library')
    return render(request,'institute_app/add_library.html' , {'form' : form })

def manage_library(request):
    books = LibraryBook.objects.all
    return render(request,'institute_app/manage_library.html',{'books' : books})

def update_library(request,id):
    if request.method=='POST':
        pi = LibraryBook.objects.get(pk=id)
        fm = LibraryBookForm(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
            messages.success(request,'Book Details updated successfully!')
            return redirect('manage_library')
    else:
        pi = LibraryBook.objects.get(pk=id)
        fm = LibraryBookForm(instance=pi)
    return render(request,'institute_app/update_library.html', {'form' : fm})

def delete_library(request,id):
    library = get_object_or_404(LibraryBook , pk=id)

    if request.method == 'POST':
        confirm = request.POST.get('confirm')
        if confirm == 'Y':
            library.delete()
            messages.success(request, "Book deleted successfully.")
            return redirect('manage_library')  # Or your preferred URL
        else:
            messages.info(request, "Deletion cancelled.")
            return redirect('manage_library')
    return render(request, 'institute_app/confirm_delete_library.html', {'library': library })

def add_routine(request):
    form = RoutineForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request,'Routine added successfully!')
        return redirect('manage_routine')
    return render(request,'institute_app/add_routine.html' , {'form' : form })

def manage_routine(request):
    routine = Routine.objects.all
    return render(request,'institute_app/manage_routine.html',{'routines' : routine})

def update_routine(request,id):
    if request.method=='POST':
        pi = Routine.objects.get(pk=id)
        fm = RoutineForm(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
            messages.success(request,'Routine updated successfully!')
            return redirect('manage_routine')
    else:
        pi = Routine.objects.get(pk=id)
        fm = RoutineForm(instance=pi)
    return render(request,'institute_app/update_routine.html', {'form' : fm})

def delete_routine(request,id):
    routine = get_object_or_404(Routine, pk=id)

    if request.method == 'POST':
        confirm = request.POST.get('confirm')
        if confirm == 'Y':
            routine.delete()
            messages.success(request, "Routine deleted successfully.")
            return redirect('manage_routine')  # Or your preferred URL
        else:
            messages.info(request, "Deletion cancelled.")
            return redirect('manage_routine')
    return render(request, 'institute_app/confirm_delete_routine.html', {'routine': routine })

def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)  # Important: include request.FILES
        if form.is_valid():
            form.save()
            messages.success(request,'Event added successfully!')
            return redirect('manage_event')  # Replace with your event list view name
    else:
        form = EventForm()
    return render(request, 'institute_app/add_event.html', {'form': form})

def manage_event(request):
    event = Event.objects.all
    return render(request,'institute_app/manage_event.html',{'events' : event })

def update_event(request,id):
    if request.method=='POST':
        pi = Event.objects.get(pk=id)
        fm = EventForm(request.POST,request.FILES,instance=pi)
        if fm.is_valid():
            fm.save()
            messages.success(request,'Event updated successfully!')
            return redirect('manage_event')
    else:
        pi = Event.objects.get(pk=id)
        fm = EventForm(instance=pi)
    return render(request,'institute_app/update_event.html', {'form' : fm})

def delete_Event(request,id):
    event = get_object_or_404(Event, pk=id)

    if request.method == 'POST':
        confirm = request.POST.get('confirm')
        if confirm == 'Y':
            event.delete()
            messages.success(request, "Event deleted successfully.")
            return redirect('manage_event')  # Or your preferred URL
        else:
            messages.info(request, "Deletion cancelled.")
            return redirect('manage_event')
    return render(request, 'institute_app/confirm_delete_event.html', {'events': event })