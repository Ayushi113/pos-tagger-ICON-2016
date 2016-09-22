import csv
import cStringIO
import codecs
data_file=open('/home/nash/ayushi/Projects_2016/POS_CM_challenge/CM_POS_tagged_corpus_training_testing/HI_EN/devnagri.txt', 'r').readlines()
decoded_file=[x.decode('utf-8') for x in data_file]
#print decoded_file

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
            
def extract_features(dfile):
    feature_mat=[]

    for word in dfile:
        length=str(len(word))
	prefix_list = [word[:-2], word[0], word[0:2], word[0:3]]
        suffix_list  = [word[-3:-2], word[-4:-2], word[-5:-2], word[-6:-2], word[-7:-2]]
        #print prefix_list, suffix_list     
        for i in range(len(prefix_list)-1):
            #for i in range(10):
            if prefix_list[i+1] == prefix_list[i]:
               count_p = len(prefix_list) - (i+1)
               prefix_list[(i+1):len(prefix_list)] = ["NULL" for x in range(count_p)]
        for i in range(len(suffix_list)-1):   
            if suffix_list[i+1] == suffix_list[i]:
               count_s = len(suffix_list) - (i+1)
               suffix_list[(i+1):len(suffix_list)] = ["NULL" for x in range(count_s)]

        feature_list = prefix_list + suffix_list + [length]

        feature_mat.append(feature_list)
    return feature_mat
feat_matrix=extract_features(decoded_file)

outfile=open('/home/nash/ayushi/Projects_2016/POS_CM_challenge/CM_POS_tagged_corpus_training_testing/HI_EN/extfeatures_7.txt', 'wb')
writer = UnicodeWriter(outfile)
writer.writerows(feat_matrix)

print "done"

