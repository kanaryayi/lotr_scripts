#!/bin/bash

# array of Python3 scripts to choose from
path=/home/yigit/.lotr_scripts
scripts=($path/lotr_quotes.py $path/random_lotr_quote_2.py $path/random_lotr_quote.py)

# choose a random script index
index=$((RANDOM % ${#scripts[@]}))

# run the randomly chosen script with Python3
python3 ${scripts[$index]}

