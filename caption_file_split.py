import argparse
import os

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--name", required=True,
	help="caption file name")
args = vars(ap.parse_args())

with open("Hypothesis Caption Text/" + args.get("name"), 'r') as hfile:
	with open("Processed Reference Caption Text/" + args.get("name"), 'r') as rfile:
		same = set(hfile).intersection(rfile)

same.discard('\n')

with open('some_output_file.txt', 'w') as file_out:
	for line in same:
		file_out.write(line)