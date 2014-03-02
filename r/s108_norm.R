height <- c(151, 164, 146, 158)
weight <- c(48, 53, 45, 61)

data <- data.frame(height, weight)

norm <- scale(data)[,] # データの標準化
colnames(norm) <- c("身長", "体重")
