# coding=utf-8

import json
import random

from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import logout
from django.contrib.auth.models import User, make_password
from django.contrib.auth.models import User
from django.db import transaction
from django.http import HttpResponseRedirect
from django.template import RequestContext
from altauth.models import AlternativePassword, check_alt_key, get_user_alt_key
from polling.forms import UserRegistrationForm
from polling.models import PollAlternatives, Poll, create_def_choices
from altauth.api import RSAWrapper
from settings import LOGOUT_REDIRECT_URL


rsa_wrapper = RSAWrapper()


@login_required
def index(request):
    return render(request, 'index.html', {})


@login_required
def log_out(request):
    return logout(request, next_page=LOGOUT_REDIRECT_URL)


@transaction.commit_on_success
def register(request):
    # залогиненых посылаем на глвную
    if request.user.is_active:
        return HttpResponseRedirect('/')

    p_k = rsa_wrapper.get_public_key()

    if request.method == 'POST':
        form_data = {}
        for param in request.POST:
            if param == 'csrfmiddlewaretoken':
                continue

            try:
                form_data[param] = rsa_wrapper.decrypt_str(request.POST[param])
            except Exception as ex:
                print "Couldn't decode string:%s" % request.POST[param]
                print ex.message
                continue

        form = UserRegistrationForm(form_data)
        if form.is_valid():
            # create new user
            pas = form_data.pop('password1')
            form_data['password'] = pas
            if pas != form_data.pop('password2'):
                return render_to_response(
                    'index.html', {'result': u"Не верный пароль"},
                    context_instance=RequestContext(request),
                )

            user, c = User.objects.get_or_create(**form_data)
            salt = random.randrange(1024)
            alternative_password = make_password(pas, salt)
            alt_pas = AlternativePassword()
            alt_pas.user = user
            alt_pas.alternative_password = alternative_password
            alt_pas.save()
            done = lambda x: u'Ваш код для голосования %s' % x
            error = u'Произошла ошибка'
            res = done(alternative_password) if (alternative_password
                                                 and user) else error
            return render_to_response(
                'index.html', {'result': res},
                context_instance=RequestContext(request),
            )

    data = {'public_key': 'p_k'}
    form = UserRegistrationForm(data)

    return render_to_response(
        'registration/register.html',
        {'form': form, 'public_key': json.dumps(p_k)},
        context_instance=RequestContext(request),
    )


@login_required
def poll(request):
    create_def_choices()

    if request.method == 'POST':
        # save choice Poll
        res = u"Не верный запрос"
        alt_key = request.POST[u'alt_key'] if u'alt_key' in request.POST else None
        president = request.POST[u'president'] if u'president' in request.POST else None
        if alt_key and president and check_alt_key(request.user, alt_key):
            res = u"Ваш голос учтен"
            poll = Poll()
            poll.user = request.user
            poll.choice = PollAlternatives.objects.get(president=president)
            poll.save()
        render_to_response('index.html', {'result': res})

    presidents = PollAlternatives.objects.filter().values_list('president')
    return render_to_response(
        'poll.html', {'presidents': list(presidents)},
        context_instance=RequestContext(request))


@login_required
def view_user(request, user_id):
    user = User.objects.get(pk=user_id)
    key = get_user_alt_key(user)
    return render(request, 'admin/user.html', {
        'user': user, 'alt_key': key,
    })
