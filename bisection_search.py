# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 13:07:52 2016

@author: raoga3
"""
low = 0
high = 100
guess = int((low+high)/2)
print('')
print("Is your secret number ",guess,"?")
char='h'
char = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter c to indicate I guessed correctly : ")
while char!='c':    
    if char == 'h':
        high = guess
        guess = int((low+high)/2)
    elif char == 'l':
        low = guess
        guess = int((low+high)/2)
    print('')    
    print("Is your secret number ",guess,"?")
    char = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter c to indicate I guessed correctly : ")
if char == 'c':
        print("Game over. Your secret number is:"+str(guess))