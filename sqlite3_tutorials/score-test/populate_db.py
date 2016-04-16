#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3 
import sys
import numpy as np

import pdb

someUsers = ['kaese','hendrik','jan','fritz']

someQuestions = [("Whats better, Pepsi or Coke?", ('Pepsi','Coke')),
                 ("Whats cooler, London or NYC?", ('London','NYC')),
                 ("Whos hotter, Angelina Jolie or Gisele Buendchen?", ('Angelina','Gisele'))]

con = None

def addNewUser(cursor,name):
    # check if user already in the database
    cur.execute('SELECT * FROM Users WHERE Name=(?)',[name])   
    entry=cur.fetchone()
    if not entry:
        cur.execute("INSERT INTO Users(Name) VALUES (?)",[name])

def addNewQuestion(cursor,user_id,question,answer1,answer2):
    # do i still need to escape apostrophes ?
    cur.execute('INSERT INTO Questions(User_Id, Question, Answer1, Answer2) \
                 VALUES (?, ?, ?, ?);',[user_id,question,answer1,answer2])
#


try:
    #connection
    con=sqlite3.connect('test.db')
    #cursor
    cur=con.cursor()
    
    #add User
    for e in someUsers:
        addNewUser(cur,e)

    #add Questions
    currentUser='Booya'
    #getCurrentUserID(current_user)
    currentUserId=133

    for e in someQuestions:
        addNewQuestion(cur,currentUserId,e[0],e[1][0],e[1][1])

    con.commit()

# Finalise ...
except sqlite3.Error as e:
    if con:
        con.rollback()
    print('ERROR: {}'.format(e.args[0]))
    sys.exit()
finally:
    if con:
        con.close()
