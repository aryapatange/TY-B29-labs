#ARYA PATANGE B-29
#Assignment No. 05
packages <- c("mlbench", "caret", "randomForest", "DALEX", "ggplot2")
install.packages(setdiff(packages, rownames(installed.packages())), dependencies = TRUE)

library(mlbench)
library(caret)
library(randomForest)
library(DALEX)
library(ggplot2)

#Load the Pima Indians Diabetes Dataset
data(PimaIndiansDiabetes)
df <- na.omit(PimaIndiansDiabetes)
cat("Dataset loaded successfully!\n")
head(df)

#Split Data into Training and Testing Sets
set.seed(123)
index <- createDataPartition(df$diabetes, p = 0.8, list = FALSE)
train <- df[index, ]
test  <- df[-index, ]
cat("Training and test sets created.\n")

#Train the Random Forest Model
model_rf <- randomForest(diabetes ~ ., data = train, ntree = 100, importance = TRUE)
print(model_rf)

#Evaluate Model Performance
pred <- predict(model_rf, test)
conf_mat <- confusionMatrix(pred, test$diabetes)
cat("\nConfusion Matrix:\n")
print(conf_mat)

#Feature Importance
cat("\nFeature Importance (Random Forest):\n")
print(importance(model_rf))

# Plot feature importance
varImpPlot(model_rf, main = "Feature Importance in Diabetes Prediction")

#Explain the Model using DALEX
explainer_rf <- explain(model_rf, 
                        data = test[, -9], 
                        y = test$diabetes, 
                        label = "Random Forest")

vip <- model_parts(explainer_rf)
plot(vip)

#Bias and Fairness Check
cat("\nClass distribution in dataset:\n")
print(table(df$diabetes))

#Save Model and Session Info
saveRDS(model_rf, "diabetes_rf_model.rds")
cat("\nModel saved as diabetes_rf_model.rds\n")

cat("\nSession Information:\n")
print(sessionInfo())
