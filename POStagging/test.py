#!/usr/bin/env python
#  -*- coding:utf-8 -*-

'Use PKU data to create the word list as reference'
from __future__ import division
__author__ = 'caozhen_2014211182'

def computeTest(testout, testReference, state):
    dict = {0: 'a', 1: 'l', 2: 'h', 3: 'k', 4: 'i', 5: 'p', 6: 'd', 7: 'm', 8: 'w', 9: 's', 10: 'q', 11: 'f', 12: 'n',
            13: 'c', 14: 'v', 15: 'z', 16: 'o', 17: 'b', 18: 'j', 19: 'e', 20: 'y', 21: 't', 22: 'r', 23: 'u'}
    max = 0
    for i in range(len(state)):
        if state[max] < state[i]:
            max = i
    equalnum = 0
    max_equal = 0
    print len(testout), len(testReference)
    for i in range(len(testout)):
        arr = testReference[i].split('/')
        if testout[i] == testReference[i]:
            equalnum += 1
        # else:
        #     print i, testout[i], testReference[i]
        if arr[1] == dict[max]:
            max_equal += 1
    accuracy = equalnum/len(testout)
    accuracy_max = max_equal/len(testout)

    print equalnum,
    print "标注测试集的准确率：", accuracy
    print "若全部测试集词按照出现频率最高的词性标注，准确率：", accuracy_max

    return accuracy, accuracy_max
