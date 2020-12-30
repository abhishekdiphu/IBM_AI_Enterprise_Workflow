



**[IBM_AI_Enterprise_Workflow](https://www.coursera.org/specializations/ibm-ai-workflow?)**


# THE DESIGN THINKING PROCESS
Transforming data and feature engineering are processes that can take place at any stage of the design thinking process. In this case, AAVAiL has completed most of the data gathering work associated with the Empathize phase and is moving on to the Define phase where information and data are being sorted and organized in order to define the challenges that AAVAiL is facing.

This is one point at which we can start to incorporate domain experts to help us to translate their insights into usable features in our data. Playbacks, interviews, and data understanding exercises are all important tools we would use to take advantage of the knowledge of domain experts.


# the basics of data transformation, but now you get to use that knowledge in a more applied setting. An important aspect of applying data transformations is making sure you apply them correctly in your AI workflow. This in turn generally involves iteration.

#### Feature engineering is about the selection of data "features" that enhance the performance of your model. Another useful aspect of feature engineering is the augmentation of your original matrix with new features that often contain domain specific insight. All of the transforms for feature engineering we will touch on are meant to be compared with each other. From a software engineering perspective this will mean working with pipelines, because they are useful to compare variants of the workflow.



# 1.Transforms with scikit-learn
---------------------------------

We have been using scikit-learn to this point, but we have not talked much about the package itself [1]. scikit-learn has a very well-designed API and a brief description here will help put the tools and vocabulary used in this course into perspective [2].

There are three interfaces meant to work together:

Transformer interface
Used to convert data from one form to another
Estimator interface
Used to build and fit models
Predictor interface
Used to making predictions
NumPy arrays and SciPy sparse matrices are used as standardized input to these interfaces. The estimator interface provides  a .fit() method for model training. All supervised and unsupervised algorithms use this interface. Feature extraction, feature selection and dimension reduction are also cases of the estimator interface. Some estimators also have a transform interface, like the StandardScaler.