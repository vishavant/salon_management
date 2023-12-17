from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import BranchRegistrationForm
from django.contrib import messages
from .models import Branch

def register_branch(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST)
        branch_form = BranchRegistrationForm(request.POST)
        
        if user_form.is_valid() and branch_form.is_valid():
            user = user_form.save()
            branch = branch_form.save(commit=False)
            branch.user = user
            branch.save()
            
            messages.success(request, 'Branch registered successfully.')
            return redirect('login')
    else:
        user_form = UserCreationForm()
        branch_form = BranchRegistrationForm()

    return render(request, 'salon_app/register_branch.html', {'user_form': user_form, 'branch_form': branch_form})
