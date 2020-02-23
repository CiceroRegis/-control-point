import time

from django.contrib import messages
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView, ListView, UpdateView
from django.views.decorators.http import require_GET
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.debug import sensitive_post_parameters

from collaborator.form import CollaboratorForm
from collaborator.models import Collaborator, User

from .forms import LoginForm, RegisterForm

@login_required
def logout_view(request):
    logout(request)
    return redirect("collaborator:logout")


User = get_user_model()


@login_required
def login_page(request):
    form = RegisterForm(request.POST or None)
    context = {
        "form": form,
    }
    if request.method == "POST":
        if form.is_valid():
            print(form.cleaned_data)
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            new_user = User.objects.create_user(username, email, password)
            print(new_user)
            messages.success(request, _("Usuario salvo com sucesso"))
            context = {"form": RegisterForm()}
        else:
            messages.warning(request, _("Não foi possivel salvar este usuario. Verifique se os campos estão correto"))
    return render(request, "auth/register.html", context)

@login_required
def registerDataCollaborator(request, *args, **kwargs):
    form = CollaboratorForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            form = CollaboratorForm()
            messages.success(request, _("Usuario salvo com sucesso"))
        else:
            messages.warning(request, _("Não foi possivel salvar os dados. Verifique se os campos estão correto!"))    
    return render(request, "register/register_collaborator.html", {'form':form})

@login_required
@require_GET
def listCollaborators(request):
    context = {
        'collaborators': Collaborator.objects.all().order_by('nome')
    }
    return render(request, 'collaborator/collaborator_list.html', context)

def updateProfileCollaborator(request, collaborator):
     c = Collaborator.objects.get(pk=collaborator)
     if not c:
        messages.warning(request, _('This collaborator not found.'))
     else:
        return redirect('collaborator:list-collaborator')
    
    
@login_required
@require_GET
def disableProfileCollaborator(request, collaborator):
    c = Collaborator.objects.get(pk=collaborator)
    if not c:
        messages.warning(request, _('This Collaborator not found.'))
    try:
       if c:
           c.delete()
           messages.success(request, _('Collaborator canceled.'))
    except Exception:
        messages.warning(request, _('Collaborator not canceled.'))
        
    return redirect('collaborator:list-collaborator')
    

@login_required
@require_GET
def showProfile(request):
    context = {"profile": Collaborator.objects.filter(user=request.user)}
    return render(request, "collaborator/profile_collaborator.html", context)
