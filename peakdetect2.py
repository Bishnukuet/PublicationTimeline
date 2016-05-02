import sys
from numpy import NaN, Inf, arange, isscalar, asarray, array
import matplotlib.pyplot as plt
import numpy
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

def plotFreqGraph(year,frequency):
    #x = [1,3,5,7,9,9,9,9,9]
    #y = [1,2,3,4,5,6,7,8,9]
    x = year
    y = frequency
    plt.plot(x, y)
    plt.show()


def getFreqVsYear():
    f1=[1, 1, 40, 1, 10, 1, 1, 3, 2, 3, 3, 2, 1, 3, 2, 4, 4, 4, 3, 2]
    y1=[1975, 1977, 1981, 1982, 1986, 1988, 1989, 1990, 1992, 1993, 1994, 1995, 1997, 1998, 1999, 2000, 2002, 2003, 2004, 2008]

    f2=[3, 1, 1, 1, 2, 1, 1, 5, 1, 1, 1, 5, 1, 1, 2, 4, 2, 2, 2, 3, 3, 4, 4, 11, 1, 2, 4]
    y2=[1924, 1930, 1937, 1938, 1942, 1959, 1960, 1963, 1967, 1970, 1972, 1982, 1985, 1990, 1992, 1993, 1994, 1996, 1997, 1998, 1999, 2002, 2003, 2004, 2005, 2006, 2007]

    f3=[1, 1, 2, 1, 1, 1, 2, 1, 1, 1, 1, 3, 2, 1, 2, 10, 1, 2, 1, 2, 1, 1, 2, 1, 7, 1, 1, 1, 1]
    y3=[1843, 1904, 1907, 1917, 1935, 1952, 1960, 1965, 1967, 1971, 1979, 1982, 1985, 1986, 1990, 1993, 1994, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2008]

    f4=[2, 4, 1, 5, 6, 10, 5, 2, 7, 4, 1, 1, 4]
    y4=[1930, 1932, 1933, 1935, 1936, 1937, 1938, 1939, 1940, 1941, 1942, 1943, 2007]

    f5=[1, 16, 2, 1, 1, 1, 1, 3, 1, 3, 4, 3, 3, 3, 2, 5, 3, 9, 1, 3, 3, 3, 4, 11, 6, 3, 9, 5, 1, 10]
    y5=[1958, 1959, 1964, 1966, 1967, 1973, 1980, 1981, 1983, 1984, 1985, 1987, 1988, 1989, 1990, 1991, 1993, 1994, 1995, 1996, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007]

    f6=[3,4,7,4,5,4,4,9,8,9,9,5,3,6,4,9,9,8,3,4]
    y6=[1975,1977,1981,1982,1986,1988,1989,1990,1992,1993,1994,1995,1997,1998,1999,2000,2002,2003,2004,2008]

    return f1,y1,f2,y2,f3,y3,f4,y4,f5,y5,f6,y6

def getFreqVsYearNew():
    f1=[1, 1, 40, 1, 4, 1, 1, 3, 2, 3, 3, 8, 7, 6, 3, 2,1, 2, 1, 3]
    y1=[1975, 1977, 1981, 1982, 1986, 1988, 1989, 1990, 1992, 1993, 1994, 1995, 1997, 1998, 1999, 2000, 2002, 2003, 2004, 2008]

    f2=[3, 1, 1, 1, 2, 1, 1, 5, 1, 1, 1, 2, 1, 1, 2, 3, 3, 4, 4, 5, 1, 2, 4, 4, 2, 2, 2 ]
    y2=[1924, 1930, 1937, 1938, 1942, 1959, 1960, 1963, 1967, 1970, 1972, 1982, 1985, 1990, 1992, 1993, 1994, 1996, 1997, 1998, 1999, 2002, 2003, 2004, 2005, 2006, 2007]

    f3=[1, 1, 2, 1, 1, 1, 2, 1, 1, 1, 1, 3, 2, 1, 2, 10, 1, 2, 1, 2, 1, 1, 2, 1, 3, 1, 1, 1, 1]
    y3=[1843, 1904, 1907, 1917, 1935, 1952, 1960, 1965, 1967, 1971, 1979, 1982, 1985, 1986, 1990, 1993, 1994, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2008]

    f4=[2, 4, 1, 5, 6, 10, 5, 2, 7, 4, 1, 1, 4]
    y4=[1930, 1932, 1933, 1935, 1936, 1937, 1938, 1939, 1940, 1941, 1942, 1943, 2007]

    f5=[1, 16, 2, 1, 1, 1, 1, 3, 1, 3, 4, 3, 3, 3, 2, 5, 3, 9, 1, 3, 3, 3, 4, 3, 6, 3, 1, 5, 1, 10]
    y5=[1958, 1959, 1964, 1966, 1967, 1973, 1980, 1981, 1983, 1984, 1985, 1987, 1988, 1989, 1990, 1991, 1993, 1994, 1995, 1996, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007]

    f6=[3,4,7,4,5,2,3,4,3,4,9,5,3,6,4,3,3,1,1,4]
    y6=[1975,1977,1981,1982,1986,1988,1989,1990,1992,1993,1994,1995,1997,1998,1999,2000,2002,2003,2004,2008]

    return f1,y1,f2,y2,f3,y3,f4,y4,f5,y5,f6,y6

