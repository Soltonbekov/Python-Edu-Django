#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response

def index ( index ) :
    return HttpResponse( u"Rango Says: Hello World!!! <a href='/rango/about'>About</a>" )

def about ( about ) :
    return HttpResponse( u"Rango Says: Here is the about page <a href='/rango/'>Index</a>" )
