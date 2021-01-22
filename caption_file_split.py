import argparse
from fuzzywuzzy import fuzz, process

import os
# Use fuzzy to chunkify and alignment: https://www.datacamp.com/community/tutorials/fuzzy-string-python
def caption_file_align_and_split():
	ap = argparse.ArgumentParser()
	ap.add_argument("-i", "--name", required=True,
		help="caption file name")

	ap.add_argument("-j", "--fname", required=True,
		help="caption folder name")

	args = vars(ap.parse_args())

	with open("Processed Reference Caption Text/" + args.get("name"), 'r') as hfile:
		reference_lines = hfile.readlines()
	with open("Processed Hypothesis Caption Text/" + args.get("name"), 'r') as rfile:
		hypothesis_lines = rfile.readlines()
	# same = set(hfile).intersection(rfile)
	# line_number = int(args.get("number"))
	# Token_Set_Ratio = fuzz.token_set_ratio(hypothesis_lines[line_number].lower(),reference_lines[line_number].lower())

	# while(hyp_index<len(hypothesis_lines)):
	# 	Token_Set_Ratio = 0
	# 	if(hypothesis_lines[hyp_index]<reference_lines[ref_index]):
	# 		Token_Set_Ratio= max(fuzz.token_set_ratio(hypothesis_lines[line_number].lower(),
	# 										   reference_lines[line_number].lower()),fuzz.token_set_ratio(hypothesis_lines[line_number].lower(),
	# 										   reference_lines[line_number].lower()+reference_lines[line_number+1].lower()
	# 																									  ))
	#
	# 	if(Token_Set_Ratio>70):
	# 		ftext = open("Split Hypothesis Files/" + ref_index+".txt", "w+")
	# 		ftext.write(reference_lines+"\n"+hypothesis_text+"\n")
	# 		ftext.close()


	# print(hypothesis_lines[line_number]+" "+str(Token_Set_Ratio))
	# print(len(hypothesis_lines[line_number])/len(reference_lines[line_number]))
	# if(len(hypothesis_lines[line_number])/len(reference_lines[line_number])<0.40):
	# 	Ratios = process.extract(hypothesis_lines[line_number].lower().replace('\n','')+hypothesis_lines[line_number+1].lower(),
	# 							 reference_lines[line_number].lower().split())
	# 	print(hypothesis_lines[line_number].lower().replace('\n','')+hypothesis_lines[line_number + 1].lower())
	# else:
	# 	Ratios = process.extract(hypothesis_lines[line_number].lower(), reference_lines[line_number].lower().split())
	# 	print(hypothesis_lines[line_number].lower())
	# print(reference_lines[line_number].lower())
	#
	# abc_7_jul_8
	reference_text=""
	hypthesis_text=""
	total_length = len(hypothesis_lines)
	for i in range(0,len(hypothesis_lines)-1):
		if i%4==0 and hypthesis_text != "":
			ftext = open("Split Hypothesis Files/"+ args.get("fname")+"/" + str(int(i/4))+".txt", "w+")
			ftext.write(hypthesis_text)
			ftext.close()
			ftext = open("Split Reference Files/"+ args.get("fname")+"/" + str(int(i/4))+".txt", "w+")
			ftext.write(reference_text)
			ftext.close()
			hypthesis_text=""
			reference_text=""
		hypthesis_text = hypthesis_text + hypothesis_lines[i]
		reference_text = reference_text + reference_lines[i]
	if hypthesis_text != "":
		ftext = open("Split Hypothesis Files/"+ args.get("fname")+"/" + str(int(total_length/4)+1) + ".txt", "w+")
		ftext.write(hypthesis_text)
		ftext.close()
		ftext = open("Split Reference Files/"+ args.get("fname")+"/" + str(int(total_length/4)+1) + ".txt", "w+")
		ftext.write(reference_text)
		ftext.close()
	# print(Token_Set_Ratio)

caption_file_align_and_split()