# FrozenLava-Encryptcon
Team Frozenlava's submission for the 24-hour hackathon, encryptcon.

## Project environment 

There is no dependency apart from the default jupyter notebook enviroment

## Defining project aim and goal

Objective is to detect suspicious/ fraudulent transactions based on behavorial analysis.

## Methodology
This project clusters customers with similar behaviour together, and trains a model on the behavior of these customers. Whenever a transaction is made by a customer,

- If it is a new customer, Based on the customer's detail, he is assigned a cluster.
- The model belonging to that cluster, will check whether the transaction look fraudulent or not ( if it is similar to other transactions made by customers belonging to the same cluster, then non fraudulent)
- This model does NOT prove it is a fraudulent transaction, rather detects abnormal transactions. It must be supplemented with a system which does secondary verification, if the activity looks suspicious.
  
## Foldername and their description

- Models: Contains the trained models used by our demonstration py files.
- Demonstration: Contains the py files used for demonstration of our submission.
- Data engineering and model-building notebooks: Contains the ipynb files used to build models and create data.
- Dataset: Contains links and description for the data used.

## How to run?

1. Download the trained models, from under the folder **Models**.
2. Download the demonstration python file, from under the folder **Demonstration**
3. Place every file under same directory, run index.py and observe the predictions!

## Images
![WhatsApp Image 2024-01-05 at 14 40 30_9cf58f56](https://github.com/A-V-Jagannathan/FrozenLava-Encryptcon/assets/98120916/7dcdf1cb-ccda-435b-9f11-0de439abccc6)
![WhatsApp Image 2024-01-05 at 14 40 59_c0bbc7d7](https://github.com/A-V-Jagannathan/FrozenLava-Encryptcon/assets/98120916/39fd360d-f595-4b2e-aff7-879f6617adc6)
![WhatsApp Image 2024-01-05 at 14 41 51_f47e7db1](https://github.com/A-V-Jagannathan/FrozenLava-Encryptcon/assets/98120916/b6fcc587-848e-4159-b783-99f398db822a)





