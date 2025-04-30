from django.shortcuts import render,redirect,get_object_or_404
from .forms import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required



# Create your views here.
# @login_required
def home(request):
    return render(request,'home.html')

def index(request):
    return render(request,'index.html')

def base(request):
    return render(request,'base.html')

def contact(request):
    if request.method =='POST':
        name = form.cleaned_data['name']
        age=form.cleaned_data['age']
        return render(request,'home.html')
    else:
        form = Contact()
    return render(request,'student.html', {'frm':form})

def student(request):
    if request.method =='POST':
        form = StudentForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form = StudentForm()
    return render(request,'student.html', {'for':form})

def stud(request):
    if request.method =='POST':
        nam = request.POST.get('nm')
        ag = request.POST.get('ag')
        emai = request.POST.get('em')
        st = Student(name=nam, age=ag, email=emai)
        st.save()
        return redirect('home')
    else:
        form = Student()
    return render(request,'htmlform.html')

def signUp(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
          form.save()
          return redirect('home')
    else:
        form = UserCreationForm
    return render(request, 'register.html',{'reg':form})

def signIn(request):
    if request.method == 'POST':
        form = SigninForm(request.POST)
        if form.is_valid():
            usernm = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            usr = authenticate(username=usernm,password=password)
            if usr is not None:
                login(request.usr)
                return redirect('home')
            else:
                return 'invalid'
    else:
        form = SigninForm
    return render (request,'signin.html',{'sign':form})

def stlist(request):
    st = Student.objects.all()
    # st = Student.objects.filter(name='fazil')
    return render(request, 'list.html', {'item':st})

def delt(request, pk):
    it = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        it.delete()
        return redirect('list')

def userlogout(request):
    logout(request)
    return redirect('signin')

def editt(request, pk):
    itm = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST,instance=itm)
        form.is_valid()
        form.save()
        return redirect('list')
    else:
        form = StudentForm(instance=itm)
    return render(request,'edit.html',{'for':form})

# https://learndjango.com/tutorials/django-login-and-logout-tutorial