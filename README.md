# machine_learning_project
first ml project
https://github.com/avnyadav/machine_learning_project
git - https://git-scm.com/downloads
Heroku
VS code

simple hello world flask app and deploy it on Heroku using docker
set the env path for anaconda installation to environment variable
run vscode and open the terminal -> command prompt
conda create -p venv python=3.7 -y
conda activate E:\Books\INueron-AI\machine_learning_project\venv
conda activate venv/
or
conda activate venv
pip install -r requirements.txt

git log
git add .
git commit
git push origin main
To check remote url
git remote -v

to setup CI/CD pipe line

HEROKU_EMAIL=vermaashishmca@gmail.com
HEROKU_API_KEY=010fe994-810d-44fe-8ca6-85ab9a926dc3
HEROKU_app_name=

configure above 3 parameters in git hub secrets

build docker image
docker build -t <image_name>:<tagname>

note: image name must be in lowercase

to list docker images

docker images

to run image

docker run -p 5000:5000 -e PORT=5000 <image ID>

to stop the docker

docker ps

to stop docker container 

docker stop <container ID>

deployed link

https://ml-regression-app.herokuapp.com/