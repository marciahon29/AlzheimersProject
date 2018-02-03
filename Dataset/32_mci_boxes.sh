#!/bin/bash

mkdir mci_boxes
mkdir mci_boxes/box_00
mkdir mci_boxes/box_01
mkdir mci_boxes/box_02
mkdir mci_boxes/box_03
mkdir mci_boxes/box_04

cd /home/marcia/Desktop/Alzheimers_2018/ADNI_Data/drive-download-20180120T210120Z-001/Processed_32_per_subject/32_MCI_Resized

mv `ls | shuf -n 320` ../mci_boxes/box_00
mv `ls | shuf -n 320` ../mci_boxes/box_01
mv `ls | shuf -n 320` ../mci_boxes/box_02
mv `ls | shuf -n 320` ../mci_boxes/box_03
mv `ls | shuf -n 320` ../mci_boxes/box_04
