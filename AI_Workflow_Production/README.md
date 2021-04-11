# Week 1

# Feedback Loops and Unit Tests: Through the Eyes of Our Working Example

Our Story
As you know, the data science team at AAVAIL systematically uses containers to deploy nearly all of their models and services. But you may only be partially aware of why this is the case. You have some experience with Docker so it is clear that portability is one of the driving motivations. AAVAIL uses custom built machines, each with multiple GPUs to train their deep-learning models. Some of the video processing and machine translation models can take over a week to train, so AAVAIL uses very different environments for training and deployment. Containerization has enabled AAVAIL to move models seamlessly between training, development and production environments.

This course will provide you with the essentials you will need for working with deployed models. You are nearly ready to start deploying your first model to production, but first we will discuss unit tests, performance monitoring and container orchestration so that you use the same best practices as the rest of the team. The goals of these best practices are to:

Provide you with a clear process for properly deploying a model
Promote code re-usability
Help you automate as much of the process as possible


## THE DESIGN THINKING PROCESS
A critical part of the Design Thinking Process is getting your work in front of customers and stakeholders and receiving their feedback. This occurs throughout the process but especially in the Prototype and Test phases and requires moving your model off the small, controlled environment where it was developed and into the real world. Any time you move code from one environment to another, there is a risk of something breaking. Files may be missing, the names of directories might be different, settings of firewalls or proxy servers might prevent access to critical resources. In addition, there might be other factors, such as security and scalability that you haven’t needed to address yet.

Data Scientists aren’t expected to be experts at these aspects of the  process. There are other disciplines such as data engineers, data architects, infrastructure engineers, and (more recently) DevOps AI experts, who have specialized skills in this area.  However, as a Data Scientist, you will ultimately be responsible for the operation  of your models. The more of these tasks you can handle on your own, in a streamlined, automated way, the more quickly you will be able to get  your models into production and receive feedback from users.

An organized, automated, repeatable process of deployment is key to iterating quickly, receiving feedback and advancing the project. It also sets a stage for systematic checks for model improvement via feedback loops



# Feedback Loops
A reusable deployment process, with Docker images as templates, will save you, and those who work closely with you, a lot of time. Feedback loops represent all of the possible ways you can return to an earlier stage in the AI enterprise workflow. We discussed feedback loops in the first course of this specialization.

## Common feedback loops to keep in mind
## Production –> Business Opportunity  
The business opportunity that was refined and decided on in the beginning is in some ways a statement of purpose for your models. If a model has less of an impact on the business than originally anticipated this is often the first feedback loop that you will visit. It is a place to discuss the other potentially relevant feedback loops. Once all of the least time-consuming feedback loops have been explored this is also the place where you discuss the opportunity cost of continued workflow iteration.

## Production –> Data Collection
This is a very common feedback loop especially when using deep-learning models. Because of their flexibility, neural networks can overfit a model. You may plot learning curves to help guide the decision to obtain more data. In some cases, obtaining more data means labeling more data which can be costly so ensure that you engage in discussions to determine the best course of action.

## Production –> EDA
This is an important and often overlooked feedback loop. Once a model has been in production for some time, it becomes necessary to investigate the relationship between model performance and the business metric. This can be thought of as an extension of EDA, where visualization and hypothesis testing are the most important tools. Investigations into the underlying causes of model performance drift can re-purpose much of the code developed during EDA.

## Production –> Model Selection and Development 
If a model performs poorly in production, perhaps due to latency issues or because there is an over-fitting issue, it is reasonable to return to try a different model. If it is an overfitting scenario and obtaining more data is not an option, choosing a model with lower complexity (e.g. SGDClassifier) is a reasonable next step. Spark ML models tend to have more latency than deployed scikit-learn models. Latency is the effective runtime for a prediction. You can run simulations to test different models, which can help optimize for latency. Another reason to return to the \verb|models|models stage from production is if we observe performance drift (a topic covered in the next unit).
There are other feedback loops such as trying different data transformations to improve a model’s performance or optimizing the way data are collected to reduce the number of transformations that are necessary to run a machine learning model. The most important aspect of all feedback loops is that they end with a return to a previous stage of the workflow. This is the only way to ensure that your entire workflow does not contain a weak link, and also the best way to keep track of each stage of the workflow.



# Unit tests

