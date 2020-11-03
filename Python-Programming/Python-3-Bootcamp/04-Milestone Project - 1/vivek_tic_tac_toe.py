# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 09:09:15 2020

@author: vivek
"""

# milestone project 1 - tic-tac-toe game

import random
import math

b=[['*|','1','2','3'],
   ['1|',' ',' ',' '],
   ['2|',' ',' ',' '],
   ['3|',' ',' ',' ']]

def ttt_out(ll):
    print('\n\n---------------------')
    print(ll[0])
    print('---------------------')
    print(ll[1])
    print(ll[2])
    print(ll[3])
    print('---------------------')
    return

def ttt_start():
    print('-----  lets play tic-tack-toe (vs the computer)  -----')
    un=input('\nplease enter your name:')
    print(f'\nwelcome {un}')
    print('\nnow we will randomly decide if you or the computer goes first')

    s=random.random()
    if s>.5:
        print('\ncomputer won the toss and goes first..',
              '\ncomputer will play with 0.. you will play with X..')
        m=0 # flag to show cthat its computers move next
    else:
        print('\nyou won the toss and go first..',
              '\nyou will play with X.. computer will play with 0..')
        m=1
    return m # flag to show that its users move next

def ttt_comp_move(s):
    i=0
    j=0
    while b[i][j]!=' ':
        i=math.ceil(random.random()*3)
        j=math.ceil(random.random()*3)
    b[i][j]=s

def ttt_user_move(s):
    i=0
    j=0
    while b[i][j]!=' ':
        i=int(input('\nenter the row (1,2, or 3):'))
        while i not in [1,2,3]:
            print('\nout of range.. try again..')
            i=int(input('\nenter the row (1,2, or 3):'))
        j=int(input('\nenter the column (1,2, or 3):'))
        while j not in [1,2,3]:
            print('\nout of range.. try again..')
            j=int(input('\nenter the column (1,2, or 3):'))
        if b[i][j]!=' ':
            print('\nplace already occupied.. try again..')
            continue
    b[i][j]=s  

def ttf_win_chk(p):
    w=False
    b2=[b[i][1:4] for i in range(1,4)] # extract just the tic-tac-toe board and exclude indexes
    for i in range(1,3):
        if b2[i][0:3]==[p,p,p]:
            w=True
        if list(list(zip(*b2))[i][0:3])==[p,p,p]: #we transpose the list b using list(zip(*b))
            w=True    
        if [b2[i][i] for i in range(3)] == [p,p,p]: # upper diagonal
            w=True
        if [b2[3-1-i][i] for i in range(3-1,-1,-1)] == [p,p,p]:   # lower diagonal
            w=True        
    return w

def ttt_game():
    m=ttt_start()
    w=False
    ttt_out(b)
    while w==False:
        if m==0:
            s='0'
            ttt_comp_move(s)
            ttt_out(b)
            w=ttf_win_chk('0')
            m=1 # change move to user
        else:
            s='X'
            ttt_user_move(s)
            ttt_out(b)
            w=ttf_win_chk('X')
            m=0 # change move to computer
    if s=='0':
        print('\n\nCOMPUER WON!!')
    else:
        print('\n\nYOU WON!!')
    exit
    
