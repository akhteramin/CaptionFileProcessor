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
    # reference_lines = ''
    # hypothesis_lines = ''
    # with open("Reference Caption Text/"+args.get("name")) as fr:
    #     reference_lines = fr.readlines()
    # with open("Processed Hypothesis Caption Text/"+args.get("name")) as fh:
    #     hypothesis_lines = fh.readlines()
    # ##########################Sentence Tokenizer Start##################################
    # ref_lines = reference_lines[0:]
    # # ref_lines = reference_lines[value_index:]
    # # hypothesis_lines = reference_lines
    # reference_text = ""
    # for r_line in ref_lines:
    #     reference_text = reference_text + r_line
    #
    # ftext = open("Processed Reference Caption Text/" + args.get("name"), "w+")
    #
    # # texts = ' '.join(map(str, reference_lines[value_index:]))
    #
    # # reference_text = reference_text.replace('.','.\n')
    # sentence = tokenize.sent_tokenize(reference_text)
    # reference_text = ""
    # for line in sentence:
    #     line = re.sub(r"[^a-zA-Z0-9.?! ]+", "", line)
    #     reference_text = reference_text + "\n" + line
    #
    # ftext.write(reference_text)
    # ftext.close()
    ##########################Sentence Tokenizer End##################################

    ##################################Max Matching################################
    with open("Automatic Annotation Hypothesis Text/" + args.get("name")) as fh:
        hypothesis_lines = fh.readlines()
    with open("Automatic Annotation Reference Text/"+args.get("name")) as fr:
        reference_lines = fr.readlines()
    max_match_sentence = ''
    # matching_map = [[]]
    num_of_lines = min(50, len(hypothesis_lines))
    range_match_forward = 5
    range_match_backward = 5
    matching_map = {}
    aligned_hypothesis_lines = ["" for x in range(num_of_lines)]

    i = 0
    value_index = 0
    for j in range(num_of_lines):
        h_line = hypothesis_lines[j]
        max_val = 0
        current_hypothesis_index = j

        max_match_sentence = h_line

        # h_line = h_line.replace('.', '').replace(',',' ')
        h_line = re.sub(r"[^a-zA-Z0-9.?! ]+", "", h_line)
        h_line_words = h_line.lower().split()
        # identify first non-empty line#
        if len(h_line_words) > 0:
            i += 1
        else:
            continue

        ###################################
        upper_boundary=max(j+range_match_forward,value_index+range_match_forward)
        if j < range_match_backward:
            range_match_backward = j
        if len(reference_lines) <= upper_boundary:
            upper_boundary = len(reference_lines)
        for k in range(min(j-range_match_backward,value_index-1), upper_boundary):
            # print(h_line_words)
            r_line = reference_lines[k]
            actual_r_line = r_line
            current_reference_index = reference_lines.index(actual_r_line)
            # r_line = r_line.replace('.', '').replace(',', ' ')
            r_line = re.sub(r"[^a-zA-Z0-9.?! ]+", "", r_line)
            r_line_words = r_line.lower().split()
            if len(r_line_words) > 0:
                if max_val < LCSubStr(r_line_words, h_line_words, len(r_line_words), len(h_line_words)):
                    max_match_sentence = actual_r_line

                max_val = max(max_val, LCSubStr(r_line_words, h_line_words, len(r_line_words), len(h_line_words)))
            else:
                continue

        print(max_match_sentence)
        print(h_line_words)

        try:
            value_index = reference_lines.index(max_match_sentence)

            aligned_hypothesis_lines[j] = max_match_sentence
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

        if i == num_of_lines:
            break
    print(matching_map)

    ftext_ref = open("Automatic Annotation Reference Text/"+ "Annotated_V2_" +args.get("name"), "w+")
    ftext_hyp = open("Automatic Annotation Hypothesis Text/" + "Annotated_V2_" + args.get("name"), "w+")
    annotated_ref_text=""
    annotated_hyp_text=""
    for key,value in matching_map.items():
        annotated_ref_text = annotated_ref_text + reference_lines[key]
        temp_hyp_lines = ""
        for r_index in value:
            temp_hyp_lines=temp_hyp_lines+" "+hypothesis_lines[r_index].strip('\n')
        annotated_hyp_text = annotated_hyp_text +"\n"+ temp_hyp_lines

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