#!/usr/bin/env python
#  -*- coding:utf-8 -*-

'Use PKU data to create the word list as reference'

from __future__ import division
__author__ = 'caozhen_2014211182'

import sys
import hidMM
import pre
import numpy as np
import test

def main():
    default_encoding = "utf-8"
    if default_encoding != sys.getdefaultencoding():
        reload(sys)
        sys.setdefaultencoding(default_encoding)

    testwords = pre.preTest("wordSeg_test.txt", "testwords.txt")
    testReference = pre.preprocess("wordSeg_test.txt", "testReference.txt")
    HMMobject = hidMM.HMM()
    HMMobject.create_lambda(testwords)
    out = np.array([], np.int)
    words = np.array([], np.str)
    for sentence in testwords:
        if len(sentence) == 0:
            continue
        Pro, I = HMMobject.viterbi(sentence)
        out = np.concatenate((out, I))
        words = np.concatenate((words, np.array(sentence)))
    print "words", len(words)
    testout = pre.output(words, out, "output.txt")
    test.computeTest(testout, testReference)

if __name__ == '__main__':
    main()
