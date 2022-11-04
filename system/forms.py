from django import forms
from .models import Iha, Order, PrivateMsg

#İha ekleme, Sipariş yaratma ve Mesaj formlarının modelleri bu dosyada oluşturuldu
class IhaForm(forms.ModelForm):
    class Meta:
        model = Iha
        fields = [
            "image",
            "iha_name",
            "company_name",
            "iha_weight",
            "content",
        ]
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            "iha_name",
            "employee_name",
            "cell_no",
            "address",
            "date",
            "to",
        ]
class MessageForm(forms.ModelForm):
    class Meta:
        model = PrivateMsg
        fields = [
            "name",
            "email",
            "message",
        ]
