#!/bin/bash
# ./stats
# Author: Xinyi Zhu



if [ ! -f $1 ]
    then
		echo -e "Error cannot find file $1"
		exit 1
fi

# Count the number of lines
file_name=$1
num_lines=$(wc -l < "$file_name")
if (( $num_lines < 10000 ))  #一会记得改
    then
        echo "The input file is smaller than 10000 lines!"
        exit 1
else
    echo $num_lines
fi

# Print the first line
echo $(head -n 1 $file_name)

# The number of lines in the last 10,000 rows of the file 
# that contain the string “potus” (case-insensitive).
echo $(tail -10000 sample.csv | grep 'potus' | wc -l)

# The number of lines in rows 100-200 (inclusive)
# that contain the word "fake"
echo $(sed -n '100,200p;201p' $file_name | grep 'fake' | wc -l)