data = read.data("trial_data.txt", header=TRUE)
 plot(data$DupRatio, data$AUC, type="o", col="red", main="样本重复率 vs AUC", xlab="样本重复率", ylab="AUC", family='STXihei')
