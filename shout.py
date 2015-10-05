#!/usr/bin/env python
# -*- coding: utf-8 -*-

def shout(phrase):
    if phrase == phrase.upper():
        return "YOU'RE SHOUTING!"
        print phrase
    else:
        return "Can you speak up?"
        
print "Hello!"

phrase = raw_input("Enter yours phrase:\n")

print shout(phrase)
