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

