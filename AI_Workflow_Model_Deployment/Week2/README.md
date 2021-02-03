



# Spark Recommenders:Through the Eyes of Our Working Example

## THE DESIGN THINKING PROCESS:

Design Thinking is ideally suited for coming up with a solution to the challenge of deciding what a good recommender would look like for AAVAIL’s end users. Creating and defining persona descriptions for each type of end user would have been part of the early design thinking process. Workshops with actual AAVAIL subscribers would have included activities such as “As-Is” exercises to determine what subscribers currently do. Needs statements, Empathy Maps, and Hopes and Fears would have been captured and documented as well, to build a more complete picture of the subscriber base.

Those data would have informed your initial models for recommender systems, and those initial models (along with their user interfaces) would be presented to actual subscribers during the Prototype phase. Their feedback would have informed your design of the next iteration of models, and you would have continued on this cycle of prototyping and testing until the end users were satisfied with the results.

This process emphasizes how important it is to be able to make rapid changes to models for prototyping purposes. If you end up having to use a neural network-based model, you’ll need to inform the rest of the team of the time and effort required to re-train new iterations of the model.

## Recommendation Systems
In terms of a business opportunity, we can consider the use of a recommender system when any of the following questions are relevant:

- What would a user like?
- What would a user buy?
- What would a user click?

- Most recommender systems today are able to leverage both explicit (e.g. numerical ratings) and implicit (e.g. likes, purchases, skipped, bookmarked) patterns in a ratings matrix. The SVD++ algorithm is an example of a method that exploits both patterns.


Recommendation systems
The majority of modern recommender systems embrace either a collaborative filtering or a content-based approach. A number of other approaches and hybrids exist, making some implemented systems difficult to categorize.

Collaborative filtering - Collaborative filtering is a family of methods that identify a subset of users who have preferences similar to the target user. From these, a ratings matrix is created. The items preferred by these users are combined and filtered to create a ranked list of recommended items.

Content-based filtering - Predictions are made based on the properties and characteristics of an item. User behavior is not considered.

Matrix factorization is a class of collaborative filtering algorithms used in recommender systems. Matrix factorization algorithms work by decomposing the user-item interaction matrix into the product of lower-dimension matrices. In general, the user-item interaction matrix will be very, very large, and very sparse. The lower-dimension matrices will be much smaller and denser and can be used to reconstruct the user-item interaction matrix, including predictions where values were previously missing.

Matrix factorization is generally accomplished using Alternating Least Squares (ALS) or Stochastic Gradient Descent (SGD). Hyperparameters are used to control regularization and the relative weighting of implicit versus explicit ratings matrices. With recommender systems we are most concerned with scale at prediction. Because user ratings change slowly, if at all, the algorithm does not need to be retrained frequently. For this reason, Spark is a common platform for developing recommender systems. The computation is already distributed under the Spark framework so scaling infrastructure is straightforward.

There are several Python packages available to help create recommenders including surprise. Because scale with respect to prediction is often a concern for recommender systems, many production environments use the implementation found in Spark MLlib. The Spark collaborative filtering implementation uses Alternating least Squares.


## Recommendation Systems in Production
One issue that arises with recommender systems in production is known as the cold-start problem. There are two scenarios when it comes to the cold start problem:

What shall we recommend to a new user?

If the recommender is popularity-based then the most popular items are recommended and this is not a problem. If the recommender is similarity-based, the user could rate five items as part of the sign-up or you could attempt to infer similarity based on user meta-data such as age, gender, location, etc. Even if recommendations are based on similarities, you may still use the most popular items to get the user started, but you would likely want to customize the list possibly based on meta-data.
How should we treat a new item that hasn't been reviewed?

In order to make good recommendations, you need data about how users review the item. But until the item has been recommended, it’s unlikely that users will review it. To overcome this dilemma, the item could be randomly suggested for a trial period to collect data. You could put it in a special section such as new releases to gauge initial interest. You can also use meta-data associated with the item to find similar items and infer its recommendations from these similar items.
Concurrency can be a challenge for recommender systems. A recommender might, for example, find the 20 closest users based on latent factor profiles. From those users it would identify a list of potential recommendations that could be sorted and filtered given what is known about the user. The distances between users can often be pre-computed to speed up the recommendations because user characteristics change slowly. Nevertheless this process has a few steps to it that require a burst of compute time. If five users hit the service at the same time, there is the possibility that the processors get weighed down with these simultaneous requests and recommendations become unusually slow.

Spark can help get around the problem of concurrency because it has a cluster manager that handles the distribution of compute tasks. The package celery, which works well with Flask, can also be used to mitigate this problem. If concurrency could be an issue in a system that you develop, even one based on Spark, it is worth taking the time to simulate the problem. Send a batch of requests over a set of pre-defined intervals and then plot times to response.

Additional resources
Recommender systems approaches and algorithms



# Case Study : Model Deployment

## Model Deployment: Through the Eyes of Our Working Example


THE DESIGN THINKING PROCESS
This case study will allow you to learn the actual methods you’ll be working with in a fast-moving Design Thinking project.

Keep in mind that you’re using Apache Spark to make scaling the model much easier, and Docker will help you to more quickly deploy different versions of your models. These skills are important because you’re focused on the end user, and building solutions for end users in a Design Thinking project means you have to move quickly.



# Spark Machine Learning
There are two APIs for Spark MLlib. The RDD-based API and the dataframe based API, which is often referred to as Spark ML. Each has its own documentation.

Spark MLlib docs
Spark ML docs
Spark MLlib has a suite of available tools for unsupervised learning—namely dimension reduction and clustering. For clustering K-means and Gaussian Mixture Models (GMMs) are the main tools. Latent Dirichlet Allocation (LDA) is available as a tool for clustering over documents of natural language.

Spark clustering documentation
Spark MLlib has a number of available supervised learning algorithms that is classification and regression. Many of the commonly used algorithms have been implemented including: random forests, gradient boosted trees, linear support vector machines and even basic multilayer perceptrons.

Spark MLlib - supervised learning
Spark Recommenders
The majority of modern recommender systems embrace either a collaborative filtering or a content-based approach. A number of other approaches and hybrids exists making some implemented systems difficult to categorize.

Collaborative filtering - Based of a ratings matrix collaborative filtering is a family of methods that infers a subset of users that have behavior similar to a particular user. The items preferred by these users are combined and filtered to create a ranked list of recommended items.

Content-based filtering - Predictions are made based on the properties/characteristics of an item. User behavior is not considered.

Matrix factorization is a class of collaborative filtering algorithms used in recommender systems. Matrix factorization algorithms work by decomposing the user-item interaction matrix into the product of lower dimensionality matrices.

There are several Python packages available to help create recommenders including surprise. Because scale with respect to prediction is often a concern for recommender systems many production environments use the implementation found in Spark MLlib. The Spark collaborative filtering implementation uses Alternating least Squares.

CASE STUDY: model deployment
We used a Docker image to create a local Spark environment. In this environment a recommender systems was created using Spark MLlib’s collaborative filtering implementation. The model itself was tuned, by modifying hyperparameters and by toggling between implicit and explicit versions of the underlying algorithm. \verb|spark-submit|spark-submit was used to simulate a deployed model.