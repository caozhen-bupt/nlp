#!/usr/bin/env python
#  -*- coding:utf-8 -*-

'Use PKU data to create the word list as reference'

__author__ = 'caozhen_2014211182'
import re
def preprocess(in_file, out_file):
    words = []
    a = re.compile(r" *")
    f = open(in_file, 'r').read().strip()
    raw_word = a.split(f)
    i = 0
    while i < len(raw_word):
        if re.compile(r"\d+\-\d+\S+").search(raw_word[i]):
            i += 1
            continue

        if re.compile(r"{.*}|{\n.*}").search(raw_word[i]):
            raw_word[i] = re.compile(r"{.*}|{\n.*}").sub('', raw_word[i])

        if re.compile(r"\[").search(raw_word[i]):
            raw_word[i] = re.compile(r"\[").sub('', raw_word[i])
            if re.compile(r"\]").search(raw_word[i]):
                if re.compile(r"\]nt").search(raw_word[i]):
                    raw_word[i] = re.compile(r"/.*").sub('/bt', raw_word[i])
                elif re.compile(r"\]nz").search(raw_word[i]):
                    raw_word[i] = re.compile(r"/.*").sub('/bz', raw_word[i])
                elif re.compile(r"\]ns").search(raw_word[i]):
                    raw_word[i] = re.compile(r"/.*").sub('/bs', raw_word[i])
                elif re.compile(r"\]i|\]l").search(raw_word[i]):
                    raw_word[i] = re.compile(r"/.*").sub('/bl', raw_word[i])
                else:
                    print "other",raw_word[i]

                words.append(raw_word[i])
                i += 1
            else:
                temp = i
                while not re.compile(r"\]").search(raw_word[i]):
                    i += 1
                if re.compile(r"\]nt").search(raw_word[i]):
                    raw_word[temp] = re.compile(r"/.*").sub('/bt', raw_word[temp])
                    words.append(raw_word[temp])
                    temp += 1
                    while not re.compile(r"\]").search(raw_word[temp]):
                        raw_word[temp] = re.compile(r"/.*").sub('/it', raw_word[temp])
                        words.append(raw_word[temp])
                        temp += 1
                    raw_word[temp] = re.compile(r"/.*").sub('/it', raw_word[temp])
                    words.append(raw_word[temp])
                    i += 1
                elif re.compile(r"\]nz").search(raw_word[i]):
                    raw_word[temp] = re.compile(r"/.*").sub('/bz', raw_word[temp])
                    words.append(raw_word[temp])
                    temp += 1
                    while not re.compile(r"\]").search(raw_word[temp]):
                        raw_word[temp] = re.compile(r"/.*").sub('/iz', raw_word[temp])
                        words.append(raw_word[temp])
                        temp += 1
                    raw_word[temp] = re.compile(r"/.*").sub('/iz', raw_word[temp])
                    words.append(raw_word[temp])
                    i += 1
                elif re.compile(r"\]ns").search(raw_word[i]):
                    raw_word[temp] = re.compile(r"/.*").sub('/bs', raw_word[temp])
                    words.append(raw_word[temp])
                    temp += 1
                    while not re.compile(r"\]").search(raw_word[temp]):
                        raw_word[temp] = re.compile(r"/.*").sub('/is', raw_word[temp])
                        words.append(raw_word[temp])
                        temp += 1
                    raw_word[temp] = re.compile(r"/.*").sub('/is', raw_word[temp])
                    words.append(raw_word[temp])
                    i += 1
                elif re.compile(r"\]i|\]l").search(raw_word[i]):
                    raw_word[temp] = re.compile(r"/.*").sub('/bl', raw_word[temp])
                    words.append(raw_word[temp])
                    temp += 1
                    while not re.compile(r"\]").search(raw_word[temp]):
                        raw_word[temp] = re.compile(r"/.*").sub('/il', raw_word[temp])
                        words.append(raw_word[temp])
                        temp += 1
                    raw_word[temp] = re.compile(r"/.*").sub('/il', raw_word[temp])
                    words.append(raw_word[temp])
                    i += 1
                else:
                    print "other", raw_word[i]
                    i += 1
        else:
            raw_word[i] = re.compile(r"/.*").sub('/o', raw_word[i])
            words.append(raw_word[i])
            i += 1
    fl = open(str(out_file), 'w')
    fl.writelines(item + '\n' for item in words)
    fl.close()
    return words

def preTest(in_file, out_file):
    words = []
    sentence = []
    raw_word = open(in_file, 'r').read().strip().split()
    for item in raw_word:
        if re.compile(r"\d+\-\d+\S+").search(item):
            words.append(sentence)
            sentence = []
            continue
        elif re.compile(r"\]|\[|\{.*\}|/").search(item):
            item = re.compile(r"\]|\[|\{.*\}|/.*").sub('', item)
            sentence.append(item)
    words.append(sentence)

    fl = open(str(out_file), 'w')
    for sentence in words:
        for item in sentence:
            fl.writelines(item + '\n')

    fl.close()
    return words

def output(testwords, Q, out_file):
    out = []
    I = []
    dict = {0: 'o', 1: 'bt', 2: 'it', 3: 'bz', 4: 'iz', 5: 'bs', 6: 'is', 7: 'bl', 8: 'il'}
    for i in range(len(Q)):
        I.append(dict[Q[i]])
    for i in range(len(testwords)):
        out.append(testwords[i] + '/' + I[i])
    fl = open(str(out_file), 'w')
    fl.writelines(item + '\n' for item in out)
    fl.close()
    return out

