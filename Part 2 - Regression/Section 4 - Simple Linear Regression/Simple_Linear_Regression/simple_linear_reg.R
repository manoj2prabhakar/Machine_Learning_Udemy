# Data Preprocessing

#importing datasheet
dataset = read.csv('Salary_Data.csv')
# dataset = dataset[, 2:3]

#splitting the data into training and test set
install.packages('caTools')

set.seed(123)
split = sample.split(dataset$Salary, SplitRatio = 2/3)
training_set = subset(dataset, split ==TRUE)
test_set = subset(dataset, split ==FALSE)

# training_set[, 2:3] = scale(training_set[, 2:3])
# test_set[, 2:3] = scale(test_set[, 2:3])

#Fitting Simple linear Regression to training set
regressor = lm(formula = Salary ~ YearsExperience,
               data = training_set)

#predict the test set
y_pred = predict(regressor, newdata = test_set)
# install.packages('ggplot2')

ggplot() + 
  geom_point(aes(x = training_set$YearsExperience , y = training_set$Salary), 
             colour = 'red') + 
  geom_line(aes(x = training_set$YearsExperience , y = predict(regressor, newdata = training_set)),
            colour = 'blue') + 
  ggtitle('Salary vs Experience( Training Set )') +
  xlab(' Years of Experience ') +
  ylab(' Salary ')
  

ggplot() + 
  geom_point(aes(x = test_set$YearsExperience , y = test_set$Salary), 
             colour = 'red') + 
  geom_line(aes(x = training_set$YearsExperience , y = predict(regressor, newdata = training_set)),
            colour = 'blue') + 
  ggtitle('Salary vs Experience( Training Set )') +
  xlab(' Years of Experience ') +
  ylab(' Salary ')


