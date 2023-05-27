import io
import string
import random
import datetime

import qrcode
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.core.files import File
from PIL import Image, ImageDraw

from Dashboard.models import Certificate

random = random.Random()


class UploadCertView(View):

    template_name = "dashboard/upload_cert.html"

    @method_decorator(login_required())
    def get(self, request):
        user = request.user
        return render(request, self.template_name, {'user': user})

    @method_decorator(login_required())
    def post(self, request):
        if request.method == "POST":
            last_name = request.POST.get("last_name").strip().upper()
            first_name = request.POST.get("first_name").strip().upper()
            middle_name = request.POST.get("middle_name").strip().upper()
            discipline = request.POST.get("discipline")
            institution = request.POST.get("institution").strip().upper()
            graduation_date = request.POST.get("grad_date").strip().upper()
            cert_type = request.POST.get("cert_type").strip()
            image = request.POST.get("image")

            user_date = graduation_date.split('-')
            user_date = datetime.date(int(user_date[0]), int(user_date[1]), int(user_date[2]))

            if not Certificate.objects.filter(**{'last_name': last_name, 'first_name': first_name, 'middle_name': middle_name, 'certificate_type': cert_type}).exists():
                while True:
                    cert_no = "CERT" + ''.join([random.choice(string.digits) for i in range(8)])
                    if not Certificate.objects.filter(certificate_no=cert_no).exists():
                        break

                cert = Certificate.objects.create(last_name=last_name, first_name=first_name, middle_name=middle_name,
                                           discipline=discipline, institution=institution, graduation_date=user_date,
                                           certificate_type=cert_type, certificate_no=cert_no)

                cert.image = image

                # Create the qr code
                qrcode_img = qrcode.make(f"{cert_no}")
                canvas = Image.new("RGB", (300, 300), "white")
                ImageDraw.Draw(canvas)
                canvas.paste(qrcode_img)
                buffer = io.BytesIO()
                canvas.save(buffer, "PNG")

                cert.qr_code.save(f"{cert_no}", File(buffer), save=False)
                canvas.close()

                cert.save()

                messages.success(request, "Certificate successfully uploaded")
                print(cert_no)
                return HttpResponseRedirect(reverse("Dashboard:view_certificate", args=(cert.id,)))
            else:
                messages.error(request, "Certificate already exists")

                return HttpResponseRedirect(reverse("Dashboard:upload_certificate"))


class VerifyCertView(View):

    template_name = "dashboard/verify_cert.html"

    def get(self, request):
        if request.user:
            user = request.user
            return render(request, self.template_name, {'user': user})

    def post(self, request):
        if request.method == "POST":
            institution = request.POST.get("institution").strip().upper()
            cert_no = request.POST.get("cert_no").strip().upper()

            if Certificate.objects.filter(**{"institution": institution, "certificate_no": cert_no}).exists():
                cert = Certificate.objects.get(institution=institution, certificate_no=cert_no)
                return HttpResponseRedirect(reverse("Dashboard:view_certificate", args=(cert.id,)))

            else:
                messages.error(request, "Certificate not available")
                return HttpResponseRedirect(reverse("Dashboard:upload_certificate"))


class CertificateView(View):

    template_name = "dashboard/view_cert.html"

    def get(self, request, cert_id):
        cert = Certificate.objects.get(id=cert_id)
        return render(request, self.template_name, {"cert": cert})