Unit testing is the process of testing small portions of the software, also known as units. This is done one test at a time, to verify that an expected result is returned under controlled conditions. Importantly, the unit tests are usually organized as a suite and return objective evidence, in the form of a boolean value, which is a key element that enables workflow automation. The boolean value indicates whether or not each and every part of the software that was tested performed as expected. Ideally every portion of the code would be tested under every conceivable combination of conditions, however this is clearly not possible in the real world. The amount of source code that is actually tested when compared to the total amount of testable code is known as test coverage. There is even a package in Python called coverage that estimates the total coverage of your tests.

Important
There is an important trade-off in data science between the amount of test coverage and prioritizing other tasks. In many ways this trade-off is the same as the one that software engineers face, except data science has a sizable component of experimentation. This means that many models that get created never see production and many models that see production never come to fruition. There are many reasons for this and the AI workflow presented here is designed to minimize this risk, but nonetheless many modeling efforts are shelved. Because of this, we present as part of the overall workflow a way to properly include unit tests, but we do so in a way that includes only a minimum number of tests along with the scaffolding to expand once a model or service proves its worth.
It is important to think about opportunity cost when determining the appropriate amount of test coverage. We will refer to the unit testing approach presented here as a test harness, because it is implemented as an automated test framework. Much like data ingestion, the idea is to have the necessary components of a task bundled under a single script. In this case it will be called \verb|run-tests.py|run-tests.py. To help ensure that our unit tests are a test harness we will use the script to setup a hook.

The field of software testing is out of the scope of this specialization, but it is worth noting that there are many viable testing frameworks and technologies that can be used in place of the approach presented here. One of the reasons to create unit tests is to ensure that iterative improvements to code do not break the functionality of the model or API. This is known as regression testing, because when the code does not perform as expected it is a regression. Including regression testing, here is a summary of the principal reasons to package unit tests with your deployed machine learning model:

## Regression 
Testing: Ensure that previously developed and tested software still performs after a change
## Code Quality:
Promote the use of well-written code along with well-conceived designs
## Documentation: 
Unit tests are a form of documentation that can help you and members of your team understand the details of how the software works, unit-by-unit
## Automatic Performance Monitoring: 
Having a suite of unit tests that are kicked off when training is performed can help monitor for performance drift in an automated way

Unit tests also helps ensure that when software fails, it fails gracefully. This means it stops execution without causing additional errors and takes any steps, such as closing open connections or saving data to a file that may be necessary for recovery. This is an important aspect of software design that can save significant amounts of time when debugging a problematic query.


## Unit Testing in Python
Three of the most useful libraries in Python to carry out unit testing are:

- pytest
- nose
- unittest

## Test-Driven Development (TDD)
Traditionally, software developers write software by first writing their functions, algorithms, classes, etc… and then, once they are satisfied that everything is working, they write a series of unit tests to provide objective evidence that it works as expected. The downside to this approach is that, without a defined completion criteria, it may result in writing more code than is necessary, and, without a clear definition of the expected outcome, the programmer might not know what completion criteria they are working towards until late in the process.

Test-Driven Development extends the idea of unit testing by recognizing that the sucessful completion of the test is the most important outcome of the software development process. Assuming the test is well-written and has sufficient coverage, any code that produces an ‘OK’ is ready for production; any code that does more than this is simply superfluous. TDD can have the same effect as using pseudocode to template a piece of software or a script before writing the code. When working on large software projects, it is easy to get caught up in non-essential portions of the code. TDD and pseudocode can serve as a checklist of tasks that need to be completed to obtain that all-import boolean result: ‘OK’. This can help keep you within a pre-defined set of boundaries all the way through the development process, saving time and effort.

To this end, TDD starts by clearly defining the expected outcomes under various conditions first. We then write only enough code to achieve successful unit test results. There are other methodologies to produce completion criteria, some of which use requirement analysis as part of the software design process, but here we show a simple approach to demonstrate how unit testing through TDD can be used to build a test harness.


### CI/CD
In software engineering CI/CD, sometimes written as CICD, refers to continuous integration and continuous delivery. Depending on the context, CD may also refer to Continuous Deployment. CI/CD is a concept to be aware of when learning about the DevOps side of data science. Continuous Integration is the practice of merging all developers’ changes frequently (usually daily) into a single central source often called the trunk.

