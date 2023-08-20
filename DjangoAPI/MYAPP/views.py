from django.shortcuts import render
from . import forms

from rest_framework import viewsets
from rest_framework.decorators import api_view
from django.core import serializers
from rest_framework.response import Response
# from rest_framework.request import Request
from django.http import JsonResponse,request
from rest_framework.parsers import JSONParser
from .models import Approval
from . serliazers import approvalSerializers
from sklearn.ensemble import VotingClassifier
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.preprocessing import MinMaxScaler
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.metrics import ConfusionMatrixDisplay
import matplotlib.pyplot as plt
import pandas as pd
import joblib
import gzip
from . forms import ApprovalForm
import pickle
with open('C:\Data\FULLSTACK\model_Bankloan.pkl','rb') as file:
    model =joblib.load(file)
# Create your views here.
class ApprovalView(viewsets.ModelViewSet):
    queryset=Approval.objects.all()
    serialiser_class=approvalSerializers

def preprocess_data(Gender, Married, Dependents, Education, Self_Employed,
       ApplicantIncome, CoapplicantIncome, LoanAmount,
       Loan_Amount_Term, Credit_History, Property_Area):
    # Convert categorical variables to numerical values
    gender_num = 1 if Gender == 'Male' else 0
    married_num = 1 if Married == 'Yes' else 0
    graduateeducation_num = 1 if Education == 'Graduate' else 0
    selfemployed_num = 1 if Self_Employed == 'Yes' else 0

    area_map = {'Rural': 0, 'SemiUrban': 1, 'Urban': 2}
    area_num = area_map.get(Property_Area, 0)  

    columns = ['Gender', 'Married', 'Dependents', 'Education', 'Self_Employed',
       'ApplicantIncome', 'CoapplicantIncome', 'LoanAmount',
       'Loan_Amount_Term', 'Credit_History', 'Property_Area']
    data = [[gender_num, married_num, Dependents, graduateeducation_num, selfemployed_num,
       ApplicantIncome, CoapplicantIncome, LoanAmount,
       Loan_Amount_Term, Credit_History, area_num]]
    df = pd.DataFrame(data, columns=columns)

    return df

def contactx(request):
    prediction_result=None
    if request.method == "POST":
        form = ApprovalForm(request.POST)
        if form.is_valid():
            # Extract form data
            ApplicantIncome = form.cleaned_data["ApplicantIncome"]
            CoapplicantIncome=form.cleaned_data["CoapplicantIncome"]
            Dependents=form.cleaned_data["Dependents"]
            LoanAmount = form.cleaned_data["LoanAmount"]
            Loan_Amount_Term=form.cleaned_data["Loan_Amount_Term"]
            Credit_History = form.cleaned_data["Credit_History"]
            Gender = form.cleaned_data["Gender"]
            Married = form.cleaned_data["Married"]
            Education = form.cleaned_data["Education"]
            Self_Employed = form.cleaned_data["Self_Employed"]
            Property_Area = form.cleaned_data["Property_Area"]


            # Preprocess the data
            input_data = preprocess_data(Gender, Married, Dependents, Education, Self_Employed,
       ApplicantIncome, CoapplicantIncome, LoanAmount,
       Loan_Amount_Term, Credit_History, Property_Area)
            print(input_data)
            # Make predictions using the loaded model
            prediction = model.predict(input_data)
            print(prediction)

            # Prepare the prediction result for display
            prediction_result = "Approved" if prediction[0] == 1 else "Not Approved"
            print(prediction_result)
        else:
            print("Form Errors:", form.errors)
            # Return the prediction result to the template

    else:
        print("GET-Method")
        form = ApprovalForm()

    return render(request, 'MyForm/cxform.html', {'form': form, 'prediction_result': prediction_result})