



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


# Class imbalance: Through the Eyes of our Working Example




THE DESIGN THINKING PROCESS
During the Define and Ideate phases of the design thinking process, there will be a lot of work accomplished that is related to the identification of data sources that can be used to create machine learning models. You’ll be building and testing numerous pipelines, comparing the performance of each one with the others, and utilizing the best ones.

Utilizing them for what? Supporting the Define and Ideate processes. During these phases of the design thinking process the most important rule is to use your creativity to help develop a view of the challenges facing the company, and also to develop possible solutions for those challenges. It is impossible to know ahead of time what those challenges are. As a result, you will need the ability to effectively iterate using pipelines to do things like compare strategies that deal with imbalanced classes. Iteration and the ability to concisely summarize the finding is critical to your ability to support your team during the Define and Ideate stages of design thinking.


## Class Imbalance
Many machine learning algorithms used for classification contain implicit assumptions about having relatively equal numbers of examples of each class. For example you might train a logistic regression model to predict whether or not an email is spam, or whether or not a customer is likely to churn (i.e. leave a service). Such a model will usually have an easier time classifying these cases if there are similar numbers in each class.

However, there are many important problems where a reasonable balance between classes cannot be expected. A common example from business is in fraud detection, such as when a credit card processor flags a transaction as potentially fraudulent. A large credit card processor will go through many millions of transactions per day and the vast majority of these are likely to be legitimate, so finding suspicious ones requires particular care. Fraud detection in this context presents a prototypical problem of class imbalance.

Dealing with problems of class imbalance often requires finesse, and this unit introduces several potential approaches. These methods employ different tactics to avoid being overwhelmed by the majority class. Typically being overwhelmed during the model’s training directly affects the model’s accuracy. Accuracy, that is the proportion of predictions that are correct, is an intuitive metric for classification, but can be misleading with imbalanced classes. For example, if one percent of a processor’s transactions in a training sample are fraudulent, then a model that always predicts “not fraudulent” will be 99% accurate but of no practical use.

WARNING: Accuracy is not an appropriate metric for imbalanced classes. Use F1 Score or another metric instead.

The solution to misleading metrics is to break the correct vs. incorrect dichotomy of binary classification into four pieces: true positives, true negatives, false positives, and false negatives. There are many ways to combine these values with an even larger number of naming conventions.


