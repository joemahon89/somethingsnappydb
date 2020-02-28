from django.core.management.base import BaseCommand
from somethingsnappydb_app.models import (Patient,
										SampleType,
										SomaticInformation,
										Sample,
										Sequencer,
										Analysis,
										Variant,
										RefGenome,
										AnalysisVariant,
										Interpretation,
										Criteria,
										InterpretationCriteria,)


class Command(BaseCommand):
	help = 'Wipes the tables'

	def handle(self, *args, **kwargs):
		""" Wipes the tables of the database completely."""
		answer = None
		while answer not in ("Y", "N"):
			answer = input("Do you want to wipe the db?").upper()
		if answer == "Y":

			InterpretationCriteria.objects.all().delete()
			Criteria.objects.all().delete()
			Interpretation.objects.all().delete()
			AnalysisVariant.objects.all().delete()
			RefGenome.objects.all().delete()
			Variant.objects.all().delete()
			Analysis.objects.all().delete()
			Sequencer.objects.all().delete()
			Sample.objects.all().delete()
			SomaticInformation.objects.all().delete()
			SampleType.objects.all().delete()
			Patient.objects.all().delete()

			print("WIPED")
