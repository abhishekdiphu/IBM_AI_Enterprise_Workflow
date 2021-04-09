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
