#!/usr/bin/env python
#  -*- coding:utf-8 -*-

'Use PKU data to create the word list as reference'
from __future__ import division
__author__ = 'caozhen_2014211182'

import sys
import numpy as np
import pre
import hiddenMM
import test
import matplotlib.pyplot as plt

def main():
    default_encoding = "utf-8"
    if default_encoding != sys.getdefaultencoding():
        reload(sys)
        sys.setdefaultencoding(default_encoding)

    testwords = pre.preTest("wordSeg_test.txt", "testwords.txt")
    testReference = pre.preprocess("wordSeg_test.txt", "testReference.txt")
    HMMobject = []
    state = []
    accuracy = []
    accuracy_max = []
    for i in range(3):
        delta = i*0.000001
        HMMobject.append(hiddenMM.HMM())
        state.append(HMMobject[i].create_lambda(testwords, delta))
        out = np.array([], np.int)
        words = np.array([], np.str)
        for sentence in testwords:
            if len(sentence) == 0:
                continue
            Pro, I = HMMobject[i].viterbi(sentence)
            out = np.concatenate((out, I))
            try:
                words = np.concatenate((words, np.array(sentence)))
            except ValueError:
                print "ValueError", np.array(sentence), words
        testout = pre.output(words, out, "output.txt")
        a, b = test.computeTest(testout, testReference, state[i])
        accuracy.append(a)
        accuracy_max.append(b)

    x = []
    for i in range(3):
        x.append(i * 0.000001)
    plt.figure()
    plt.plot(x, accuracy, 'b', label = 'accuracy')
    plt.plot(x, accuracy_max, 'r', label='accuracy_max')
    plt.legend(loc="upper right")  # 显示图中的标签
    plt.xlabel("delta")
    plt.ylabel('accuracy')
    plt.show()

if __name__ == '__main__':
    main()