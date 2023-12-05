

# Running TensorFlow Serving
## Directly from the terminal
```bash
docker run -it --rm \
    -p 8500:8500 \
    -v "$(pwd)/clothing-model:/models/clothing-model/1" \
    -e MODEL_NAME="clothing-model" \
    tensorflow/serving:2.7.0
```
## Using Dockerfile
```bash
docker build -t zoomcamp-10-model:xception-v4-001 -f image-model.dockerfile .

docker run -it --rm \
    -p 8500:8500 \
    zoomcamp-10-model:xception-v4-001
```
# Running Gateway using Dockerfile
```bash
docker build -t zoomcamp-gateway:002 -f image-gateway.dockerfile .

docker run -it --rm \
    -p 9696:9696 \
    zoomcamp-gateway:002
```

# Debugging [breaking change](https://protobuf.dev/news/2022-05-06) in protobuf when running tf-serving
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


## Converting ipynb to script
```bash
jupyter nbconvert --to script tf-serving-connect.ipynb
```

# Setup pipenv
```
pipenv install protobuf==3.19.0 grpcio==1.42.0 flask keras-image-helper gunicorn tensorflow-protobuf==2.7.0
```

# Kubernetes
- Node: Server/computer
    - Each node can have multiple containers/pods
- Pod: Docker container, runs on a node
- Deployment: Group of pods, with the image and config  
- Service: The entrypoint of an application, routes requests to pods
    - External: Load balancer
    - Internal: Cluster IP
- Ingres: The entrypoint to the cluster
- HPA: Horizontal Pod AutoScaler