Continuous Delivery refers to the iteration on software in short cycles using a straightforward and repeatable deployment process. Continuous Delivery uses manual deployments, which is in contrast to Continuous Deployment which makes use of automated deployments. The unit testing framework presented here can be readily integrated into several CI/CD pipelines. This is not a course in DevOps nor is it a course in data engineering, so we will not go so far as to make recommendations about deployment systems and architectures, but being aware of the terminology can promote cross-team functionality.

Historically, software updates were deployed infrequently, perhaps once per year, and only after extensive, months-long testing cycles. CICD improves this process tremendously, allowing developers to see the results of their efforts almost immediately. However, the increased pace of change comes at the risk of introducing bugs. For this reason, CICD depends heavily on a robust testing process. Without automated testing, CICD would not be possible.

Additional resources
Why you should use microservices and containers
Managed CI/CD Kubernetes services (IBM)
GitHub actions
Jenkins


# Performance Monitoring: Through the Eyes of Our Working Example

## Our Story
You have seen how other data scientists on the AAVAIL team work and you now have a good idea what the lifecycle of a deployed model or service looks like. One thing that you have observed is that once a model has been running for some time, either management or senior members of the data science team will ask about how the model is doing. You have also noticed that most members of the team respond by talking about the same fundamental concepts: performance drift, load, latency, and average runtime.

However, an important consideration that often gets overlooked is *business value*; is the model having a significant effect on business metrics as intended?  It is important to be able to use log files that have been standardized across the team to answer questions about business value as well as performance monitoring. 

## THE DESIGN THINKING PROCESS
Concerns about performance and monitoring are generally not raised in the design thinking process until the prototype or test phases. Indeed, performance monitoring is historically treated as an afterthought during implementation or long-term production support and is occasionally left as a consideration for other members of the team with specialized skills in systems optimization. Needless to say, planning for performance monitoring early in the process yields dividends down the line and eases the transition from development to production.


## Logging
Like all problems in data science, performance monitoring starts with collecting the right data in the right format. Because performance monitoring is a concern in nearly all customer-facing computer systems, there is a well-established set of tools and techniques for collecting this data. Data for performance monitoring is generally collected using log files. Recall the following best practice:

Important
Ensure that your data are collected at the most granular level possible. This means each data point should represent one user making one action or one event.
Naturally, collecting very granular data will result in very large data sets. If there is a need, you can always summarize the data after it has been collected. Summary level data may mask important patterns and generally it is not possible to go from summary data to granular data. Log files with several million entries can be analyzed on a single node or on a personal machine with little overhead.  

Note:  If the logging is handled by another member of your team or by another another team you should ensure that the minimally required data discussed here are available or it will be difficult to monitor your model’s performance and/or debug performance related issues.


## Minimal Requirements for Log Files
These are data that are minimally required for performance monitoring for most model deployment projects. There are other features that fall into this category that are situation dependent, like user_id in a recommendation system, so do not view this list as comprehensive, simply keep it as a reference starting point.

- runtime - The total amount of time required to process the request. This is a factor that directly affects the end user’s experience and should be monitored.

- timestamp - Timestamps are needed to evaluate how well the system handles load and concurrency. Additionally, timestamps are useful when connecting predictions to labels that are acquired afterwards. Finally, they are needed for the investigation of events that might affect the relationship between the performance and business metrics.

- prediction - The prediction is, of course, the primary output of a predition model. It is necessary to track the prediction for comparison to feedback to determine the quality of the predictions. Generally, predictions are returned as a list to accommodate multi-label classification.

- input_data_summary - Summarizing information about the input data itself. For the predict endpoint this is the shape of the input feature matrix, but for the training endpoint the features and targets should be summarized.

- model_version_number - The model version number is used to better understand the influence of model improvements (or bugs) on performance.

Additional features that can be optionally logged
These are the features that are considered nice to have, but they are not always relevant to the circumstances or sometimes there can be practical limitations (e.g. disk space or computational resources) that limit the ability to save these features.

- request_unique_id - Each request that has been made should correspond to an entry in the log file. It is possible that a request corresponds to more than one entry in the log file for example if more than one model is called. This is also known as correlation_id.

- data - Saving the input features that were provided at the time of a predict request makes it much easier to debug broken requests. Saving the features and target at the time of training makes it easier to debug broken model training.

