#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3 
import sys
import numpy as np

con = None

# the real stuff
try:
    #connection
    con=sqlite3.connect('test.db')
    #cursor
    cur=con.cursor()
    cur.execute('SELECT Question, Answer1, Answer2 FROM Questions')
    allQuestions=cur.fetchall()
    for q in allQuestions:
        print 'You really want to know: {0}\n'.format(q[0])
        print 'Could be {0} or {1}\n'.format(q[1],q[2])
    print('==============================')

# Finalise ...
except sqlite3.Error as e:
    if con:
        con.rollback()
    print('ERROR: {}'.format(e.args[0]))
    sys.exit()
finally:
    if con:
        con.close()
