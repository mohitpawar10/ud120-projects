#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""

import sys
import numpy as np 
from time import time
sys.path.append("../tools/")

from email_preprocess import preprocess
from sklearn import svm


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

clf = svm.SVC(C=10000,kernel = "rbf");

t_train = time()

clf.fit(features_train, labels_train)

print "Training time:", round(time()-t_train, 3), "s"

t_predict = time()

### use the trained classifier to predict labels for the test features
pred = clf.predict(features_test)

print "Prediction for 10 ", pred[10]
print "Prediction for 26 ", pred[26]
print "Prediction for 50 ", pred[50]

print "Chris Email", np.unique(pred, return_counts=True)

print "Prediction time:", round(time()-t_predict, 3), "s"

### calculate and return the accuracy on the test data
### this is slightly different than the example, 
### where we just print the accuracy
### you might need to import an sklearn module
accuracy = clf.score(features_test, labels_test)

print(accuracy)