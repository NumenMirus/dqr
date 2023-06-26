from django.shortcuts import redirect, render
from default.models import *

# Create your views here.
def index(request):
    qrcodes = Qrcode.objects.all()

    context = { 'qrcodes': qrcodes }
    return render(request, 'default/index.html', context=context)

def addqrcode(request):
    if request.method == 'POST':
        qrcode = Qrcode()
        qrcode.name = request.POST['x-name']
        qrcode.url = request.POST['x-url']
        qrcode.save()

    return redirect(request.META.get('HTTP_REFERER', '/'))

def deleteqrcode(request):
    if request.method == 'POST':
        qrcode_id = request.POST['x-id']
        qrcode = Qrcode.objects.get(id=qrcode_id)
        qrcode.delete()

    return redirect(request.META.get('HTTP_REFERER', '/'))