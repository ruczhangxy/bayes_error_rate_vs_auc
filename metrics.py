#!/usr/bin/env python
# encoding=utf8
from sklearn import metrics
'''
计算样本数据的AUC。
'''

SAMPLE_FNAME = 'sample_prob.txt'

def read_data():
    def to_pair(line):
        tokens = line.split('\t')
        feature_id = int(tokens[0])
        label = int(tokens[1])
        prob = float(tokens[2])
        return (feature_id, label, prob)

    with open(SAMPLE_FNAME) as f:
        table = map(to_pair, f)

    return table

def compute_auc():
    table = read_data()
    table = zip(*table)
    y = table[1]
    y_pred = table[2]
    auc = metrics.roc_auc_score(y, y_pred)
    print 'AUC=%s' % auc
    return auc

def compute_bayes_error_rate():
    table = read_data()
def main():
    compute_auc()
    return

if __name__ == '__main__':
    main()
