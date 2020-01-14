import nltk as nlp
import argparse
import os

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--dir", required=True,
	help="path to caption file")
args = vars(ap.parse_args())

file_lists=os.listdir(args.get("dir")+" Caption Text")

for file in file_lists:
    all_text = ''
    no_of_words = 0
    print(file)
    try:
        with open(args.get("dir")+" Caption Text/"+file) as f:
            lines = f.readlines()
            for line in lines:
                no_of_words = no_of_words + len(line.split())
                all_text = all_text + line
        Words = all_text.split()
        frequency_distribution = nlp.FreqDist(Words)
        print(frequency_distribution)
        print(frequency_distribution['<i>'])
        print(str(no_of_words))
    except:
        print("Error Appeared")

