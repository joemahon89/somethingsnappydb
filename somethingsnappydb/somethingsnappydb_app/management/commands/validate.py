import pandas
import random
import re
from django.core.management.base import BaseCommand
import somethingsnappydb_app.management.commands.clean_data as clean_data
import datetime
from django.contrib.auth.models import User
from somethingsnappydb_app.models import (
											Patient,
											SampleType,
											Sequencer,
											InterpretationCriteria,
											Criteria,
											Interpretation,
											AnalysisVariant,
											RefGenome,
											Variant,
											Analysis,
											Sample,
											SomaticInformation,)
from configparser import RawConfigParser

		

class Command(BaseCommand):
	help = "Seed the database"

	def add_arguments(self, parser):
		parser.add_argument("-d", "--data_path",
							help = 'The path to the validation subset',
							nargs = 1)
	
	def clean_data(self, data_path):
		print(data_path)
		data = clean_data.Data(data_path)
		data.read_data_into_df(data_path)
		data.fix_affected_relatives()
		data.fix_proband()
		data.fix_evidence_codes()
		data.fix_dob()
		return data


	def handle(self, *args, **kwargs):
		# Create a list containing samples in the given path
		if kwargs['data_path']:
			data_path = kwargs['data_path']
			# Clean the data
			cleaned_data_df = self.clean_data(data_path[0])
			# Insert the data
			validate_data(cleaned_data_df)



def validate_data(cleaned_data):
	"""Insert data into the database"""
	# Loop through each row
	   # patients = Patient.objects.all()


	goodpatients = 0
	allpatients = Patient.objects.all().count()

	goodstages = 0
	allstages = SomaticInformation.objects.all().count()
	for index, row in cleaned_data.df.iterrows():

		# Patient check
		first_name = row["Name"].split(" ")[1]
		if Patient.objects.filter(first_name=first_name).exists():
			goodpatients +=1


	print(str(goodpatients)+"/"+str(allpatients)+" Patients added correctly")




		#last_name = row["Name"].split(" ")[2]
		#patient


		
