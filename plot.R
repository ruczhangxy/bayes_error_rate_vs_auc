data = read.table("trial_data.txt", header=TRUE)

jpeg("样本重复率vsAUC.jpg")
plot(data$DupRatio, data$AUC, type="o", col="red", main="样本重复率 vs AUC", xlab="样本重复率", ylab="AUC", family='STXihei')
dev.off()

jpeg("样本重复率vs贝叶斯错误率.jpg")
plot(data$DupRatio, data$BER, type="o", col="red", main="样本重复率 vs 贝叶斯错误率", xlab="样本重复率", ylab="贝叶斯错误率", family='STXihei')
dev.off()

jpeg("AUCvs贝叶斯错误率.jpg")
plot(data$AUC, data$BER, type="o", col="red", main="AUC vs 贝叶斯错误率", xlab="AUC", ylab="贝叶斯错误率", family='STXihei')
dev.off()

jpeg("AUCvs贝叶斯正确率.jpg")
plot(data$AUC, 1 - data$BER, type="o", col="red", main="AUC vs 贝叶斯正确率", xlab="AUC", ylab="贝叶斯正确率", family='STXihei')
abline(a=0, b=1, col="blue")
dev.off()
