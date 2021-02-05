# caption-file-reader
Reading caption file(i.e: srt, vtt etc) and convert them to JSON object.
caption-processor

This is offline closed caption processor. This processor will linearize the caption text in different format of caption. Then feed the file into different caption analyzer such as ACE, SCLITE and others. Our goal is to analysis between ground truth and caption transcription.

# Caption Reader

Create a Python environment with python 3.6/3.7
Activate the environment before jumping into the code execution
Run the command below Command:
`python3 bulk_caption_file_converter.py --dir [Directory name where the srt files resides]`

As example: While reading srt files from "Hypothesis Caption SRT" directory our execution command will be like this:

`python3 bulk_caption_file_converter.py --dir Hypothesis`

# Alignment Instruction
Question: Why do we need alignement?
Answer: Our ACE or ACE2 framework measure quality of caption comparing between two direct transcription. But in real life scenario, sometimes reference caption transcription may contain additional text which impede the files to be evaluated by ACE. Therefore, we need to find the intial starting point in reference file so that additional intial information are rescinded before feeding these files into ACE. To know more about ACE please follow this GIT url:

First, we recommend to look into both of the hypothesis and reference file side by side.

Second, identify the 1st sentence of hypothesis file in reference file.

Third, try to make them as close as possible by performing some wizard-of-oz actions such as if the sentence breaks into multiple sentence in reference file, merge them before running the following script.

Run caption alignment file:
`python3 caption_reference_alignment.py --name 'NFL Live2-Jul 3.en.txt'`

-- The processed aligned text file will be saved in "Processed Reference Caption Text" folder. And the file name will remain same.

# Hypothesis Cleanup
To cleanup hypothesis file run this command:
`python3 caption_hypothesis_cleanup.py --name 'NFL Live2-Jul 3.en.txt'`
-- The processed hypothesis text file will be saved in "Processed Hypothesis Caption Text" folder. And the file name will remain same.

# File splitting for feeding into ACE
Line by line comparison command:
`python3 caption_file_split.py --name 'ABC 7 News at Noon - Jul 8.en.txt' --fname 'abc_jul_8'`

Before running this command a folder named "abc_jul_8" need to be created under both "Split Hypothesis Files" and "Split Reference Files"

# Hypothesis and Reference File manual Alignment segment
We have manually aligned the file till the text matched substantially side by side. 
1. ABC 7 News at Noon - Jul 8.en.txt -- 87 lines
2. CNN With Poppy Harlow&Jim Sciutto -Jul 8.en.txt -- 16 lines


