#!/bin/bash
ARR1=(`du -sh /* 2> /dev/null | sort -hr | head | awk '{print $NF}'`) #Getting list of dirs under / 

#Getting list of dirs that are under / filesystem only
for i in ${ARR1[@]};
 {
   if [ `df -h  $i| grep -v Filesystem | awk '{print $NF}'|wc -m` -eq 2 ]
     then
       ARR2+=($i)
   fi
 }
 
echo "Directories under / filesystem are:"
 
for i in ${ARR2[@]}; { echo $i ; } 
 
echo 

k=`for i in ${ARR2[@]}; { du -s  $i ; } | sort -k1 -nr  | head -1 | awk '{print $NF}'`

echo "Directory with highest usage is: $k"


function fsv() { 
a=$1; b=`du -s $a/* | sort -hr | head -1 | awk '{print $NF}'`;
echo $b;
}

p=`fsv $k`
q=`fsv $p`
r=`fsv $q`

echo "Subdirectory with highest usage is: $r"