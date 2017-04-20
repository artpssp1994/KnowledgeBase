from django.shortcuts import render
from social.exceptions import AuthForbidden
from user_profile.models import UserDetails


def index(request):
    user = request.user
    if user and not user.is_anonymous():
        user_details = UserDetails.objects.get_or_create(user=user)[0]
        context = {'request': request, 'user': user, 'user_details': user_details}
        return render(request, 'home/index.html', context)
    else:
        return render(request, 'home/login.html', {'request': request})


def email_check(strategy, details, *args, **kwargs):
    mail = str(details.get('email'))
    if not mail.endswith('@eng.src.ku.ac.th'):
        raise AuthForbidden(kwargs.get('backend'))
