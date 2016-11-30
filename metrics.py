#!/usr/bin/env python
# encoding=utf8
from sklearn import metrics
import itertools

'''
计算样本数据的AUC和贝叶斯错误率。
'''

SAMPLE_FNAME = 'sample_prob.txt'

def read_data():
    '''
    将样本数据读取为如下格式返回：
    [(feature_id, label, prob), ...]
    '''
    def to_pair(line):
        tokens = line.split('\t')
        feature_id = int(tokens[0])
        label = int(tokens[1])
        prob = float(tokens[2])
        return (feature_id, label, prob)

    with open(SAMPLE_FNAME) as f:
        table = map(to_pair, f)

    return table

def compute_auc(table):
    table_t = zip(*table)
    y = table_t[1]
    y_pred = table_t[2]
    auc = metrics.roc_auc_score(y, y_pred)
    print 'AUC=%s' % auc
    return auc

def compute_bayes_error_rate(table):
    table = read_data()
    err_cnt = 0
    groups = itertools.groupby(table, lambda x: x[0])

    for _, group in groups:
        group = list(group)
        # 一组特征只对应一个样本的话不会有错误发生。
        if len(group) == 1:
            continue
        y_pred = [1 if ele[2] > 0.5 else 0 for ele in group]
        err_cnt += sum(1 if ele[1] != y_hat else 0 for (ele, y_hat) in zip(group, y_pred))

    err_rate = err_cnt * 1.0 / len(table)
    print 'Bayes Error Rate=%s' % err_rate
    return err_rate

def main():
    table = read_data()
    compute_auc(table)
    compute_bayes_error_rate(table)
    return

if __name__ == '__main__':
    main()
