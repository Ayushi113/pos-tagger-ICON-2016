import csv
import cStringIO
import codecs
import numpy

data_file=numpy.genfromtxt('/home/nash/ayushi/Projects_2016/POS_CM_challenge/CM_POS_tagged_corpus_training_testing/HI_EN/extfeatures_4.txt', delimiter='\t')
#decoded_file=[x.decode('utf-8') for x in data_file]
class UnicodeWriter:
    """
    A CSV writer which will write rows to CSV file "f",
    which is encoded in the given encoding.
    """

    def __init__(self, f, dialect=csv.excel, encoding="utf-8", **kwds):
        # Redirect output to a queue
        self.queue = cStringIO.StringIO()
        self.writer = csv.writer(self.queue, dialect=dialect, **kwds)
        self.stream = f
        self.encoder = codecs.getincrementalencoder(encoding)()

    def writerow(self, row):
        self.writer.writerow([s.encode("utf-8") for s in row])
        # Fetch UTF-8 output from the queue ...
        data = self.queue.getvalue()
        data = data.decode("utf-8")
        # ... and reencode it into the target encoding
        data = self.encoder.encode(data)
        # write to the target stream
        self.stream.write(data)
        # empty queue
        self.queue.truncate(0)

    def writerows(self, rows):
        for row in rows:
            self.writerow(row)   

#decoded_file=numpy.asarray(decoded_file)
print data_file.ndim, d_file.shape
def extract_NER(dfile):
	wordlist=dfile[:,0]
	for word in wordlist:
		if word.startswith('@') == True or word.startswith('#') == True:
			print word

extract_NER(data_file)