## Deploying a simple ping applciation to Kubernetes
- Install kubectl & kind (for creating clusters locally)
- Setup a local Kubernetes cluster using Kind
- Create a deployment 
- Create a service
## Create cluster locally
```bash
kind create cluster
```
- output:
```
Creating cluster "kind" ...
 ✓ Ensuring node image (kindest/node:v1.27.3) 🖼 
 ✓ Preparing nodes 📦  
 ✓ Writing configuration 📜 
 ✓ Starting control-plane 🕹️ 
 ✓ Installing CNI 🔌 
 ✓ Installing StorageClass 💾 
Set kubectl context to "kind-kind"
You can now use your cluster with:

kubectl cluster-info --context kind-kind
```
## Start cluster
```bash
kubectl cluster-info --context kind-kind
```
- Output:
```
Kubernetes control plane is running at https://127.0.0.1:35397
CoreDNS is running at https://127.0.0.1:35397/api/v1/namespaces/kube-system/services/kube-dns:dns/proxy

To further debug and diagnose cluster problems, use 'kubectl cluster-info dump'.
```
## Check whether cluster is created
```bash
kubectl get service
```
- Output:
```
NAME         TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)   AGE
kubernetes   ClusterIP   10.96.0.1    <none>        443/TCP   21m
```
```
kubectl get pod
> No resources found in default namespace.
kubectl get deployments
> No resources found in default namespace.
```
```
docker ps
```
- Output:
```
CONTAINER ID   IMAGE                  COMMAND                  CREATED          STATUS          PORTS                                       NAMES
b16f665b5cae   kindest/node:v1.27.3   "/usr/local/bin/entr…"   26 minutes ago   Up 26 minutes   127.0.0.1:35397->6443/tcp                   kind-control-plane
```
- `Kind` creates cluster locally using `Docker`
## Apply `deployment.yaml` using `kubectl`
```
kubectl apply -f deployment.yaml
> deployment.apps/ping-deployment created
```
## Check:
```
kubectl get deployment
```
- Output:
```
NAME              READY   UP-TO-DATE   AVAILABLE   AGE
ping-deployment   0/1     1            0           77s
```
```
kubectl get pod
```
- Output:
```
NAME                               READY   STATUS             RESTARTS   AGE
ping-deployment-6b67c67c45-qw5s8   0/1     ImagePullBackOff   0          4m42s
```
```
kubectl describe pod ping-deployment-6b67c67c45-qw5s8
```
- Output:
```
Name:             ping-deployment-6b67c67c45-qw5s8
Namespace:        default
Priority:         0
Service Account:  default
Node:             kind-control-plane/172.22.0.2
Start Time:       Tue, 05 Dec 2023 19:08:11 +0600
Labels:           app=ping
                  pod-template-hash=6b67c67c45
Annotations:      <none>
Status:           Pending
IP:               10.244.0.5
IPs:
  IP:           10.244.0.5
Controlled By:  ReplicaSet/ping-deployment-6b67c67c45
Containers:
  ping-pod:
    Container ID:   
    Image:          ping:001
    Image ID:       
    Port:           9696/TCP
    Host Port:      0/TCP
    State:          Waiting
      Reason:       ImagePullBackOff
    Ready:          False
    Restart Count:  0
    Limits:
      cpu:     500m
      memory:  128Mi
    Requests:
      cpu:        500m
      memory:     128Mi
    Environment:  <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-5jtpj (ro)
Conditions:
  Type              Status
  Initialized       True 
  Ready             False 
  ContainersReady   False 
  PodScheduled      True 
Volumes:
  kube-api-access-5jtpj:
    Type:                    Projected (a volume that contains injected data from multiple sources)
    TokenExpirationSeconds:  3607
    ConfigMapName:           kube-root-ca.crt
    ConfigMapOptional:       <nil>
    DownwardAPI:             true
QoS Class:                   Guaranteed
Node-Selectors:              <none>
Tolerations:                 node.kubernetes.io/not-ready:NoExecute op=Exists for 300s
                             node.kubernetes.io/unreachable:NoExecute op=Exists for 300s
Events:
  Type     Reason     Age                     From               Message
  ----     ------     ----                    ----               -------
  Normal   Scheduled  8m23s                   default-scheduler  Successfully assigned default/ping-deployment-6b67c67c45-qw5s8 to kind-control-plane
  Normal   Pulling    6m38s (x4 over 8m23s)   kubelet            Pulling image "ping:001"
  Warning  Failed     6m23s (x4 over 8m17s)   kubelet            Failed to pull image "ping:001": rpc error: code = Unknown desc = failed to pull and unpack image "docker.io/library/ping:001": failed to resolve reference "docker.io/library/ping:001": pull access denied, repository does not exist or may require authorization: server message: insufficient_scope: authorization failed
  Warning  Failed     6m23s (x4 over 8m17s)   kubelet            Error: ErrImagePull
  Warning  Failed     6m10s (x6 over 8m17s)   kubelet            Error: ImagePullBackOff
  Normal   BackOff    3m13s (x18 over 8m17s)  kubelet            Back-off pulling image "ping:001"
```
## Load local Docker image into Kind
```
kind load docker-image ping:001
```
- Output:
```
Image: "ping:001" with ID "sha256:3ba5cb50e1a5cde7b4b000f8bc23911c3ea2310db428600841b701efebed0fb5" not yet present on node "kind-control-plane", loading...
```
## Test Deployment before creating Service
- Port-forwarding using `kubectl` to connect container's port with laptop's port.
```
kubectl port-forward ping-deployment-6b67c67c45-qw5s8 9696:9696
```
Test using curl
```
curl localhost:9696/ping
```
## Apply `service.yaml` using `kubectl`
```
kubectl apply -f service.yaml 
```
### Check:
```
kubectl get service
kubectl get svc
```
- Output:
```
NAME         TYPE        CLUSTER-IP    EXTERNAL-IP   PORT(S)   AGE
kubernetes   ClusterIP   10.96.0.1     <none>        443/TCP   5h44m
ping         ClusterIP   10.96.11.16   <none>        80/TCP    67s
```
## Change service type to LoadBalancer
```yaml
// service.yaml
apiVersion: v1
kind: Service
metadata:
  name: ping
spec:
  type: LoadBalancer
  selector:
    app: ping
  ports:
  - port: 80
    targetPort: 9696
```
```
kubectl apply -f service.yaml
```
- Output:
```
NAME         TYPE           CLUSTER-IP    EXTERNAL-IP   PORT(S)        AGE
kubernetes   ClusterIP      10.96.0.1     <none>        443/TCP        6h11m
ping         LoadBalancer   10.96.11.16   <pending>     80:32086/TCP   28m
```
- External-IP will forever be in <pending> state for local Kind cluster.
### Check
```
kubectl port-forward service/ping 8080:80
```
- Output
```
Forwarding from 127.0.0.1:8080 -> 9696
Forwarding from [::1]:8080 -> 9696
```
```
curl localhost:8080/ping
```