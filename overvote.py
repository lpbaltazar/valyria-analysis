import pandas as pd
import numpy as np
import warnings
import os

warnings.filterwarnings('ignore')

from utils.utils import readFile, saveFile

dump = os.path.abspath('../dump/78')
static = os.path.abspath('../static/')
filename = 'results.csv'

results = readFile(os.path.join(dump, filename))
precincts = readFile(os.path.join(static, 'precincts.csv'))
results = results.merge(precincts, left_on = 'PRECINCT_CODE', right_on = 'CLUSTERED_PREC')
overvotes = results.drop_duplicates('PRECINCT_CODE', keep = 'first')


