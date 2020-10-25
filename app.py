from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('churn_predictor_model.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        Gender=request.form['Gender']
        if(Gender=='Male'):
            Gender_Male=1
            Gender_Male=0
        else:
            Gender_Male=0
            Gender_Male=1
        Scitizen = int(request.form['scitizen'])
        Life_Partner=request.form['Life_Partner']
        if(Life_Partner='Yes'):
            Life_Partner_Yes=1
            Life_Partner_No=0
        else:
            Life_Partner_Yes=0
            Life_Partner_No=1
        Dependents = request.form['Dependents']
        if(Dependents='Yes'):
            Dependents_Yes = 1
            Dependents_No = 0
        else:
            Dependents_Yes=0
            Dependents_No=1
        Tenure = int(request.form['scitizen'])
        Phone_Service=request.form['Phone_Service']
        if(Phone_Service='Yes'):
            Phone_Service_Yes = 1
            Phone_Service_No = 0
        else:
            Phone_Service_Yes = 0
            Phone_Service_No = 1
        Multiple_Lines=request.form['Multiple_Lines']
        if(Multiple_Lines='Yes'):
            Multiple_Lines_Yes = 1
            Multiple_Lines_No = 0
            MultipleLines_No_phone_service = 0
        elif(Multiple_Lines='No'):
            Multiple_Lines_Yes = 0
            Multiple_Lines_No = 1    
            MultipleLines_No_phone_service = 0
        else:
            Multiple_Lines_Yes = 0
            Multiple_Lines_No = 0  
            MultipleLines_No_phone_service = 1  
        Internet_Service = request.form['Internet_Service']    
        if(Internet_Service='Yes'):
            InternetService_DSL = 1
            InternetService_Fiber_optic = 0
            InternetService_No = 0
        elif(Internet_Service='No'):
            InternetService_DSL = 0
            InternetService_Fiber_optic = 1
            InternetService_No = 0
        else:
            InternetService_DSL = 0
            InternetService_Fiber_optic = 0
            InternetService_No = 1
        Online_Security = request.form['Online_Security']    
        if(Online_Security='Yes'):
            OnlineSecurity_Yes = 1
            OnlineSecurity_No = 0
            OnlineSecurity_No_internet_service = 0
        elif(Online_Security='No'):
            OnlineSecurity_Yes = 0
            OnlineSecurity_No = 1
            OnlineSecurity_No_internet_service = 0
        else:
            OnlineSecurity_Yes = 0
            OnlineSecurity_No = 0
            OnlineSecurity_No_internet_service = 1  

        Online_Backup = request.form['Online_Backup']    
        if(Online_Backup='Yes'):
            OnlineBackup_Yes = 1
            OnlineBackup_No = 0
            OnlineBackup_No_internet_service = 0
        elif(Online_Security='No'):
            OnlineBackup_Yes = 0
            OnlineBackup_No = 1
            OnlineBackup_No_internet_service = 0
        else:
            OnlineBackup_Yes = 0
            OnlineBackup_No = 0
            OnlineBackup_No_internet_service = 1 
        Device_Protection = request.form['Device_Protection']        
        if(Device_Protection='Yes'):
            DeviceProtection_Yes = 1
            DeviceProtection_No = 0
            DeviceProtection_No_internet_service = 0
        elif(Device_Protection='No'):
            DeviceProtection_Yes = 0
            DeviceProtection_No = 1
            DeviceProtection_No_internet_service = 0
        else:
            DeviceProtection_Yes = 0
            DeviceProtection_No = 0
            DeviceProtection_No_internet_service = 1 

        Tech_Support = request.form['Tech_Support']             
        if(Tech_Support='Yes'):
            TechSupport_Yes = 1
            TechSupport_No = 0
            TechSupport_No_internet_service = 0
        elif(Tech_Support='No'):
            TechSupport_Yes = 0
            TechSupport_No = 1
            TechSupport_No_internet_service = 0
        else:
            TechSupport_Yes = 0
            TechSupport_No = 0
            TechSupport_No_internet_service = 1 
        Streaming_TV = request.form['Streaming_TV']     
        if(Streaming_TV='Yes'):
            StreamingTV_Yes = 1
            StreamingTV_No = 0
            StreamingTV_No_internet_service = 0
        elif(Streaming_TV='No'):
            StreamingTV_Yes = 0
            StreamingTV_No = 1
            StreamingTV_No_internet_service = 0
        else:
            StreamingTV_Yes = 0
            StreamingTV_No = 0
            StreamingTV_No_internet_service = 1    
        Streaming_Movies = request.form['Streaming_Movies']   
        if(Streaming_Movies='Yes'):
            StreamingMovies_Yes = 1
            StreamingMovies_No = 0
            StreamingMovies_No_internet_service = 0
        elif(Streaming_Movies='No'):
            StreamingMovies_Yes = 0
            StreamingMovies_No = 1
            StreamingMovies_No_internet_service = 0
        else:
            Streaming_Movies = 0
            StreamingMovies_No = 0
            StreamingMovies_No_internet_service = 1
        Contract = request.form['Contract']   
        if(Contract='Month-to-month'):
            Contract_Month-to-month = 1
            Contract_One_year = 0
            Contract_Two_year = 0
        elif(Contract='One year'):
            Contract_Month-to-month = 0
            Contract_One_year = 1
            Contract_Two_year = 0
        else:
            Contract_Month-to-month = 0
            Contract_One_year = 0
            Contract_Two_year = 1
        Paperless_Billing = request.form['Paperless_Billing']   
        if(Paperless_Billing='Yes'):
            PaperlessBilling_Yes = 1
            PaperlessBilling_No = 0
        else:
            PaperlessBilling_Yes = 0
            PaperlessBilling_No = 1
        Payment_Method = request.form['Payment_Method']         
        if(Payment_Method='Bank Transfer (Automatic)'):
            PaymentMethod_Bank_transfer_(automatic) = 1
            PaymentMethod_Credit_card_(automatic)    = 0
            PaymentMethod_Electronic_check  = 0
            PaymentMethod_Mailed_check = 0
        elif(Payment_Method='PaymentMethod Credit card (automatic)'):
            PaymentMethod_Bank_transfer_(automatic) = 0
            PaymentMethod_Credit_card_(automatic)    = 1
            PaymentMethod_Electronic_check= 0
            PaymentMethod_Mailed_check = 0
        elif(Payment_Method='PaymentMethod_Electronic check'):
            PaymentMethod_Bank_transfer_(automatic) = 0
            PaymentMethod_Credit_card_(automatic)    = 0
            PaymentMethod_Electronic_check = 1
            PaymentMethod_Mailed_check = 0
        else:
            PaymentMethod_Bank_transfer_(automatic) = 1
            PaymentMethod_Credit_card_(automatic)    = 0
            PaymentMethod_Electronic_check = 0
            PaymentMethod_Mailed_check = 1

        MonthlyCharges = float(request.form['Monthly_Charges'])
        TotalCharges=float(request.form['Total_Charges'])
        
        prediction=model.predict([['No._of_Senior_Citizens', 'Tenure', 'MonthlyCharges', 'TotalCharges',
       'Churn', 'Gender_Female', 'Gender_Male', 'LifePartner_No',
       'LifePartner_Yes', 'Dependents_No', 'Dependents_Yes', 'PhoneService_No',
       'PhoneService_Yes', 'MultipleLines_No',
       'MultipleLines_No_phone_service', 'MultipleLines_Yes',
       'InternetService_DSL', 'InternetService_Fiber_optic',
       'InternetService_No', 'OnlineSecurity_No',
       'OnlineSecurity_No_internet_service', 'OnlineSecurity_Yes',
       'OnlineBackup_No', 'OnlineBackup_No_internet_service',
       'OnlineBackup_Yes', 'DeviceProtection_No',
       'DeviceProtection_No_internet_service', 'DeviceProtection_Yes',
       'TechSupport_No', 'TechSupport_No_internet_service', 'TechSupport_Yes',
       'StreamingTV_No', 'StreamingTV_No_internet_service', 'StreamingTV_Yes',
       'StreamingMovies_No', 'StreamingMovies_No_internet_service',
       'StreamingMovies_Yes', 'Contract_Month-to-month', 'Contract_One_year',
       'Contract_Two_year', 'PaperlessBilling_No', 'PaperlessBilling_Yes',
       'PaymentMethod_Bank_transfer_(automatic)',
       'PaymentMethod_Credit_card_(automatic)',
       'PaymentMethod_Electronic_check', 'PaymentMethod_Mailed_check']])
        output=round(prediction[0],2)
        if output=0:
            return render_template('index.html',prediction_texts="This customer will not churn")
        else:
            return render_template('index.html',prediction_text="This customer will churn")
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)

