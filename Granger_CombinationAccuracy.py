import pandas as pd
import itertools
import sys
from scipy import stats

#our functions from other files
import Granger_Combination as cmb
import Granger_CognitiveDiversity as cogdiv

# sets up a pandas dataframe with the gaze data, based on command line inputs.
def setup_data():
	# trys to take in the argument (names of gaze data file) from the command line
	try:
		gazeData = pd.read_csv("Gaze_DataFile.csv")
		rankData = pd.read_csv("Gaze_DataRanks.csv")

		gazeData = gazeData.iloc[:, 1:]
		rankData = rankData.iloc[:, 1:]


		return(gazeData, rankData)

	#ends the program if the data is not input correctly.
	except (ZeroDivisionError, IndexError):
		print "Error with the input file"
		quit()

# returns a list of lists, which includes all possible subsets of the original list. Takes in a list of items, which can be either numbers or strings
def combinations(data):
	combos = []
	for i in range(len(data)+1):
		els = [list(x) for x in itertools.combinations(data, i)]
		combos.extend(els)

	#removes the empty list from our list of lists
	if [] in combos:
		combos.remove([])

	return combos

def main():

	#setup variables
	precisionAt = [100,200,300]
	gazeData, rankData = setup_data()
	combos = combinations( range(gazeData.shape[1]-1))

	singlecombos = [0,1,2,3,4]
	print "Cognitive Diversity: "
		#	for attr1 in combos:
		#		diversity_sum = 0.0
		#
		#		for attr2 in combos:
		#			if attr1 == attr2:
		#				continue
		#			#print "Score diversity between " + str(attr1) + " and " + str(attr2) + " is " + str(cogdiv.calculateDiversity(gazeData, attr1, attr2))
		#			temp1 = cogdiv.calculateDiversity(gazeData, attr1, attr2)
		#			diversity_sum += temp1[0]
		#			print "Cog diversity single max diff between " + str(map(lambda x: chr(x+65), attr1)) + " and " + str(map(lambda x: chr(x+65), attr2)) + " is " + str(temp1[1])
		#		print "\n\tScore diversity of " + str(attr1) + " against all other attribute combinations is " + str(round(diversity_sum, 2)) + "\n"
	print "\tOmitted\n"

	# runs score and rank total for each combinations, and neatly prints out the result.
	for attrs in combos:
		print map(lambda x: chr(x+65), attrs)
		print "\tScore combination accuracy percentages: " + str(cmb.accuracy(gazeData, attrs, precisionAt))
		print "\tRank  combination accuracy percentages: " + str(cmb.accuracy(rankData, attrs, precisionAt))
		print


if __name__ == '__main__':
	main()
