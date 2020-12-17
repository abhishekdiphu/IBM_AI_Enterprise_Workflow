


+ **[AI Workflow: Business Priorities and Data Ingestion](https://www.coursera.org/learn/ibm-ai-workflow-business-priorities-data-ingestion?specialization=ibm-ai-workflow)**


# 1. Data science process models
The goal of the following few sections is to familiarize you with several process models being used today. The intent and general flow for all of these models is very much the same. In this course we will use the process of design thinking, but it is the consistent application of a process in practice that is important not the exact process itself. There are a number of reasons for choosing the design thinking process, but the most important is that it is being applied in a cross-disciplinary way—that is outside of data science. Historically, learning from other disciplines has been a hallmark of scientific achievement.

Important:This course is not focused on adhering to the specifics of a process model or a way of thinking. The focus is to incorporate best practices into your workflow and in general to scaffold these practices.

### OSEMN
Before the first stage of the OSEMN process a data scientist is required to identify the business opportunities. This is an important step in any data science process and perhaps one that deserves its own stage in the process.

According to the OSEMN framework, the elements of data science are:

Obtaining data
Scrubbing data
Exploring data
Modeling data
Interpreting data
and yes the acronym OSEMN is pronounced as Awesome.

### CRISP-DM
The CRoss-Industry Standard Process for Data Mining (CRISP-DM) is a process model that uses an open standard. The project has been around since 1996 and there are a lot of similarities to the OSEMN process. 

# 2.The Design Thinking Process:

### Playbacks
Bring stakeholders into the loop in a safe space to tell stories and exchange feedback.

### Hills
Are statements of intent written as meaningful user outcomes.

### Sponsor Users
Are real-world users that regularly contribute their domain expertise.

# 3.Data Science Workflow Combined with Design Thinking

Project : Café Sherlock
A friend of yours just opened a new Sherlock Holmes themed café. Her café is state-of-the-art complete with monitors built into the tables. The business is off to a good start, but she has gotten some feedback that the games could use improvement. She knows that good games keep the customers around a little longer. The games are a way to keep customers entertained while they drink coffee and buy food items. She has some games already, but wants your help to create a few more games to keep customers both informed and entertained.

### Empathize
In this stage time is dedicated to understanding the business opportunities.

In this setting the frequency and duration of customer visits are going to be related to overall sales. The initial business opportunity here is: How do you ensure new games drive revenue? There are many other business opportunities, like what is the optimal menu for the customer-base and do seasonal variations of offerings help the business? For now,  let's focus on ensuring that new games drive revenue for this example.
 
As part of this stage you would talk with your friend, her employees and some customers to do your best to fully understand the experience of the customer. The important thing here is to spend time on-site simulating the experience of a customer to obtain as genuine an understanding of the problem as possible. You may realize that most customers are there to work or most of them are just passing through. This domain knowledge is useful when making decisions like which new types of new games to create.
 
 After you have gathered your information and studied it you will generally articulate the business scenario using a scientific thought process—this means a statement that can be tested. The business opportunity should be stated in a way that minimizes the presence of confounding factors.

There are logical follow-up questions to ask to fully understand the problem, but the next two stages are the more appropriate places to get into these details. Now that you understand the problem it is time to gather the data.

HINT:  This is the stage where we gather all of the data and we make note of what would be ideal data.  

The data here are mostly sales and customer profiles. There are two important aspects of the data that would be ideal:

The data are at a transaction level (each purchase and its associated data are recorded)
We can associate game usage with transactions.
Fortunately for us this is a modern cafe so customers order and play games through the same interface. Additionally, they are incentivized to login to the system and generate a customer profile. In this stage we go through the process of gathering the raw data. This may involve querying a database, gathering files, web-scraping and other mechanisms. It is important to gather all of the relevant data in this stage, because access and quality of the data may force you to modify the business question. It is very difficult to assess the quality of data when it is not in hand. If possible, efforts should be made to collect even marginally related data.

Lets assume that your initial investigation led you to understand that games that used quotations from the books in an interactive way were the most effective. So you have come up with the idea to develop a game that is built on a chatbot that has been trained to talk like Sherlock. This would involve Natural Language Processing (NLP) and we would need a corpus of textual data. As a start you might download The Adventures of Sherlock Holmes, by Arthur Conan Doyle from Project Gutenberg.





### Define
This is the data wrangling stage

Given the data, an understanding of the business scenario and your gathered domain knowledge you will next perform your data cleaning and preliminary exploratory data analysis. To get to the point of preliminary investigation into the findings from the empathize stage it is frequently the case that we need to clean our data.

This could involve parsing JSON, manipulating SQL queries, reading CSV, cleaning a corpus of text, sifting through images, and so much more. One common goal of this part of the process is the creation of one or more pandas dataframes or NumPy arrays that will be used for initial exploratory data analysis (EDA).  



EDA: Exploratory Data Analysis
Exploratory data analysis (EDA) is the process of analyzing data sets to create summaries and visualizations of the data. These summaries and visualizations are then used to guide the use of the data for solving business challenges.  
If we continue with the book example we could first read the data back in  




### Ideate
This is the stage where we modify our data and our features

Now that you have clean data the data processing must continue until you are ready to input your data into a model. This stage contains all of the possible data manipulations you might perform before modeling. Perhaps the data need to be log transformed, standardized, reduced in dimensionality, kernel transformed, engineered to contain more features or transformed in some other way.

For our text data we would likely want to dig into the sentences themselves to make sure they fit the desired use case. If we were building a chatbot to engage with in a very Holmes manner then we would likely want to remove any sentences that were not said by Mr. Holmes, but his name was mentioned. If we were building a predictive model to determine which story a phrase would most likely have been generated, we would need to create a new column in our data frame representing the books themselves.

When working with text data many models that we might consider prefer a numeric representation of the data. This may be occurrences, frequencies, or another transformation of the original data. It is in this stage that these types of transformations are readied or carried out. For example here we import the necessary transformers for usage in the next stage.  
    There are a lot of ways to prepare data for different models. In some case you will not know the best transformation or series of transformations until you have run the different models and made a comparison. The concept of pipelines is extremely useful for iterating over different permutations of transformers and models. The following topics will be covered in detail during Module 3.

Unsupervised learning
Feature engineering
Dimension Reduction
Simulation
Missing value imputation
Outlier detection
HINT:  This is the stage where we enumerate the advantages and disadvantages of the possible modeling solutions  

Once the transformations are carried or staged as part of some pipeline it is a valuable exercise to document what you know about the process so far. The form that this most commonly takes is a table of possible modeling strategies complete with the advantages and disadvantages of each.  

### Prototype
This is the modeling stage

The data have been cleaned, processed and staged (ideally in a pipeline) for modeling. The modeling (classic statistics and machine learning) is the bread and butter of data science. This is the stage where most data scientists want to spend the majority of their time. It is where you will interface with the most intriguing aspects of this discipline.  

To illustrate the process to the end shown below is a Support Vector Machine with Stochastic gradient decent as a model. The process involves the use of a train-test split and a pipeline because we want you to be exposed from the very beginning of this course with best practices. Given this example we also see that there can be considerable overlap between the ideate and prototype stages. The overlap exists because transformations of data are generally specific to models–as you will explore which model fits the situation best you will be modifying the transformations of your data.  

1234567891011121314151617
from sklearn.linear_model import SGDClassifier
from sklearn.model_selection import train_test_split

carry out the train test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

from sklearn.linear_model import SGDClassifier
text_clf = Pipeline([
    ('vect', CountVectorizer()),
    ('tfidf', TfidfTransformer()),

### Testing
This is the production, testing and feedback loop stage

The model works and there are evaluation metrics to provide insight into how well it works. However, the process does not end here. Perhaps the model runs, but it is not yet in production or maybe you want to try different models and/or transformers. Once in production you might want to run some tests to determine if it will handle load or if it will scale well as the data grows. A working model with an impressive f-score does not mean it will be effective in practice. This stage is dedicated to all of the considerations that come after the initial modeling is carried out.  

It is also the stage where you will determine how best to iterate. Design thinking like data science is an iterative process. Our model performed very well (see below), possibly because Dr. Holmes and Dr. Watson are described in very different ways in the stories, but it could be something else.  

1234567
from sklearn import metrics

### evaluate the model performance
predicted = text_clf.predict(X_test)

print(metrics.classification_report(y_test, predicted,
      target_names=['sherlock','watson']))
12345678
                precision    recall  f1-score   support

    sherlock       0.96      1.00      0.98       150
      watson       1.00      0.83      0.91        36

    accuracy                           0.97       186
   macro avg       0.98      0.92      0.94       186
weighted avg       0.97      0.97      0.97       186
As a scientist you always want to remain skeptical about your findings until you have multiple ways to corroborate them. You will also want to always be aware of the overall goal of why you are doing the work you are doing. This example is an interesting metaphor for what can happen as a data scientist. It is possible to go down a path that may only marginally be related to the central business question. Developing a game here is not unlike using a new model for deep-learning or incorporating a new technology into your workflow—it may be fun and it may to some degree help the business case, but you need to always ask yourself is this the best way for me or my team to address the business problem? The questions your ask here are going to guide how best to iterate on the entire workflow.  
    


