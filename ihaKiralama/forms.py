from django import forms
from django.contrib.auth import(
    authenticate,
    get_user_model,
    login,
    logout
)

User = get_user_model()

#Giriş ve kayıt formları Django'nun forms metodundan alındığı için 'username', 'password' gibi alanlar ne yazık ki Türkçe değil
class userLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

#Form için tanımlanan doğrulama tanımlarının karşılanıp karşılanmadığını garanti altına almak için cleaned_data metoduyla veriyi temizliyoruz
    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)

            if not user:
                raise forms.ValidationError('Ya böyle bir kullanıcı yok ya da şifrenizi yanlış girdiniz.')
            if not user.is_active:
                raise forms.ValidationError('Bu kullanıcı artık aktif değil')
        return super(userLoginForm,self).clean(*args, **kwargs)

class userRegisterForm(forms.ModelForm):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password'
        ]