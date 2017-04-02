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
    flag = 1
    for item in raw_word:
        if re.compile(r"\d+\-\d+\S+").search(item):
            continue
        if re.compile(r"\]|\[|\{.*\}|\{\n.*\}").search(item):
            item = re.compile(r"\]|\[|\{.*\}|\{\n.*\}").sub('', item)

        if re.compile(r"/w").search(item):
            item = re.compile(r"/w.*").sub('/w', item)
        elif re.compile(r"/ad|/d|/D").search(item):
            item = re.compile(r"/ad|/d.*|/D.*").sub('/d', item)
        elif re.compile(r"/n|/N").search(item):
            item = re.compile(r"/n.*|/N.*").sub('/n', item)
        elif re.compile(r"/a|/A|/Bg").search(item):
            item = re.compile(r"/a.*|/A.*|/Bg").sub('/a', item)
        elif re.compile(r"/m|/M").search(item):
            item = re.compile(r"/m.*|/M.*").sub('/m', item)
        elif re.compile(r"/u|/U").search(item):
            item = re.compile(r"/u.*|/U.*").sub('/u', item)
        elif re.compile(r"/r|/R").search(item):
            item = re.compile(r"/r.*|/R.*").sub('/r', item)
        elif re.compile(r"/T|/t").search(item):
            item = re.compile(r"/T.*|/t.*").sub('/t', item)
        elif re.compile(r"/j").search(item):
            item = re.compile(r"/j.*").sub('/j', item)
        elif re.compile(r"/v|/V").search(item):
            item = re.compile(r"/v.*|/V.*").sub('/v', item)
        elif re.compile(r"/q|/Q").search(item):
            item = re.compile(r"/q.*|/Q.*").sub('/q', item)
        elif re.compile(r"/i").search(item):
            item = re.compile(r"/i.*").sub('/i', item)
        elif re.compile(r"/l").search(item):
            item = re.compile(r"/l.*").sub('/l', item)
        elif re.compile(r"/h|/k|/p|/s|/f|/c|/z|/o|/b|/e|/y").search(item):
            pass
        else:
            flag = 0
            print "others", item

        if flag == 1:
            words.append(item)
        else:
            flag = 1

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
            if item == '。' or item == '？' or item == '！':
                sentence.append(item)
                words.append(sentence)
                sentence = []
            elif len(sentence) > 8:
                if item == '，':
                    sentence.append(item)
                    words.append(sentence)
                    sentence = []
                else:
                    sentence.append(item)
            else:
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
    dict = {0: 'a', 1: 'l', 2: 'h', 3: 'k', 4: 'i', 5: 'p', 6: 'd', 7: 'm', 8: 'w', 9: 's', 10: 'q', 11: 'f', 12: 'n',
            13: 'c', 14: 'v', 15: 'z', 16: 'o', 17: 'b', 18: 'j', 19: 'e', 20: 'y', 21: 't', 22: 'r', 23: 'u'}
    for i in range(len(Q)):
        I.append(dict[Q[i]])
    for i in range(len(testwords)):
        out.append(testwords[i] + '/' + I[i])
    fl = open(str(out_file), 'w')
    fl.writelines(item + '\n' for item in out)
    fl.close()
    return out

if __name__ == '__main__':
    preprocess("wordSeg_train.txt", "words.txt")
    preTest("wordSeg_test.txt", "testwords.txt")
