from django.urls import path

from Dashboard.views import UploadCertView, CertificateView, VerifyCertView

app_name = "Dashboard"

urlpatterns = [
    path("upload_certificate", UploadCertView.as_view(), name="upload_certificate"),
    path("upload_certificate/verify", VerifyCertView.as_view(), name="verify_certificate"),
    path("view_certificate/<int:cert_id>", CertificateView.as_view(), name="view_certificate"),
]
