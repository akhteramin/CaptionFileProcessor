# caption-file-reader

This is offline closed caption processor. This processor will linearize the caption text in different format of caption. Then feed the file into different caption transcription evaluator ACE. Our goal is to perform evaluation between ground truth and caption transcription.

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

# Hypothesis File Cleanup
To cleanup hypothesis file run this command:
`python3 caption_hypothesis_cleanup.py --name 'NFL Live2-Jul 3.en.txt'`
-- The processed hypothesis text file will be saved in "Processed Hypothesis Caption Text" folder. And the file name will remain same.

# Reference File Cleanup

To cleanup reference file run this command:
`python3 caption_reference_alignment.py --name 'NFL Live2-Jul 3.en.txt'`

-- The processed aligned text file will be saved in "Processed Reference Caption Text" folder. And the file name will remain same.

# Further Alignment Phase 2
After thoroughly observing the reference and hypothesis files, if you feel that both text are not properly aligned then run this command below:
`python3 caption_reverse_alignment_V3.py --name 'NFL Live2-Jul 3.en.txt'`

-- This step is used to align reference text with hypothesis text which is reverse approach to the previous one. The generated files will be saved in "Automatic Annotation Hypothesis Text" and "Automatic Annotation Reference Text" folder. Please note that a prefix is added to each aligned files which is "Annotated_".

# In file discrepancy resolver 
After running the above alignment commands, you can look into the files to manually observe how close both of text are. If you feel that there remains a discrepancy between these hypothesis and reference file(sentence level), try this command given below:
`python3 caption_alignment_V2.py --name 'Annotated_NFL Live2-Jul 3.en.txt'`
-- This command will load hypothesis and reference file from "Automatic Annotation *" folder. This is why we have added the prefix "Annotated_" to the file name in the command.
# File splitting for feeding into ACE
Before running the command below, a folder named "abc_jul_8"(Pseudo name, for each file title should be selected uniquely.) need to be created under both "Split Hypothesis Files" and "Split Reference Files"

Line by line comparison command:
`python3 caption_file_split.py --name 'ABC 7 News at Noon - Jul 8.en.txt' --fname 'abc_jul_8'`


# Hypothesis and Reference File manual Alignment segment
Automatic Text Alignment Report can be found here:
https://docs.google.com/spreadsheets/d/1KHIr2VKnDIGRh81kyz0C8gHg3rm9c6cz5bV2TFookcg/edit#gid=0

