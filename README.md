# Bank Loan Prediction System :india: 

## Table of Content
  * [Demo](#demo)
  * [Overview](#overview)
  * [Motivation](#motivation)
  * [Technical Aspect](#technical-aspect)
  * [Installation](#installation)
  * [Run](#run)
  * [Directory Tree](#directory-tree)
  * [To Do](#to-do)
  * [Bug Request](#bug-request)
  * [Technologies Used](#technologies-used)
  * [Team](#team)
  * [Credits](#credits)


## Demo
![Capture1](https://github.com/RPNSINGH/Bank_Loan_Prediction_System/blob/main/Bank_loan_prediction/images/Capture1.PNG)
![Capture2](https://github.com/RPNSINGH/Bank_Loan_Prediction_System/blob/main/Bank_loan_prediction/images/Capture2.PNG)

## Overview
This is a simple Tkinter app trained with machine learning algorithms. The trained model (`Tkinter_GUI`) takes inputs (*ie Applicant's_Income($),CoApplicant's_Income($),Loan_Amount($),Loan_Amount_Term($),Gender,Married,Dependents,Education,Credit_History,Property_Area,Self_Employed*) as an input and predicts the loan approval status.

## Motivation
During Covid pandemic all banks as well as customers faced tons of difficulties because of restrictions and due to that some customesrs whose business went down needed some funds (or Loans) from their banks to restart their business ,but due to unavailablity of their employees banks were unable . 
So to overcome this and with respect to future aspects we must be prepared and thats where this Idea striked me about making a model that can perform analysis on a loan request (based on old loan requests and their eligiblity)  decides whether that request is eligible or not .

## Technical Aspect
This project is divided into four part:
1. Data analysis and data preprocessing :
   - Using pandas to open and manipulate CSV file in jupyter notebook.
   - Visulization using :
     - Seaborn 
     - Matplotlib
   - Label Encoading 
   - Standardization
2. Outliers detection and removal using : 
    - Percentile method
    - Z score method
    - IOR method
3. Model selection and model training:
  - Decision Tree Classifier
  - Random Forest Classifier
4. GUI (Tkinter)

## Installation
The Code is written in Python 3.7. If you don't have Python installed you can find it [here](https://www.python.org/downloads/). If you are using a lower version of Python you can upgrade using the pip package, ensuring you have the latest version of pip. To install the required packages and libraries  

## Run
[Python](https://www.python.org/downloads/)<br>
[Pandas](https://pandas.pydata.org/)<br>
[Numpy](https://numpy.org/install/)<br>
[Matplotlib](https://matplotlib.org/stable/users/installing.html)<br>
[Seaborn](https://seaborn.pydata.org/installing.html)<br>
[Sci-kit Learn](https://scikit-learn.org/stable/install.html)<br>
[Jupyter notebook](https://jupyter.org/install)<br>

__Attention__: Please perform the steps given in these tutorials at your own risk. Please don't mess up with the System Variables. It can potentially damage your PC. __You should know what you're doing__. 
- https://www.tenforums.com/tutorials/121855-edit-user-system-environment-variables-windows.html
- https://www.onmsft.com/how-to/how-to-set-an-environment-variable-in-windows-10
## Directory Tree 
```
├── code 
│   ├── final.py
│   ├── data_analysis.ipynb
│   ├── models_training.ipynb
│   ├── outliers_detectiona_removal.ipynb
│   └── TKINTER_GUI.ipynb
├── datasets
│   ├── bank.csv
│   ├──preprocessed.csv
│   ├──train.csv
│
├── images

```

## To Do
1. Convert the app to Django plateform.
2. Add a better vizualization chart to display the predictions.

## Bug Request
If you find a bug (the website couldn't handle the query and / or gave undesired results), kindly open an issue [here](https://github.com/RPNSINGH/Bank_Loan_Prediction_System/issues/new) by including your search query and the expected result.

If you'd like to request a new function, feel free to do so by opening an issue [here](https://github.com/RPNSINGH/Bank_Loan_Prediction_System/issues/new). Please include sample queries and their corresponding results.

## Technologies Used
![python](https://github.com/RPNSINGH/Bank_Loan_Prediction_System/blob/main/Bank_loan_prediction/images/python.png)
![pandas](https://github.com/RPNSINGH/Bank_Loan_Prediction_System/blob/main/Bank_loan_prediction/images/pandas.png)
![numpy](https://github.com/RPNSINGH/Bank_Loan_Prediction_System/blob/main/Bank_loan_prediction/images/numpy.png)
![matplot](https://github.com/RPNSINGH/Bank_Loan_Prediction_System/blob/main/Bank_loan_prediction/images/matplot.jpg)
![seaborn](https://github.com/RPNSINGH/Bank_Loan_Prediction_System/blob/main/Bank_loan_prediction/images/seaborn.png)
![sci](https://github.com/RPNSINGH/Bank_Loan_Prediction_System/blob/main/Bank_loan_prediction/images/sci.png)
![jupyter](https://github.com/RPNSINGH/Bank_Loan_Prediction_System/blob/main/Bank_loan_prediction/images/jupyter.png)

## Team
[![RPN](https://github.com/RPNSINGH/RPNSINGH/blob/main/RPN.jpg)] |
-|
[Ratanjeet Pratap Narayan Singh]|)

## Credits
- [Kaggle Datasets](https://www.kaggle.com/datasets) - This project wouldn't have been possible without this tool. It saved my enormous amount of time while collecting the data. A huge regards to [Krish Naik](https://in.linkedin.com/in/naikkrish) ,[Sudhanshu Kumar](https://www.linkedin.com/in/-sudhanshu-kumar/) and [iNeuron](https://ineuron.ai/) .
