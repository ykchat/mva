heights <- c(151, 164, 146, 158)
weights <- c(48, 53, 45, 61)

data <- data.frame(heights, weights)

data.cor <- cor(data) # 相関行列
colnames(data.cor) <- c("身長", "体重")
rownames(data.cor) <- colnames(data.cor)
