import argparse
import os
import argparse
import re
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
    ##################################Max Matching################################
    with open("Processed Hypothesis Caption Text/" + args.get("name")) as fh:
        hypothesis_lines = fh.readlines()
    with open("Processed Reference Caption Text/"+args.get("name")) as fr:
        reference_lines = fr.readlines()
    max_match_sentence = ''
    # matching_map = [[]]
    num_of_lines = min(100, len(reference_lines))
    range_match_forward = 5
    range_match_backward = 5
    matching_map = {}
    aligned_reference_lines = ["" for x in range(num_of_lines)]

    i = 0
    value_index = 0
    for j in range(num_of_lines):
        r_line = reference_lines[j]
        max_val = 0

        max_match_sentence = r_line

        r_line = re.sub(r"[^a-zA-Z0-9.?! ]+", "", r_line)
        r_line_words = r_line.lower().split()
        # identify first non-empty line#
        if len(r_line_words) > 0:
            i += 1
        else:
            continue

        ###################################
        upper_boundary = max(j+range_match_forward, value_index+range_match_forward)
        lower_bound = min(j-range_match_backward, value_index-1)
        if lower_bound < 0:
            lower_bound = 0
        if len(hypothesis_lines) <= upper_boundary:
            upper_boundary = len(hypothesis_lines)
        for k in range(lower_bound, upper_boundary):
            # print(h_line_words)
            h_line = hypothesis_lines[k]
            actual_h_line = h_line

            h_line = re.sub(r"[^a-zA-Z0-9.?! ]+", "", h_line)
            h_line_words = h_line.lower().split()
            if len(h_line_words) > 0:
                if max_val < LCSubStr(h_line_words, r_line_words, len(h_line_words), len(r_line_words)):
                    max_match_sentence = actual_h_line

                max_val = max(max_val, LCSubStr(h_line_words, r_line_words, len(h_line_words), len(r_line_words)))
            else:
                continue

        print(max_match_sentence)
        print(r_line_words)
        ######################## Hash Map Start ##############################
        # Matching Map is a `hashmap` which can contain list of index        #
        # against one index, for example:                                    #
        # if line 3,4,5 of hypothesis file possess high                      #
        # longest common subsequence score with line 2 of reference file,    #
        # then this information will be stored in  matching_map like this:   #
        #  matching_map[2]=[3,4,5]                                           #
        ######################################################################
        try:
            value_index = hypothesis_lines.index(max_match_sentence)

            aligned_reference_lines[j] = max_match_sentence
        except:
            print("An exception occurred")
        print(value_index)
        arr = []
        if value_index in matching_map:
            arr = matching_map[value_index]
            arr.append(j)
            matching_map[value_index] = arr
        else:
            arr.append(j)
            matching_map[value_index] = arr
        ###################### Hash Map End #####################################

        if i == num_of_lines:
            break
    print(matching_map)

    ftext_ref = open("Automatic Annotation Reference Text V2/" + "Annotated_" + args.get("name"), "w+")
    ftext_hyp = open("Automatic Annotation Hypothesis Text V2/" + "Annotated_" + args.get("name"), "w+")
    annotated_ref_text=""
    annotated_hyp_text=""
    for key,value in matching_map.items():
        annotated_hyp_text = annotated_hyp_text + hypothesis_lines[key]
        temp_ref_lines = ""
        for r_index in value:
            temp_ref_lines=temp_ref_lines+" "+reference_lines[r_index].strip('\n')
        annotated_ref_text = annotated_ref_text +"\n"+ temp_ref_lines

    ftext_ref.write(annotated_ref_text)
    ftext_ref.close()

    ftext_hyp.write(annotated_hyp_text)
    ftext_hyp.close()


    # for line in aligned_hypothesis_lines:
    #     line = re.sub(r"[^a-zA-Z0-9.?! ]+", "", line)
    #     annotated_ref_text = annotated_ref_text + "\n" + line
    #
    #
    # ftext.write(annotated_ref_text)
    # ftext.close()
    ##################################Max Matching End################################





caption_alignement()