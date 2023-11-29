#### Convert ipynb to py using `nbconvert`
```
jupyter nbconvert --to script w9-tflite.ipynb
```

### Docker
#### Build
```
docker build -t clothing-model .
```
#### Run
```
docker run -it --rm -p 8080:8080 clothing-model:latest
```