- request_type - Relevant attributes about the request (e.g. webapp request, browser request).

- probability - Probability associated with a prediction (if applicable).

The value of logging most of the mentioned data is fairly intuitive, but saving the data itself might seem unnecessary. If we save the input features, when a predict endpoint was hit, we can reconstruct the individual prediction, stepping through each part of the prediction process. For training, the archiving of all the data is often unnecessary, because there is a system in place, like a centralized database, that can re-create the training data for a given point in time. One option is to archive only the previous iteration of training data.

If very granular levels of performance monitoring are needed, we could model the distribution of each feature in the training data matrix and determine if new batches of data fall outside the normal range. We could also use one of the models we have discussed for novelty detection, but insight would be at the level of observations across all features rather than at the feature level. For most models the latter option is sufficient.

Warning: If you decide to log the data, be aware of disk space and read/write bottlenecks. It is also important to ensure compliance with company policies or regulations such as HIPAA, or GDPR concerning personally identifiable or sensitive information, depending on jurisdiction.


## Model Performance Drift
With a system for logging in place, the overall goal is to keep the performance of a model high over time, and ideally to see continuous improvement. The log files are key to identifying when a change has occurred, but it helps to know what kind of performance drift to expect. When we monitor model performance, we look for any significant changes in model performance, in order to both identify issues early and capitalize on changes that result in performance improvements.

Note:  Software decay or software rot occurs when there is any decrease in model performance.

Common forms of performance drift or software decay include:

 concept drift
sampling bias changes
selection bias changes
software changes
data changes.  
Each of these is covered below.

Concept drift
Concept drift, is when the statistical distribution of a target variable changes over time.  One example of this would be fraud detection.  If fraud was a fraction of a percentage of all known cases before we deployed a machine learning algorithm, it would be reasonable to assume that the percent of fraud will decrease over time, effectively changing the distribution.  The change will likely have consequences on model performance.  This type of drift would appear as decreased model performance, but you could also detect it by checking the training log files.

Sampling bias and selection bias changes
After a model is deployed, any newly introduced sampling bias. could result in subgroups of the data being under or over represented and the model would not generalize well to new data, which would decrease model performance.  Any newly encountered selection bias is also likely to affect model performance.

For example, imagine a model was built to diagnose a specific medical  condition from a chest X-ray.  Perhaps the standards and technology have changed the way the radiologist makes a diagnosis,  implying that the way the labels were initially generated is different today than it was in the past.  Supervised learning in its  current form requires accurate and consistent labeling of targets.  If the process for labeling data has changed, it will  likely affect model performance.  We often observe the change in model performance through a detected outlier, but  it requires some investigation before the reason for performance drift can be confidently identified.

Software changes
Another cause of performance drift can come from changes in the the model and container software.  This is why we explicitly use a model version, used in conjunction with version control.  If a library dependency, code optimization, or feature addition were to blame for the performance drift it should be easy to track based on the model version.

For example, imagine you have just converted a neural network into the newest version of TensorFlow or another deep-learning package.  This change should be tied to a specific model version.  You can create releases in GitHub or you may directly add tags to your docker image.  Additionally, there are many features in GitHub that help you track, review and ready version changes for code for deployment.  There are version control strategies specific to AI applications (this article is on Medium, and may require a subscription for access) as well.

Data changes
It is worth noting that performance drift can arise from changes in  the data itself, and it can be anticipated by directly monitoring the features in the data.  There are several methods that can be used to  compare an established distribution to a new one, e.g., from a new batch of training data.  It is also possible that for a  given use case there is a specific feature or two that are of critical importance and checks on those features should be  implemented as a step for quality assurance.  Two commonly used methods to compare distributions are:

Kullback–Leibler divergence
Wasserstein_metric
We will show in the following screencast how to implement performance monitoring at the level of evaluation metric using a model-based approach.  This example could serve as a template to add more granular feature-level monitoring.




## Security and Machine Learning Models
Adversarial attacks of machine learning systems have become an indisputable threat. Attackers can compromise the training of machine learning models by injecting malicious data into the training set (poisoning attacks), or by crafting adversarial samples that exploit the blind spots of machine learning models at test time (evasion attacks). 

Defending machine learning models involves certifying and verifying model robustness and model hardening with approaches such as:

