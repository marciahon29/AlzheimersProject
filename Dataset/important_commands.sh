// RESIZE IMAGE
convert myfigure.png -resize 200x100 myfigure.jpg

// GET IMAGE SIZE
identify -format '%w %h' img.png

// RESIZE WITH RATIO
convert '*.jpg[200x]' resized%03d.jpg

// RESIZE, CENTER, and PADDING (BLACK)
convert 10.jpg -resize 176x208 -gravity center -background "rgb(0,0,0)" -extent 176x208 10_out.jpg


// Loop to convert size of images
for f in ./*.jpg; do
  convert ./"$f" -resize 176x208 -gravity center -background "rgb(0,0,0)" -extent 176x208 ./"${f%.jpg}_YAL.jpg"
done
