import re, sys
import argparse

def is_time_stamp(l):
  if re.search('-->', line):
    return True
  return False

def has_letters(line):
  if re.search('[a-zA-Z]', line):
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


ap = argparse.ArgumentParser()
ap.add_argument("-rf", "--hfile", type=str,
	help="path to optinal reference file")
ap.add_argument("-hf", "--rfile", type=str,
	help="path to optinal reference file")
ap.add_argument("-en", "--encode", type=str,
	help="path to optinal encoding type")
args = vars(ap.parse_args())

try:
    files = [args["hfile"],args["rfile"]]
    for file in files:
        file_encoding = 'utf-8' if len(args) < 3 else args["encode"]
        with open(file) as f:
            lines = f.readlines()
            for line in lines:
                if is_time_stamp(unicode(line, 'utf-8')):
                    print("timestamp")
                elif len(line) < 3:
                    print("Break")
                elif has_no_text(unicode(line, 'utf-8')):
                    print("Line Number::"+str(len(unicode(line, 'utf-8'))))
                elif has_letters(unicode(line, 'utf-8')):
                    print("text")
                print(line.strip())
except ValueError:
    print("No file Parameter provided.")

    # print(lines)clc