


+ **[AI Workflow: Business Priorities and Data Ingestion](https://www.coursera.org/learn/ibm-ai-workflow-business-priorities-data-ingestion?specialization=ibm-ai-workflow)**

# Exploratory data analysis:

- provide summary level insight in a dataset.
- uncover underlying pattern and structure in a dataset. 
- uncover , missing , outlier ,  class imbalance and data related issues.
- relate the available data  to the bussiness opputunity or opputunities.
- tootls to be used are visusalizing tools , summary tables and hypothesis tesing .




# Why is Exploratory Data Analysis Necessary?
Exploratory Data Analysis (EDA) is a de-facto standard part of the data science workflow. The goals of this part of the process vary with the given data and business opportunity, but in general practitioners use visualization tools, tabular summaries and hypothesis testing in order to:

Provide summary level insight into a data set
Uncover underlying patterns and structure in the data
Identify outliers, missing data and class balance issues
Carry out quality control checks
Let’s use a movie example to help explain why this part of the process is so important.

Imagine you are part of a group of friends who decide to go to a movie with an unfamiliar title. This decision will likely lead the friends to ask a lot of questions. To get some answers they might learn about the cast, the crew, the reviews. It turns out review website Rotten Tomatoes has already done much of this EDA for you. It provides summary statistics, production shots and a link to the trailer. It goes without saying that these visuals will factor heavily into how you perceive the yet unseen film.

The movie analogy has similarities to the AI workflow. Before committing to a modeling procedure (in this case the movie), which is generally time-consuming, you will explore some of the evidence that is available to support such a decision. Some models can be created and deployed in less than an hour, but others can consume days, weeks or possibly more of your time. If the next movie you wanted to go see was the first in a lengthy trilogy you might invest even more time exploring.

The time spent on a project is a part of the investment a company makes to pursue a business opportunity. EDA serves to maximize the efficiency of your overall time spent on a project. We will use IBM Watson studio and other state-of-the art tools to formalize the investigation of business opportunities. At the end of this stage it will be time to communicate your findings to business stakeholders. Communicating your findings is a step that is just as important as the EDA itself.

#### Important:  For some business opportunities, a sound solution can be easily identified through thoughtful data visualization. Models are not always a part of the AI workflow.

Data scientists are largely familiar with EDA, its benefits and its place in the overall AI workflow, but this is one part of the workflow that will always have room for improvement. Data visualization and results communication are both analogous to downhill skiing—in just a few tries you can obtain the minimum level of proficiency, but it takes many years to become an expert. One challenge on the road to proficiency is the many options in how data can be visualized and similarly how results can be communicated. The general procedure for EDA has several aspects that are consistent despite the variation.  








# Example EDA Process
1. Load data into pandas, NumPy or another similar tool and summarize the data
2. Use tables, text and visualizations to tell the story that relates the business opportunity to the data
3. Identify a strategy to deal with missing values
4. Investigate the data and underlying business scenario with visualizations and hypothesis testing
5. Communicate your findings




# Data Visualization:

- what you have done. 
- what are you doing. 
- what you plan to do.  

during the  "THE DESIGN THINKING PROCESS"

Your other team members are working with AAVAIL team members on the Empathize phase of their design thinking process. They are gathering data and facts related to AAVAIL’s business challenges and will be presenting that to everyone in a playback after it is summarized.

#### Your data visualization deliverables will become an important part of a playback! It is part of one of the key principles of design thinking:
Observation and Reflection.

IMPORTANT:  For some business opportunities, a sound solution can be easily identified through thoughtful data visualization. Models are not always a part of the AI workflow.


# Some popular libraries :

- Bokeh  -  Bokeh supports streaming, real-time data and is used to create interactive, web-ready plots, which can output as JSON objects, HTML documents, or interactive web applications.

- plotly  -  While plotly is widely known as an online platform for data visualization, it can be accessed from a Python notebook. Like Bokeh, Plotly’s strength lies in making interactive plots, and it offers some charts not found in most libraries, like contour plots.

- dash  -  Dash is Python framework for building web applications. It built on top of Flask, Plotly.js, React and React Js. It enables you to build dashboards using pure Python.

- ggplot  -  ggplot is a Python visualization library based on R’s ggplot2 and the Grammar of Graphics. It lets you construct plots using high-level grammar without thinking about the implementation details.

- folium  -  Based on leaflet.js, it is a great tool for working with geographic data for example choropleth visualizations.

- Analytics dashboard in IBM Watson Studio  -  You can build sophisticated visualizations of your analytics results, communicate the insights that you’ve discovered in your data on the dashboard and then share the dashboard with others.







# Missing Data: Introduction
Exploratory data analysis is mostly about gaining insight through visualization and hypothesis testing. Recall from the beginning of this unit that the ETL process is useful for holding the data to a minimum standard with respect to quality assurance. This unit deals with the imputation of missing values and it is where EDA and ETL meet. Missing value imputation could exist as part of the ETL process, but it is not often clear which strategy is the best until we can make comparisons. The comparisons are best made by evaluating model performance using a hold-out data set. One missing value strategy may be better for some models, but for others another strategy may show better predictive performance.  


Our Story
Missing data is a common problem in most real-world scientific datasets. While the best way for dealing with missing data will always be preventing the occurrence in the first place, it will still remain a problem. Sometimes data is collected from sensors that fail to record or data collection is distributed across individuals and the merged data does not harmonize well. There are a variety of ways for dealing with missing data, from more simplistic to very sophisticated, but a standard metric by which we measure utility will still be model performance.

This module is focused on ensuring that you are aware of how to deal with missing values and the consequences that arise from deciding how they are dealt with. At AAVAIL and nearly all companies with accumulated data there eventually you will encounter missing values and the actions you take at this stage of the overall workflow can heavily influence the downstream business of your models utility.


THE DESIGN THINKING PROCESS
This unit relates to the Empathize phase of their design thinking process. Discuss with your colleagues to ensure that you understand why data are missing. It is not enough to systematically deal with missing values in the same way for every dataset you encounter. Significant model performance improvements can be achieved by leveraging discussions with with those close to the data generation process.

Introduction to Missing Values:


## Flag missing values
One strategy for accounting for missing values is to simply ignore them. This is usually not a good idea because you often have little insight into how the missing data influenced the results.

### Many machine learning models require a feature matrix that does not have missing values. At a minimum, you may need to convert missing elements to a flag that can be ingested by the model. For example, when dealing with missing values in a column of categorical data, an option is to treat “missing” as one of the categories for the model to train on. In such a scenario, it is important to follow the standard practice of “dummifying” the categorical variable, such as with Pandas’ get_dummies method.

### Converting a numerical missing value to a flag to denote that it is missing is generally not good practice, because the choice of the value of the flag will have implications on how your model treats such data. It is usually best to use an imputation technique, such as those discussed below. The fact that a value was missing may be useful to track. You can do so even when you have imputed a replacement value, by adding a new column to the dataset that flags whether values from the newly complete column were originally missing.

##Complete case analysis
The opposite strategy from tracking all your missing values is to delete either rows (observations) or columns (features), from your training data. In the case of deleting rows, this is called complete case analysis, and is quite common.

Complete case analysis can lead to undesirable results, but the degree to which it does depends on the category of missingness. The categories of missingness are detailed in the following sections.

If you plan to use a predictive model on the data that you have, you will still need a plan to account for missing values. Complete case models in training can yield additional problems in the future. Sometimes complete-case analysis is used as a first pass through the workflow.



## Categories of Missing Data
The categories of "missingness" can have important implications for statistical bias and power. The three categories of missing data are:

### Missing completely at random or MCAR:
When data are MCAR, missing cases are, on average, identical to non-missing cases, with respect to the feature matrix. Complete case analysis will reduce the power of the analysis, but will not affect bias.
### Missing at random or MAR:
When data are MAR the missing data often have some dependence on measured values, and models can be used to help impute what the likely data would be. For example, in a Major League Baseball (MLB) survey, there might be a disproportionate number of male respondents completing all of the questions as compared to females, since males comprise most of the MLB's viewership.
### Missing not at random or MNAR:
In this case the missing data depend on unmeasured or unknown variables. There is no information available to account for the missingness.

- Of these three categories, the best case scenario is that the data are MCAR. It should be noted that imputing values under the other two types of missingness can result in an increase in bias. Many strategies have been proposed for the management and replacement of missing values—a process known as imputation. In this unit we will illustrate the method of simple imputation, as well as two more sophisticated strategies: Multiple imputation and Bayesian imputation. In the case study that follows we will also exemplify the iterative process for deciding which strategy is best.






-----------------------------
# SUMMARY :
-----------------------------
## Exploratory Data Analysis
##### The main goals of EDA are:

Provide summary level insight into a data set
Uncover underlying patterns and structure in the data
Identify outliers, missing data and class balance issues
Carry out quality control checks
The principal steps in the process of EDA are:
Summarize the data - Generally done using dataframes in R or Python
Tell the Story - Summarize the details of what connects the dataset to the business opportunity
Deal with missing data - Identify the strategy for dealing with missing data
Investigate - Using data visualization and hypothesis testing delve into the relationship between the dataset and the business opportunity
Communicate - Communicate the findings from the above steps


## Data visualization

Jupyter notebooks in combination with pandas and simple plots are the basis for modern EDA when using Python as a principal language.

### Advantages of Jupyter notebooks:

They are portable: They can be used locally on private servers, public cloud, and as part of IBM Watson Studio.
They work with dozens of languages.
They mix markdown with executable code in a way that works naturally with storytelling and investigation.
matplotlib and its child libraries like seaborn are the core of the Python data visualization landscape.
pandas and specifically the dataframe class works naturally with Jupyter, matplotlib and downstream modeling frameworks like sk-learn.

### EDA and Data Visualization best practices

The majority of code for any data science project should be contained within text files. This is a software engineering best practice that ensures re-usability, allows for unit testing and works naturally with version control. In Python the text files can be executable scripts, modules, a full Python package or some combination of these.
Keep a record of plots and visualization code that you create. It is difficult to remember all of the details of how visualizations were created. Extracting the visualization code to a specific place will ensure that similar plots for future projects will be quick to create.
Use you plots as a quality assurance tool. Given what you know about the data it can be useful to make an educated guess before you execute the cell or run the script. This habit is surprisingly useful for quality assurance of both data and code.

## Missing values

Dealing with missing data sits at the intersection of EDA and data ingestion in the AI enterprise workflow.
Ignoring missing data may have unintended consequences in terms of model performance that may not be easy to detect.
Removing either complete rows or columns in a feature matrix that contain missing values is called complete case analysis.
Complete case analysis, although commonly used, can lead to undesirable results. The category or categories of missingness present in the data can significantly impact the quality of these results. 

### The categories of missingness are:

Missing completely at random or MCAR.
Missing at random or MAR.
Missing not at random or MNAR.

The best case scenario is that the data are MCAR. It should be noted that imputing values under the other two types of missingness can result in an increase in bias.
In statistics the process of replacing missing data with substituted values is known as imputation
It is a common practice to perform multiple imputations
The practice of imputing missing values introduces uncertainty into the results of a data science project
One way to deal with that additional uncertainty is to try a range of different values for imputation and measure how the results vary between each set of imputations. This technique is known as multiple imputation

### Bayesian Imputation
While missing values are usually handled prior to the modeling phase of a data science project, it is worth noting an exception where missing values can be handled automatically as part of the modeling process. This is is the case when a model is treated in a fully Bayesian way, that is priors are used to govern parameters of the model. Then Expectation-Maximization, Markov Chain Monte Carlo (MCMC) or another method of inference can be use to infer both the parameters, hyper-parameters and missing values.

##### See the following resources to learn more.

1. PyMC3  -  package for probabilistic programming in Python.

2. TensorFlow Probability  -  another package for Python that enables the Bayesian treatment of models

3. PyMC3 Getting Started  - continue on to Case Study 2 to see how missing values are automatically imputed during inference





## CASE STUDY: Data visualization: 
It can be easy to get lost in the details of the findings when communicating the finding from EDA to business stakeholders. Project planning and milestones are important so remember to talk about what you:

Have done.
Are doing.
And plan to do.
Remember that deliverables are generally a presentation or a report and they should use a portable format (e.g. PDF or HTML).
Deliverables should be concise and clear. Appendices are useful as supplemental materials to a deliverable and they help keep them free of unnecessary items.
Visual summaries are a key component of EDA deliverables.
There is no single right way to communicate EDA, but a minimum bar is that the data summaries, key findings, investigative process, conclusions are made clear
 