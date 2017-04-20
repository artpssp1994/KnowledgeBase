from django.shortcuts import render, render_to_response
from django.template.context import RequestContext
from user_profile.models import UserDetails
from django.contrib.auth.decorators import login_required
from user_profile.forms import UserProfileForm


@login_required(login_url='/')
def profile(request):
    user = request.user
    user_details = UserDetails.objects.get_or_create(user=user)[0]
    context = {'request': request, 'user': user, 'user_details': user_details}
    return render(request, 'user_profile/profile.html', context)


@login_required(login_url='/')
def get_general_profile_panel(request):
    user = request.user
    user_details = UserDetails.objects.get_or_create(user=user)[0]
    context = {'request': request, 'user': user, 'user_details': user_details}
    return render(request, 'user_profile/general_profile_panel.html', context)


@login_required(login_url='/')
def get_general_profile_form(request):
    user_details = UserDetails.objects.get(user=request.user)
    form = UserProfileForm(instance=user_details)

    context = {'form': form, 'user': request.user, 'user_details': user_details}
    return render(request, 'user_profile/general_profile_form.html', context)


@login_required(login_url='/')
def edit_general_profile(request):
    if request.method == 'POST':
        user = request.user
        user_details = UserDetails.objects.get(user=user)
        form = UserProfileForm(request.POST, instance=user_details)

        if form.is_valid():
            form.save()
            return get_general_profile_panel(request)
        else:
            return render_to_response('user_profile/general_profile_form.html', {'form': form},
                                      context_instance=RequestContext(request))