pre-processing inputs
augmenting training data with adversarial examples
leveraging runtime detection methods to flag any inputs that might have been modified by an adversary
The resources listed below are for your reference and will help with understanding basic concepts around ML security.

To learn more about machine learning adversarial attacks, defenses, and consequences, see A taxonomy and terminology of adversarial machine learning 
Use a demo where you can create and simulate attacks and different defense methods for machine learning models
Learn more about The Adversarial Robustness Toolbox, a Python library to verify model robustness
Examples and hands-on tutorials to help you defend machine learning models against adversarial threats and make AI systems more secure and trustworthy



## SUMMARY OF WEEK 1 : 

Feedback Loops and Unit Testing
Feedback loops are the possible paths that can be taken to iterate on the workflow. Any time new information or new results causes you to revise or revisit a previous decision or approach, it is a feedback loop. Data Science is an inherently experimental discipline, so you should strive to embrace the process of trying out different approaches. However, if not properly managed, the process of iteration can become bogged down in a miasma of tedious, manual steps, unforeseen impacts to code that was previously working and changes to environments and dependencies. The iterative process relies upon a smooth, automated, reliable and repeatable deployment process.


Moving a model from development to production can be a tricky and time-consuming process. Any time the compute environment changes, there is a risk that something will break. Containers are used to overcome this problem and to handle other issues such as scalabilty. These containers allow for the precise, programmatic creation of compute environments that can be easily moved from one machine to another or deployed on multiple machines. A Docker container with endpoints that can be targeted programmatically is a powerful template for deploying models quickly, repeatably and at different scales according to demand.

When iterating on a model, automation and performance monitoring are the two core principles to keep in mind. The purpose of iteration is to realize performance improvements. Without performance monitoring, there would be not point in iteration. Without automation, iteration can be difficult or impossible.

Some of the feedback loops include:

production –> business opportunity

The business opportunity that was refined and decided on in the beginning is in some ways a statement of purpose for your models. If a model has less of an impact on the business than originally anticipated, this is often the first feedback loop that you will visit. It is a place to discuss the other potentially relevant feedback loops. Once all of the least time-consuming feedback loops have been explored, this is also the place where you discuss the opportunity cost of continued workflow iteration.
production –> data collection

This is a very common feedback loop especially when using deep-learning models. Because of their flexibility, neural networks can overfit a model. You may plot learning curves to help guide the decision to obtain more data. In some cases, obtaining more data means labeling more data which can be costly so ensure that you engage in discussions to determine the best course of action.
production –> EDA

This is an important and often overlooked feedback loop. Once a model has been in production for some time, it becomes necessary to investigate the relationship between model performance and the business metric. This can be thought of as an extension of EDA, where visualization and hypothesis testing are the most important tools. Investigations into the underlying causes of model performance drift can re-purpose much of the code developed during EDA.
production –> model selection and development

If a model performs poorly in production perhaps, due to latency issues or because there is an over-fitting issue, it is reasonable to try a different model. If it is an overfitting scenario and obtaining more data is not an option, choosing a model with lower complexity (e.g. SGSGDclassifier) is a reasonable next step. Spark ML models tend to have more latency than deployed scikit-learn models. Latency, is the effective runtime for a prediction. You can run simulations to test different models, which can help optimize for latency. Another reason to return to the model selection and development stage from production is if we observe performance drift.
Unit Tests
Unit testing is the process of testing small portions of the software, one test at a time, to verify that each and every portion of the software works as expected under controlled conditions. Unit tests return objective evidence, in the form of a boolean value, which is a key aspect that enables workflow automation.

The amount of source code that is actually tested when compared to the total amount of testable code is known as test coverage.

Some of the reasons to include unit tests with your model are:

Regression Testing
Code Quality - they promote the use of well-written code along with well-conceived designs
Documentation - unit tests are a form of documentation that can help you and members of your team understand the details of how the software works
Automates Performance Monitoring Tasks - having a suite of unit tests that are kicked off when training is performed can help monitor for performance drift in an automated way
Promotes the Use of CI/CD - unit tests help enable a software to be integrated into CI/CD pipelines
Test Driven Development
Test Driven Development (TDD) is the process of writing the unit tests first, and then writing just enough code to acheive a passing result in the test suite. In this way, the unit tests serve as an outline, a plan and a completion criteria for the task of writing code and you are more likely to write relevant tests with high coverage.

