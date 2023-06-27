from django.shortcuts import redirect, render
from default.models import *
import hashlib
import qrcode as qrcode_maker

# Create your views here.
def index(request):
    qrcodes = Qrcode.objects.all()

    context = { 'qrcodes': qrcodes }
    return render(request, 'default/index.html', context=context)

def addqrcode(request):
    if request.method == 'POST':
        url = request.POST['x-url']

        new_qrcode = Qrcode()
        new_qrcode.name = request.POST['x-name']
        new_qrcode.external_url = url
        
        # Hash the url
        sha256_hash = hashlib.sha256()
        sha256_hash.update(url.encode('utf-8'))
        hashed_url = sha256_hash.hexdigest()
        new_qrcode.internal_url = hashed_url # "http://michaelbasta.it/dqr/" + hashed_url

        new_qrcode.save()


    return redirect(request.META.get('HTTP_REFERER', '/'))

def deleteqrcode(request):
    if request.method == 'POST':
        qrcode_id = request.POST['x-id']
        qrcode = Qrcode.objects.get(id=qrcode_id)
        qrcode.delete()

    return redirect(request.META.get('HTTP_REFERER', '/'))

def redirect_to_external_url(request, internal_url):
    qrcode = Qrcode.objects.get(internal_url=internal_url)
    return redirect(qrcode.external_url)

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