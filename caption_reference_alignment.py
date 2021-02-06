import argparse
import os
import argparse
import os
from nltk import tokenize

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--name", required=True,
	help="caption file name")
args = vars(ap.parse_args())


 # Returns length of longest common substring of X[0..m-1]  and Y[0..n-1] */
def LCSubStr(X,Y,m,n):
    # Create a table to store lengths of
    # longest common suffixes of substrings.
    # Note that LCSuff[i][j] contains the
    # length of longest common suffix of
    # X[0...i-1] and Y[0...j-1]. The first
    # row and first column entries have no
    # logical meaning, they are used only
    # for simplicity of the program.

    # LCSuff is the table with zero
    # value initially in each cell
    LCSuff = [[0 for k in range(n + 1)] for l in range(m + 1)]

    # To store the length of
    # longest common substring
    result = 0

    # Following steps to build
    # LCSuff[m+1][n+1] in bottom up fashion
    for i in range(m + 1):
        for j in range(n + 1):
            if (i == 0 or j == 0):
                LCSuff[i][j] = 0
            elif (X[i - 1] == Y[j - 1]):
                LCSuff[i][j] = LCSuff[i - 1][j - 1] + 1
                result = max(result, LCSuff[i][j])
            else:
                LCSuff[i][j] = 0
    return result


def caption_alignement():
    reference_lines = ''
    hypothesis_lines = ''
    with open("Reference Caption Text/"+args.get("name")) as fr:
        reference_lines = fr.readlines()
    with open("Hypothesis Caption Text/"+args.get("name")) as fh:
        hypothesis_lines = fh.readlines()
    ##################################Max Matching################################
    max_match_sentence = ''
    i = 0
    for h_line in hypothesis_lines:
        max_val = 0

        max_match_sentence = h_line
        h_line = h_line.replace('.', '').replace(',',' ')
        h_line_words = h_line.lower().split()
        # identify first non-empty line#
        if len(h_line_words) > 0:
            i = 1
        else:
            continue
        ###################################
        for r_line in reference_lines:
            print(h_line_words)
            actual_r_line = r_line
            r_line = r_line.replace('.', '').replace(',', ' ')
            r_line_words = r_line.lower().split()
            if len(r_line_words)>0:
                if max_val < LCSubStr(r_line_words,h_line_words,len(r_line_words),len(h_line_words)):
                    max_match_sentence = actual_r_line

                max_val = max(max_val,LCSubStr(r_line_words,h_line_words,len(r_line_words),len(h_line_words)))
            else:
                continue

        if i == 1:
            break
    print(max_match_sentence)
    value_index = reference_lines.index(max_match_sentence)
    print(value_index)
    ##################################Max Matching End################################
    ref_lines =reference_lines[0:]
    # hypothesis_lines = reference_lines
    reference_text=""
    for r_line in ref_lines:
        reference_text = reference_text + r_line

    ftext = open("Processed Reference Caption Text/" + args.get("name"), "w+")

    # texts = ' '.join(map(str, reference_lines[value_index:]))

    # reference_text = reference_text.replace('.','.\n')
    sentence = tokenize.sent_tokenize(reference_text)
    reference_text = ""
    for line in sentence:
        reference_text = reference_text + "\n" + line

    ftext.write(reference_text)
    ftext.close()




caption_alignement()