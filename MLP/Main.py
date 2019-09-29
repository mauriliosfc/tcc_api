import pandas as pd
import numpy as np
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix

class Main(object):

    @staticmethod
    def main():

        df = pd.read_csv("C:\\Users\\Gustavo\\Documents\\projetoTCCDjango\\MLP\\src\\arquivos\\G4 - Base_Simulacao.txt", sep="\t", header=None)
        df = df.reindex(np.random.permutation(df.index))

        #x = df.iloc[:,0:23]
        #y = df.iloc[:,28]
        
        #x = df.iloc[:,0:21]
        #y = df.iloc[:,24]

        x = df.iloc[:,0:23]
        y = df.iloc[:,27]
        print (y)
        # rename = {
        #     "Sim":"1",
        #     "Nao":"0"
        # }
        #y =y.map(rename)

        x_train, x_test, y_train, y_test = train_test_split(x,y, test_size= 0.25, random_state=27)

        clf = MLPClassifier(hidden_layer_sizes=(10,10,10,10), max_iter=5000, alpha=0.0001,
                     solver='sgd', verbose=10,  random_state=21)

        #clf = MLPClassifier(alpha=1e-15, hidden_layer_sizes=(5, 5, 5), max_iter=5000,verbose=10,early_stopping =True)
        clf.fit(x_train, y_train)
        y_pred = clf.predict(x_test)
        print(y_pred)

        acuracia = accuracy_score(y_test, y_pred)
        print ("auc: "+str(acuracia))

        count = 0
        count_2 = 0
        for item in y_pred:
            if(item == 0):
                count= count+1
            else:
                count_2 = count_2+1

        print (count)
        print(count_2)
if __name__ == '__main__':
    Main.main()
