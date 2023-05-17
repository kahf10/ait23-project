# Using deep learning for electricity theft detection in AMIs

* Aithmad, Youssef
* DaSilva, Rakesh
* Hussain, Kahf


## Abstract
Advanced Metering Infrastructure (AMI) is one of the key components of a smart grid, consisting of smart meters that monitor the
power usage as well as communicate and control energy usage. Smart meters also introduce numerous new methods of electricity theft.
Malicious users are presented with the novel opportunity to hack into smart meters by way of advanced instruments or cyberattack
techniques. This illegal practice causes a vast amount of financial loss every year. Our objective is to exploit deep learning
techniques to analyze the load profiles and electricity consumption patterns of users we are able to identify malicious energy users
committing energy theft and reporting fraudulent meter readings. 

We are using an electricity consumption dataset released by State Grid Corporation of China (SGCC) which contains the electricity consumption data of 42,372 electricity customers within 1,035 days (1, 2014 to October 31, 2016).

- Link to dataset: https://drive.google.com/file/d/1xplUHpHIDizcRkvamVSchNhhZ4eAP9-d/view?usp=share_link
- Link to cleaned csv file (after dealing with null values and outliers): https://drive.google.com/file/d/14aAfMf-0GJ_WMqpr2Eg1shfoAP3FHAna/view?usp=share_link

## Documentation

# Importing Data

To load the dataset into the Colab Notebook, please follow these steps:

1. Download the cleaned (after dealing with null values and outliers) csv file through the link: https://drive.google.com/file/d/14aAfMf-0GJ_WMqpr2Eg1shfoAP3FHAna/view?usp=share_link
2. Open your Google Drive associated with the Colab Notebook account.
3. Navigate to the "Colab Notebooks" folder.
4. Upload the "cleaned.csv" file to this folder.

Once the file is uploaded, you can run the code to load the cleaned dataset.
By following the above steps, the cleaned dataset will be successfully loaded into the Colab Notebook.

Please ensure that you have the correct file name ("cleaned.csv") and that it is placed in the designated folder ("Colab Notebooks") to avoid any issues with loading the dataset.

# Data Preperation

Meter reading data may contain erroneous data or missing data, which may be due to a variety of reasons, such as:
• Broken electrical components
• Aging of resistors
• Error of transmission
• Bad connections
To recover these missing values, the mean value method is used. In which the average value of each row is taken and
utilized to fill any NULL value within such row.
In addition, there are also some erroneous values (i.e., outliers) in the metering data. There for, we recover those
values by using the “three-sigma rule of thumb”.
In cases where the row values are beyond recoverable or usable data (i.e., the row is missing more than 50% of its
data) the entire row is deleted to avoid faulty and skewed readings.
We then prepared the training and testing sets by performing an 80:20 train-test split with stratification to ensure
the percentage of fraudulent data is equal among the two sets and split each set into two groups: the readings, and their
‘flags’ (whether the reading was legitimate or not).

# Data Augmentation

Data Augmentation is beneficial in improving performance and outcomes of classification models by developing new
and distinct examples to train data sets. This can be accomplished by adding vaguely modified copies of previous data
or synthesising data from available data sets. The augmentation method used in this project was SMOTE (Synthetic Minority Oversampling TEchnique).

# Evaluation

Previous solutions incorporated numerous machine learning techniques such as XGBoost, SVMs (Support Vector Machines), RF (Random Forest), and CatBoost. However, these solutions have very mixed results, having difficulty accurately flagging fradulent data points.

So for our project, we incorporated a deep learning solution, as well as using data augmentation methods to highlight one of the possible ways to improve results outside of tuning models.
