# coding=utf-8
import base64
import json

from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import logout
from django.contrib.auth.models import User
from settings import LOGOUT_REDIRECT_URL
from django.contrib.auth.models import User
from django.template import RequestContext

from polling.forms import UserRegistrationForm
from polling.models import PollAlternatives
from altauth.api import RSAWrapper

rsa_wrapper = RSAWrapper()

@login_required
def index(request):
    return render(request, 'index.html', {})


@login_required
def log_out(request):
    return logout(request, next_page=LOGOUT_REDIRECT_URL)


def register(request):
    # залогиненых посылаем на глвную
    if request.user.is_active:
        return HttpResponseRedirect('/')

    p_k = rsa_wrapper.get_public_key()

    if request.method == 'POST':
        form_data = {}
        for param in request.POST:
            try:
                form_data[param] = rsa_wrapper.decrypt_str(request.POST[param])
            except Exception as ex:
                print "Couldn't decode string:%s" % request.POST[param]
                continue

        form = UserRegistrationForm(form_data)
        if form.is_valid():
            # create new user
            import pdb;pdb.set_trace()
            u,c = User.objects.get_or_create(**form_data)

            return HttpResponseRedirect('/')

    data = {'public_key': 'p_k'}
    form = UserRegistrationForm(data)

    return render_to_response(
        'registration/register.html',
        {'form': form, 'public_key': json.dumps(p_k)},
        context_instance=RequestContext(request),
    )

@login_required
def poll(request):
    # do not forget to check if already polled - repolled?
    if request.method == 'POST':
        #save choise
        return HttpResponseRedirect('/')
    import pdb;pdb.set_trace()
    presidents = PollAlternatives.objects.filter().values_list('president')
    return render_to_response(
        'poll.html', {'presidents': presidents},
        context_instance=RequestContext(request))

@login_required
def view_user(request, user_id):

    user = User.objects.get(pk=user_id)

    return render(request, 'admin/user.html', {
        'user': user,
    })
