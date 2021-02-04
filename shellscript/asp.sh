#!/bin/sh
#The () Statements enclosed within parenthesis are are executed in subshell
#The {} Statements enclosed within curly bases are are executed in current shell
set -x
echo `pwd`
echo `date`
sum=`expr 12 + 23`
echo $sum
#prompt[2]="Enter your name:"
#echo ${prompt[2]}
name="sadashiv hb"
echo $name
echo ${name}
echo ${#name}
filename=advanced.txt
echo ${filename%txt}
prompt1="Employe ID:"
x=1; eval echo \$prompt$x
exec date
exec > exefile
