



**[IBM_AI_Enterprise_Workflow](https://www.coursera.org/specializations/ibm-ai-workflow?)**


# 1. Data at scale: Through the Eyes of Our Working Example

## THE DESIGN THINKING PROCESS:

The Prototype phase of the design thinking process is where ideas are tested in real-life to see if they work in solving business challenges. The Prototype phase is about making a model work. At this stage, you’ll be developing and tweaking many different models, all in an attempt to select the best model for the job.

You’ll also learn about the non-linear aspects of design thinking. As you create and test prototype models you will probably discover that you don’t have all of the data or user insights that you need. Recall that design thinking is user-centric. As your users engage with your models they will come up with more suggestions and ideas for making your models more useful. During the earliest stages of prototyping you’ll be building new data pipelines and new models, testing your abilities every day.

## Connecting the Dots:

Some business opportunities can be solved by running a tuned model once on all available data. For example, if AAVAIL was interested in whether or not to continue investing in a particular market, a time-series forecasting model could be created for both the new market and a baseline. This model, along with some visualizations and additional analysis, would likely be compiled into a report and there would be no need for it to exist in a persistent state with callable endpoints. Ideally, the forecasting model would be written in way that would allow it to be easily adopted to other market analyses.

Depending on the needs of your business, it is possible that a sizable percentage of models exist as standalone projects that would provide little added value if they were deployed. It is also possible that nearly all models need to be deployed in production to be of benefit to the business. Either way it is likely that model deployment will become a necessity at some point and optimization is a key consideration for any model or service that is to be deployed.


# 2.Optimizing Performance in Python:

Today data scientists have more tooling than ever before to create model-driven or algorithmic solutions. Because of tooling availability and a general rising interest in the field of data science, many practicing data scientists only have a few years of experience. This trend has resulted in a lack of awareness when it comes to code optimization. There are many ways to increase the speed of code and for some business applications speed is directly related to revenue. Before we jump into the strategies and tools to help optimize code, it is important to know when to take the time to make code optimizations.

An example of a situation where it is difficult to make speed improvements through code is when we have a model that takes several days on multiple GPUs to train. A speech-to-text engine is a good example, but almost any large neural network with a reasonable amount of data falls into this category. You can profile TensorFlow models using TensorBoard, but if you have already optimized the model for performance, it becomes tricky to make improvements from a code perspective. You can always use more GPUs or other computational resources, but beyond saving model checkpoints in the event that there is a failure, little can be done to improve training time.

With scikit-learn model training it is also difficult to optimize, apart from using the \verb|njobs|njobs argument and trying several optimization algorithms when appropriate. In general, unless you write your own inference portion of the code, as is sometimes the case with expectation-maximization, improving on the efficiency of available inference algorithms is either difficult or unrealistic. For model prediction there are several best practices, such as keeping the trained model in memory, that we will discuss later that will help ensure optimized performance.

There are plenty of examples where a well-written script addresses a business opportunity even without the use of machine learning. Perhaps the AAVAIL sales team wanted to optimize quarterly travel schedules. This would be an example of the traveling salesman problem where you could write a brute-force algorithm or use some variant on a minimal spanning tree to solve it. Either way, these are useful tools that do not use machine learning algorithms.

## Two important areas of data science where machine learning algorithms may not be the best solution are:

- optimization
- graph theory
The first rule to ensuring that you are optimizing your code in a smart way is to look around for implementations before creating one from scratch. The scipy.optimize submodule has a number of optimizers and algorithms (some of them general purpose) already implemented. If your problem is in graph space like customer journeys or social networks then check out the algorithms implemented by NetworkX before you set off building your own.

Finally, we come to the scripts or blocks of code that need speed improvements, but you have come to the conclusion that there is no optimized code readily available. The task of optimizing the code then falls to you. The first step is to identify which parts of your code are bottlenecks. This is done using profiling or more specifically Python profilers. Once the specific pieces of code that need to be optimized are identified, then there are a number of common tools that may be used to improve the speed of programs. Several of these tools make use of the fact that modern computers have multiple available processor cores on a machine. To see how many processor cores are available on your machine or compute resource try the following code.

1234
from multiprocessing import Pool, cpu_count
total_cores = cpu_count()
print('total cores: ', total_cores)

1
total cores: 8
A list of commonly used techniques and tools to optimize code:
Use appropriate data containers - For example, a Python set has a shorter look-up time than a Python list. Similarly, use dictionaries and NumPy arrays whenever possible.

Multiprocessing - This is a package in the standard Python library and it supports spawning processes (for each core) using an API similar to the threading module. The multiprocessing package offers both local and remote concurrency.

Threading - Another package in the standard library that allows separate flows of execution at a lower level than multiprocessing.

Subprocessing - A module that allows you to spawn new processes, connect to their input/output/error pipes, and obtain their return codes. You may run and control non-Python processes like Bash or R with the subprocessing module.

mpi4py - MPI for Python provides bindings of the Message Passing Interface (MPI) standard for the Python programming language, allowing any Python program to exploit multiple processors.

ipyparallel - Parallel computing tools for use with Jupyter notebooks and IPython. Can be used with mpi4py.

Cython - An optimizing static compiler for both the Python programming language and the extended Cython programming language. It is generally used to write C extensions for slow portions of code.

CUDA (Compute Unified Device Architecture) - Parallel computing platform and API created by Nvidia for use with CUDA-enabled GPUs. CUDA in the Python environment is often run using the package PyCUDA.

Additional materials
scipy-lectures tutorial for optimizing code
mpi4py tutorial
ipyparallel demos
Cython tutorial




# 3.High Performance Computing

We mentioned in a previous section that inference can be difficult to optimize and that one way around this is to add more GPUs. The general idea of using an aggregation of compute resources to dramatically increase available compute resources is known as high-performance computing (HPC) or supercomputing. Within this field there is the important concept of parallel computing, which is exactly what we enable by adding multiple GPUs to computation tasks.

Supercomputers and parallel computing can help with model training, prediction and other related tasks, but it is worth noting that there are two laws that constrain the maximum speed-up of computing: Amdahl’s law and Gustafson’s law. Listed below is some of the important terminology in this space.

Symmetric multiprocessing - Two or more identical processors connected to a single unit of memory.

Distributed computing - Processing elements are connected by a network.

Cluster computing - Group of loosely (or tightly) coupled computers that work together in a way that they can be viewed as a single system.

Massive parallel processing - Many networked processors, usually > 100, used to perform computations in parallel.

Grid computing - distributed computing making use of a middle layer to create a virtual super computer.

An important part of this course is dealing with data at scale, which is closely related to both code optimization and parallel computing. In this course will be using Apache Spark, a cluster-computing framework, to enable parallel computing.

If we talk about scale in the context of a program or model, we may be referring to any of the following questions. Let the word service in this context be both the deployed model and the infrastructure.

Does my service train in a reasonable amount of time given a lot more data?
Does my service predict in a reasonable amount of time given a lot more data?
Is my service ready to support additional request load?
It is important to think about what kind of scale is required by your model and business application in terms of which bottleneck is most likely going to be the problem associated with scale. These bottlenecks will depend heavily on available infrastructure, code optimizations, choice of model and type of business opportunity. The three questions above can serve as a guide to help put scale into perspective for a given situation.

Additional resources
High performance computing at IBM
