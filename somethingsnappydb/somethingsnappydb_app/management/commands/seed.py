

import pandas as pd
import datetime
from dateutil.relativedelta import relativedelta
from django.core.management.base import BaseCommand
import somethingsnappydb_app.management.commands.insert as inserter
import somethingsnappydb_app.management.commands.clean_data as clean_data





class Command(BaseCommand):
	help = "Seed the database"

	def add_arguments(self, parser):
		parser.add_argument("-d", "--data_path",
							help = 'The path to the data',
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
				inserter.insert_data(cleaned_data_df)
				
