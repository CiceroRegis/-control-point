from django import forms
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

from appointment.models import Appointment, TypeAppointment
from collaborator.models import Profile
from pacient.models import Pacient


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        exclude = (
            "updateAt",
            "createAt",
        )

    type_appointment = forms.ModelMultipleChoiceField(
        error_messages={"required": _("type appointment is required")},
        widget=forms.SelectMultiple(
            attrs={
                "class": "form-control js-example-basic-multiple",
                "name": "type_appointment[]",
                "multiple": "multiple",
            }
        ),
        required=False,
        queryset=TypeAppointment.objects.all(),
    )

    pacient = forms.ModelChoiceField(
        widget=forms.Select(
            attrs={"class": "form-control", "placeholder": "Paciente"}
        ),
        queryset=Pacient.objects.all()
    )

    professional = forms.ModelChoiceField(
        widget=forms.Select(attrs={"class": "form-control", "placeholder": "Profissional"}),
        queryset=Profile.objects.all()
    )

    date_appointment = forms.DateTimeField(
        error_messages={"required": _("date appointment is required")},
        widget=forms.DateTimeInput(
            attrs={
                "class": "form-control datetimepicker",
                "autocomplete": "off",
                "placeholder": "Data da consulta",
            }
        ),
    )
