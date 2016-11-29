#!/usr/bin/env python
# encoding=utf8
from sklearn import metrics
'''
计算样本数据的AUC。
'''

SAMPLE_FNAME = 'sample_prob.txt'

def compute_auc():
    def to_pair(line):
        tokens = line.split('\t')
        label = int(tokens[1])
        prob = float(tokens[2])
        return (label, prob)

    with open(SAMPLE_FNAME) as f:
        table = map(to_pair, f)
    table = zip(*table)
    y = table[0]
    y_pred = table[1]
    auc = metrics.roc_auc_score(y, y_pred)
    print 'AUC=%s' % auc
    return auc

def main():
    compute_auc()
    return

if __name__ == '__main__':
    main()
