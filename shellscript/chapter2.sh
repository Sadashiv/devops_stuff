#!/bin/bash 
#-xv
#First line is to executing program in which like bash or sh 
#[description for future usage] this script is fallowing chapter examples
#Comment are not allowed in the debug mode
echo "List of users"
echo
w
echo "Colors"
COLOR="red"
value="9"
echo "This is color:$COLOR"

echo "This is color:$value"
echo "To run bash script in the debug mode -->bash -x chapter2.sh"
#Overview of set debugging options
#Short notation  Long notation   Result
#set -f  set -o noglob   Disable file name generation using metacharacters (globbing).
#set -v  set -o verbose  Prints shell input lines as they are read.
#set -x  set -o xtrace   Print command traces before executing command.
