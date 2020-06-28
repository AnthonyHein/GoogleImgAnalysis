# Set working directory.
setwd("~/GoogleImgAnalysis")

# Read the csv file.
train <- read.csv("googleimganalysis.csv")
View(train)

# Make classifier.
fit.train <- glm(Race ~ Red + Blue + Green, family = binomial, data=train)
fit.train$coefficients

train[, "pred"] <- predict(fit.train, newdata = train, type="response") >= .5

mean(train$Race == train$pred)
mean(train$Race == 0)

# Test
test <- read.csv("test.csv")
View(test)

test[, "pred"] <- predict(fit.train, newdata = test, type="response") >= 0.5
test[, "plogis"] <- predict(fit.train, newdata = test, type="response")

sum(test$pred == 0)

