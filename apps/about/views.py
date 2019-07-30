# -*- coding:utf-8 -*-
'''
__author__ = 'XD'
__mtime__ = 2019/7/29
__project__ = Mxonline3
Fix the Problem, Not the Blame.
'''
from django.shortcuts import render
from django.views.generic.base import View


class AboutView(View):
    def get(self, request):
        return render(request, 'about.html')


class ContactView(View):
    def get(self, request):
        return render(request, 'contact.html')

class MapView(View):
    def get(self, request):
        return render(request, 'map.html')
