from django.contrib.auth import login
from django.shortcuts import render, redirect

from .forms import SignUpForm

def frontpage(request):
    return render(request, 'chat/frontpage.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        # Checking if the form is valid:
        if form.is_valid():
            # Saving the form:
            user = form.save()
            
            # Logging in the user:
            login(request, user)

            # Redirecting to the front page:
            return redirect('frontpage')
    else:
        form = SignUpForm()
    
    return render(request, 'chat/signup.html', {'form': form})