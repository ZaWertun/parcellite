#!/usr/bin/env bash
for i in 16 20 22 24 32 36 40 48 64 72 96 128 192 256; do
    size=${i}x${i}
    echo $size
    mkdir -v $size 2>/dev/null
    if [ $i -lt 22 ]; then
        antialias="+antialias"
    fi
    convert $antialias -density 1200 -resize $size -background none \
        parcellite.svg $size/parcellite.png
done

optipng -o 7 */parcellite.png
