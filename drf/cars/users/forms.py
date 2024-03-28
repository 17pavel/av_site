from django import forms
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Message


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ["answer"]


def save(request):
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            answer = form.cleaned_data["answer"]
            form.save()
            return HttpResponseRedirect("/admin/")
    else:
        form = MessageForm()

    return render(request, "admin/send_message.html", {"form": form})
