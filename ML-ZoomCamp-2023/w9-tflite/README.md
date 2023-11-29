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

### Creating λ function
#### Setup CLI
```bash
pip install awscli
aws configure
```
#### Create repository for docker image
```bash
aws ecr create-repository --repository-name clothing-tflite-images
```
- Stdout:
```json
{
    "repository": {
        "repositoryArn": "arn:aws:ecr:us-west-1:xoxoxoxoxoxo:repository/clothing-tflite-images",
        "registryId": "xoxoxoxoxoxo",
        "repositoryName": "clothing-tflite-images",
        "repositoryUri": "xoxoxoxoxoxo.dkr.ecr.us-west-1.amazonaws.com/clothing-tflite-images",
        "createdAt": 1701256704.0,
        "imageTagMutability": "MUTABLE",
        "imageScanningConfiguration": {
            "scanOnPush": false
        },
        "encryptionConfiguration": {
            "encryptionType": "AES256"
        }
    }
}
```
#### Log into ecr
```
aws ecr get-login --no-include-email | sed 's/[0-9a-zA-Z=]\{20,\}/PASSOWRD/g'
$(aws ecr get-login --no-include-email)
```

```bash
ACCOUNT=xoxoxoxoxoxo
REGION=us-west-1
REGISTRY=clothing-tflite-images
PREFIX=${ACCOUNT}.dkr.ecr.${REGION}.amazonaws.com/${REGISTRY}

TAG=clothing-model-xception-v4-001
REMOTE_URI=${PREFIX}:${TAG}

echo $REMOTE_URI
    xoxoxoxoxoxo.dkr.ecr.us-west-1.amazonaws.com/clothing-tflite-images:clothing-model-xception-v4-001

docker tag clothing-model:latest ${REMOTE_URI}
docker push ${REMOTE_URI}
```