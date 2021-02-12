import argparse
import os
from nltk import tokenize
import re
####################nltk text file download and install start##########################
# import nltk
# import ssl
#
# try:
#     _create_unverified_https_context = ssl._create_unverified_context
# except AttributeError:
#     pass
# else:
#     ssl._create_default_https_context = _create_unverified_https_context
#
# nltk.download()
####################nltk text file download and install end##########################


# Use fuzzy to chunkify and alignment: https://www.datacamp.com/community/tutorials/fuzzy-string-python
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--name", required=True,
	help="caption file name")
args = vars(ap.parse_args())

def subsequent_matching_removal(pre_string, current_str):
    start = 0
    result = ""
    pre_words = pre_string.split()
    current_words = current_str.split()
    try:
        for i in range(len(pre_words)):
            if pre_words[i] == current_words[start]:
                start = start + 1
            elif pre_words[i] != current_words[start] and start < 2:
                start = 0

    except IndexError:
        return result

    for i in range(start, len(current_words)):
        print(current_words[i])
        result = result+" " + current_words[i]
    return result


def cleanup_hypothesis_file():
    i=0
    previous_sentence=""
    with open("Hypothesis Caption Text/"+args.get("name")) as fh:
        hypothesis_lines = fh.readlines()
    hypthesis_text=""
    for h_line in hypothesis_lines:
        if i==0:
            i=i+1
            previous_sentence = h_line
            hypthesis_text = hypthesis_text + previous_sentence
        else:
            hypthesis_text=hypthesis_text+subsequent_matching_removal(previous_sentence,h_line)
            previous_sentence = h_line
    sentence = tokenize.sent_tokenize(hypthesis_text)
    hypthesis_text = ""
    for line in sentence:
        line = re.sub(r"[^a-zA-Z0-9.?! ]+", "", line)
        hypthesis_text = hypthesis_text+ "\n" + line
    ftext = open("Processed Hypothesis Caption Text/" + args.get("name"), "w+")
    # texts = ' '.join(map(str, hypthesis_text))

    ftext.write(hypthesis_text)
    ftext.close()

cleanup_hypothesis_file()