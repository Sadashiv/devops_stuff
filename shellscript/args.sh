#!/bin/sh
echo "Program $0 the number of arguments specifiedis $# the arguments are $1,$2"
#$0 takes the program name
#$* stores the all the arguments
#$1,$2, to pass the two arguments
grep "$1" "$2"
grep director emp.lst > /dev/null; echo $? #0 means success
grep mark emp.lst > /dev/null; echo $? #1 means failure
grep 'marketing' emp.lst && echo "Pattern found" #using the logical operator && and ||
#&& and || can be used for the very small decision making we can use for large decision if 
#numeric comparison
#operator,-eg,-ne,-gt,-ge,-lt,lei
#if starts
if grep "^$1" /et/passwd 2>/dev/null # search username at thebegining of line
then
    echo "Pattern found job over" 
else 
    echo "Pattern not found"
fi
#if ends
echo "\n Job over"
