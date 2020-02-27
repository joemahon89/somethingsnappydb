import django_tables2 as tables
from .models import Patient

class PatientTable(tables.Table):
    first_name = tables.Column()
    last_name = tables.Column()
    dob = tables.Column()
    proband = tables.Column()
    affected_relatives = tables.Column()

    class Meta:
        model: Patient
        template_name = "django_tables2/bootstrap.html"
        fields = ("first_name","last_name","dob","proband","affected_relatives")