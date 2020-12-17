


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
    


# 4. Data Collection Objectives
Throughout these units you will learn or reinforce what you already know about identifying and articulating business opportunities. In this module you will learn the importance of applying a scientific thought process to the task of understanding the business use case. This process has many similarities to that of being an investigator. You will also acquire a healthy respect for the need to pause, step back and think scientifically about the main processes in this stage.  

Empathize Process
1.  Get as close to the source of data as possible usually by interviewing the people involved
2.  Identify the business problem
3.  Obtain all of the relevant the data
4.  Translate the business problem into a testable hypothesis or hypotheses
As we have seen, there are several viable processes for conducting data science, but none omit the important step of understanding the needs of the business. To take it a step further, we set out the expectation that the process be viewed through the lens of scientific thinking. It is this practice that allows valuable time and resources to be conserved.  





# 5. Identifying the Business Opportunity: Through the Eyes of our Working Example

### Articulate the business question
There are generally many business questions that can be derived from a given situation. It is an important thought exercise to enumerate the possible questions, that way it makes the discussion easier when you work with the involved stakeholders in order to focus and prioritize. In this situation here are some ways of articulating the business case.

Can we use marketing to reduce the rate of churn?
Can we salvage the Singapore market with new products?
Are there factors outside of our influence that caused the situation in Singapore and is it temporary?
Can we identify the underlying variables in Singapore that are related to churn and can we use the knowledge to remedy the situations?
The business problem in all of these examples is written shown in terms of the data we have.

NOTE:  This case study can be approached in many different ways and there may not be a clear right or wrong. During the various modules of this course, we will provide guidance when there are multiple paths to choose from.

### Prioritize
It is logical, but there is a need to prioritize If there are several distinct business objectives. In this case maybe one is related to reducing churn directly and another is about profitability.

There are three major contributing factors when it comes to priority.

Stakeholder or domain expert opinion
In situations where considerable domain expertise is required to effectively prioritize (e.g. Physics, Medicine and Finance) prioritization will likely be driven by the people closest to the domain.

### Feasibility
Do we have the necessary data to address the business questions?
Do we have clean enough data to address the business questions?
Do we have the technology infrastructure to deploy a solution once the data are modeled?
Impact
When looking at Impact we’re purely looking at expected dollar contribution and added value from a monetary perspective. When possible, calculating the back-of-the-envelope ROI is a crucial step that you can do. This is an expectation and not a real ROI calculation, but it can serve as a guiding principle nonetheless.

The ROI calculation should be an expected dollar value that you can generate based on all available information you currently have in your organization combined with any domain insight you can collect.

### Measuring the back-of-the-envelope ROI calculation could make use of any of the following:

Estimates for fully-loaded salaries of employees involved
Cost per unit item and/or time required to produce
Number of customers, clients, or users
Revenue and more




# 6. Scientific Thinking for Business:


Science is a process and the route to solving problems is not always direct
A common argument made by statisticians and mathematicians is that data science is not really a science. This is untrue, mainly because data science involves a lot of investigations through sometimes chaotic data sets, in search of meaningful patterns that might help in solving particular problems.

Since data science implies a scientific approach, it is important that all data scientists learn to adopt and use a scientific thought process. A scientific thought process of observation, developing hypotheses, testing hypotheses, and modifying hypotheses is critical to your success as a data scientist.

Pulling in data and jumping right into exploratory data analysis can make your work prone to exactly the types of negative issues that plague data science today. There are a number of well-discussed issues revolving around data science and data science teams not living up to promised potential.

At the heart of this problem is the process of communicating results to leadership. It should begin with a meaningful and well-articulated business opportunity. If that opportunity is stated too simply, as say, increasing overall revenue then the central talking point for communication is too vague to be meaningful from the data side.

#### The business scenario needs to be communicated in a couple of ways:
1.  Stated in a testable way in terms of data
2.  Stated in a clear way that minimizes the influence of confounding factors

#### Testable hypotheses
There is no one single best way to articulate a business opportunity as a testable hypothesis. In some cases the statement will be intuitive, but in other cases there will be some back and forth with stakeholders and domain experts.

#### Guidelines for creating testable hypotheses
Become a scientist of the business
Spend a little bit less time learning new algorithms and Python packages and more time learning the levers that make your specific business go up or down and the variables that impact those levers.

#### Make an effort to understand how the data are produced
If it comes down to it, sources of variation can be explicitly accounted for in many types of models. If the data come from a database you should ask about the process by which the data are stored. If the data are compiled by another person then dig into the details and find out about the compiling process as well as the details of what happened before the data arrived on their desk.

#### Make yourself part of the business
Do not under any circumstances become siloed. Proactively get involved with the business unit as a partner, not a support function.

