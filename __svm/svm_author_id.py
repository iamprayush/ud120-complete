#!/usr/bin/python

"""
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:
    Sara has label 0
    Chris has label 1
"""

import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###
from sklearn import svm
from sklearn.metrics import accuracy_score


clf = svm.SVC(kernel='rbf', C = 10000)

features_train = features_train[:int(len(features_train)/1)] 
labels_train = labels_train[:int(len(labels_train)/1)] 

clf.fit(features_train, labels_train)
pred = clf.predict(features_test)
count = 0
for i in pred:
	if i == 1:
		count += 1
accuracy = accuracy_score(clf.predict(features_test), labels_test)
print(accuracy)
print(count)
#########################################################
