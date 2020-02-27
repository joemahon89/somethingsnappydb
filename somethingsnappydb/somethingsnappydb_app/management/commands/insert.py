import pandas
import random
import re
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




def insert_data(cleaned_data):
	"""Insert data into the database"""
	config = RawConfigParser()
	config.read('../credentials.ini')

	# Get or create a legacy user
	legacy_username = config.get('legacy', 'legacy_username')
	legacy_password = config.get('legacy', 'legacy_password')
	user, created = User.objects.get_or_create(username=legacy_username, email="no email")
	if not created:
		user.set_password(legacy_password)
	user.is_superuser=False
	user.is_staff=False
	user.save()


	# Loop through each row
	for index, row in cleaned_data.df.iterrows():


		# Insert patient information
		first_name = row["Name"].split(" ")[0]
		last_name = row["Name"].split(" ")[1]
		patient, created = Patient.objects.get_or_create(
				first_name = first_name,
				last_name = last_name,
				dob = row["DOB"],
				proband = row["Proband"],
				affected_relatives = row["Affected Relatives"],
				)

		# Insert sample type information
		sample_type, created = SampleType.objects.get_or_create(
				sample_type = "Unknown",)

		# Insert somatic information
		somatic_information, created = SomaticInformation.objects.get_or_create(
				stage = row["Stage"],
				description = row["Description"])

		# Insert sample information
		random_sample_name = random.randint(0,1000000000)
		sample, created = Sample.objects.get_or_create(
				patient_id = patient,
				sample_name = random_sample_name,
				sample_type = sample_type,
				workflow = -1,
				somatic_information = somatic_information)

		# Insert sequencer information
		sequencer, created = Sequencer.objects.get_or_create(
				name = row["Sequencer"],)	

		# Insert analysis information
		analysis, created = Analysis.objects.get_or_create(
				sample_id = sample,
				sequencer = sequencer,
				date_sequenced = datetime.datetime.now(),
				runfolder = "Unknown",
				capture = 1)


		# Insert variant information
		pos = row["Variant Genome"].remove("(").remove(")")
		pos = pos.split(".")[1]
		position = re.findall(r"([0-9]*)",pos)[0]
		if ">" in pos:
			ref = pos.split(">")[0][-1]
			alt = pos.split(">")[1][0]
		else:
			ref = "?"
			alt = "?"
		variant, created = Variant.objects.get_or_create(
				chrom = 17,
				pos = position,
				ref = ref,
				alt = alt)

		# Insert RefGenome information
		refgenome, created = RefGenome.objects.get_or_create(
				name = "Unknown",)		

		analysisvariant, created = AnalysisVariant.objects.get_or_create(
				variant_id = variant,
				analysis_id = analysis,
				depth = 0,
				genome_id = refgenome)

		interpretation, created = Interpretation.objects.get_or_create(
				analysis_variant_id = analysisvariant,
				date_analysed = datetime.datetime.now(),
				analysed_by = user,
				pathogenicity = row["Pathogenicity"],
				active = True,)

		criteria, created = Interpretation.objects.get_or_create(
				criteria_code = row["Criteria"],
				description = "test description",
				)


		interpretationcriteria, created = InterpretationCriteria.objects.get_or_create(
				criteria_id = criteria,
				interpretation_id = interpretation,
				)

		
