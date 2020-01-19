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


file_lists=os.listdir(args.get("dir")+" Caption SRT")



avg_word_per_minute = 0
sum_wpm = 0
for file in file_lists:
    all_text = ''
    print(file)
    try:
        ftext = open(args.get("dir")+" Caption Text/"+file.replace('.srt','')+".txt", "w+")
        with open(args.get("dir")+" Caption SRT/"+file) as f:
            lines = f.readlines()
            latency = 0
            no_of_words = 0
            texts = ''
            count = 1;
            for line in lines:
                if is_time_stamp(str(line)):
                    print("timestamp")
                    times = str(line).replace(',', '.').split(' --> ')
                    latency = float(get_sec(times[1]) - get_sec(times[0]))
                    # print(times[0]+" "+times[1])
                elif len(line) < 3:

                    all_text = all_text+ texts
                    try:
                        word_per_minute = float((no_of_words - 1) * 60 / latency)
                        sum_wpm = sum_wpm + word_per_minute
                        print("word per minute::" + str(latency))
                        print("word per minute::" + str(word_per_minute))
                    except:
                        print("Division by Zero error")
                    print(line.strip())
                    no_of_words = 0
                    texts = ''
                    print("Break")
                    count = count + 1
                elif has_no_text(str(line)):
                    print("Line Number::" + str(len(str(line))))
                elif has_letters(str(line)):
                    texts = texts.rstrip() + " " + str(line)
                    words = str(texts).split(" ")
                    no_of_words = len(words)
                    print("text::" + texts)
                    texts = re.sub(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', '\n', texts)
        all_text = ' '.join(all_text.split())
        all_text = re.sub(r'<.*?>','',all_text)
        # ftext.write(all_text.replace('\n','').replace('\r','').replace('\"','').replace('♪','[Music]').replace('<','').replace('>',''))

        ftext.write(all_text.replace('\n', '').replace('\r', '').replace('\"', '').replace('♪', '[Music]').replace('>>> ','\n').replace('>> ','\n').replace('- ','\n').replace('. ','.\n'))
        ftext.close()
        avg_word_per_minute = float(sum_wpm / count);
        print ("Average Word Per minute: " + str(avg_word_per_minute))
    except:
        print("File Not Found Error.")