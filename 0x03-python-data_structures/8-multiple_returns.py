#!/usr/bin/python3

def multiple_returns(sentence):
    if not sentence:
        sentence = None
    if sentence:
        sLen = len(sentence)
    else:
        sLen = 0
    return (sLen, sentence if not sentence else sentence[:1])
