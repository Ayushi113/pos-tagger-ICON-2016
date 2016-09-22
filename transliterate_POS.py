from litcm import LIT
import csv
import cStringIO
import codecs
lit = LIT(labels=['hin', 'eng'], transliteration=True)
text = "FOOD security bill pass ,. . acchi baat hai .... . Congress ke accoeding desh ke 80 carore logo ke liye tha ye bil ... . .. . .. . .. . .. . .. . .. . .. . . but I've a question ,. . kya yahi hai congress kaa bharat nirmaan , ki 65 years raaz karney ke baad bhi 80 carore log garib hain ... . Kitna lootego desh ko . . .. . .. . . or ek baat or jab desh kii aarthik condition ICU mai ho ,. . tab is situation mai ye bill laakr kya ram ram sath krbana hai desh kaa ..... ."
with open('/home/nash/ayushi/Projects_2016/POS_CM_challenge/CM_POS_tagged_corpus_training_testing/HI_EN/to_transliterate.txt', 'r') as myfile:
    data=myfile.readlines()
    print len(data)

transcribed=[]
for element in data:
    element_tr = lit.identify(element)
    transcribed.append(element_tr)
print len(transcribed)

decoded=[]
for x in transcribed:
	x_dec = x.decode('utf-8')
	decoded.append(x_dec)

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
outfile=open('/home/nash/ayushi/Projects_2016/POS_CM_challenge/CM_POS_tagged_corpus_training_testing/HI_EN/devnagri.txt', 'wb')
writer = UnicodeWriter(outfile)
writer.writerows(decoded)


