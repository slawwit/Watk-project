from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import Permission
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import RegisterForm


@login_required
@permission_required('auth.add_user')
def register(response):
    if response.user.is_authenticated:
        if response.method == "POST":
            form = RegisterForm(response.POST)
            if form.is_valid():
                user = form.save()
                permission = Permission.objects.get(name="Can add tag")
                user.user_permissions.add(permission)

            return redirect(reverse("home"))
        else:
            form = RegisterForm()
        return render(response, "accounts/register.html", {"form": form})
    return redirect(reverse('login'))
