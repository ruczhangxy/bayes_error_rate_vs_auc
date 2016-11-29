#!/usr/bin/env python
# encoding=utf8

'''
生成实验所需要的样本数据。
'''
import random
import itertools

NUM_SAMPLE = 10000
DUP_RATIO = 0.7
SAMPLE_FNAME = 'sample.txt'

'''
生成特征和样本标签。
'''
def generate_sample(num_sample, dup_ratio):
    feature_id = 0
    with open(SAMPLE_FNAME, 'w') as f:
        for i in range(num_sample):
            if random.random() > dup_ratio:
                feature_id += 1
            label = random.randint(0, 1)
            print >> f, '%s\t%s' % (feature_id, label)
    return

'''
根据样本的标签计算真实点击率。
'''
def compute_prob():
    def to_pair(line):
        return tuple(map(int, line.strip().split('\t')))

    with open(SAMPLE_FNAME, 'r') as f:
        table = map(to_pair, f)

    fout = open('sample_prob.txt', 'w')
    groups = itertools.groupby(table, lambda x: x[0])
    for feature_id, samples_iter in groups:
        samples = list(samples_iter)
        prob = sum(token[1] for token in samples) * 1.0 / len(samples)
        for k, v in samples:
            print >> fout, '%s\t%s\t%s' % (k, v, prob)
    fout.close()

    return

def main():
    generate_sample(NUM_SAMPLE, DUP_RATIO)
    compute_prob()

if __name__ == '__main__':
    main()
