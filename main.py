#!/usr/bin/env python
# encoding=utf8
import numpy as np
from generate_data import generate_sample
from metrics import compute_metrics

def main():
    granularity = 0.001
    trial_cnt = 10
    fout = open('trial_data.txt', 'w')
    print >> fout, 'DupRatio\tAUC\tBER'
    for dup_ratio in np.arange(0, 1, granularity):
        print '==========DupRatio=%s==========' % dup_ratio
        for _ in range(trial_cnt):
            generate_sample(dup_ratio)
            auc, ber = compute_metrics()
            print >> fout, '%s\t%s\t%s' % (dup_ratio, auc, ber)
    fout.close()
    return

if __name__ == '__main__':
    main()
