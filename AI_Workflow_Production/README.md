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
