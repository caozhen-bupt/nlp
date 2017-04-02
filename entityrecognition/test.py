#!/usr/bin/env python
#  -*- coding:utf-8 -*-

'Use PKU data to create the word list as reference'
from __future__ import division
__author__ = 'caozhen_2014211182'

def computeTest(testout, testReference):
    equalnum = 0
    sum_entity = {'sum': 0, 'nt': 0, 'ns': 0, 'nz': 0, 'l': 0}
    sum_recog = {'sum': 0, 'nt': 0, 'ns': 0, 'nz': 0, 'l': 0}
    correct_entity = {'sum': 0, 'nt': 0, 'ns': 0, 'nz': 0, 'l': 0}

    for i in range(len(testout)):
        arr1 = testout[i].split('/')
        arr2 = testReference[i].split('/')
        if testout[i] == testReference[i]:
            equalnum += 1
            if arr1[1] != 'o':
                correct_entity['sum'] += 1
            if arr1[1] == 'bt' or arr1[1] == 'it':
                correct_entity['nt'] += 1
            elif arr1[1] == 'bz' or arr1[1] == 'iz':
                correct_entity['nz'] += 1
            elif arr1[1] == 'bs' or arr1[1] == 'is':
                correct_entity['ns'] += 1
            elif arr1[1] == 'bl' or arr1[1] == 'il':
                correct_entity['l'] += 1

        if arr2[1] != 'o':
            sum_entity['sum'] += 1
        if arr2[1] == 'bt' or arr1[1] == 'it':
            sum_entity['nt'] += 1
        elif arr2[1] == 'bz' or arr1[1] == 'iz':
            sum_entity['nz'] += 1
        elif arr2[1] == 'bs' or arr1[1] == 'is':
            sum_entity['ns'] += 1
        elif arr2[1] == 'bl' or arr1[1] == 'il':
            sum_entity['l'] += 1

        if arr1[1] != 'o':
            sum_recog['sum'] += 1
        if arr1[1] == 'bt' or arr1[1] == 'it':
            sum_recog['nt'] += 1
        elif arr1[1] == 'bz' or arr1[1] == 'iz':
            sum_recog['nz'] += 1
        elif arr1[1] == 'bs' or arr1[1] == 'is':
            sum_recog['ns'] += 1
        elif arr1[1] == 'bl' or arr1[1] == 'il':
            sum_recog['l'] += 1

    accuracy = equalnum/len(testout)
    precision = {}
    recall = {}
    F_measure = {}
    print "总的实体数", sum_entity
    print "总的识别的实体数", sum_recog
    print "正确识别的实体数", correct_entity
    for key in sum_entity:
        try:
            precision[key] = correct_entity[key] / sum_recog[key]
        except ZeroDivisionError:
            precision[key] = -1
        recall[key] = correct_entity[key] / sum_entity[key]
        F_measure[key] = (2 * precision[key] * recall[key]) / (precision[key] + recall[key])
    print equalnum
    print "标注测试集与参考比较的正确率：", accuracy

    print "准确率：\t", precision
    print "召回率：\t", recall
    print "F-测度值：\t", F_measure
