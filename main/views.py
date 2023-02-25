from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .forms import ContactForm, UserProfileForm
from . import services
from django.urls import reverse


def home(request):
    return render(request, "main/index.html")


@login_required
def about(request):
    return render(request, "main/about.html", {})


@login_required
def contact(request):
    if request.method == "POST":
        form = ContactForm(data=request.POST)
        if form.is_valid():
            services.send_message(form.cleaned_data)
    else:
        form = ContactForm()

    return render(request, 'main/contact.html', {"form": form})


def user_profile(request, user_id):
    user = get_object_or_404(get_user_model(), id=user_id)
    if request.method == 'post':
        try:
            profile = user.userprofile
            form = UserProfileForm(request.POST, instance=profile)
        except AttributeError:
            pass
        if form.is_valid():
            form.save()
    else:
        try:
            profile = user.userprofile
            form = UserProfileForm(instance=profile)
        except AttributeError:
            form = UserProfileForm(initial={"user": user, "bio": ""})
        if request.user != user:
            for field in form.fields:
                form.fields[field].disabled = True
            form.helper.inputs = []
    return render(request, 'main/userprofile.html', {'form': form})
