#!/usr/bin/python
# -*- coding: utf-8 -*-
import numpy as np
from sklearn import svm

from process_email import process_email
from email_features import email_features
from get_vocabulary_dict import get_vocabulary_dict


def read_file(file_path: str) -> str:
    """Return the content of the text file under the given path.

    :param file_path: path to the file
    :return: file content
    """

    # FIXME: Implement.
    f = open(file_path, 'r')
    f = f.read()
    return f


# %% ==================== Part 1: Email Preprocessing ====================
#  To use an SVM to classify emails into Spam v.s. Non-Spam, you first need
#  to convert each email into a vector of features. In this part, you will
#  implement the preprocessing steps for each email. You should
#  complete the code in process_email.py to produce a word indices vector
#  for a given email.

print('\nPreprocessing sample email (emailSample1.txt)\n')

file_contents = read_file('data/emailSample1.txt')
word_indices = process_email(file_contents)

# Print Stats
print('Word Indices: \n')
print(word_indices)
print('\n\n')

# input('Program paused. Press enter to continue.\n')

# %% ==================== Part 2: Feature Extraction ====================
#  Now, you will convert each email into a vector of features in R^n. 
#  You should complete the code in email_features.py to produce a feature
#  vector for a given email.

print('\nExtracting features from sample email (emailSample1.txt)\n')

# Extract Features
file_contents = read_file('data/emailSample1.txt')
word_indices = process_email(file_contents)
features = email_features(word_indices)

# Print Stats
print('Length of feature vector: {}\n'.format(len(features[0])))
print('Number of non-zero entries: {}\n'.format(sum(sum(features > 0))))

# input('Program paused. Press enter to continue.\n')

# %% =========== Part 3: Train Linear SVM for Spam Classification ========
#  In this section, you will train a linear classifier to determine if an
#  email is Spam or Not-Spam.

# Load the Spam Email dataset
# You will have X, y in your environment

print('\nLoading the training dataset...')
X_train = np.genfromtxt('data/spamTrain_X.csv', delimiter=',')
y_train = np.genfromtxt('data/spamTrain_y.csv', delimiter=',')
print('The training dataset was loaded.')

print('\nTraining Linear SVM (Spam Classification)\n')
print('(this may take 1 to 2 minutes) ...\n')

# FIXME: Create a linear SVC classifier (with C = 0.1).
clf = svm.SVC(kernel='linear', C=0.1, random_state=13, probability=True)

# FIXME: Fit the SVC model using the training data.
clf.fit(X_train, y_train)

# FIXME: Predict the labelling.
y_pred = clf.predict(X_train)

# FIXME: Compute the training accuracy.
acc_train = clf.score(X_train, y_train)
print('Training Accuracy: {:.2f}%\n'.format(acc_train * 100))

# %% =================== Part 4: Test Spam Classification ================
#  After training the classifier, we can evaluate it on a test set.

# FIXME: Load the test dataset ('data/spamTest_X.csv', 'data/spamTest_y.csv').
# You will have Xtest, ytest in your environment
X_test = np.genfromtxt('data/spamTest_X.csv', delimiter=',')
y_test = np.genfromtxt('data/spamTest_y.csv', delimiter=',')

print('\nEvaluating the trained Linear SVM on a test set ...\n')

# FIXME: Predict the labelling.
y_pred = clf.predict(X_test)

# FIXME: Compute the training accuracy.
acc_test = clf.score(X_test, y_test)
print('Test Accuracy: {:.2f}%\n'.format(acc_test * 100))

# input('Program paused. Press enter to continue.\n')


# %% ================= Part 5: Top Predictors of Spam ====================
#  Since the model we are training is a linear SVM, we can inspect the
#  weights learned by the model to understand better how it is determining
#  whether an email is spam or not. The following code finds the words with
#  the highest weights in the classifier. Informally, the classifier
#  'thinks' that these words are the most likely indicators of spam.

# FIXME: Print the list of 15 most prominent features.
# (i.e. words which gives strongest evidence for an email being a spam)
# - Obtain the weights of the SVC model.
# - Obtain the indices that would sort the weights in the descending order.
# - Obtain the vocabulary.

weights = clf.coef_
idx = np.flip(weights.argsort())

vocabulary_dict = get_vocabulary_dict()

print('\nTop predictors of spam: \n')
for i in range(15):
    # FIXME: Replace each `None` with an appropriate expression.
    print(' {word:<20}: {weight:10.6f}'.format(
        word=vocabulary_dict[idx[0, i]+1], weight=weights[0][idx[0, i]]))

print('\n\n')
# input('\nProgram paused. Press enter to continue.\n')

# %% =================== Part 6: Try Your Own Emails =====================
#  Now that you've trained the spam classifier, you can use it on your own
#  emails! In the starter code, we have included spamSample1.txt,
#  spamSample2.txt, emailSample1.txt and emailSample2.txt as examples. 
#  The following code reads in one of these emails and then uses your 
#  learned SVM classifier to determine whether the email is Spam or 
#  Not Spam

# Set the file to be read in (change this to spamSample2.txt,
# emailSample1.txt or emailSample2.txt to see different predictions on
# different emails types). Try your own emails as well!
filename = 'data/spamSample1.txt'

# Read and predict
file_contents = read_file(filename)
word_indices = process_email(file_contents)
x = email_features(word_indices)
# FIXME: Predict the labelling.
y_pred = clf.predict(x)

print('\nProcessed {}\n\nSpam Classification: {}\n'.format(filename, y_pred[0] > 0))
print('(1 indicates spam, 0 indicates not spam)\n\n')
