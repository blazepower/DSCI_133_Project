# Machine Learning: The Accuracy and Shortfalls of Artificial Intelligence in Fact Checking Presidential Candidates

#### Authored by [Rishik Hombal](rsh83@case.edu), [Brandon Rudolph](brr30@case.edu), and [Jack Zhang](cxz416@case.edu)
***
##### Read the [Project Report](https://github.com/blazepower/DSCI_133_Project/tree/master/Project_Report.docx) for the detailed methodology and analysis.

###### Abstract:
###### The purpose of this report was to train machine learning algorithms to fact check Presidential candidates. Using training data provided by William Yang Wang, we trained Google’s machine learning libraries Keras and Tensorflow to develop a supervised-learning algorithm to determine the truth of the program’s inputs. Outputs are enumerated from 0 (not true) through 5 (entirely true), spanning a set of 6 possible results per input. After testing the algorithm, it received an accuracy of 30%. We then proceed to use our data to make correlational connections between the honesty of a candidate and their political performances.
***

[DataGather.py](https://github.com/blazepower/DSCI_133_Project/blob/master/DataGather.py) is code which gathers and cleans the candidates Tweets. 

The [Tweets](https://github.com/blazepower/DSCI_133_Project/tree/master/Tweets) folder contains those Tweets as gathered on 4/22/29 in the form of Excel Workbooks.

The [Data](https://github.com/blazepower/DSCI_133_Project/tree/master/Data) folder contains CSV files containing the scores of the individual Tweets by each candidate.

Take a look at the [RunTime Videos and Output](https://github.com/blazepower/DSCI_133_Project/tree/master/RunTime_Videos_and_Output) folder to see videos of our code running and the outputs that they produce.

The [Project Presentation](https://github.com/blazepower/DSCI_133_Project/blob/master/Project_Presentation.pdf) contains the presentation files used during the class presentation on 4/25/19.
