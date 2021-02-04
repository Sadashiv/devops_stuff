#!/bin/bash
#while.sh Show the use of while loop
set -x
answer=y
while [ "$answer" = "y" ]
do
   echo "Enter the code and description" >/dev/tty
   read code description
   echo "$code | $description" >> newlist
   echo "Enter any mode (y/n):\c" >/dev/tty   
   read anymore
   case $anymore in
        y*|Y*) answer=y;;
#        sleep 60
        n*|N*) answer=n;;
            *) answer=y;;
    esac
done
