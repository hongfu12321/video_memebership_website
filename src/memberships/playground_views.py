from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.views.generic import ListView
from django.urls import reverse

from .models import Membership, UserMembership, Subscription

import stripe

def playgroundView(request):
    context = {
        'request': request,
    }
    return render(request, "playgrounds/playground_zone1.html", context)