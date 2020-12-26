


+ **[AI Workflow: Business Priorities and Data Ingestion](https://www.coursera.org/learn/ibm-ai-workflow-business-priorities-data-ingestion?specialization=ibm-ai-workflow)**


# The dataset
The original dataset is the classical titanic dataset. We have taken the liberty to modify some of the features to mimic a dataset that more aligns with the AAVAIL company. Let’s us walk through the whole process of creating a dashboard as an investigative. AAVAIL gave away free trials in three separate markets (corresponding to the ports where passengers embarked). For each passanger there are a number of features. Here survival indicates whether or not a customer made it to point of becoming a paid subscriber.
----------------------------------------------------------------------------------------
Customer Id: Unique id given to each customer
Is_Subscribed: If a customer is subscribed or not.
Tier of Free Trial: There are 3 tiers of free trial, 1st, 2nd and 3rd.
Name
Sex
Age
The Subscribtion number
The Market: This describes three possible markets that the free trial was carried out in. Three possible values S,C,Q

-------------------------------------------------------------------------------------------

## Types of features
Categorical  -  Tier_Free_Trial, Sex, Market, Is_Subscribed
Continuous  -  Age, Customer Id, Subscription_Number
Alphanumeric  -  Name
Let’s load the dataset in IBM Watson Studio.  Download the aavail-customer-data.csv file below to get started:

aavail-customer-data.csv


## Data summary
Once summarized you can make the following observations:

There are a total of 891 customers in our training dataset.
Since the Is_Subscribed column has discrete data, the mean gives us the number of people survived from 891 i.e. 38%.
Most people belonged to Tier_Free_Trial = 3

### Taking a look at our categorical features we find that:

Most of the subscribed customers were men.
Market has three possible values with most customers having maximum number of streams.
Names of all customers are unique.
Building dashboards
The AAVAIL dataset provides observations for each customer and subscribers outcome. The problem statement entails predicting whether a customer would be subscriber or not given the features such as customers, market, gender, age, number of streams, Is_Subscribed and others. In this dashboard we will be analyzing each of the stated features with respect to Is_Subscribed outcome based on the training dataset. Analyses based on data visualization can be an effective tool to provide insight into conditional probability relationships between features and the outcome variable.

Now that we have our observations, let’s create a simple dashboard on the IBM Watson Studio. To create the IBM Watson Dashboards follow the instructions in here:  https://developer.ibm.com/tutorials/create-interactive-dashboards-on-watson-studio/.

The first visualization we will be creating is to calculate the subscriber percentage and subscriber vs free trial.


We can see from the above analysis that the subscriber percentage is 38.4% and non subscriber percentage is 61.6%.

Now let’s look at the subscriber rate for Tier_Free_Trial.


The analysis above shows that 63% customers are from tier 1, 47% from tier 2 and 24% from tier 3 are subscribed out of the total customers. It seems that the customers that embarked from a particular market had a higher rate of subscription at 55%. Let’s move forward to see some more data analysis.


The analysis above shows that the free tier percentage subscribed for a market and the Subscriber_percentage is 35%, 54%, 46%, 25%, 17% respectively. Looks like customers who had either tier 1, 2 or 3 had a higher possibility of subscribing than the ones who had none. However, having more than 3 made the possibility even lesser.


The analysis above shows that from the customers with tier 1, out of 94, 91 female customers subscribed. In the customer tier 2, out of 152 female customers only 70 subscribed and in tier 3 out of 432 female customers only 72 subscribed. For the male customers in tier 1 out of 1,041 only 47 subscribed, in tier 2 out of 122, 45 subscribed and in tier 3 out of 216 only 17 subscribed.

### Summary of Findings
The bar plots show the relationship between:

median subscription, gender and subscriber outcome
age/gender and subscriber outcome
This simple dashboard demonstrate that features such as subscribed, age and gender can play critical roles in determining the subscriber outcome. Additionally, the features such as Tier_Free_Trial, streams and market can also influence the subscriber outcome. The dashboard from this tutorial can be found here.


# Overview
Estimation and hypothesis testing build upon probability. Specifically, they are built on probability distributions, which in turn depend on the concept of random variables and this unit assumes you are familiar with these topics.

Khan Academy resource on random variables and distributions

Scientists use statistical models to make general statements about real-world observations. Many types of data collected from many different sources often follow recognizable patterns. For example, many of the measurable things in our world (e.g., IQ scores) follow a normal or Gaussian distribution.

When data are observed to follow probability distributions, and the data were collected in a way that maximizes the chances that they are representative of the larger population from which they were taken, it is possible to make estimates about the properties of that population.

Making inferences about some population by matching a sample of data with a probability distribution and estimating its parameters requires that the sample meet certain criteria. Specifically, you should have reason to believe that:

- the data follow the chosen type of distribution, and
- each point is independent and identically distributed (IID).

- That is, the data were collected in a way that makes it likely that each data point is statistically independent from every other one, and each was drawn from a distribution with identical parameters. The nuances of how to collect data in ways that maximize the chances that your dataset satisfy these criteria are referred to as sampling techniques and fall outside the scope of this course.

Assuming you have a dataset that can be reasonably parameterized with a probability distribution, the process of estimating those parameters, also known as statistical inference is relatively straightforward.


## Notes :

- sttistical infernence has :
1. Population : set of similar events or items , which are intersting for us to answere a particular question or experiments .it is difficult to gain access to the population

2. Sample :  SO we take the help of sample distribution , and random sampling to get good represtation  of the population , so when we collect data , we make sure that they follow pariticular distribution , so as to estimate the parametrs of the original population.

3. statistics of the sample distribution.

4. parametrs of the sample distribution.


# Statistical Inference
In the previous video there is a example fitting a distribution and using that fit to make probability statements. Although simple, this is a powerful tool at your disposal to communicate important aspects of the data. This concept can be extended to conditional probability statements as well.

We also introduce the notion of the bootstrap as a tool to provide confidence intervals around an estimate. The notion of confidence in an estimate is extended in Bayesian estimation example. An analytical solutions. approach is used in the example via a conjugate prior. This A/B testing example when viewed through the Bayesian lens is closely related to solutions to the multi-armed bandit problem.

To learn more about Bayesian solutions th multi-armed bandit problem



# Two-sample independent t-test
In this example we are interested in comparing the amount of time elapsed between a client request and stream availability for the company AAVAIL’s streaming servers. Specifically we want to compare our locally hosted servers to a cloud service in terms of speed. The data are arrival times (in seconds) for a stream, meaning the time it takes from submission to receive a link with the modified version of the stream.

Remember to formalize your hypothesis.

Pose your question - Is it faster, on average, to process streams for viewing on a cloud service compared to our locally hosted servers?
Find the relevant population - The population consists of all possible streams
Specify a null hypothesis - There is no difference, on average, between local and hosted services for stream processing times location after I submit my ride request.
Select the test and the significance level, two-sample independent t-test with α=0.05



# Unequal variances t-test
The use of a Student’s t-distribution, accounts for a specific bias that the Gaussian distribution does not, because it has heavier tails.

The t-distribution always has mean 0 and variance 1, and has one parameter, the degrees of freedom. Smaller degrees of freedom have heavier tails, with the distribution becoming more and more normal as the degrees of freedom gets larger.

The default version of a Student’s t-test assumes that the sample sizes and variances of your two samples are equal. In the case of our arrival times above we cannot state that the variances of the two samples are suppose to be the same. The unequal variances t-test, also called Welch’s t-test is a more appropriate variant of the t-test for this example.

There are many variants of the t-test and depending on the field of study some have different names for the same variant. The unequal variances t-test in Python can be accessed with the equal_var keyword argument.


# One-way Analysis of Variance (ANOVA)
The previous scenarios have been concerned with distinguishing between a sample and a baseline, and between two samples. Suppose you want 
to distinguish between three or more samples, that is your data fall into three-plus categories and you want to establish whether there is
a difference in outcomes based on those categories.

If AAVAIL wanted to run the performance tests from the previous example comparing several cloud providers and several architectures then an ANOVA would be more appropriate here.

  

# p-value Limitations
Because science has for many decades been using p-values to confirm novel experimental results, trends of p-value misuse have also emerged. Scientific journals, traditional new outlets and a to a lesser extent data science product managers have at least one thing in common—they all need new and exciting findings.

A p-value is the probability of finding the observed, or more extreme, results when the null hypothesis (H-zero) of a study question is true.

In other words it is a tool to quantify the evidence against the null hypothesis. The null hypothesis is rejected when this evidence is under some predefined, but arbitrarily defined threshold. It turns out there are many ways to modify the data get the value under the threshold.

If we re-run the experiment multiple times changing the features until we arrive at the best p-value
If we go back and collect a few more samples to get the p-value just over the threshold
If we remove one or more outliers to ensure that the p-value is smaller
If we set the level of alpha after the hypothesis has been tested
These scenarios and a number of others are known as p-value hacking and they are carried out because there is a push in academia and in business for novel and impactful findings. If we return to the core idea of degree of belief from the module on scientific thinking then the notion of reproducibility should outweigh the importance of novelty.

In the A/B testing example with two different versions of a website, we used different p-values as an investigative tool, not as specific number to base decisions on or draw conclusions from. We also showed another powerful tool that does not use p-values at all, that is the posterior distribution. The degree of belief for that experiment was quantified as the posterior distribution, which is a far more informative tool for decision making than the p-value itself. Viable alternatives to p-values exist through the use of Bayes Factors and Posterior Predictive Checks.

The important thing to remember is that p-values themselves are not a source of ground truth, but they are nonetheless quite useful if used appropriately. If the testing of a specific model is business critical then it might be worth taking the time to test the ideas within a Bayesian framework. This can give you more confidence in your conclusions for a given experiment, but whether it is Bayesian or frequentist treatment of the experiment the study still needs to be repeated with newly collected data to ensure reproducibility.

Additional resources
Wiki article on Data Dredging
An interactive tool that illustrates p-hacking
Bayesian Estimation instead of a T-Test
Bayes Factors in PyMC3
Posterior Predictive Checks PyMC3
Nature Methods article about interpreting *p*-values



# Multiple Testing
It was mentioned in the p-value limitations unit that running more than one test at a time, on the same data is an example of p-value hacking. This is because there is an expected false positive rate for running one test, and if we run multiple tests say using different combinations of features this expected rate should be higher.

Bonferroni Correction
The Bonferroni Correction is a simple way to rectify the over testing issue.

Suppose we want to test a combined hypothesis as a threshold of α. The Bonferroni correction procedure then tests each of the individual hypotheses at a threshold of:


This type of adjustment for dealing with multiple testing was popular for some time, but today when the number of tests can scale into the hundreds or thousands the method has become less widely used when compared to other methods.

Other methods to correct for multiple tests
The Bonferroni Correction is probably the simplest way to avoid increasing your false positive rate when running several tests at once. You simply divide your threshold by the number of tests you are running. This conservative method does penalize potentially significant results, so there is an increase in false negatives. This may necessitate considering alternative ways of dealing with multiple tests.

Note:  If we have a data set with 1000 observations and we repeat a t-test for each observation then (with α=0.05) we can expect 50 observation to be found significant purely by random chance.

A bonferroni Correction in the above example is likely too conservative. Fortunately, there are a number of other methods that have been developed.

The statsmodels library in Python has the following methods in the multipletests submodule:

1. bonferroni : one-step correction
2. sidak : one-step correction
3. holm-sidak : step down method using Sidak adjustments
4. holm : step-down method using Bonferroni adjustments
5. simes-hochberg : step-up method (independent)
6. hommel : closed method based on Simes tests (non-negative)
7. fdr_bh : Benjamini/Hochberg (non-negative)
8. fdr_by : Benjamini/Yekutieli (negative)
9. fdr_tsbh : two stage fdr correction (non-negative)
10. fdr_tsbky : two stage fdr correction (non-negative)
11. The fdr_bh method is a commonly used method. The p-values are ranked, multiplied by the number of features, and divided by their corresponding rank. It is another form of p-value 12. adjustment.

These methods are reasonable for many types of data, but they still have some limitations. One major assumption is that the p-values follow a certain distribution, but in practice this is known to be invalid for certain types of data like genomics. There is a whole body of literature dedicated to permutation tests as a from of assessing significance in these types of situations. Recall that we use a permutation test in the A/B testing example as well. Here is an example of several methods.





# Explain Methods for Dealing with Multiple Testing
The management team at AAVAIL is preparing to deploy a large number of teams each tasked with integration into a different new market. They claim to have optimized the teams fairly with respect to skills and experience. They are asking you to come up with a framework to evaluate the makeup of their teams. They have not finished hiring and creating all of the teams so naturally before you even get the data you wanted to get a head start.

Getting a head start usually involves finding a similar dataset and writing the code in a way that the new data, once obtained can be added with little effort.

When we perform a large number of statistical tests, some will have p-values less than the designated level of α (e.g. 0.05) purely by chance, even if all the null hypotheses are really true. This is an inherent risk of using inferrential statistics. Fortunately, there are several techniques to mitigate the risk.

We are going to look at the 2018 world cup data in this example.

The case study is comprised of the following sections:

Data Cleaning
Data Visualization
NHT
Adjust NHT results for multiple comparisons
Data science work that focuses on creating a predictive model is perhaps the hallmark of the field today, but there are still many use cases where inferential statistics are the best tool available. One issue with statistical inference is that there are situations where performing multiple tests is a logical way to accomplish a task, but it comes at the expense of an increased rate of false positives or Type I errors.

In this case study you will apply techniques and knowledge from all of the units in Module 2.


