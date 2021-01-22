# -*- coding: utf-8 -*-
import os
import re, sys
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--dir", required=True,
	help="path to caption file")
args = vars(ap.parse_args())


def is_time_stamp(l):
  if re.search('-->', l):
    return True
  return False

def has_letters(line):
  if re.search('[a-zA-Z]', line):
    return True
  return False

def is_lowercase_letter_or_comma(letter):
  if letter.isalpha() and letter.lower() == letter:
    return True
  if letter == ',':
    return True
  return False

def has_no_text(line):
  l = line.strip()
  if not len(l):
    return True
  if l.isnumeric():
    return True
  if is_time_stamp(l):
    return True
  if l[0] == '(' and l[-1] == ')':
    return True
  if not has_letters(line):
    return True
  return False

def clean_up(lines):
  """
  Get rid of all non-text lines and
  try to combine text broken into multiple lines
  """
  new_lines = []
  for line in lines[1:]:
    if has_no_text(line):
      continue
    elif len(new_lines) and is_lowercase_letter_or_comma(line[0]):
      #combine with previous line
      new_lines[-1] = new_lines[-1].strip() + ' ' + line
    else:
      #append line
      new_lines.append(line)
  return new_lines

def get_sec(time_str):
    h, m, s = time_str.split(':')
    return float(h) * 3600 + float(m) * 60 + float(s)

def caption_file_to_text_converter():
    file_lists = os.listdir(args.get("dir")+" Caption SRT")
    avg_word_per_minute = 0
    sum_wpm = 0
    for file in file_lists:
        all_text = ''
        # file = "ABC 7 News at Noon - Jul 8.en.srt"
        # print(file)
        try:
            ftext = open(args.get("dir")+" Caption Text/"+file.replace('.srt','')+".txt", "w+")
            with open(args.get("dir")+" Caption SRT/"+file) as f:
                lines = f.readlines()
                latency = 0
                no_of_words = 0
                texts = ''
                count = 1
                old_line = ''
                for line in lines:
                    if is_time_stamp(str(line)):
                        # print("timestamp")
                        times = str(line).replace(',', '.').split(' --> ')
                        latency = float(get_sec(times[1]) - get_sec(times[0]))
                        texts = texts + os.linesep
                    elif len(line) < 3:

                        print("text::")

                    elif has_no_text(str(line)):
                        print("Line Number::" + str(line))

                    elif has_letters(str(line)):
                        if old_line == line:
                            continue
                        else:
                            texts = texts + " " + line.rstrip()
                            words = str(texts).split(" ")
                            no_of_words = len(words)
                            old_line = line

            ftext.write(texts.replace('>>> ','').replace('- ','').replace('>> ','').replace(' >>','').replace('>>>','').replace('>>',''))
            ftext.close()

        except:
            print("File Not Found Error.")
        # i = 1
        # if i == 1:
        #     break

caption_file_to_text_converter()

