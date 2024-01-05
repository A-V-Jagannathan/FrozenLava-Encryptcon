# FrozenLava-Encryptcon
Team Frozenlava's submission for the hackathon encryptcon.

## Project environment setup

There is no dependency apart from the default jupyter notebook enviroment

## Defining project aim and goal

Objective is to detect suspicious/ fraudulent transactions based on behavorial analysis.

## Methodology
This project clusters customers with similar behaviour together, and trains a model on the behavior of these customers. Whenever a transaction is made by a customer,

- If it is a new customer, Based on the customer's detail, he is assigned a cluster.
- The model belonging to that cluster, will check whether the transaction look fraudulent or not ( if it is similar to other transactions made by customers belonging to the same cluster, then non fraudulent)
- This model does NOT prove it is a fraudulent transaction, rather detects abnormal transactions. It must be supplemented with a system which does secondary verification, if the activity looks suspicious.
  
## Filename, Foldername and their description

- Models: Contains the trained models used by our demonstration py files.
- Demonstration: Contains the py files used for demonstration of our submission.
- data-cleaning-encryptcon.ipynb: The data cleaning notebook which operated on dataset ( https://www.kaggle.com/datasets/shivamb/bank-customer-segmentation) To produce two cleaned files, Customerdata and transaction data.
- clustering-frozenlava.ipynb: The notebook which clusters similar customers together. based on this models are built for groups of similar customers for fraudulent transaction detection
- data-creation-frozenlava.ipynb: The notebook which creates cluster-wise datasets for the classification models that are built.
- knn-clusterdetect.ipynb: Given a new testdata, using KNN this notebook's model detects the cluster that it belongs to.
- xgboost-encryptcon.ipynb: The Notebook used to train the XGBoost model.


