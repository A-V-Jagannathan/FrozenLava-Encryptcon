import tkinter as tk
from tkinter import messagebox
from xgboost import XGBClassifier
import joblib
from datetime import datetime , date
import time
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier

prediction = 0
def on_submit():
    if selected_option.get() == "M":
        gen = 1
    else:
        gen = 0
    global df
    df["Age"]=[entry_widgets[0].get()]
    df["Gender"]=[gen]
    df["Average bank balance"]=[entry_widgets[1].get()]
    df["Average unix time of transaction"]=[get_time()]
    df["Amount"]=[entry_widgets[2].get()]
    print(df)
    loaded_scaler = joblib.load('standard_scaler.pkl')
    knn_classifier=KNeighborsClassifier(n_neighbors=5)
    knn_classifier=joblib.load("knn_model.joblib")
    scaled_data=loaded_scaler.transform(df[['Age','Gender','Average bank balance','Average unix time of transaction']])
    cluster=knn_classifier.predict(scaled_data[0].reshape(1,4))[0]
    newdf=pd.DataFrame()
    newdf["CustAccountBalance"]=[int(df.iloc[0,2])]
    newdf["TransactionTime"]=[int(df.iloc[0,3])]
    newdf["TransactionAmount (INR)"]=[int(df.iloc[0,4])]
    print(newdf)
    if(cluster==0):
        #Load model and predict
        model_cluster0 = XGBClassifier()
        model_cluster0=joblib.load("model_cluster0.joblib")
        prediction=model_cluster0.predict(newdf)[0]
        print("Cluster0",prediction)
    elif(cluster==1):
        #Load model and predict
        model_cluster1 = XGBClassifier()
        model_cluster1=joblib.load("model_cluster1.joblib")
        prediction=model_cluster1.predict(newdf)[0]
        print("Cluster1",prediction)
    elif(cluster==2):
        #Load model and predict
        model_cluster2 = XGBClassifier()
        model_cluster2=joblib.load("model_cluster2.joblib")
        prediction=model_cluster2.predict(newdf)[0]
        print("Cluster2",prediction)
    else:
        #Load model and predict
        model_cluster3 = XGBClassifier()
        model_cluster3=joblib.load("model_cluster3.joblib")
        prediction=model_cluster3.predict(newdf)[0]
        print("Cluster3",prediction)
    if prediction == 0 :
        messagebox.showinfo(title="Prediction Result",message="No Fraud")
    else:
        messagebox.showinfo(title="Prediction Result",message="Fraudulent")

def get_time():
    current_time = datetime.now()
    hours = int(current_time.strftime("%H"))*60*60
    minutes = int(current_time.strftime("%M"))*60
    seconds = int(current_time.strftime("%S"))
    return hours+minutes+seconds


# Initialize an empty DataFrame
df = pd.DataFrame()





today = date.today()

# Create the main window
root = tk.Tk()
root.geometry('250x250')
root.title('Fraud Detection')
root.configure(background='#CDCDCD')


# Labels and Entry Widgets
labels = ["Age:","Bank balance:","Amount:"]
options = ["M","F"]
entry_widgets = []

for i, label_text in enumerate(labels):
    label = tk.Label(root, text=label_text)
    label.grid(row=i, column=0, sticky=tk.E, padx=10, pady=10)

    entry = tk.Entry(root)
    entry.grid(row=i, column=1, padx=10, pady=10)
    entry_widgets.append(entry)



options = ["M","F"]

label = tk.Label(root, text="Gender")
label.grid(row=3, column=0, sticky=tk.E, padx=10, pady=10)



# Variable to store the selected option
selected_option = tk.StringVar(root)
selected_option.set(options[0])  # Set the default option

# Create the drop-down menu
option_menu = tk.OptionMenu(root, selected_option, *options)
option_menu.grid(row=3,column=1,padx=10,pady=10)

# Submit Button
submit_button = tk.Button(root, text="Submit", command=on_submit)
submit_button.grid(row=len(labels)+1, column=0, columnspan=2, pady=10)

# Run the Tkinter event loop
root.mainloop()
