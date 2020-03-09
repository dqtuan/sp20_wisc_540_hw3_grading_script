"""
	@author: Tuan Dinh (tuan.dinh@wisc.edu)
	Grading script for HW3 - 540 - Spring 2020
	Evaluate all students
"""

import os, sys
import importlib
from eval import evaluate

corpus_path = 'corpus'
corpus3_path = 'corpus3'
fname = 'nqueens'
for d in sorted(os.listdir(corpus_path)):
	stu_path = os.path.join(corpus_path, d)
	print(d)
	mod = False
	if os.path.isdir(stu_path) and not os.path.islink(stu_path):
		try:
			# python 3
			mod = importlib.import_module('{}.{}.{}'.format(corpus_path, d, fname))
		except:
			# python 2 -> python 3
			try:
				mod = importlib.import_module('{}.{}.{}'.format(corpus3_path, d, fname))
			except:
				print('Should comment nqueens live code!!')
		if mod:
			evaluate(stu_path, mod, num_tests=5)
