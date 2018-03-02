#!/bin/bash
#Bash script for converting images with expansion jpeg, png, gif, bmp to jpg,
#and renaming this images with current time and id
#You can choose the size of id and from which number it must be counted
#Using ImageMagic utility
#Installing ImageMagic: sudo apt-get install imagemagick

cd
declare PK=1
declare COUNT=8

#Via this loop you can specify the size
#and number from which it must be counted
while getopts 'p:i:c:' opt; do
  case $opt in
    p)
      cd $OPTARG
      ;;
    i)
      PK=$OPTARG
      ;;
    c)
      COUNT=$OPTARG	
      ;;
  esac
done

#Goes through each file in folder rename and convert
#jpeg, png, gif, bmp to jpg
for file in *; do 
  if [ ${file: -4} == ".jpg" ] || [ ${file: -4} == ".png" ] || [ ${file: -5} == ".jpeg" ] || [ ${file: -4} == ".bmp" ] || [ ${file: -4} == ".gif" ]; then
      NUM=`expr $COUNT - ${#PK}`
      ZEROS=""      
      for((j=0; j<$NUM; j++))do
          ZEROS+="0"
      done
      NAME=`date +%S_%M_%H_%d_%m_%Y`"_$ZEROS$PK.jpg";
      convert "$file" "${NAME}";
      rm $file
  fi
  let PK=PK+1    
done
