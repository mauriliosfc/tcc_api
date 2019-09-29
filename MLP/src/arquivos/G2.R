#https://archive.ics.uci.edu/ml/datasets/SPECTF+Heart
rm(list=ls(all=TRUE))
data<-read.table("G2 - Base_Simulacao.txt")
#data<-read.table("new.data")
library(kernlab)
library(RSNNS)
library(devtools)
library(nnet)
library(neuralnet)
library(BioMark)

heart <- data[sample(1:nrow(data), length(1:nrow(data))), 1:ncol(data)]
heartValues <- heart[,1:22]
heartTargets <- heart[, 25]
#23- Infeccao_Global  
#24-Infeccao_Sitio_Cirurgico	
#25-Obito	
#26-Tempo_Internacao

heartDecTargets <- decodeClassLabels(heartTargets)
heart <- splitForTrainingAndTest(heartValues, heartDecTargets, ratio = 0.25)
heart <- normTrainingAndTestSet(heart)
#Teste Modelo 1 - Std_Backpropagation
#Teste Modelo 2 - BackpropMomentum
#Teste Modelo 3 - Rprop
#Teste Modelo 4 - BackpropWeightDecay
#Teste Modelo 5 - Quickprop

model <- mlp(heart$inputsTrain, heart$targetsTrain, size =10,learnFunc="Quickprop",
             learnFuncParams = 0.01, maxit = 5000, inputsTest = heart$inputsTest, 
             targetsTest = heart$targetsTest)
predictions <- predict(model, heart$inputsTest)
confusionMatrix(heart$targetsTrain, fitted.values(model))
confusionMatrix(round(predictions[,2]), heart$targetsTest[, 2])
#summary(heart);
#summary(model);
plotIterativeError(model)
auc(round(predictions[,2]), heart$targetsTest[, 2])
plotROC(fitted.values(model)[,2], heart$targetsTrain[,2])
plotROC(predictions[,2], heart$targetsTest[,2])

