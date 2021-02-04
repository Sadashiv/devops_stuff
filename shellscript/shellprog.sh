#!/bin/sh
echo `pwd` #Print the current working directory
echo `date`
cal
echo `cal`
echo "Enter the name:\c" #\c no new line
read name #read is used to take input from the user
echo "Enter the file name:\c" #\n new line
read fname
echo "Search for the name from fname"
grep "$name" $fname
echo "Selected records show above"


