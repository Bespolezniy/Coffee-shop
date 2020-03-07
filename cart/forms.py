from django import forms
from django.utils.translation import gettext_lazy as _

PRODUCT_QUANTITY_CHICES = [(i, str(i)) for i in range(1, 21)]


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(
        label=_('Quantity'),
        choices=PRODUCT_QUANTITY_CHICES,
        coerce=int
    )
    update = forms.BooleanField(
        required=False,
        initial=False,
        widget=forms.HiddenInput
    )