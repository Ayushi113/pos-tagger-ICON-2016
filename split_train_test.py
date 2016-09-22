import sklearn
from sklearn.cross_validation import train_test_split
import argparse
import os
import codecs

def BrijImissyou(folder_path):
    trn, tst = 'train', 'test'
    for root, dirs, files in os.walk(folder_path):
    	for fl in files:
            file_read = open(os.path.join(root, fl), 'r').readlines()
            train, test = train_test_split(file_read, train_size = 0.8)
            file_train = open(os.path.join(root, fl+trn), 'wb')
            file_train.writelines(train)
            file_train.close()
            file_test = open(os.path.join(root, fl+tst), 'wb')
            file_test.writelines(test)
            file_test.close()
    return 0


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', help="Add the input path from where tokens and its features will be extracted")
#    parser.add_argument('--output', help="Add the input path from where tokens and its features will be extracted")
    args = parser.parse_args()
    BrijImissyou(args.input)
    
