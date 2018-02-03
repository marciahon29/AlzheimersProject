#!/bin/bash

mkdir data_00
mkdir data_00/train
mkdir data_00/train/normal
mkdir data_00/validation
mkdir data_00/validation/normal

mkdir data_01
mkdir data_01/train
mkdir data_01/train/normal
mkdir data_01/validation
mkdir data_01/validation/normal

mkdir data_02
mkdir data_02/train
mkdir data_02/train/normal
mkdir data_02/validation
mkdir data_02/validation/normal

mkdir data_03
mkdir data_03/train
mkdir data_03/train/normal
mkdir data_03/validation
mkdir data_03/validation/normal

mkdir data_04
mkdir data_04/train
mkdir data_04/train/normal
mkdir data_04/validation
mkdir data_04/validation/normal

# Split (1)
cp box_00/* data_00/train/normal
cp box_01/* data_00/train/normal
cp box_02/* data_00/train/normal
cp box_03/* data_00/train/normal
cp box_04/* data_00/validation/normal

cd data_00/train/normal
number=1
for d in * ; do
	mv $d "NAL"`printf %04d $number`".jpg"
	echo $d
	echo $number	
	number=$(($number + 1))
done
cd ../../..

cd data_00/validation/normal
number=1
for d in * ; do
	mv $d "NAL"`printf %04d $number`".jpg"
	echo $d
	echo $number	
	number=$(($number + 1))
done
cd ../../..

# Split (2)
cp box_01/* data_01/train/normal
cp box_02/* data_01/train/normal
cp box_03/* data_01/train/normal
cp box_04/* data_01/train/normal
cp box_00/* data_01/validation/normal

cd data_01/train/normal
number=1
for d in * ; do
	mv $d "NAL"`printf %04d $number`".jpg"
	echo $d
	echo $number	
	number=$(($number + 1))
done
cd ../../..

cd data_01/validation/normal
number=1
for d in * ; do
	mv $d "NAL"`printf %04d $number`".jpg"
	echo $d
	echo $number	
	number=$(($number + 1))
done
cd ../../..

# Split (3)
cp box_02/* data_02/train/normal
cp box_03/* data_02/train/normal
cp box_04/* data_02/train/normal
cp box_00/* data_02/train/normal
cp box_01/* data_02/validation/normal

cd data_02/train/normal
number=1
for d in * ; do
	mv $d "NAL"`printf %04d $number`".jpg"
	echo $d
	echo $number	
	number=$(($number + 1))
done
cd ../../..

cd data_02/validation/normal
number=1
for d in * ; do
	mv $d "NAL"`printf %04d $number`".jpg"
	echo $d
	echo $number	
	number=$(($number + 1))
done
cd ../../..

# Split (4)
cp box_03/* data_03/train/normal
cp box_04/* data_03/train/normal
cp box_00/* data_03/train/normal
cp box_01/* data_03/train/normal
cp box_02/* data_03/validation/normal

cd data_03/train/normal
number=1
for d in * ; do
	mv $d "NAL"`printf %04d $number`".jpg"
	echo $d
	echo $number	
	number=$(($number + 1))
done
cd ../../..

cd data_03/validation/normal
number=1
for d in * ; do
	mv $d "NAL"`printf %04d $number`".jpg"
	echo $d
	echo $number	
	number=$(($number + 1))
done
cd ../../..


# Split (5)
cp box_04/* data_04/train/normal
cp box_00/* data_04/train/normal
cp box_01/* data_04/train/normal
cp box_02/* data_04/train/normal
cp box_03/* data_04/validation/normal

cd data_04/train/normal
number=1
for d in * ; do
	mv $d "NAL"`printf %04d $number`".jpg"
	echo $d
	echo $number	
	number=$(($number + 1))
done
cd ../../..

cd data_04/validation/normal
number=1
for d in * ; do
	mv $d "NAL"`printf %04d $number`".jpg"
	echo $d
	echo $number	
	number=$(($number + 1))
done
cd ../../..
