import os
from string import ascii_lowercase
import pickle



class Term():
    def __init__(self,term,freq):
        self.term=term
        self.freq=freq

class Topic():

    def __init__(self,id,trms,dirichlet):
        self.id=id
        self.dirichlet=dirichlet
        self.keys=trms




class Document():
    def __init__(self,title,top_prob):
        self.title=title
        self.top_prob=top_prob





def readDocuments(fileName):
    documents={}
    with open(fileName) as F:
        for line in F:
            if not line[0]=="#":

                t=line.strip("\n").split()

                id=int(t[0])
                #print id
                name=t[1]
                #print name
                top=t[2:]
                #print name
                #print top
                i=0
                t={}
                while i< len(top):

                    tp=int(top[i])
                    prob=float(top[i+1])
                    #print prob
                    t.__setitem__(tp,prob)
                    #print t
                    i=i+2
                print t
                documents.__setitem__(id,Document(name,t))
                break
    #print documents
    return documents


def readTopics(fileName):
    Topics={}
    with open(fileName) as F:
        for line in F:

            t=line.strip("\n").split()
            id=int(t[0])
            dirichlet=float(t[1])
            terms=t[2:]
            Topics.__setitem__(id,terms)
    return Topics

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

def readTerms():
    terms={}
    for c in ascii_lowercase:
        termObj=read_object("ngram_"+c)
        for term in termObj:
            terms.__setitem__(term,termObj[term])
    return terms

def read_freq_count():
    year_norm = {i:1.0 for i in range(1500,2017)}
    with open('total_counts.txt') as data_file:
        for line in data_file:
            for count in line.split('\t'):
                c = count.split(',')
                year_norm[int(c[0])]=int(c[1])
    return year_norm

#print 'total terms',len(terms)

TERMS_FREQ=readTerms()
TOTAL_FREQ=read_freq_count()
TOPICS_KEYS=readTopics("topickeys.txt")

def combineTerms(terms):

    topicFreq={}

    for i in range(1500,2017):
        sum=0.0
        for term in  terms:
            if not TERMS_FREQ.has_key(term):
                sum=sum+0.0
                continue
            t=TERMS_FREQ[term]
            if t.has_key(i):
                sum=sum+t[i]
            else:
                sum=sum+0
        topicFreq.__setitem__(i,sum/TOTAL_FREQ[i])
    return topicFreq

def addDict(d1,d2):
    comDic={}
    for i in d1:
        comDic.__setitem__(i,d1[i]+d2[i])
    return comDic
def divDict(d1,d2):
    divDic={}
    for i in d1:
        divDic.__setitem__(i,d1[i]/d2[i])
    return divDic
def mulDivScalar(d1,scalar):
    mulDic={}
    for i in d1:
        mulDic.__setitem__(i,d1[i]*scalar)
    return mulDic
def combineTopics(top_prob):

    combo={i:0 for i in range(1500,2017)}
    for top in top_prob:
        #topic=top
        #print top
        prob=top_prob[top]
        terms=TOPICS_KEYS[top]
        topic_freq=combineTerms(terms)
        plt.plot(topic_freq.keys(),topic_freq.values(), marker='.')
        #plt.title("Weighted Time Series for a Document")

        #plt.show()
        combo=addDict(combo,mulDivScalar(topic_freq,prob))
        #break
    plt.xlabel("Year")
    plt.ylabel("Frequency")
    plt.show()
    return combo







import matplotlib.pyplot as plt
if __name__ == '__main__':


    #topics=

    #print freq_year[1505]
    #print " Freq:",freq_year

    #print TOPICS_KEYS[0]
    #print TOTAL_FREQ
    #print TERMS_FREQ

    id=0
    docs=readDocuments("doctopics.txt")
    timeline=combineTopics(docs[id].top_prob)
    #print docs[0].top_prob
    plt.plot(timeline.keys(),timeline.values(), marker='o',color='g')
    plt.xlabel("Year")
    plt.ylabel("Frequency")
    #plt.title("Weighted Time Series for a Document")
    plt.show()
    print timeline
    #terms=readTerms()

