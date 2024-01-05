# FrozenLava-Encryptcon
Team Frozenlava's submission for the hackathon encryptcon.

# Filename and description

data-cleaning-encryptcon.ipynb: The data cleaning notebook which operated on dataset ( https://www.kaggle.com/datasets/shivamb/bank-customer-segmentation) To produce two cleaned files, Customerdata and transaction data.

clustering-frozenlava.ipynb: The notebook which clusters similar customers together. based on this models are built for groups of similar customers for fraudulent transaction detection

data-creation-frozenlava.ipynb: The notebook which creates cluster-wise datasets for the classification models that are built.

knn-clusterdetect.ipynb: Given a new testdata, using KNN this notebook's model detects the cluster that it belongs to.

xgboost-encryptcon.ipynb: The Notebook used to train the XGBoost model.

index.py and tempcoderunner.py: python files used for demonstration of our submission.

model_cluster0.joblib till model_cluster3.joblib: The trained and pickled XGBoost models used for classifying fraudulent/non fraudulent for different clusters. 
