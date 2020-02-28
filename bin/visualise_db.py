#!/usr/bin/python3
#
#
#
#
# Adriana Toutoudaki and Joseph Mahon (February 2020)
# contact: adriana.toutoudaki@addenbrookes.nhs.uk


import pandas as pd

data = pd.read_csv("/Users/Addy/Projects/somethingsnappydb/data/BRCA1_variants.txt",'\t')

print (data.columns)