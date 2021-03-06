import django_tables2 as tables
from .models import Patient, Variant

class PatientTable(tables.Table):
    patient_id_auto = tables.Column(verbose_name="Patient ID")
    
    dob = tables.DateColumn(verbose_name="Date of Birth")
    proband = tables.Column()
    affected_relatives = tables.Column(verbose_name="Affected Relatives")

    class Meta:
        model= Patient
        template_name = "django_tables2/bootstrap.html"
        fields = ("patient_id_auto","dob","proband","affected_relatives")

class VariantTable(tables.Table):
    variant_id_auto = tables.Column(verbose_name = "Variant ID")
    chrom = tables.Column(verbose_name="Chromosome")
    pos = tables.Column(verbose_name="Position")
    ref = tables.Column(verbose_name="REF")
    alt = tables.Column(verbose_name="ALT")

    class Meta:
        model= Variant
        template_name = "django_tables2/bootstrap.html"
        fields = ("variant_id_auto","chrom","pos","ref","alt")


