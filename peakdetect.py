import sys
from numpy import NaN, Inf, arange, isscalar, asarray, array
import matplotlib.pyplot as plt
import numpy
from Term import Term
from Topic import Topic
import json
from collections import OrderedDict
from string import ascii_lowercase
import os
import pickle


def peakdet(v, delta, x = None):
    """
    Converted from MATLAB script at http://billauer.co.il/peakdet.html
    https://gist.github.com/endolith/250860
    Returns two arrays

    function [maxtab, mintab]=peakdet(v, delta, x)
    %PEAKDET Detect peaks in a vector
    %        [MAXTAB, MINTAB] = PEAKDET(V, DELTA) finds the local
    %        maxima and minima ("peaks") in the vector V.
    %        MAXTAB and MINTAB consists of two columns. Column 1
    %        contains indices in V, and column 2 the found values.
    %
    %        With [MAXTAB, MINTAB] = PEAKDET(V, DELTA, X) the indices
    %        in MAXTAB and MINTAB are replaced with the corresponding
    %        X-values.
    %
    %        A point is considered a maximum peak if it has the maximal
    %        value, and was preceded (to the left) by a value lower by
    %        DELTA.

    % Eli Billauer, 3.4.05 (Explicitly not copyrighted).
    % This function is released to the public domain; Any use is allowed.

    """
    maxtab = []
    mintab = []

    if x is None:
        x = arange(len(v))

    v = asarray(v)

    if len(v) != len(x):
        sys.exit('Input vectors v and x must have same length')

    if not isscalar(delta):
        sys.exit('Input argument delta must be a scalar')

    if delta <= 0:
        sys.exit('Input argument delta must be positive')

    mn, mx = Inf, -Inf
    mnpos, mxpos = NaN, NaN

    lookformax = True

    for i in arange(len(v)):
        this = v[i]
        if this > mx:
            mx = this
            mxpos = x[i]
        if this < mn:
            mn = this
            mnpos = x[i]

        if lookformax:
            if this < mx-delta:
                maxtab.append((mxpos, mx))
                mn = this
                mnpos = x[i]
                lookformax = False
        else:
            if this > mn+delta:
                mintab.append((mnpos, mn))
                mx = this
                mxpos = x[i]
                lookformax = True

    return array(maxtab), array(mintab)

def printPlotPeaks(freqList):
    maxtab, mintab = peakdet(freqList,.3)
    print('maxtab:',maxtab)
    print('mintab:',mintab)

def plotFreqGraphAllWords_WithProbability(terms,norm = False, freq_count = {}):



    for term in terms:
        norm_year_freq = term.year_freq
        if norm:
            norm_year_freq=term.normalize_freq(freq_count)
        #print("term:")
        #print(norm_year_freq.values())
        plt.plot(norm_year_freq.keys(),norm_year_freq.values(), marker='.',)

    for term in terms:
        plt.plot(norm_year_freq.keys(),norm_year_freq.values(), marker='.',)
#    plt.axis([1843,2010,0, 280])
    #plt.axis([1500,2010,0, 0.5])

    plt.xlabel('Year')
    plt.ylabel('Frequency')
    #plt.title('Year Vs. Frequency  for Keywords of a Topic')
    #plt.legend()
    plt.show()

def read_object(filename):
    path=os.path.join("ngrams",filename+".pkl")
    with open(path,"rb") as obj:
        return pickle.load(obj)

def process_data():
    terms = []

    for c in ascii_lowercase:
        print("process " +"ngram_"+c)
        obj = read_object("ngram_"+c)

        ngrams=obj.keys()

        for ngram in ngrams:
            t= Term(ngram,obj[ngram])
            terms.append(t)

    return terms

def read_from_file():
    terms = []

    with open('file.txt') as data_file:
        for line in data_file:
            term_dict = json.loads(line,object_pairs_hook=OrderedDict)
            #t= Term(term_dict.get('ngram'),term_dict.get('year_freq'))
            t= Term(term_dict.keys()[0],term_dict.values()[0])
            terms.append(t)
            #pprint(year_freq)
            #print(t.name)
            #print(t.year_freq)
            #print(t.year_freq.get("2000",0))
    return terms

def get_topics(terms):
    topics = []
    with open('topicKeys.txt') as data_file:
        for line in data_file:
            ngrams = []
            for word in line.split(' '):
                ngram = filter(lambda x: x.name == word, terms)
                if len(ngram)>0:
                    ngrams.append(ngram[0])
            topic = Topic(ngrams)
            topics.append(topic)

    return topics

def read_freq_count():
    year_norm = {}
    with open('total_counts.txt') as data_file:
        for line in data_file:
            for count in line.split('\t'):
                c = count.split(',')
                year_norm[int(c[0])]=int(c[1])
    return year_norm


def combine_topic_ngrams(topic, freq_count):
    year_freq = OrderedDict()

    for year in xrange(1500,2017):
        freq = 0
        for ngram in topic.ngrams:
            #freq += ngram.normalize_freq(freq_count).get(year,0)
            freq += ngram.normalized_year_freq.get(year,0)
        year_freq[year]=freq

    new_ngram = Term("",year_freq)
    ngrams = list()
    ngrams.append(new_ngram)
    return Topic(ngrams)

def combine_doc_topics(docId):
    pass

if __name__=="__main__":

    #plotFreqGraphAllWords_Normalized()
    #plotFreqGraphAllWords()

    #terms = read_from_file()
    terms = process_data()
    topics = get_topics(terms)

    freq_count = read_freq_count()
    #print(freq_count)
    topic_id = 0
    while(topic_id>=0):
        #for ngram in topics[topic_id].ngrams:
        #    print(ngram.name)

        plotFreqGraphAllWords_WithProbability(topics[topic_id].ngrams, True, freq_count)
        combined_topic = combine_topic_ngrams(topics[topic_id], freq_count)


        plotFreqGraphAllWords_WithProbability(combined_topic.ngrams)
        #print(combined_topic.ngrams[0].year_freq.values())
        #normalized_year_freq = combined_topic.ngrams[0].normalize_freq(freq_count)
        #printPlotPeaks(combined_topic.ngrams[0].year_freq.values())
        topic_id = int(raw_input("Please enter topic id to draw: "))

    #plotFreqGraphAll_CLusters_WithProbability()    ##not finished yet
