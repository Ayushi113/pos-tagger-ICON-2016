import csv
import cStringIO
import codecs
data_file=open('/home/nash/ayushi/Projects_2016/POS_CM_challenge/CM_POS_tagged_corpus_training_testing/HI_EN/devnagri.txt', 'r').readlines()
decoded_file=[x.decode('utf-8') for x in data_file]

def extract_features(dfile):
    feature_mat=[]
    if len(word) >= 5:
       for word in dfile:
	       
	       pref_1=word[0]
	       pref_2=word[0:2]
	       pref_3=word[0:3]
	       suf_1=word[-1]
	       suf_2=word[-2:]
	       suf_3=word[-3:]
	       suf_4=word[-4:]
	       suf_5=word[-5:]
	   if len(word) =< 5 and len(word) > 3:
       for word in dfile:
	       pref_1=word[0]
	       pref_2=word[0:2]
	       pref_3=word[0:3]
	       suf_1=word[-1]
	       suf_2=word[-2:]
	       suf_3=word[-3:]
	       suf_4=word[-4:]
	       suf_5=word[-5:]
	feature_list = [word, pref_1, pref_2, pref_3, suf_1, suf_2, suf_3, suf_4, suf_5]
        feature_mat.append(feature_list)

    return feature_mat
feat_matrix=extract_features(decoded_file)

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

outfile=open('/home/nash/ayushi/Projects_2016/POS_CM_challenge/CM_POS_tagged_corpus_training_testing/HI_EN/extfeatures.txt', 'wb')
writer = UnicodeWriter(outfile)
writer.writerows(feat_matrix)

print "done"