Performance Monitoring and Business Metrics
The work of data science does not end when a model has been deployed to production. It is necessary to continue monitoring the model to ensure that it continues to function as originally intended and that it serves the business need for which is was designed. Drift occurs when the new, incoming data does not represent the data that the model was originally trained on. Perhaps there has been a shift in customer demographics or usage patterns, or perhaps the original training data was unbalanced or incomplete. It may be necessary to retrain the model (or select a different model) as more and newer data becomes available.

Another important consideration is how well the model (and deployment environment) handle the load. It can be very difficult to simulate real-world demand levels during the development process, so it’s often unclear how long it will take to process requests until a model is in production. A model may also become a victim of its own success. If a service becomes wildly popular, it may be unable to process all of the requests, resulting in long user wait times, dropped responses and crashes.

Monitoring for both accuracy and performance depends upon logging requests and responses to a file or database that can be examined later. Logging should be done at the most granular level possible and include as much relevant information as possible, including:

runtime - The total amount of time required to process the request.

timestamp - The date and time at which the requst was received and processed.

prediction - The model output.

input_data_summary - Summarizing information about the input data itself.

model_version_number - The model version number is used to better understand the influence of model improvements (or bugs) on performance

request_unique_id - A unique identifier that allows the request to be tracked.

data - the input data

request_type - Relevant attributes about the request (e.g. webapp request, browser request)

probability - Probability associated with a prediction (if applicable)




# WEEK 2:

## THE DESIGN THINKING PROCESS
In the Prototype phase of Design Thinking, Data Scientists generally build simple models that deliver expected results under controlled conditions. While this can be effective for rapidly demonstrating feasibility and moving a project forwards, it is at this point in the process where data may be scarce and time-saving assumptions or approximations can introduce unintentional bias. When moving to the test phase, new and larger data sets are introduced which may evolve or drift over time. Continuing to monitor the performance of the model, and identifying and addressing sources of drift, is an important responsibility, and the data scientist will likely be presenting reports of model performance during playbacks.


## Kubernetes Explained: Through the Eyes of Our Working Example

Our Story
Automation is a key to successful data science teams. Without automation, everyone on the team would get bogged down managing models and services that have already been deployed. Models running in containers need to be managed. They need to be refreshed with new training data. When a new version of a model comes online, the unit test suite needs to be run and, if there is a failure, the management systems should seamlessly fall back to a previous version. The management layer should also have the tools needed to deal with scale.

The data science team at AAVAIL uses Kubernetes for management of these tasks, so this tutorial will help ensure you know the terminology and that you have everything you need to set up a basic container orchestration environment. You will see that Kubernetes is the tool of choice for a number of reasons, but from a data science perspective, having a convenient way to deal with load and scale is perhaps the most important.


### THE DESIGN THINKING PROCESS
Deploying your machine learning models using Kubernetes clusters offers many advantages, one of the most important being flexibility. As your models move into production, they will be tested and used by end users. Depending on the complexity of the model, the number of end users, and the infrastructure supporting it, there will definitely be a need to monitor performance and also to rapidly scale up or down to match demand. You will need to present these considerations to your stakeholders. They will be interested to know what advantages the Kubernetes deployment can give them, particularly with regard to scalabilty and resiliency.

## Introduction to Kubernetes
Important
You are not expected to be an expert with Kubernetes after this tutorial. The main goals of this tutorial are that you become familiar with the technology so that you can deploy to a Kubernetes cluster and that you can communicate effectively with colleagues who manage these services.

#### Introduction
Kubernetes is a container orchestration platform for managing, scheduling and automating the deployment of Docker containers. Orchestration in the sense of containers deals with their automated configuration, coordination, and management. The containers we have developed as part of this course are essentially microservices meant to be deployed as cloud native applications. There are many advantages of the Docker workflow-template approach we presented in this course and, more generally, the cloud native microservices approach. These advantages include but are not limited to:

Reduced time to deployment
Reusable code
Ease of model iteration
Work naturally with container orchestration systems like Kubernetes
One disadvantage of cloud native applications is that they create the necessity of managing many small pieces. This is where orchestration and Kubernetes come into play.

