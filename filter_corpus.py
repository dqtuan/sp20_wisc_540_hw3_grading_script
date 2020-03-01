"""
    @author: Tuan Dinh (tuan.dinh@wisc.edu)
    Grading script for HW3 - 540 - Spring 2020
    Filter students in TA's corpus
"""
import os, shutil, glob

grader_path = "grader.txt"
submission_path = 'submissions'
log_path = 'log_grader.txt'
corpus_path = 'corpus'
fname = 'nqueens'
if not os.path.exists(corpus_path):
    os.makedirs(corpus_path)
# list of students
f = open(grader_path, "r")
students = f.readlines()
f.close()

logf = open(log_path, "w")
# move to submissions
# os.chdir(submission_path)
for s in sorted(students):
    # Name processing
    full_name = s.split('\t')[0]
    names = full_name.split(' ')
    first_name = names[0]
    last_name = names[-1]
    first_name = first_name.lower().strip()
    last_name = last_name.lower().strip()
    sid = last_name + first_name
    print(sid)
    # Files
    ls = glob.glob("{}/{}*{}*.py".format(submission_path, sid, fname))
    if len(ls) > 0:
        s_path = os.path.join(corpus_path, sid)
        if not os.path.exists(s_path):
            os.makedirs(s_path)
        src_path = ls[0]
        dst_path = os.path.join(s_path, "{}.py".format(fname))
        shutil.copy(src_path, dst_path)

    logf.write("{} {} {} {}\n".format(sid, first_name, last_name, len(ls)))