#### Think about how to measure success
When thinking about what course of action might be most appropriate, keep at the forefront of your mind how you will measure business value when said action is complete.

IMPORTANT:  Data Science is NOT Business Intelligence. BI analysts serve to derive business insights out of data. There is without a doubt some overlap, but the job of a data scientist is to investigate the business opportunity and solve it.  

There is a balancing act to maintain between directly addressing the business need and ensuring that you have thoughtfully studied the problem enough to ensure that you can account for most of the likely contingencies. The scientific method can be of some guidance here.

#### Thinking scientifically about the business scenario
A major goal of this process is to make the business objectives clear to leadership. Some of these individuals are technical and some are not, so as a good rule-of-thumb get in the habit of articulating the business problem at a level that everyone can understand. Stakeholders and leadership need to know what you are trying to accomplish before you begin work. They also need to be aware from the start what success would look like. Science is an iterative process and many experiments produce results that some might consider a failure. However, experiments that are properly setup will not fail no matter the result–the result may not useful but you have gained valuable information along the way.

Experiments in this context could refer to an actual scientific experiment (e.g. A/B testing) or it could be more subtle. Let’s say you work for a company that collects tolls in an automated way, and you want to identify the make and model of each car in order to modify pricing models based on predicted vehicle weight. After talking with the stakeholders and the folks who implemented the image storage solution you are ready to begin. The experiment here has to do with how you begin. You may think that there is enough training data to implement a huge multi-class model and just solve most of the problem. If you approach it that way then you are hypothesizing that the solution will work.

For those of you who have done much image analysis work, you could guess that approach would likely result in a significant loss of time. If we take a step back and think scientifically, we could approach the solution from an evidence driven perspective. Before investing a significant amount of time you may try to see if you can distinguish one make and model from the rest before adding more classes. You may want to first pipe the images through an image segmentation algorithm to identify the make of the car. There are many possible ways to build towards a comprehensive solution, but it is important to determine if either of these piecemeal approaches would have any immediate business value.

This might be a good time for a reminder about the steps in the scientific method.

#### The Scientific Method
It is the process by which science is carried out. The general idea is to build on previous knowledge to in order to improve an understanding of a given topic. 

Formulate the question
Generate a hypothesis to address the question
Make a prediction
Conduct an experiment
Analyze the data and draw a conclusion
We will continue with an interactive example, but first it is important to note that Scientific experiments must be repeatable in order to become reliable evidence. 

#### Question
The question can be open-ended and generally it summarizes your business opportunity. Let’s say you work for a small business that manufactures sleds and other winter gear and you are not sure which cities to build your next retail locations. You have heard that Utah, Colorado and Vermont are all states that have high rates of snowfall, but it is unclear which one has the highest rate of snowfall.

#### Hypothesis
Because the Rocky mountains are higher in elevation and they are well-known for fresh powder on their ski slopes, you hypothesize that both Utah and Colorado have more snow than Vermont.

#### Prediction
If you were to run a hypothesis test, you would find that Vermont has significantly less snow fall than Colorado or Utah

#### Experiment
You hit the NOAA weather API to get average annual snowfall by city. We have compiled these data for you in snowfall.csv. 


#### Analyze
There is not enough data to do a 1-way ANOVA. The experiment is not a failure; it has a few pieces of information.

There is not enough data
There is a small possibility that VT gets more snow on average than either CO or UT
Our degree of belief in the conclusion drawn from (2) is very small because of (1)
The notion of degree of belief is central to scientific thinking. It is somehow a part of our human nature to believe statements that have little to no supporting evidence. In science the word belief, with respect to a hypothesis is proportional to the evidence. With more evidence available, ideally, from repeated experiments, one’s degree of belief should change. Evidence is derived from the process described above and if we have none then we are stuck at the question stage and a proper scientific hypothesiscannot be made.

The other important side to degree of belief is that it never caps out at 100 percent certainty. Some hypotheses have become laws like Newton’s Law of Gravitation, but most natural phenomena in the world outside of physics cannot be explained as a law.

A hypothesis is the simplest explanation of a phenomenon. A scientific theory is an in-depth explanation of the observed phenomenon. Do not be mistaken with the word theory, there can be sufficient evidence that your degree of belief all but touches 100%, and is plenty for decision making purposes. A built-in safeguard for scientific thought is that our degree of belief does not reach 100%, which leaves some room to find new evidence that could move the dial in the other direction.

There are additional factors like external peer review that help ensure the integrity of the scientific method and in the case of implementing a model for a specific business task this could mean assigning reviewers for a pull request or simply asking other qualified individuals to check over your work.
