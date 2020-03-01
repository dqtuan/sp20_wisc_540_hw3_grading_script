# sp20_wisc_540_hw3_grading_script

How to grade:
- Download this folder of scripts
- Download submissions.zip and extract it into the script folder, name it **submissions**
- Put your grader<>.txt in this folder, name it **grader.txt**
- Run **sh grade.sh** in the script folder
- Results (score, log, output) of each student will be stored in **corpus/<studentid>/**
This script uses **Python 3**
  
Explain:
The script grade.sh consists of:
- Filter the corpus of students each TA needs to grade
- Convert python2 to python3 (corpus 3)
- Evaluate all testcases (main.py)

Notice:
- We have to use Python 3
- Expected outputs with inputs are stored in folder test
- We have to manually grade nqueens_restart (20 points)
