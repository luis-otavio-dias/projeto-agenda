from django import forms
from django.core.exceptions import ValidationError
from . import models


class ContactForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "classe-a classe-b",
                "placeholder": "Do init",
            },
        ),
        help_text="Texto ajuda",
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # self.fields["first_name"].widget.attrs.update(
        #     {
        #         "class": "classe-a classe-b",
        #         "placeholder": "Type your name",
        #     }
        # )

    class Meta:
        model = models.Contact
        fields = ("first_name", "last_name", "phone")
        # widgets = {
        #     "first_name": forms.TextInput(
        #         attrs={
        #             "class": "classe-a classe-b",
        #             "placeholder": "Type your name",
        #         },
        #     ),
        # }

    def clean(self):
        # cleaned_data = self.cleaned_data

        # self.add_error(
        #     "first_name",
        #     ValidationError(
        #         "Mensagem de erro",
        #         code="invalid",
        #     ),
        # )

        return super().clean()

    # def
