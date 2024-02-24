# Introduction
Since the advent of the Internet, it became a major part of our lives. Most of our daily activities can now be done online. This increase on internet dependence also increased the cybercrimes occurrence. It is very important for individuals and organisations to be secure while using the Internet. Our project aims at creating an ML model that classifies any network packet as legitimate or malicious. This model can be deployed on the network devices to allow only authentic packets to enter into the network. 
To build the model, NSL_KDD dataset is taken into consideration and models for Random Forest, AdaBoost and XGBoost algorithms are developed. An ensemble model is developed by combining these individual models using VotingClassifier. Random forest model, found to have the highest accuracy, is used to predict the authenticity of the network packet. 

# Usage
The project.py file contains the entire code of the project. The model with highest accuracy, i.e. , Random Forest model is pickled and saved as model_file.sav. This file will be used in predicting the authenticity of the network packet. The ui.py file contains the code for taking the input from user, processing it and displaying the prediction result. The index.html file contains the HTML code for the user interface that allows the user to enter packet details. The result.html file contains the HTML code for displaying the result. 
To run this project on Google Colaboratory, open ui.py file in a new notebook. Upload model_file.sav file. Also upload index.html and result.html in sample_data/static/templates folder of the notebook.  On running the code, an URL will be displayed, which upon clicking will display the user interface of the project. The user can now enter packet details and click on “Predict” button. The result will then be displayed on the screen. 

Project.py - [Colab link](https://colab.research.google.com/drive/1rY3o2-DwoluKb4ssYR6epqUtPs0Zv00V?usp=sharing#scrollTo=SbCXsAkPuQAM)

Ui.py – [Colab link](https://colab.research.google.com/drive/1JsGcYwDZN0nuI5UKrINOPEZlZeHWqKoD?usp=sharing#scrollTo=pX-kaIFNt5SJ)
