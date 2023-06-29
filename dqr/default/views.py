import random
from django.shortcuts import redirect, render
from default.models import *
import string
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
def index(request):
    qrcodes = Qrcode.objects.all()

    context = { 'qrcodes': qrcodes }
    return render(request, 'default/index.html', context=context)

@login_required
def addqrcode(request):
    if request.method == 'POST':
        url = request.POST['x-url']

        new_qrcode = Qrcode()
        new_qrcode.name = request.POST['x-name']
        new_qrcode.external_url = url
        
        letters = string.ascii_lowercase + string.ascii_uppercase + string.digits
        new_qrcode.internal_url = ''.join(random.choice(letters) for _ in range(50)) # 50 character random string

        new_qrcode.make_qrcode()
        new_qrcode.save()

    return redirect(request.META.get('HTTP_REFERER', '/'))

@login_required
def deleteqrcode(request):
    if request.method == 'POST':
        qrcode_id = request.POST['x-id']
        qrcode = Qrcode.objects.get(id=qrcode_id)
        qrcode.delete()

    return redirect(request.META.get('HTTP_REFERER', '/'))

@login_required
def redirect_to_external_url(request, internal_url):
    qrcode = Qrcode.objects.get(internal_url=internal_url)
    return redirect(qrcode.external_url)

@login_required
def modifyqrcode(request):

    if request.method == 'POST':
        qrcode_id = request.POST['x-id']
        qrcode = Qrcode.objects.get(id=qrcode_id)

        if request.POST['x-name'] != '':
            qrcode.name = request.POST['x-name']
        if request.POST['x-url'] != '':
            qrcode.external_url = request.POST['x-url']

        qrcode.save()

    return redirect(request.META.get('HTTP_REFERER', '/'))