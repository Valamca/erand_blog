from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def register(request):
    """Registering a new user"""
    # Validating if we have a POST request
    if request.method != "POST":
        # If no we create a blank form
        form = UserCreationForm()
    else:
        # If True; Create a form with the date
        form = UserCreationForm(data=request.POST)
        # If the form is valid
        if form.is_valid():
            # We save the values
            new_user = form.save()
            # We log in with the new user
            login(request=request, user=new_user)
            # We redirect the user to the main page
            return redirect("blog:index")
    context = {"form":form}
    return render(request=request, template_name="registration/register.xhtml", 
                context=context)
