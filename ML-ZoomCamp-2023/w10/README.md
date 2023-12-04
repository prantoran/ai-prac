

## Running TensorFlow Serving

```bash
docker run -it --rm \
    -p 8500:8500 \
    -v "$(pwd)/clothing-model:/models/clothing-model/1" \
    -e MODEL_NAME="clothing-model" \
    tensorflow/serving:2.7.0
```

## Debugging [breaking change](https://protobuf.dev/news/2022-05-06) in protobuf when running tf-serving
1. Create a new environment
```bash
conda create --name tf2 python=3.8
conda activate tf2
```
2. Install the specific versions of the following packages in the same pip command
```bash
pip install protobuf==3.19.0 grpcio==1.42.0 tensorflow-serving-api==2.7.0 jupyter keras-image-helper
```
Note:
- `tensorflow-serving-api` installs a number of packages (i.e. numpy) with versions that satisfy the constraints


### Converting ipynb to script
```bash
jupyter nbconvert --to script tf-serving-connect.ipynb
```

## Setup pipenv
```
pipenv install protobuf==3.19.0 grpcio==1.42.0 flask keras-image-helper gunicorn tensorflow-protobuf==2.7.0
```