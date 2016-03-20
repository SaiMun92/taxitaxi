import pandas as pd
import json
import speed as sp
from datetime import datetime
import numpy as np
from constants import *
import copy as cp

def load_train_file():
	print ("Reading train.csv file...")
	handle = load_file