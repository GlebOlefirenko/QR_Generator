from django.shortcuts import render
from .models import QRCode
from qrcode import make
import os
# Create your views here.
from .models import QRCode
# Create your views here.


def render_generator_qr(request):
    return render(request = request, template_name = "generator_qr/generator_qr.html")
    if request.method == 'POST':
        data = request.POST['data']
        name = request.POST['name']
        img = make(data, version = request.POST['size'], box_size = 40, )
        img.save(os.path.abspath(__file__ + f"/../../media/qrcodes/{name}.png"))
        model = QRCode(name = name , size = request.POST['size'] , color = request.POST['color'], form = request.POST['form'], link = request.POST['data'], path_qrcode = f"qrcodes/{name}.png")
        model.save()
        return render(request = request, template_name = "generator_qr/generator_qr.html", context = {"Qrcode": model})
    else:
        pass

    return render(request = request, template_name = "generator_qr/generator_qr.html")

def view_my_qrcodes(request):
    all_qrcodes = QRCode.objects.all()
    return render(request, "my_qrcodes.html", context = {"all_qrcodes": all_qrcodes} )


def view_my_qrcodes(request):
    all_qrcodes = QRCode.objects.all()
    return render(request, "my_qrcodes.html", context = {"all_qrcodes": all_qrcodes} )