from django.shortcuts import render, redirect,get_object_or_404
from app.forms import *
from app.models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required


def signup(request):
    if(request.method=="POST"):
        email=request.POST['email']
        password=request.POST['pass1']
        confirm_password=request.POST['pass2']
        if password!=confirm_password:
            return render(request,"auth/signup.html")
            

        try:
            if User.objects.get(username=email):
                popup=True
                return render(request, "auth/n.html",{'popup':popup})
        except Exception as identifier:
            pass
        user=User.objects.create_user(email,email,password)
        user.is_active=True
        user.save()
        return redirect('/login')
    return render(request,"auth/signup.html")


def handlelogin(request):
    if request.method=="POST":
        username=request.POST['email']
        password=request.POST['pass1']
        user=authenticate(request, username=username, password=password)
            # User is authenticated
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            return redirect('/login/')
    return render(request,"auth/login.html")


def handlelogout(request):
    logout(request)
    return redirect('/login')

@login_required

def home(request):
    data=Expense.objects.all()
    return render(request, 'app/index.html',{'List':data})


def add(request):
    form = ExpenseF()

    if request.method == 'POST':
        form=ExpenseF(request.POST)
        if form.is_valid():
            form.instance.created_by = request.user
            form.save()
            return redirect('/')
        
    return render(request, ('app/create.html') , {'form': form})



def edit(request, expense_id):
    expense = get_object_or_404(Expense, id=expense_id)

    # Check if the logged-in user is the creator of the expense
    if request.user != expense.created_by:
        # Handle unauthorized access, for example, redirect to home
        return redirect('home')

    form = ExpenseF(instance=expense)
    return render(request, 'app/edit.html', {'expense': expense, 'form': form})



def update_expense(request, expense_id):
    expense = get_object_or_404(Expense, id=expense_id)

    # Check if the logged-in user is the creator of the expense
    if request.user != expense.created_by:
        # Handle unauthorized access, for example, redirect to home
        return redirect('home')

    if request.method == 'POST':
        form = ExpenseF(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            return redirect('home')

    return render(request, 'app/edit.html', {'expense': expense, 'form': form})



def delete_expense(request, expense_id):
    expense = get_object_or_404(Expense, id=expense_id)

    # Check if the logged-in user is the creator of the expense
    if request.user != expense.created_by:
        # Handle unauthorized access, for example, redirect to home
        return redirect('home')

    if request.method == 'POST':
        expense.delete()
        return redirect('home')

    return render(request, 'app/delete_confirm.html', {'expense': expense})