## Getting Started (Hands-on)

In this hands-in activity we will use the Watson Machine Learning Python client to connect to the Watson Machine Learning service. You may train, test and deploy your models as APIs for application development, then share the models with colleagues. So far in this specialization we have not deployed any of the models to a cloud service so this tutorial represents the first point at which we can formally make a model available to others.

Having a tuned and trained model in hand does not necessarily make it useful. Making a model available to other people without a reliance on your personal development environment is an important step towards ensuring model utility. This tutorial is simple in that you will deploy a model and ensure that it works, but this seemingly small step is an important stride towards making the model work towards addressing a business opportunity.

Before you go through the deployment scripts for this activity there are two important steps you need to take.

### Create a WML service

Setup an appropriate runtime environment with Docker
The goal of this tutorial is to have the ability to iterate locally on a model then store and deploy it to the Watson Machine Leaning (WML) service. This specialization has spent considerable time showcasing the exchangeability of data transformations and models in the AI enterprise workflow. The easiest way for most developers to accomplish this is to develop in their natural environment, whether it is locally, on a cloud or as part of a shared compute resource. With the process of model selection out of the way this tutorial showcases that the details of deployment can be relatively easy.

In order to ensure a smooth transition from a local environment to WML you will need to align your development environment with one of the available runtime environments in WML. Fortunately, this can be achieved quickly and repeatedly with an appropriate docker container. 

##Steps to carry out before running the activity's scripts

- Create a WML service
- Go to the WML services page and login
- U​nder "Select a region" select the city that is closest to your location
- Click the button \verb|create|create
- T​hen we want to create a deployment space. First, click on "Access in Watson Studio"
- I​n the middle of the screen you will see a button "New deployment space" click on this button and select "Create an empty space"
- Give a name to the deployment space ("wml tuto deployement space" for instance) and specify a cloud storage object (if you don't already have one, you can create one here) and the Watson Machine Learning instance.
- C​reate the deployment space and go to the deployment space UI clicking on "view new space"
- Click "setting" on the main navigation bar. In the setting page you will find the space ID. - Copy and paste the Space ID in a separate text file, you will need to copy this ID in the scripts of this activity to access the deployment space via python.
- We now need to generate an API key to your ibm-cloud account
- Go to the IAM API key management page and click to "Create an IBM cloud API key"
- G​ive a name to your API key (I called mine "api_wml_tuto") and click on create
- Click on copy and past your key in a text file to save it
- Steps to setup our runtime environment with docker
- The coming steps show you how to build a simple python runtime environment with docker. The reason we use a containerized python environment here is that WML has very specific runtime environments available. If you are creating a TensorFlow or scikit-learn model for example you will need to ensure that the versions match. More specifically you will need to match the \verb|requirements.txt|requirements.txt file to the supported frameworks.

###First, download the scripts and files for completing this activity. Click left on the zip file below and click download. Then, unzip this file in your working directory.

WML-tutorial.zip
Go to the folder of the activity -that you just unzipped- and update the json file wml.json with your APIKEY and the appropriate url according to the location that you selected when creating the WML service. This json will be called from the tutorial scripts to communicate with the wml instance that you created.
1234
{
  "apikey": "YOUR API KEY",
  "url": "https://us-south.ml.cloud.ibm.com"
}
Dallas: https://us-south.ml.cloud.ibm.com // Frankfurt: https://eu-de.ml.cloud.ibm.com  //  Tokyo: https://jp-tok.ml.cloud.ibm.com // London: https://eu-gb.ml.cloud.ibm.com

2. Open a new terminal, go to your working directory and build the Docker image with the docker file. You can give a name to you image with the -t tag ("my-python-env" for instance).

12
~$ cd to/my/directory/WML-tutorial
~$ docker build -t my-python-env .


The image that you just built is a simple linux container with a python 3.7 executor. When building the image we also installed all the required python libraries that we need for this activity. The requirements are listed in requirement.txt. If you take a closer look a the Dockerfile you will also see that we install an application called vim. Vim will allow you to directly edit the scripts from the bash of the container.

3. The next step is to run the image. The process that we will run is the bash shell of the container from which we will edit and run our scripts. To run this process enter the following command line:

1
~$ docker run -it my-python-env bash
Your terminal is now the bash of your container, from this shell you can run python scripts with a python 3.7 executor. If you want comme back to your local unix shell press control+D. When exiting the container you stop the process and you will need to run the image again with the previous command line if you want to reopen a container bash. 

Important : Every editing that you do on the script inside a container are not saved locally! The files in your containers are completely isolated form your local computer. If you exit and delete your container you will loose all the modifications you made inside this container.



# Tutorial (Hands-on)
1. Run a new bash of your python image. 

1
~$ docker run -it my-python-env bash
2. Deploy the model

Before running our deployment script WML-tutorial-deploy-model.py you need to edit it with your deployment space id. You will need to do these editing directly from the bash of your container to make sure you are editing the files stored on your container. Remember your container is isolated from your local computer, when we built the image we added a command that copied all the original files from your local directory (especially the data and the scripts) so the containers that you create from this image contains all the copied original scripts and data. Editing your local files will not modify the files in your container. You can edit the files in your container directly from the bash of the container using the VIM text editor. To open and edit a script you can use the command vi.

1
~$ vi WML-tutorial-deploy-model.py
You can now copy paste the deployment space id by the space ID of your deployment space. Once edited type :wq on your keyboard and press enter to save and return to the command line interface (CLI). Your file has been edited.

We recommend you to open the script WML-tutorial-deploy-model.py either locally with your favorite text editor or directly from the terminal via the vi command and carefully look through the procedure for deploying a model. Make sure you understand all the steps.

You can now run the deployment script from the container's bash.

1
~$ python WML-tutorial-deploy-model.py
O​nce the script has run, two tokens are printed : The \verb|model_uid|model_uid and the \verb|deployment_uid|deployment_uid copy these values and save them in a text file. We will need them to test the deployment.

3. Now we will test the deployment with the script WML-tutorial-test-model.py

Edit the the test script

1
~$ vi WML-test-deploy-model.py

Replace the Deployment space ID, the deployment UID and the model UID. Type :wq and press enter to save the modifications.  Then, run the test script.

1
~$ python WML-test-deploy-model.py 

See the API documentation of WML for more details about the interface. Also, see this related tutorial to deploy a scikit-learn model for another example.

We encourage you to try this with other models. Note that the lite plan for Watson Studio will only allow one instance of WML at a time, but it does allow several models.