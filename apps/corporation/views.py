# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse

from .models import CorporationDesc, LeaveMessage


class AboutView(View):
    def get(self, request):
        desc = CorporationDesc.objects.all()[0]

        return render(request, 'about.html', {
            'desc': desc,
        })

class LeaveMsgView(View):
    """留言"""
    def post(self, request):
        content = request.POST.get('content', '')
        mobile = request.POST.get('mobile', '')
        if mobile:
            leave_msg = LeaveMessage()
            leave_msg.mobile = mobile
            leave_msg.content = content
            leave_msg.save()

            return JsonResponse({"code":"2"})
        return JsonResponse({"code":"1"})