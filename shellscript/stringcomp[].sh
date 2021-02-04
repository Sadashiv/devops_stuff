#!/bin/sh
#[] by uisng these operators we can compare the string
if [ $# -eq 0 ] ; then
    echo "Enter the string to be searched:\c"
    read pname
    if [ -z "$pname"] ; then  # -z checks for null string
       echo "You have entere not the string" ; exit 1
    fi
    echo "Enter the  file name to be used:\c"
    read fname
    if [ ! -n "$fname" ] ; then #-n is same as -z
       echo "you have not entered the file name" ; exit 2
    fi
    test.sh "$pname" "$fname" 
else
    test.sh $*
#    test.sh $@
fi 
