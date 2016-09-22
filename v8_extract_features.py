import csv
import cStringIO
import codecs
import json
import itertools
data_file=open('/home/nash/ayushi/Projects_2016/POS_CM_challenge/final_data/WA_HI_EN_FN.txt', 'r').readlines()
emoticons = json.loads(open('/home/nash/ayushi/Projects_2016/POS_CM_challenge/FEATURE_AND_PROGRAM/emoticons_formed_with_symbols.json').read())
print type(emoticons)

result=[]
for x in data_file:
    result.append(x.split('\t')[0])
feats=[]
for y in data_file:
    feats.append(y.split('\t')[1:])



def add_feat(word):
    length=len(word)
    if length <= 4:
       l='LESS'
    else:
        l='MORE'

    if word.startswith('@')== True or word.startswith('#') == True:
       N='001'
    elif word.startswith('http')==True:
         N='010'
    elif word in emoticons:
         N='100'
    else:
         N='000'

    return l, N

def extract_features(dfile):
    feature_mat=[]
    len_feat, NER_feat = '', ''
    for word in dfile:
        
        len_feat, NER_feat = add_feat(word)
        print len_feat, NER_feat 
         
	prefix_list = [word, word[0], word[0:2], word[0:3]]        
        suffix_list  = [word[-1], word[-2:], word[-3:], word[-4:], word[-5:]]
        add_feats = [len_feat, NER_feat]
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

        feature_list = prefix_list + suffix_list + add_feats

        feature_mat.append(feature_list)
    return feature_mat
feat_matrix=extract_features(result)

outfile=open('/home/nash/ayushi/Projects_2016/POS_CM_challenge/final_data/WA_HI_EN_FN_feats.txt', 'wb')
writer = csv.writer(outfile, delimiter='\t')
writer.writerows(feat_matrix)

print "done"

