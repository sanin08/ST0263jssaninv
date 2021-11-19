from mrjob.job import MRJob

class MRWordFrequencyCount(MRJob):
    def mapper(self,_,line):
        idem, sector, salary, year = line.split(',')
        yield idem, sector

    def reducer(self, idem, values):
        l = list(values)
        yield idem, l

if __name__ == '__main__':
    MRWordFrequencyCount.run()