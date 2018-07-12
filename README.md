# knnClassifier
This repository contains a project using k-NN (k-Nearest Neighbors) classifier. As example, five datasets are included in the project i.e. the famous iris, e-coli proteins, yeasts proteins, wine chemistry and weat seeds.

There are **3 python modules**, which are explained next. Also, there is a folder called **data_raw** containing one folder for each of the five datasets. This folder contains the raw data. The foldar **data** stores the subsets i.e. validation (Z2), test (Z3) and training (Z1) sets.

## geraBases.py
  This module receives the raw information contained in the **data_raw** folder, and randomly splits the samples into **data**
 folder, this way generating the validation (Z2), test (Z3) and training (Z1) sets.

## classificador.py
  This module is imported in the **methods.py** module. The functions are used in two training methods provided by the **methods.py** module, which are explained in the the next module.

## methods.py
  In this, there are two methods to train the classifier.
  ### method 1:
    First, the validation set is classified on the training for a predefined number of iterations (predefined: 30), varying the parameter k from the k-NN classifier. After, the value for k that minimize the errors is considered and the misclassified samples on the validation are swaped with random sampled from the training set, this procedure repeats for a predefined number of runs (predefined: 30). Last, the test set is classified on the optimized training set to evaluate the generated classification model.

  ### method 2:
    This method is the same as method 1, the only difference is on training step. In method 1, when the runs occur swapping the samples the k is fixed. In this method, the is also optimized again when the runs occur.
    
# In the repository, there is an article containing all detailed information of the methodology and the statistical analysis of the results (article.pdf)

# Any questions?
## gplichoski@gmail.com


