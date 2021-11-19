from mrjob.job import MRJob

class MRWordFrequencyCount(MRJob):
    def mapper(self,_,line):
        idem, sector, salary, year = line.split(',')
        yield idem, int(salary)

    def reducer(self, idem, values):
        l = list(values)
        avg = sum(l)/len(l)
        yield idem, avg

if __name__ == '__main__':
    MRWordFrequencyCount.run()