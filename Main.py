#Author@ Jack Zhang
#Learning Algorithim to Test Validity of 2020 Presidential Canidates Tweets

import csv
from os import listdir
from DeepLearningAlgorithim import textAn_model
import pandas as pd
from keras.utils import to_categorical
import sklearn.feature_extraction.text as text

train = pd.read_csv('liar_dataset/train.tsv', sep= '\t')  #Import test data from "Liar, Liar Pants n Fire":
                                                          #A New Benchmark Dataset for Fake News Detection - William Yang Wang

# Dictionary to Classify Validity on a scale 1-5 with 5 haing the most truth and 1 being the least turthful
trainDf = pd.DataFrame(data = train[train.columns[[1,2]]])
d = {'true': 5,'mostly-true': 4, 'half-true': 3,'false': 1, 'barely-true': 2, 'pants-fire': 0}
trainDf.columns = ['Validity', 'Comment']
trainDf['Validity'] = trainDf['Validity'].map(lambda x: d.get((x)))
y_train = to_categorical(trainDf['Validity'])
tf = text.TfidfVectorizer()
X_train = tf.fit_transform(trainDf['Comment']).todense()

model = textAn_model()
model.fit(X_train, y_train, epochs=5, batch_size=200, verbose=2)

print(model.predict_classes(tf.transform(["Ohio is a State", "Barrack Obama was born in Kenya", "Donald Trump is the first female President in United States history"])))













'''
dir = 'TwitterData/tweets/'
for file in listdir(dir):
    dfs = pd.read_excel(dir + file)
    ms = list(dfs)
    ms1 = ms[0]
    dfs1 = dfs[ms1]
    dsf2 = dfs1.add(ms1)
    df3 = dsf2.values
    tlist = df3.tolist()
    valideated = []
    for tweet in tlist:
        valideated.extend(model.predict_classes(tf.transform([tweet])))
    print(valideated)
    newName = file.replace(".xlsx", "")
    with open(newName + 'Num', 'w') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL, delimiter='\n')
        wr.writerow(valideated)
'''