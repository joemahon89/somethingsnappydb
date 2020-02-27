

import pandas as pd
import datetime
from dateutil.relativedelta import relativedelta
from django.core.management.base import BaseCommand
import somethingsnappydb_app.management.commands.insert as inserter




class Data:
	def __init__(self, data_path):
		self.read_data_into_df(data_path)
		self.integerdict = {"Y":1,
							"N":0,
							"U":-1}

	def read_data_into_df(self, path):
		data_df = pd.read_csv(path,'\t')
		self.df = data_df


	def fix_affected_relatives(self):
		"""Looks through each row and changes affected relatives from Y, N, na
		to 1, 0, -1
		"""
		# Loop through each row
		for index, row in self.df.iterrows():
			# Is the value na? (No value)
			if pd.isna(row["Affected Relatives"]):
				value = "U"
			else:
				value = row["Affected Relatives"]
			# Get the appropriate int e.g Y is 1
			value_int = self.integerdict[value]
			# Set the df value to the int
			self.df.loc[index,"Affected Relatives"] = value_int


	def fix_proband(self):
		"""Looks through each row and changes probands from Y, N, na
		to 1, 0, -1
		"""
		# Loop through each row
		for index, row in self.df.iterrows():
			# Is the value na? (No value)
			if pd.isna(row["Proband"]):
				value = "U"
			else:
				value = row["Proband"]
			# Get the appropriate int e.g Y is 1
			value_int = self.integerdict[value]
			# Set the df value to the int
			self.df.loc[index, "Proband"] = value_int

	def fix_evidence_codes(self):
		"""Looks through each row and changes probands from Y, N, na
		to 1, 0, -1
		"""
		# Loop through each row
		for index, row in self.df.iterrows():
			# Is the value na? (No value)
			if pd.isna(row["Evidence Codes"]):
				value = "Unknown"
			else:
				value = row["Evidence Codes"]
			self.df.loc[index, "Evidence Codes"] = value

	def fix_dob(self):
		"""Makes an assumption that the dob is current day minus
		age in years
		"""
		# Loop through each row
		self.df["DOB"] = ""
		for index, row in self.df.iterrows():
			age = int(row["Age"])
			dob = datetime.datetime.now() - relativedelta(years=age)
			self.df.loc[index, "DOB"] = dob







class Command(BaseCommand):
	help = "Seed the database"

	def add_arguments(self, parser):
		parser.add_argument("-d", "--data_path",
							help = 'The path to the data',
							nargs = 1)
	
	def clean_data(self, data_path):
		print(data_path)
		data = Data(data_path)
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
				
