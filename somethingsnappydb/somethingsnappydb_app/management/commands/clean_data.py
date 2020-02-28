import pandas as pd
import datetime
from dateutil.relativedelta import relativedelta

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
		bad_data_count = 0
		for index, row in self.df.iterrows():
			# Is the value na? (No value)
			if pd.isna(row["Affected Relatives"]):
				value = "U"
				bad_data_count +=1
			else:
				value = row["Affected Relatives"]
			# Get the appropriate int e.g Y is 1
			value_int = self.integerdict[value]
			# Set the df value to the int
			self.df.loc[index,"Affected Relatives"] = value_int
		print("Affected Relatives:"+str(bad_data_count)+" missing values")


	def fix_proband(self):
		"""Looks through each row and changes probands from Y, N, na
		to 1, 0, -1
		"""
		# Loop through each row
		bad_data_count = 0
		for index, row in self.df.iterrows():
			# Is the value na? (No value)
			if pd.isna(row["Proband"]):
				value = "U"
				bad_data_count +=1
			else:
				value = row["Proband"]
			# Get the appropriate int e.g Y is 1
			value_int = self.integerdict[value]
			# Set the df value to the int
			self.df.loc[index, "Proband"] = value_int
		print("Proband:"+str(bad_data_count)+" missing values")

	def fix_evidence_codes(self):
		"""Looks through each row and changes probands from Y, N, na
		to 1, 0, -1
		"""
		# Loop through each row
		bad_data_count = 0
		for index, row in self.df.iterrows():
			# Is the value na? (No value)
			if pd.isna(row["Evidence Codes"]):
				value = "U"
				bad_data_count +=1
			else:
				value = row["Evidence Codes"]
			self.df.loc[index, "Evidence Codes"] = value
		print("Evidence Codes:"+ str(bad_data_count) +" missing values")

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
