from contact.forms import RegisterForm
from django.shortcuts import render


def register(request):
    form = RegisterForm()

    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()

    context = {
        "form": form,
    }

    return render(request, "contact/register.html", context)
