from django import forms
from user_profile.models import UserDetails

class UserProfileForm(forms.ModelForm):
    first_name_th = forms.CharField(max_length=32, label="ชื่อจริง(ไทย)")
    last_name_th = forms.CharField(max_length=32, label="นามสกุล(ไทย)")
    internal_number = forms.CharField(max_length=16, label="หมายเลขภายใน", required=False)
    mobile_phone_number = forms.CharField(max_length=16, label="โทรศัพท์มือถือ", required=False)

    class Meta:
        model = UserDetails
        fields = ('first_name_th','last_name_th', 'internal_number', 'mobile_phone_number')