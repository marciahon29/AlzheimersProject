#!/bin/bash

mkdir data_00
mkdir data_00/train
mkdir data_00/train/mci
mkdir data_00/validation
mkdir data_00/validation/mci

mkdir data_01
mkdir data_01/train
mkdir data_01/train/mci
mkdir data_01/validation
mkdir data_01/validation/mci

mkdir data_02
mkdir data_02/train
mkdir data_02/train/mci
mkdir data_02/validation
mkdir data_02/validation/mci

mkdir data_03
mkdir data_03/train
mkdir data_03/train/mci
mkdir data_03/validation
mkdir data_03/validation/mci

mkdir data_04
mkdir data_04/train
mkdir data_04/train/mci
mkdir data_04/validation
mkdir data_04/validation/mci

# Split (1)
cp box_00/* data_00/train/mci
cp box_01/* data_00/train/mci
cp box_02/* data_00/train/mci
cp box_03/* data_00/train/mci
cp box_04/* data_00/validation/mci

cd data_00/train/mci
number=1
for d in * ; do
	mv $d "MAL"`printf %04d $number`".jpg"
	echo $d
	echo $number	
	number=$(($number + 1))
done
cd ../../..

cd data_00/validation/mci
number=1
for d in * ; do
	mv $d "MAL"`printf %04d $number`".jpg"
	echo $d
	echo $number	
	number=$(($number + 1))
done
cd ../../..

# Split (2)
cp box_01/* data_01/train/mci
cp box_02/* data_01/train/mci
cp box_03/* data_01/train/mci
cp box_04/* data_01/train/mci
cp box_00/* data_01/validation/mci

cd data_01/train/mci
number=1
for d in * ; do
	mv $d "MAL"`printf %04d $number`".jpg"
	echo $d
	echo $number	
	number=$(($number + 1))
done
cd ../../..

cd data_01/validation/mci
number=1
for d in * ; do
	mv $d "MAL"`printf %04d $number`".jpg"
	echo $d
	echo $number	
	number=$(($number + 1))
done
cd ../../..

# Split (3)
cp box_02/* data_02/train/mci
cp box_03/* data_02/train/mci
cp box_04/* data_02/train/mci
cp box_00/* data_02/train/mci
cp box_01/* data_02/validation/mci

cd data_02/train/mci
number=1
for d in * ; do
	mv $d "MAL"`printf %04d $number`".jpg"
	echo $d
	echo $number	
	number=$(($number + 1))
done
cd ../../..

cd data_02/validation/mci
number=1
for d in * ; do
	mv $d "MAL"`printf %04d $number`".jpg"
	echo $d
	echo $number	
	number=$(($number + 1))
done
cd ../../..

# Split (4)
cp box_03/* data_03/train/mci
cp box_04/* data_03/train/mci
cp box_00/* data_03/train/mci
cp box_01/* data_03/train/mci
cp box_02/* data_03/validation/mci

cd data_03/train/mci
number=1
for d in * ; do
	mv $d "MAL"`printf %04d $number`".jpg"
	echo $d
	echo $number	
	number=$(($number + 1))
done
cd ../../..

cd data_03/validation/mci
number=1
for d in * ; do
	mv $d "MAL"`printf %04d $number`".jpg"
	echo $d
	echo $number	
	number=$(($number + 1))
done
cd ../../..


# Split (5)
cp box_04/* data_04/train/mci
cp box_00/* data_04/train/mci
cp box_01/* data_04/train/mci
cp box_02/* data_04/train/mci
cp box_03/* data_04/validation/mci

cd data_04/train/mci
number=1
for d in * ; do
	mv $d "MAL"`printf %04d $number`".jpg"
	echo $d
	echo $number	
	number=$(($number + 1))
done
cd ../../..

cd data_04/validation/mci
number=1
for d in * ; do
	mv $d "MAL"`printf %04d $number`".jpg"
	echo $d
	echo $number	
	number=$(($number + 1))
done
cd ../../..
