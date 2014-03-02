heights <- c(151, 164, 146, 158)
weights <- c(48, 53, 45, 61)

data <- data.frame(heights, weights)

result <- matrix(0, ncol(data), 3)
colnames(result) <- c("平均", "分散", "標準偏差")
rownames(result) <- c("身長", "体重")

result[,1] <- sapply(data, mean) # 平均
result[,2] <- diag(var(data))    # 分散
result[,3] <- sapply(data, sd)   # 標準偏差
