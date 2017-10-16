
"""
Note: In order to run this file, you must first install 'pyparsing',
a 3rd party library.

The simplest way to install pyparsing is by using 'pip' from the
command line/terminal. (Pip is installed alongside Python):

    $ pip install pyparsing

Alternatively, You can find instructions on directly downloading and
installing pyparsing here:

    http://pyparsing.wikispaces.com/Download+and+Installation

The lab computers and attu have pyparsing pre-installed for Python 2.

You do not (and should not) need to understand how pyparsing works in
order to complete this assignment.

You may complete this assignment using either Python 2 or Python 3.
"""
import pronouncing
import nltk
from nltk import sent_tokenize, word_tokenize, pos_tag
from nltk.corpus import gutenberg
from collections import defaultdict
from random import *
import re

syllables = 0

def main():
    list = pronouncing.rhymes("christine")
    emma = gutenberg.words('austen-emma.txt')
    emma2 = nltk.pos_tag(emma)
    dic = map(emma2)
    pattern = ['PRP', 'VBD', 'WP', 'UH', 'NN']
    print(len(pattern))
    phrase = ""
    global syllables
    count = 0
    while syllables != 10:
    	print(pattern[count])
    	word = newWord(pattern[count], dic)
    	if word == '-1':
    		syllables = 0
    		phrase = ""
    		count = 0
    	else:
    		phrase += word
    		phrase += " "
    		count += 1
    		if count == len(pattern):
    			count = 0
    		print(count)
    print(phrase)
    # list2 = []
    # for l in list:
    # 	list2.append(word_tokenize(l))
    # for i in list2:
    #     print(nltk.pos_tag(i))

def newWord(grammar, dic):	
	global syllables
	go = 1
	while go:
		word = dic[grammar][randrange(0, (len(dic[grammar]) - 1))]
		p = pronouncing.phones_for_word(word)
		if len(p) > 0:
			go = 0
	s = pronouncing.syllable_count(p[0])
	syllables += s
	if syllables > 10:
		return '-1'
	return word

def map(values):
	d1 = defaultdict(list)
	for v in values:
		d1[v[1]].append(v[0])
	return d1

if __name__ == "__main__":
    main()

