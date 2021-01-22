import argparse
import os
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

    hypthesis_text = hypthesis_text.replace('.', '.\n')
    ftext = open("Processed Hypothesis Caption Text/" + args.get("name"), "w+")
    # texts = ' '.join(map(str, hypthesis_text))

    ftext.write(hypthesis_text)
    ftext.close()

cleanup_hypothesis_file()