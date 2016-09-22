import csv
import cStringIO
import codecs
data_file=open('/home/nash/ayushi/Projects_2016/POS_CM_challenge/final_data/FB_HI_EN_CR.txt', 'r').readlines()
print data_file[1:5]

result=[]
for x in data_file:
    result.append(x.split('\t')[0])
print result[1:5]
def extract_features(dfile):
    feature_mat=[]

    for word in dfile:
        length=str(len(word))
	prefix_list = [word, word[0], word[0:2], word[0:3]]
#        print prefix_list
        suffix_list  = [word[-1], word[-2:], word[-3:], word[-4:], word[-5:]]
 #       print suffix_list
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
feat_matrix=extract_features(result)

#print feat_matrix

outfile=open('/home/nash/ayushi/Projects_2016/POS_CM_challenge/final_data/FB_HI_EN_CR_feats.txt', 'wb')
writer = csv.writer(outfile)
writer.writerows(feat_matrix)

print "done"

