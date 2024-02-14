#!/bin/bash

pid=$$
width=$(identify -format "%w" /home/erwann/Pictures/earth.png)
height=$(identify -format "%h" /home/erwann/Pictures/earth.png)
segment=200
seg=$(($height/$segment))
nbr_de_chiffre=5

mkdir /tmp/earth${pid}

for ((i=0; $i<$segment; i++)); do
	zero=""
	len=$((${nbr_de_chiffre}-${#i}))
	for ((j=0; $j<$len;j++)); do
		zero=$zero'0'
	done
	magick -extract ${width}x${seg}+0+$(($seg*$i)) infra.png - | magick composite -geometry +0+$(($seg*$i)) - earth.png /tmp/earth${pid}/earthinfra${zero}${i}.png
done
#magick /tmp/earth${pid}/* /tmp/earth${pid}/final.gif
#convert -delay 50 -loop 0 /tmp/earth${pid}/final.gif /tmp/earth${pid}/final.gif
convert -delay 50 -loop 0 /tmp/earth${pid}/* /tmp/earth${pid}/final.gif
swww img /tmp/earth${pid}/final.gif
