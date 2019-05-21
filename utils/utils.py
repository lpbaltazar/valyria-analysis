import pandas as pd
import numpy as np

import warnings
import os

warnings.filterwarnings('ignore')

def readFile(file):
	df = pd.read_csv(file, sep = ',', encoding = 'utf-8', dtype = str, low_memory = False)
	return df

def saveFile(df, path, filename, index = False):
	df.to_csv(os.path.join(path, filename), sep = ',', encoding = 'utf-8', index = index)
	print('Saved file {}'.filename)

def sliceDataframe(df, precincts, order, slicer, out_path):
	t = slicer*order
	precincts_included = precincts[:t]
	tranmission = df.loc[df.PRECINCT_CODE.isin(precincts_included)]
	filename = "results_"+str(order-1)+".csv"
	saveFile(tranmission, out_path, filename)

def makeDummy(file):
	df = readFile(file)
	precincts = df.PRECINCT_CODE.unique()

	slicer = int(len(precincts)*.2)

	for i in range(1,6):
		print('Dummy data: ', i)
		sliceDataframe(df, precincts, i, slicer)