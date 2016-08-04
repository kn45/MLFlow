#!/usr/bin/env python

import sys
sys.path.append('../')
try:
    from titanic import *
except:
    raise

data_file = 'data_all'
train_file = 'data_train'
valid_file = 'data_valid'

data = None
with open(data_file) as f:
    data = np.array([l.rstrip('\r\n').split('\t') for l in f.readlines()])

X = data[:, 1:]
y = data[:, 0]
valid_ratio = 0.15
skf = StratifiedKFold(y, round(1./valid_ratio))
train_idx, valid_idx = next(iter(skf))
"""
X_train, y_train = X[train_idx], y[train_idx]
X_valid, y_valid = X[valid_idx], y[valid_idx]
"""
data_train = data[train_idx]
data_valid = data[valid_idx]

with open(train_file, 'w') as fo_train:
    for line in data_train:
        print >> fo_train, '\t'.join(line)
with open(valid_file, 'w') as fo_valid:
    for line in data_valid:
        print >> fo_valid, '\t'.join(line)