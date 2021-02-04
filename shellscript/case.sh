#!/bin/sh
echo " ********************* MENU **************\n
1. List of files
2. Process of user
3. Today's date
4. Users of system 
5. Quit to UNIX
   Enter your option:\c"
read choice 
case "$choice" in #keep condition
    1) ls -l ;;
    2) ps -f ;;
    3) date ;;
    4) who ;;
    5) exit ;;
    *) echo "Invalid option"
esac
echo "Do you wish to continue? (y/n):\c"
read answer
case "$answer" in
   y|Y) ;;
   n|N) exit;;
esac
expr 3 + 5 #expr used to perform airthmetic operation on integers and manipulate integers
expr "sada" : '.*' #Find the length of string
