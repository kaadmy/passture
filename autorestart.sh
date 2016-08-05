#!/bin/sh

while [ 1 ]
do
    echo "\033[34mGenerating BZW...\033[00m"
    ./pybzw_build.py
    echo "\033[34mDone\033[00m\n"

    echo "\033[34mServer started on \033[33m`date`\033[00m"
    bzfs -conf passture.conf -g

    echo "\033[31mServer stopped on \033[33m`date`.\033[00m\n"

    echo "========================================\n"
done