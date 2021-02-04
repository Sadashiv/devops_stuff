#!/bin/sh
if [ ! -e $1 ] ; then
     echo "File doesn't exist"
elif [ ! -r $1 ] ; then
     echo "File not readable"
elif [ ! -w $1 ] ; then
     echo "File not writable" 
else
     echo "File is readable and writeble" 
fi
#-f file exists and is regular file
#-r file exists and is readable
#-w  "                 writable
#-x  "                 executable
#-d  "                 directory
#-s  "		 has greater size
#-L      	 and symbolic link
