from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

# Create your models here.

class Patient (models.Model):
    patient_id_auto = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    dob = models.DateField()
    proband = models.IntegerField(choices=(
        (0,'N'),
        (1,'Y'),
        (-1,'U')),
        blank=False,
        validators=[MinValueValidator(-1),
                    MaxValueValidator(1)])
    affected_relatives = models.IntegerField(choices=(
        (0,'N'),
        (1,'Y'),
        (-1,'U')),
        blank=False,
        validators=[MinValueValidator(-1),
                    MaxValueValidator(1)]
)

class SampleType(models.Model):
    sample_type_id_auto = models.AutoField(primary_key=True)
    sample_type = models.CharField(max_length=50)

class SomaticInformation (models.Model):
    somatic_id_auto = models.AutoField(primary_key=True)
    stage = models.IntegerField()
    description = models.CharField(max_length=50)

class Sample (models.Model):
    sample_id_auto = models.AutoField(primary_key=True)
    patient_id = models.ForeignKey(Patient, on_delete=models.CASCADE)
    sample_name = models.CharField(max_length=15)
    sample_type = models.ForeignKey(SampleType, on_delete=models.CASCADE)
    workflow = models.IntegerField(choices=(
        (-1,'U'),
        (1,'Germline'),
        (2,'Somatic')),
        blank=False,
        validators=[MinValueValidator(-1),
                    MaxValueValidator(2)])
    somatic_information=models.ForeignKey(SomaticInformation,blank=True,null=True, on_delete=models.CASCADE)

class Sequencer (models.Model):
    sequencer_id_auto = models.AutoField(primary_key=True)
    name = models.CharField(max_length=15)
    
class Analysis (models.Model):
    analysis_id_auto = models.AutoField(primary_key=True)
    sample_id = models.ForeignKey(Sample, on_delete=models.CASCADE)
    sequencer = models.ForeignKey(Sequencer, on_delete=models.CASCADE)
    date_sequenced = models.DateField()
    runfolder = models.CharField(max_length=50)
    capture = models.IntegerField(choices=(
        (-1,'U'),
        (1,'Targeted'),
        (2,'WGS'),
        (3,'WES')),
        blank=False,
        validators=[MinValueValidator(-1),
                    MaxValueValidator(3)])

class Variant (models.Model):
    variant_id_auto = models.AutoField(primary_key=True)
    chrom = models.CharField(max_length=2)
    pos = models.IntegerField()
    ref = models.CharField(max_length=15)
    alt = models.CharField(max_length=15)

class RefGenome (models.Model):
    genome_id_auto = models.AutoField(primary_key=True)
    name = models.CharField(max_length=6)

class AnalysisVariant (models.Model):
    av_id_auto = models.AutoField(primary_key=True)
    variant_id = models.ForeignKey(Variant,on_delete=models.CASCADE)
    analysis_id = models.ForeignKey(Analysis,on_delete=models.CASCADE)
    depth = models.IntegerField()
    genome_id = models.ForeignKey(RefGenome,on_delete=models.CASCADE)
    

class Interpretation (models.Model):
    interpretation_id_auto = models.AutoField(primary_key=True)
    analysis_variant_id = models.ForeignKey(AnalysisVariant,on_delete=models.CASCADE)
    date_analysed = models.DateField()
    analysed_by = models.ForeignKey(User,on_delete=models.PROTECT)
    # Pathogenicity, -1-5 (0 is unscored, -1 is legacy unknown)
    pathogenicity = models.IntegerField(choices=(
        (1, 'Class 1 - Certain non-pathogenic variant'),
        (2, 'Class 2 - Likely non-pathogenic variant'),
        (3, 'Class 3 - Uncertain pathogenicity variant'),
        (4, 'Class 4 - Likely pathogenic variant'),
        (5, 'Class 5 - Certain pathogenic variant')), 
        blank=False,
        validators=[MinValueValidator(-1), MaxValueValidator(5)])
    active = models.BooleanField()
 
class Criteria (models.Model):
    criteria_id_auto = models.AutoField(primary_key=True)
    criteria_code = models.CharField(max_length=4)
    description = models.CharField(max_length=100)

class InterpretationCriteria (models.Model):
    ic_id_auto = models.AutoField(primary_key=True)
    criteria_id = models.ForeignKey(Criteria,on_delete=models.CASCADE)
    interpretation_id = models.ForeignKey(Interpretation,on_delete=models.CASCADE)
   



