# coding=utf-8
import json
from altauth.api import rsa_gen_keys
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import logout

from settings import LOGOUT_REDIRECT_URL
from django.contrib.auth.models import User
from django.template import RequestContext
from polling.forms import UserRegistrationForm


@login_required
def index(request):
    return render(request, 'index.html', {})


@login_required
def log_out(request):
    return logout(request, next_page=LOGOUT_REDIRECT_URL)


def register(request):
    p_k, pr_k = rsa_gen_keys(128)

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            # create new user
            params = json.loads(request.POST[u'encryptedTextDict'])
            return HttpResponseRedirect('/')
    p_k_str = p_k.save_pkcs1().split('\n')[1]
    p_k_num = p_k_str
    data = {'public_key': p_k_num}
    form = UserRegistrationForm(data)

    return render_to_response(
        'registration/register.html',
        {'form': form},
        context_instance=RequestContext(request),
    )


@login_required
def view_user(request, user_id):

    user = User.objects.get(pk=user_id)

    return render(request, 'admin/user.html', {
        'user': user,
    })
