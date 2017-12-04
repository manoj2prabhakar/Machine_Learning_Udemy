# Data Preprocessing Template

# Importing the dataset
dataset = read.csv('50_Startups.csv')

# Splitting the dataset into the Training set and Test set
# install.packages('caTools')
# library(caTools)

#Encoding categorical Data
dataset$State = factor(dataset$State,
                 levels = c('New York', 'California', 'Florida'),
                 labels = c(1,2,3))

set.seed(123)
split = sample.split(dataset$Profit, SplitRatio = 0.8)
training_set = subset(dataset, split == TRUE)
test_set = subset(dataset, split == FALSE) 

# Feature Scaling
# training_set = scale(training_set)
# test_set = scale(test_set)

#Fitting the Multi linear regression to training set
# regressor = lm(formula = Profit ~ R.D.Spend + Administration + Marketing.Spend + State)
regressor = lm(formula = Profit ~ .,
               data = training_set)

#Predicting the Test set result
y_pred = predict(regressor, newdata = test_set)
 




