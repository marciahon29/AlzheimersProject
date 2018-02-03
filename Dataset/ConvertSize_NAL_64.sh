#!/bin/bash

resize_dir=$(pwd)"/64_Normal_Resized/"

mkdir -p $resize_dir


for d in */ ; do

	cd $d
	d=${d%?}

	if [ "$d" != "64_Normal_Resized" ] ; then
		echo "$d"

		for f in *.jpg; do
			convert "$f" -resize 176x208 -gravity center -background "rgb(0,0,0)" -extent 176x208 "$resize_dir""$d""_${f%.jpg}_NAL.jpg"
		done
        fi

	cd ..
done
