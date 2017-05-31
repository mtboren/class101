# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from .models import Server


def server_list(request):
    servers = Server.objects.all()
    template = loader.get_template('dashboard/server_list.html')

    return HttpResponse(template.render(
        {'server_list': servers}, request
    ))
