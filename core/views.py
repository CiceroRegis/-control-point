import time

from django.contrib import messages
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView, ListView, UpdateView

from collaborator.form import CollaboratorForm
from collaborator.models import Collaborator

from .forms import LoginForm, RegisterForm


def logout_page(request):
    context = {"content": "Você efetuou o logout com sucesso!"}
    logout(request)
    return render(request, "auth/login.html", context)


User = get_user_model()


@login_required
def login_page(request):
    form = RegisterForm(request.POST or None)
    # context = {
    #     "form": form,
    # }

    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data["username"]
        email = form.cleaned_data["email"]
        password = form.cleaned_data["password"]
        new_user = User.objects.create_user(username, email, password)
        print(new_user)
        messages.success(request, _("Usuario salvo com sucesso"))
        context = {"form": RegisterForm()}

    return render(request, "auth/register.html", context)


def completeDataCollaborator(request):
    if request.method == "POST":
        form = CollaboratorForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, _("Usuario salvo com sucesso"))
        else:
            messages.warning(request, _("Não foi possivel salvar este usuario. Verifique se os campos estão corretos!"))    
    return render(request, "register/register_collaborator.html", {'form':form})


def showProfile(request):
    context = {"profile": Collaborator.objects.filter(user=request.user)}
    return render(request, "collaborator/profile_collaborator.html", context)
