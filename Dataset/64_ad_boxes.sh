#!/bin/bash

mkdir ad_boxes_64
mkdir ad_boxes_64/box_00
mkdir ad_boxes_64/box_01
mkdir ad_boxes_64/box_02
mkdir ad_boxes_64/box_03
mkdir ad_boxes_64/box_04

cd /home/marcia/Desktop/Alzheimers_2018/ADNI_Data/drive-download-20180120T210120Z-001/Processed_64_per_subject/64_AD_Resized

mv `ls | shuf -n 640` ../ad_boxes_64/box_00
mv `ls | shuf -n 640` ../ad_boxes_64/box_01
mv `ls | shuf -n 640` ../ad_boxes_64/box_02
mv `ls | shuf -n 640` ../ad_boxes_64/box_03
mv `ls | shuf -n 640` ../ad_boxes_64/box_04
