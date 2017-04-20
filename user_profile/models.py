from django.db import models
from django.contrib.auth.models import User


class UserDetails(models.Model):
    user = models.OneToOneField(User)

    # User Profile

    first_name_th = models.CharField(max_length=32)
    last_name_th = models.CharField(max_length=32)
    internal_number = models.CharField(max_length=16, blank=True)
    mobile_phone_number = models.CharField(max_length=16, blank=True)

    '''
        Registering User Permissions Here
    '''

    

    '''
        End of Registering User Permissions
    '''

    # Overrided methods

    def save(self, *args, **kwargs):
        self.first_name_th = self.first_name_th.strip()
        self.last_name_th = self.last_name_th.strip()
        self.internal_number = self.internal_number.strip()
        self.mobile_phone_number = self.mobile_phone_number.strip()
        super(UserDetails, self).save(*args, **kwargs)

    def __str__(self):
        if self.first_name_th and self.last_name_th:
            return self.first_name_th + ' ' + self.last_name_th
        else:
            return self.user.get_full_name()
