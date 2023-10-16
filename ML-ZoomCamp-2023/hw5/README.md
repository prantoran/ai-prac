#### Use 3.10 in Conda env for Jupyter notebook for h5
conda create --name py10 python=3.10 
conda activate py10
conda deactivate

pipenv --python 3.10

#### Install Scikit Learn

pipenv install scikit-learn==1.3.1

#### Run server locally

gunicorn --bind 0.0.0.0:9696 predict:app

#### Pull docker image

docker pull svizor/zoomcamp-model:3.10.12-slim
docker pull svizor/zoomcamp-model

$ docker images | grep svizor
svizor/zoomcamp-model   3.10.12-slim   08266c8f0c4b   7 days ago      147MB

#### Build docker image

docker build -t zoomcamp-hw .

docker run -it --rm --entrypoint=bash zoomcamp-hw

#### Run docker image

docker run -it --rm -p 9696:9696 zoomcamp-hw