def printPlotPeaks(freqList):
    maxtab, mintab = peakdet(freqList,.3)
    print('maxtab:',maxtab)
    print('mintab:',mintab)


def plotFreqGraphAllWords():
    (f1,y1,f2,y2,f3,y3,f4,y4,f5,y5,f6,y6)=getFreqVsYearNew()
    printPlotPeaks(f1)
    printPlotPeaks(f2)
    printPlotPeaks(f3)
    printPlotPeaks(f4)
    printPlotPeaks(f5)
    printPlotPeaks(f6)

    plt.plot(y1,f1, marker='o',)
    plt.plot(y2,f2, marker='o',)
    plt.plot(y3,f3, marker='o',)
    plt.plot(y4,f4, marker='o',)
    plt.plot(y5,f5, marker='o',)
    plt.plot(y6,f6, marker='o',)

#    plt.axis([1843,2010,0, 40])
    plt.axis([1920,2010,0, 41])

    plt.xlabel('Year')
    plt.ylabel('Frequency')
    plt.title('WS Model')
    plt.legend()
    plt.show()

def normalize(freqList):
    raw = freqList
    #print('raw',raw)
    norm = [float(i)/sum(raw) for i in raw]
    #print('norm',norm)
    return norm



def plotFreqGraphAllWords_Normalized():
    (f1,y1,f2,y2,f3,y3,f4,y4,f5,y5,f6,y6)=getFreqVsYearNew()

    f1=normalize(f1)
    f2=normalize(f2)
    f3=normalize(f3)
    f4=normalize(f4)
    f5=normalize(f5)
    f6=normalize(f6)

    plt.plot(y1,f1, marker='o',)
    plt.plot(y2,f2, marker='o',)
    plt.plot(y3,f3, marker='o',)
    plt.plot(y4,f4, marker='o',)
    plt.plot(y5,f5, marker='o',)
    plt.plot(y6,f6, marker='o',)



#    plt.axis([1843,2010,0, 40])
    plt.axis([1920,2010,0, 0.45])

    plt.xlabel('Year')
    plt.ylabel('Frequency')
    plt.title('WS Model')
    plt.legend()
    plt.show()





def plotFreqGraphAllWords_WithProbability():

    (f1,y1,f2,y2,f3,y3,f4,y4,f5,y5,f6,y6)=getFreqVsYearNew()
    f1 = numpy.multiply(7,f1)
    f2 = numpy.multiply(7,f2)
    f3 = numpy.multiply(2,f3)
    f4 = numpy.multiply(2,f4)
    f5 = numpy.multiply(1,f5)
    f6 = numpy.multiply(1,f6)

    printPlotPeaks(f1)

    f1=normalize(f1)
    f2=normalize(f2)
    f3=normalize(f3)
    f4=normalize(f4)
    f5=normalize(f5)
    f6=normalize(f6)

    plt.plot(y1,f1, marker='o',)
    #plt.plot(y2,f2, marker='o',)
    #plt.plot(y3,f3, marker='o',)
    #plt.plot(y4,f4, marker='o',)
    #plt.plot(y5,f5, marker='o',)
    #plt.plot(y6,f6, marker='o',)

#    plt.axis([1843,2010,0, 280])
    plt.axis([1920,2010,0, 0.45])

    plt.xlabel('Year')
    plt.ylabel('Frequency')
    plt.title('WS Model')
    plt.legend()
    plt.show()

def computeWeightedSum(f1,f2):    #not weighted for now
    f1L=len(f1)
    f2L=len(f2)
    leng=0
    f12=[]

    if(f1L<f2L):
        leng=f1L
    else:
        leng=f2L

    for x in range(0, leng):
        f12.append(f1[x]+f1[x])

    #print(f1L,f2L,len(f12))
    return f12


def plotFreqGraphAll_CLusters_WithProbability():   #not finished, bcz we dont have probabilities

    (f1,y1,f2,y2,f3,y3,f4,y4,f5,y5,f6,y6)=getFreqVsYearNew()

    f12=computeWeightedSum(f1,f2)
    f34=computeWeightedSum(f3,f4)
    f56=computeWeightedSum(f5,f6)

    f12 = numpy.multiply(7,f12)
    f34 = numpy.multiply(2,f34)
    f56 = numpy.multiply(1,f56)

    f1=normalize(f12)
    f2=normalize(f34)
    f3=normalize(f56)

    plt.plot(y1,f12, marker='o',)
#    plt.plot(y2,f34, marker='o',)
#    plt.plot(y3,f56, marker='o',)

#    plt.axis([1843,2010,0, 280])
    plt.axis([1920,2010,0, 0.45])

    plt.xlabel('Year')
    plt.ylabel('Frequency')
    plt.title('WS Model')
    plt.legend()
    plt.show()


if __name__=="__main__":

    #plotFreqGraphAllWords_Normalized()
    #plotFreqGraphAllWords()
    plotFreqGraphAllWords_WithProbability()
    #plotFreqGraphAll_CLusters_WithProbability()    ##not finished yet
