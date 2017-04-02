#!/usr/bin/env python
#  -*- coding:utf-8 -*-

'Use PKU data to create the word list as reference'

from __future__ import division
__author__ = 'caozhen_2014211182'

import numpy as np
import pre
import math
class HMM:

    def viterbi(self, sentence):
        self.O = np.zeros(len(sentence), np.int)
        for i in range(len(sentence)):
            self.O[i] = self.mapwk[sentence[i]]
        T = len(self.O)
        I = np.zeros(T, np.float)

        delta = np.zeros((T, self.N), np.float)
        psi = np.zeros((T, self.N), np.float)

        for i in range(self.N):
            try:
                delta[0, i] = self.Pi[i] + self.B[i, self.O[0]]
                psi[0, i] = 0
            except IndexError:
                print "IndexError", T, self.N, i

        for t in range(1, T):
            for i in range(self.N):
                delta[t, i] = self.B[i, self.O[t]] + np.array([delta[t - 1, j] + self.A[j, i] for j in range(self.N)]).max()
                psi[t, i] = np.array([delta[t - 1, j] + self.A[j, i] for j in range(self.N)]).argmax()

        P_T = delta[T - 1, :].max()
        I[T - 1] = delta[T - 1, :].argmax()

        for t in range(T - 2, -1, -1):
            I[t] = psi[t + 1, I[t + 1]]

        return P_T, I

    def create_5_tuple(self, wk):
        words = pre.preprocess("wordSeg_train.txt", "words.txt")
        self.dict = {'o': 0, 'bt': 1, 'it': 2, 'bz': 3, 'iz': 4, 'bs': 5, 'is': 6, 'bl': 7, 'il': 8}
        self.mapwk = {}
        x = 0
        for item in wk:
            self.mapwk[item] = x
            x += 1

        start_state = np.zeros(self.N, np.int)
        transition = np.zeros((self.N, self.N), np.int)
        transition_from = np.zeros(self.N, np.int)
        observation = np.zeros((self.N, self.M), np.int)
        state = np.zeros(self.N, np.int)

        arr = words[0].split('/')
        start_state[self.dict[arr[1]]] += 1
        for i in range(len(words)-1):
            arr1 = words[i].split('/')
            arr2 = words[i+1].split('/')
            try:
                transition[self.dict[arr1[1]], self.dict[arr2[1]]] += 1
                transition_from[self.dict[arr1[1]]] += 1
                state[self.dict[arr1[1]]] += 1
                observation[self.dict[arr1[1]], self.mapwk[arr1[0]]] += 1
                if arr1[0] == '。' or arr1[0] == '？' or arr1[0] == '！':
                    start_state[self.dict[arr2[1]]] += 1
            except IndexError, e:
                print "IndexError:", e
            except KeyError, e:
                print "KeyError:", e
        arr = words[len(words)-1].split('/')
        observation[self.dict[arr[1]], self.mapwk[arr[0]]] += 1
        state[self.dict[arr[1]]] += 1

        print "start_state = ", start_state
        print "transition = "
        print transition
        print "transition_from", transition_from
        print "observation = "
        print observation
        print "state", state
        return start_state, transition, transition_from, observation, state

    def create_lambda(self, testwords):
        wk1 = pre.preTest("wordSeg_train.txt", "wk.txt")

        c = []
        for sentence in wk1:
            c += sentence
        for sentence in testwords:
            c += sentence

        wk2 = []
        wk = list(set(c))
        for item in wk:
            if item == '':
                continue
            else:
                wk2.append(item)
        self.N = 9
        self.M = len(wk)
        print "self.M", self.M

        start_state, transition, transition_from, observation, state = self.create_5_tuple(wk2)

        self.Pi = np.array([float("-inf") for i in range(self.N)])
        self.A = np.array([[float("-inf") for j in range(self.N)] for i in range(self.N)])
        self.B = np.array([[float("-inf") for j in range(self.M)] for i in range(self.N)])
        sum = 0
        for i in range(self.N):
            sum += start_state[i]
        for i in range(self.N):
            try:
                self.Pi[i] = math.log(start_state[i]/ sum, 2)

            except ValueError:
                self.Pi[i] = float("-inf")

        for i in range(self.N):
            for j in range(self.N):
                try:
                    self.A[i, j] = math.log(transition[i, j] / transition_from[i], 2)

                except ValueError:
                    self.A[i, j] = float("-inf")
        for j in range(self.N):
            for k in range(self.M):
                try:
                    self.B[j, k] = math.log(observation[j, k] / state[j], 2)

                except ValueError:
                    self.B[j, k] = float("-inf")
        print "Pi = "
        print self.Pi
        print "A = "
        print self.A
        print "B = "
        print self.B
