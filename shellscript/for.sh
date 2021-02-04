#!/bin/sh
#for.sh--
set -x
for file in emp.lst dep.lst;
do
     cp $file ${file}.bak
     echo "$file copied to ${file}.bak"
done
set 123 456 789
echo "\$1 is $1, \$2 is $2, \$3 is $3"
echo "The $# arguments are $*"
#trap command used to interrupting a program
#debugging set -x[on] set +x[off]
set +x
#$0 is program name $1,$2 etc are positional parameters
#$# store the number of argumnets Both $# and $@ contain all arguments but use of $@ is prefered
