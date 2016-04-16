#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3 , sys, random, os, argparse

con = None
def parse_args():
    parser = argparse.ArgumentParser(description='Creating an sql data base')
    parser.add_argument('--output-file','-o', dest='output_file', action='store', 
            default='test.db',  help='Name of output date base file')
    parser.add_argument('--recreate', dest='recreate', action='store_true', 
            default=False,  help='Recreate data base, i.e. delete existing file if exists')
    return parser.parse_args()

args= parse_args()

if args.recreate:
    os.remove()


def createDatabase(thisDatabase):
    # the real stuff
    try:
        #connection
        con=sqlite3.connect(thisDatabase)
        #cursor
        cur=con.cursor()

        cur.execute('CREATE TABLE IF NOT EXISTS Users(Id INTEGER PRIMARY KEY AUTOINCREMENT, \
                                                      Name TEXT, Score REAL DEFAULT 0.0)')

        cur.execute('CREATE TABLE IF NOT EXISTS Questions(Id INTEGER PRIMARY KEY AUTOINCREMENT, User_Id INTEGER, \
                                                          Question TEXT, Answer1 TEXT, Answer2 TEXT, \
                                                          nReply1 INTEGER DEFAULT 0, nReply2 INTEGER DEFAULT 0)')

        cur.execute('CREATE TABLE IF NOT EXISTS AnswrdQs(Id INTEGER PRIMARY KEY AUTOINCREMENT, User_Id INTEGER,\
                                                         Question_Id INTEGER)')
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


dbName=args.output_file
createDatabase(dbName)
