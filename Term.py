from collections import OrderedDict

class Term(object):
    def __init__(self,name='', year_freq=None):
        self.name = name
        self.year_freq = year_freq
        self.normalized_year_freq = {}

    def normalize_freq(self, freq_count):
        '''
        year_norm = {}
        y = 1
        freq_total = 20000000
        for i in xrange(1500,2010):
            y *= 1.02
            year_norm[i]=freq_total*y
        '''
        normalized_year_freq = OrderedDict()

        freq_sum = sum(self.year_freq.values())


        sorted_year_freq =  OrderedDict(sorted(self.year_freq.iteritems()))
        for year in sorted_year_freq:
            #norm = float(self.year_freq[year])/freq_sum
            norm = float(self.year_freq[year])/freq_count[year]
            normalized_year_freq[year]=norm

        #return OrderedDict(sorted(normalized_year_freq.iteritems()))
        self.normalized_year_freq = normalized_year_freq
        return normalized_year_freq


    def normalize_freq_unsorted(self, freq_count):
        normalized_year_freq = {}
        freq_sum = sum(self.year_freq.values())


        sorted_year_freq =  OrderedDict(sorted(self.year_freq.iteritems()))
        for year in sorted_year_freq:
            #norm = float(self.year_freq[year])/freq_sum
            norm = float(self.year_freq[year])/freq_count[year]
            normalized_year_freq[year]=norm

        #return OrderedDict(sorted(normalized_year_freq.iteritems()))
        return normalized_year_freq