(For more details, and the source of the table, click here:  https://en.wikipedia.org/wiki/Evaluation_of_binary_classifiers). 

Conventionally the rare or minority class (e.g. fraud) is designated as the positive class, so two of the more commonly used alternative metrics to accuracy—precision and recall—have the true positives in their numerators. You’ll also see F1 score, which is the harmonic mean of precision and recall.

Having better metrics for measuring performance in imbalanced classification is necessary, but not sufficient, to get better results. A simple logistic regression model optimizes a cost function where the cost of a false negative is the same as a false positive, so when negative training examples are much more common the results will tend toward the “always predict negative” end of the spectrum. You can of course adjust your cost function to weigh the errors differently, and certain ML models are more amenable to this than others. But we will start with a different set of solutions where we adjust the training data to make the classes more balanced. This involves either up-sampling or down-sampling your data, making the minority class more common through some type of repetition or making the majority class less common by throwing away some observations.

Different machine learning models vary in how well they deal with making predictions in imbalanced situations, so we end this section with a few examples of models that tend to perform well in such circumstances.


## Sampling Techniques
The most common approaches are sampling based, or more specifically, re-sampling based. Between up-sampling and down-sampling (also called over-sampling and under-sampling), down-sampling is a bit simpler conceptually. Fundamentally, if you have a minority class or classes that is noticeably underrepresented. In a random way you can drop some of those from the training data so that the proportions are more closely matched across classes. There are additional methods, one of which is inspired by K Nearest Neighbors (KNN) that can improve on pure random selection.

A major caveat to down-sampling is that we are not using all of our data. Over-sampling techniques also come in several flavors, from random or naive versions to classes of algorithms like the Synthetic Minority Oversampling Technique (SMOTE) [2] and the Adaptive Synthetic (ADASYN) [8] sampling method. Synthetic Minority Over-sampling Technique for Nominal and Continuous (SMOTENC) is an extension of the original SMOTE method designed to handle a mixture of categorical and continuous features. SMOTE has a number of other variants including ones that make use of Support Vector Machines and K-means clustering to improve on the synthetic samples.

## Models that Naturally Handle Imbalance
Some models are more sensitive to imbalanced classes than others. Neural networks for example are very sensitive to imbalanced classes. Support Vector Machines on the other hand and to some extent tree based methods are more resilient. If available, the class_weight argument should be used when working with imbalanced classes.


## Data Bias
There has been a lot of discussion in the literature and in the media about the use of biased algorithms. Facial recognition technologies in particular have been in the spotlight regarding (1) their misuse and (2) the fact that most available datasets are biased toward Caucasians and males. If we put privacy and ethical concerns aside for just a moment the problem is very similar to the imbalanced classes problem. There are underrepresented parts of the training data that need more data to become a better system. This is an important topic and if you want to learn more see the *Diversity in Faces* blogpost by IBM Research or the Diversity in Faces* research paper  



# Dimensionality Reduction: Through the Eyes of Our Working Example




## THE DESIGN THINKING PROCESS
Along with managing bias in your data, you’ll also be expected to manage the complexity of your data via dimensionality reduction as you pass through the Ideate and Prototyping phases of the design thinking process. One key area where dimensionality reduction is very useful is in data visualization. You will be asked to generate visuals of critical data distributions, and it will almost always be necessary to employ various dimensionality reduction techniques to arrive at a data set that can be easily used in a data plot.


## Why is Dimensionality Reduction Important?
Principal reasons to consider dimensionality reduction techniques in your workflow:

visualization
remove multicolinearity
remove redundant features
deal with the curse of dimensionality
identify structure for supervised learning
high-dimensional data
NOTE:  We will be using some of the concepts like Principal Component Analysis (PCA), singular value decomposition (SVD) and eigenvalue decomposition throughout this module with the assumption that you have some fundamental knowledge. If you need a refresher on these concepts we refer you to the appropriate section 2.7-2.12 in the Deep-Learning textbook [1].

Deep-Learning book Chapter 2

scikit-learn matrix decomposition tutorial



## Dimensionality reduction
Examples of data that often require dimensionality reduction either for visualization or for modeling purposes include images, texts, signal processing data, astronomical data, and health data. The sklearn.decomposition module includes a number of matrix decomposition algorithms including PCA, NMF and ICA. Matrix decomposition has been used for a long time to enable dimensionality reduction. One major drawback to using PCA is that non-linear or curved surfaces tend to not be well-explained by the approach. Manifold learning for dimensionality reduction has gained a lot of traction recently. In particular the t-distributed stochastic neighbor embedding (tSNE) family of approaches have become a viable alternative to PCA. It is also worth noting that feature selection techniques like using an ANOVA to select K features (see SelectKBest ) is also a valid form of dimensionality reduction.

# Topic models
Latent Dirichlet Allocation (LDA) and non-negative matrix factorization (NMF) are both commonly used in the context of topic modeling. Generally, these approaches use a bag-of-words representation. These models are in practice a form of dimensionality reduction. The embedding approach tSNE is often used to visualize the results of topic model representations in lower dimensional space to both tune the model as well as gather insights from the data. The package pyLDAvis is specifically purposed with visualizing the results of these models.

Topic modeling has a number of use cases apart from feature engineering for supervised learning. There is utility in being able to organize a large corpus of data. Take for example a law firm that has used the same types of forms for decades. Before the form was electronic it was simply put in a folder. Now that the forms are electronic they are organized into categories. LDA can be used to model the new corpus before the trained model is fed the historical documents. The trained model would then make probability estimates for membership in the categories.

Additional resources
Review paper about topic model applications
LDA was used to extract information from clinical notes in this example about sleep medication prescriptions and clinical decision-making



## Topic modeling: Through the Eyes of our Working Example



## THE DESIGN THINKING PROCESS
Feature engineering is yet another key skill you will be employing (along with dimensionality reduction and bias mitigation) as a data scientist during the Ideate, Prototype, and Testing phases of a design thinking project. Feature engineering in relation to text analysis is especially important because most large enterprises are looking for ways to deal with the vast amounts of unstructured data (text) available in the organization.

--------------------------------------------------------------------
# SUMMARY 
--------------------------------------------------------------------


The data-transformations part of the AI workflow is the first point in the overall process that explicitly encourages iteration. This stage encompasses all possible transformations of the data, such as dimensionality reduction, outlier detection, clustering and other forms of unsupervised learning. Combining these activities into a single process is done mainly because selecting a suitable transformation or tuning a given transformation takes the same form. That form builds on the three interfaces of scikit-learn and the container class pipelines.

Transformer interface
Used to convert data from one form to another
Estimator interface
Used to build and fit models
Predictor interface
Used to making predictions
It is worth noting that these interfaces in combinations with pipelines have had such an impact on the data science workflow that Apache Spark now has similar ML pipelines.

Class imbalance, data bias
Imbalanced classes are common especially in specific application scenarios like fraud detection and and customer retention. The first guideline is to ensure that you do not use accuracy as the metric as the results can be misleading. Accuracy is the number of correct calls divided by all of the calls.

accuracy = \frac{tp+tn}{tp + fp + tn + fn} 
tp+fp+tn+fn
tp+tn
​	
 

If our positive class is only a small percentage of the overall data you can see that the model will be optimized for the negative class. The ability of a model to resolve true positives will not be well-represented in the metric because it will be overwhelmed by the influence of the majority class. Metrics based on precision and recall will be more specific to the problem because TN (true negatives) is not part of the numerator.

precision = \frac{tp}{tp + fp} 
tp+fp
tp
​	
 

precision = \frac{tp}{tp + fn} 
tp+fn
tp
​	
 

The most common approaches to address imbalanced classes are sampling based. Between over-sampling and under-sampling, under-sampling is conceptually simpler. Given a minority class or classes that are noticeably underrepresented, you may randomly drop some of those observations from the training data so that the proportions are more closely matched across classes. A major caveat to under-sampling is that we are not using all of the data.

Over-sampling techniques come in several forms, from random or naive versions to classes of algorithms like the Synthetic Minority Oversampling Technique (SMOTE) [1] and the Adaptive Synthetic (ADASYN) [2] sampling method. There are a number of variants of these over-sampling algorithms that can be compared.

All of the sampling techniques that we discussed are implemented in the imbalanced-learn Python package. This package is convenient because it allows for the implementation of multiple sampling techniques as pipelines. Additionally, it interfaces with TensorFlow and Keras in a convenient way as well, which is important because neural networks are generally sensitive to class imbalance. Support Vector Machines (SVM) are an example of a machine learning algorithm that is less sensitive to imbalanced classes. SVMs can be tuned to accommodate situations with unbalanced class proportions making them a reasonable tool for outlier detection as well.

Dimensionality reduction
Applications of data science that often require dimensionality reduction for visualization or for modeling purposes are: image analysis, text analysis, signal processing, astronomy, and medicine. We discuss three main categories of dimensionality reduction techniques: matrix decomposition, manifold learning, and topic models. The techniques developed for topic models generally fall under one of the first two categories, but the application is natural language processing. The principal reasons for considering dimensionality reduction in your workflow are:

visualization
remove multicolinearity
remove redundant features
deal with the curse of dimensionality
identify structure for supervised learning
high-dimensional data
These materials review principal components analysis (PCA), Non-negative matrix factorization (NMF) and singular value decomposition (SVD) as examples of matrix decomposition algorithms. A major drawback to using PCA is that non-linear or curved surfaces tend to not be well-explained by the approach. An alternative approach uses manifold learning for dimensionality reduction. Specifically, we discuss the tSNE family of approaches.

We present NMF and Latent Dirichlet Allocation (LDA) as example methods to carry out topic modeling. The embedding approach tSNE is often used to visualize the results of topic model representations in lower dimensional space to both tune the model as well as gather insight into the data. The package pyLDAvis is specifically purposed with visualizing the results of these models.

sklearn.decomposition
sklearn.manifold



# CASE STUDY: topic modeling
Topic modeling is a commonly used form of dimensionality reduction. When we use visualization tools to explore the results of topic modeling we do so to identify features that are relevant to the domain. These insights can be transformed into new features that may be used directly or appended to the feature matrix. We use topic modeling in this case study to enable domain specific feature engineering.



