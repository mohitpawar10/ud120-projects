ud120-projects
==============

Starter project code for students taking Udacity ud120

Docker Set Up [Optional]
==============

If you want to install all software dependancies using docker. Just run following commands in the root directory.

docker build -t udacity-120-projects .

Above command will create docker image with all dependancies in the requirements file.

docker run -it --volume $(pwd):/usr/src/app udacity-120-projects

Above command will start the container and mount the current directory in the /usr/src/app. See the dockerfile for more info. 

docker exec -it udacity-120-projects /bin/bash

Using above command you can bash into the container and use all software.  