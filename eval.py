"""
    @author: Tuan Dinh (tuan.dinh@wisc.edu)
    Grading script for HW3 - 540 - Spring 2020
"""
import numpy as np
import os, shutil
import io
import ast
import signal
from contextlib import redirect_stdout
import re

from testcases import testset
from soln import succ as soln_succ
from soln import choose_next as soln_choose_next
from soln import f as soln_f
from soln import nqueens as soln_nqueens
from soln import nqueens_restart as soln_nqueens_restart
# from nqueens import succ, f, choose_next, nqueens, nqueens_restart

# target functions
soln_fns = [soln_succ, soln_f, soln_choose_next, soln_nqueens, soln_nqueens_restart]
func_names = ['succ', 'f', 'choose_next', 'nqueens', 'nqueens_restart']

#####------------Helpers-----------------###

def compare(k, answer, output):
    if k == 0: # succ
        # a list of list
        return sorted(answer) == sorted(output)
    else: #f, choose_next, nqueens-answers
        return answer == output

def convert_succ_to_lst(out):
    lst = out.split('\n')
    lst_succ = []
    for x in lst:
        r = re.search(r'\[[^\]]*\]', x)
        if r:
            lst_succ.append(ast.literal_eval(r.group()))
    return lst_succ

def get_nqueens(fn, x):
    o = io.StringIO()
    with redirect_stdout(o):
        re = fn(x['state'], boulderX=x['boulder'][0], boulderY=x['boulder'][1])
    out = o.getvalue()
    return out, re

def write_output(output, fpath):
    f = open(fpath, "w")
    f.write(str(output))
    f.close()

def mkdir(name, rm=True):
    if not os.path.exists(name):
        os.makedirs(name)
    elif rm:
        shutil.rmtree(name)
        os.makedirs(name)

class TimeOutException(Exception):
   pass

def handler(signum, frame):
    raise TimeOutException()

####---- Evaluation function ############
def get_fn(k, mod):
    if k == 0:
        return mod.succ
    if k == 1:
        return mod.f
    if k == 2:
        return mod.choose_next
    if k == 3:
        return mod.nqueens
    if k == 4:
        return mod.nqueens_restart

def evaluate(stu_path, mod, num_tests=4):
    report_path = '{}/scores.txt'.format(stu_path)
    log_path = '{}/log.txt'.format(stu_path)
    output_path = '{}/output'.format(stu_path)
    mkdir(output_path)
    freport = open(report_path, 'w')
    logf = open(log_path, 'w')
    score = 0
    signal.signal(signal.SIGALRM, handler)
    # Not Restart
    for k in range(num_tests):
        func_name = func_names[k]
        # print(func_name)
        cases = testset[str(k)]
        fn = soln_fns[k]
        try:
            stu_fn = get_fn(k, mod)
        except:
            freport.write("{}: No function found\n".format(func_name))
            continue
        output = ""
        for i in range(len(cases)):
            x = cases[i]
            test_name = "{}_{}".format(func_name, i)
            try:
                signal.alarm(2)
                if k < 3:
                    answer = fn(x['state'], boulderX=x['boulder'][0], boulderY=x['boulder'][1])
                    output = stu_fn(x['state'], boulderX=x['boulder'][0], boulderY=x['boulder'][1])
                elif k == 3:
                    succ_answer, answer = get_nqueens(fn, x)
                    succ_output, output = get_nqueens(stu_fn, x)
                elif k == 4:
                    o = io.StringIO()
                    with redirect_stdout(o):
                        stu_fn(n=x['n'], k=x['k'], boulderX=x['boulder'][0], boulderY=x['boulder'][1])
                    output = o.getvalue()
                # compare results
                signal.alarm(0)

                if k == 4:
                    # default setting
                    score += x['score']
                    mess3 = 'passed +{}'.format(x['score'])
                    freport.write("{}_solution: {}\n".format(test_name, mess3))
                    score += x['score']
                    message = 'passed +{}'.format(x['score'])
                else:
                    # write report
                    result = compare(k, answer, output)
                    if result:
                        score += x['score']
                        message = 'passed +{}'.format(x['score'])
                    else:
                        message = 'wrong output'
                    # nqueens
                    if k == 3:
                        try:
                            out_succ = convert_succ_to_lst(succ_output)
                            ans_succ = convert_succ_to_lst(succ_answer)
                            if out_succ == ans_succ:
                                mess3 = 'passed +{}'.format(x['score'])
                                score += x['score']
                            else:
                                mess3 = 'wrong output'
                            # for printing
                            output = "{}=> {}".format(succ_output, output)
                        except:
                            mess3 = 'comparison exception'
                        freport.write("{}_finalstate: {}\n".format(test_name, mess3))
            except TimeOutException as exc:
                message = "Time Out"
            except:
                message = "Function Exception"
            # print out
            freport.write("{}: {}\n".format(test_name, message))
            fname = '{}.txt'.format(test_name)
            fpath_output = os.path.join(output_path, fname)
            write_output(output, fpath_output)
            # write_output(answer, fpath_answer)

    print('===> score: {}'.format(score))
    freport.write('Total: {}/100'.format(score))
    freport.close()
