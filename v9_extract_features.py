import csv
import cStringIO
import codecs
import json
import itertools
import numpy
data_file=open('/home/nash/ayushi/Projects_2016/POS_CM_challenge/final_data/miscel_interim/featsall/FB_HI_EN_CR_featsall.txt', 'r').readlines()
data_rows, data_final=[], []
for row in data_file:
    row_list=row.split(' ')
    data_rows.append(row_list)

for feat_list in data_rows:
    if len(feat_list) < 2:
        feat_list = feat_list + ['\n'] 
        data_final.append(feat_list)
    elif feat_list[11] == 'en':
         if feat_list[0][0].isupper()==True:
            feat_list = feat_list + ['11']
            data_final.append(feat_list)
         elif feat_list[0][0].isupper()==False:
              feat_list = feat_list + ['10']
              data_final.append(feat_list)
    elif feat_list[11] != 'en':
         feat_list = feat_list + ['00']
         data_final.append(feat_list)


print data_final

outfile=open('/home/nash/ayushi/Projects_2016/POS_CM_challenge/final_data/miscel_interim/featsall/FB_HI_EN_CR_feats_num.txt', 'wb')
writer = csv.writer(outfile, delimiter='\t')
writer.writerows(data_final)



