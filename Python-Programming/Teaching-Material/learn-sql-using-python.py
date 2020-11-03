# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 17:52:48 2020

@author: vivek
"""

import sqlite3

# create new database
conn = sqlite3.connect('.\sql_db\Demo_table.db')

# create Cursor to execute queries
cur = conn.cursor()

print('Databse created.')

