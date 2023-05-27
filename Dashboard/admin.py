from django.contrib import admin
from Dashboard.models import Certificate


class CertificateAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'middle_name', 'discipline', 'institution', 'graduation_date', 'certificate_type', 'certificate_no')


admin.site.register(Certificate, CertificateAdmin)