Let’s say we have an API that runs Latent Dirichlet Allocation on a corpus of user comments generated from the AAVAIL mobile app and website. Following best practices, you have bundled this service inside a container. The model in this case is not enough to provide utility so you have containerized another Flask app that serves a suite of visualization tools so that management, marketing and any other teams at AAVAIL have a tool to explore the data. For example, the container might run, pyLDAvis, the visualization tool we used earlier in this specialization. Additionally the suite of tools might contain a simple dashboard so that a user could browse summary plots, word clouds and tabular summaries. The workflow-templates you have seen so far bundle a basic HTML service that could be expanded to meet all of these needs.

Hint:  The decoupling of a data visualization suite and the underlying model into two separate services promotes code re-usability.

There are two separate containers in this example. If these two containers are often run together, it is worth considering the use of Docker Compose, a tool for running multi-container Docker applications. Docker Compose uses a single YAML file to connect and configure the different containers in your application. Then, with a single command, you can launch all of the services. The convenience of Docker Compose, sometimes just called Compose, is very real and if your application needs more than one container, which is often the case, you should be using Docker Compose.

#### Kubernetes terminology
kubectl CLI - Kubectl is a command line interface for running commands that communicate with a Kubernetes cluster.

Minikube - A tool that makes it easy to run Kubernetes locally. It runs a single-node cluster inside of a virtual machine. It is an important environment for learning the essentials and it serves as a sandbox to try out ideas.

kubelet - The primary ‘node agent’ on each node. It is the lowest level component in Kubernetes and it is responsible for the processes running on an individual machine.

pod - Pods are the smallest deployable units of computing that can be managed by Kuberntes. Pods are made up of one or more containers (usually Docker), with shared storage/network, and a specification for how to run the containers.

As a reference here is a glossary of Kubernetes terminology.

## Summary/Review
TUTORIAL: IBM Watson OpenScale

IBM Watson OpenScale is a suite of tools that provide monitoring for drift, fairness and explainability. OpenScale works with models built and deployed on several major cloud systems. The automatic data discovery tools examine the training data for a model, identify the features, labels, predictions and probabilities for supervised machine learning models of binary, multinomial and regression.

In situations where unintentional bias is a concern, OpenScale identifies both the features that are at risk of discrimination and the outcomes that are undesirable. OpenScale then monitors transactions on an on-going basis to ensure that outcomes are not unduly influenced by demographic or other sensitive information values.

OpenScale can also automatically rebalance training data and provide improved models to correct for unintentional bias.

Individual transactions can be analyzed to determine which features are most responsible for the result that was determined and the minimum amount that these values would need to be changed to produce a different result. This explainability tool can be an import guide to business decisions and feedback for customers and users.

CASE STUDY: Performance Monitoring
Templates can greatly reduce the work and time needed to deploy a model while also improving reliability. The Dockerfile which defines a Docker container is in a format that is easy to read and extend, so it serves as an excellent template. Unit test suites also provide a convenient itemized list of tasks to complete and proof of success.

Flask is a web framework which allows python to work in a web-based environment, receiving data from web requests and return results in a web browser. Flask can be built into a Docker container that exposes ports to allow data to pass in and out of the container.

Once deployed, the Docker container exposes an API endpoint which can receive requests and respond by sending back data. JSON is a data format, similar in structure to a Python dictionary, which is used for passing data to and from an API endpoint. Docker containers may have multiple endpoints for training, predicting and logging, or these functions may be divided among several containers that work together.

TUTORIAL: Managing with Kubernetes
Kubernetes is a tool for container orchestration. It does not replace Docker, but rather works with Docker to enhance its capabilities and automate tasks. This is especially useful in systems where components are deployed as microservices and spread over several containers that need to be configured, deployed and managed in concert. Kubernetes is especially useful in situations where different components need to scale differently to meet different demands.

Elements of Kubernetes include:

kubectl CLI - a command line interface for communicating with a Kubernetes cluster.

Minikube - a tool that runs a single-node Kubernetes cluster locally as a test environment.

kubelet - the primary agent on each node. It is the lowest level component in Kubernetes and it is responsible for the processes running on an individual machine.

pod - the smallest deployable units of computing that can be managed by Kuberntes. Pods are made up of one or more containers (usually Docker), with shared storage/network, and a specification for how to run the containers.
