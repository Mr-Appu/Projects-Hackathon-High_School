### Imports ###
# add imports - classes and defs
import sys
from predictor import predictRuns
import warnings
warnings.filterwarnings("ignore")

"""
sys.argv[1] is the input test file name given as command line arguments

"""
runs = predictRuns('inputFile.csv')

print("Predicted Runs: ", runs)