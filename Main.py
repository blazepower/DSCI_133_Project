import csv
from os import listdir
from DeepLearningAlgorithim import textAn_model
import pandas as pd
from keras.utils import to_categorical
import sklearn.feature_extraction.text as text
# Import test data from "Liar, Liar Pants on Fire":
# A New Benchmark Dataset for Fake News Detection - William Yang Wang
train = pd.read_csv('liar_dataset/train.tsv', sep='\t')

# Dictionary to Classify Validity on a scale 1-5 with 5 having the most truth and 1 being the least truthful
trainDf = pd.DataFrame(data=train[train.columns[[1, 2]]])
d = {'true': 5, 'mostly-true': 4, 'half-true': 3, 'false': 1, 'barely-true': 2, 'pants-fire': 0}
trainDf.columns = ['Validity', 'Comment']
trainDf['Validity'] = trainDf['Validity'].map(lambda x: d.get(x))
y_train = to_categorical(trainDf['Validity'])
tf = text.TfidfVectorizer()
X_train = tf.fit_transform(trainDf['Comment']).todense()

model = textAn_model()
model.fit(X_train, y_train, epochs=5, batch_size=200, verbose=2)

# This code was used only for demonstration purposes because the full algorithm takes well over and hour to run
# print(model.predict_classes(tf.transform(["Ohio is a State", "Barrack Obama was born in Kenya", "Donald Trump is
# the first female President in United States history"])))

# The following code is used to read and run the machine learning model on the gathered Tweets
dir = 'Tweets/'
for file in listdir(dir):
    dfs = pd.read_excel(dir + file)
    ms = list(dfs)
    ms1 = ms[0]
    dfs1 = dfs[ms1]
    dsf2 = dfs1.add(ms1)
    df3 = dsf2.values
    tlist = df3.tolist()
    validated = []
    for tweet in tlist:
        validated.extend(model.predict_classes(tf.transform([tweet])))
    print(validated)
    newName = file.replace(".xlsx", "")
    with open(newName + 'Num', 'w') as my_file:
        wr = csv.writer(my_file, quoting=csv.QUOTE_ALL, delimiter='\n')
        wr.writerow(validated)
