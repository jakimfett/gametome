from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect


@login_required
def profile_view(request):
    return render(request, 'profile.html', {})

# Override Django admin login
from django.contrib.admin import site
from django.contrib.auth.decorators import login_required
from functools import wraps
def staff_member_required(view_func):
    @wraps(view_func)
    def _checklogin(request, *args, **kwargs):
        if request.user.is_staff:
            # The user is valid. Continue to the admin page.
            return view_func(request, *args, **kwargs)
        return HttpResponseRedirect('/')
    return _checklogin
site.login = login_required(staff_member_required(site.login))