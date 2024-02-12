from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit
from django import forms
from .models import DostawaOkulickiego


class StanPaliwSaveForm(forms.ModelForm):
    class Meta:
        model = DostawaOkulickiego
        fields = ['dostawca', 'number', 'zb_98', 'zb_95', 'zb_on', 'zb_ontir', 'zb_lpg', 'zb_adblue']
        labels = {
                    "dostawca": 'Dostawca',
                    "number": "Numer Dostawy",
                    "zb_98": "Pb98",
                    "zb_95": "Pb95",
                    "zb_on": "ON",
                    "zb_ontir": "ON TIR",
                    "zb_lpg": "LPG",
                    "zb_adblue": "Ad Blue"
                }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit("stan_save", "Zapisz"))
        # self.helper.add_input(Submit('stan_cancel', 'Anuluj', css_class='btn btn-secondary'))
	# self.fields['number'].widget.attrs
        self.helper.layout = Layout(
            Fieldset(
                'Zapisz Dostawę',
                'dostawca',
                'number',
                'zb_98',
                'zb_95',
                'zb_on',
                'zb_ontir',
                'zb_lpg',
                'zb_adblue',

            ),
            Fieldset(
                ' '
            )
        )
