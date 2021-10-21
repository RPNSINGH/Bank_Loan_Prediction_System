# Indian Paper Curreny Prediction :india: 

## Table of Content
  * [Demo](#demo)
  * [Overview](#overview)
  * [Motivation](#motivation)
  * [Technical Aspect](#technical-aspect)
  * [Installation](#installation)
  * [Run](#run)
  * [Deployement on Heroku](#deployement-on-heroku)
  * [Directory Tree](#directory-tree)
  * [To Do](#to-do)
  * [Bug / Feature Request](#bug---feature-request)
  * [Technologies Used](#technologies-used)
  * [Team](#team)
  * [License](#license)
  * [Credits](#credits)


## Demo
![Capture1](https://github.com/RPNSINGH/Bank_Loan_Prediction_System/blob/main/Bank_loan_prediction/Capture1.PNG)
![Capture2](https://github.com/RPNSINGH/Bank_Loan_Prediction_System/blob/main/Bank_loan_prediction/Capture2.PNG)

## Overview
This is a simple image classification Flask app trained on the top of Keras API. The trained model (`app/model/model.h5`) takes an image (Indian Paper Currency) as an input and predict the class of image from __10, 20, 50, 100, 200, 500, 2000__ denomination.

## Motivation
Lets Predict because we can do.

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


## To Do
1. Convert the app to run without any internet connection, i.e. __PWA__.
2. Add a better vizualization chart to display the predictions.

## Bug / Feature Request
If you find a bug (the website couldn't handle the query and / or gave undesired results), kindly open an issue [here](https://github.com/RPNSINGH/Bank_Loan_Prediction_System/issues/new) by including your search query and the expected result.

If you'd like to request a new function, feel free to do so by opening an issue [here](https://github.com/RPNSINGH/Bank_Loan_Prediction_System/issues/new). Please include sample queries and their corresponding results.

## Technologies Used

![](https://forthebadge.com/images/badges/made-with-python.svg)

[<img target="_blank" src="https://keras.io/img/logo.png" width=200>](https://keras.io/) [<img target="_blank" src="https://flask.palletsprojects.com/en/1.1.x/_images/flask-logo.png" width=170>](https://flask.palletsprojects.com/en/1.1.x/) [<img target="_blank" src="https://number1.co.za/wp-content/uploads/2017/10/gunicorn_logo-300x85.png" width=280>](https://gunicorn.org) [<img target="_blank" src="https://www.kindpng.com/picc/b/301/3012484.png" width=200>](https://aws.amazon.com/s3/) 

[<img target="_blank" src="https://sentry-brand.storage.googleapis.com/sentry-logo-black.png" width=270>](https://www.sentry.io/) [<img target="_blank" src="https://openjsf.org/wp-content/uploads/sites/84/2019/10/jquery-logo-vertical_large_square.png" width=100>](https://jquery.com/)

## Team
[![Rohit Swami](https://avatars1.githubusercontent.com/u/16516296?v=3&s=144)](https://rohitswami.com/) |
-|
[Rohit Swami](https://rohitswami.com/) |)

## License
[![Apache license](https://img.shields.io/badge/license-apache-blue?style=for-the-badge&logo=appveyor)](http://www.apache.org/licenses/LICENSE-2.0e)

Copyright 2020 Rohit Swami

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

## Credits
- [Google Images Download](https://github.com/hardikvasa/google-images-download) - This project wouldn't have been possible without this tool. It saved my enormous amount of time while collecting the data. A huge shout-out to its creator [Hardik Vasa](https://github.com/hardikvasa).
