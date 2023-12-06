# All the Kubernetes configuration files for Tensorflow-serving and gateway.

## Load Docker images to Kind
```
kind load docker-image zoomcamp-10-model:xception-v4-001
```
## Kubectl apply deployment
```
kubectl apply -f model-deployment.yaml
```
```
kubectl get pod
```
- Output:
```
NAME                                         READY   STATUS    RESTARTS   AGE
tf-serving-clothing-model-55d9b7586b-x5tkv   1/1     Running   0          54s
```
---
kubectl describe pod tf-serving-clothing-model-55d9b7586b-x5tkv
```
- Output
```
Name:             tf-serving-clothing-model-55d9b7586b-x5tkv
Namespace:        default
Priority:         0
Service Account:  default
Node:             kind-control-plane/172.22.0.2
Start Time:       Tue, 05 Dec 2023 21:29:56 +0600
Labels:           app=tf-serving-clothing-model
                  pod-template-hash=55d9b7586b
Annotations:      <none>
Status:           Running
IP:               10.244.0.6
IPs:
  IP:           10.244.0.6
Controlled By:  ReplicaSet/tf-serving-clothing-model-55d9b7586b
Containers:
  tf-serving-clothing-model:
    Container ID:   containerd://6e9a19dbf61e6b49d805cdfd67b072a1121113c77bc3611e88f51448ce11c6b9
    Image:          zoomcamp-10-model:xception-v4-001
    Image ID:       docker.io/library/import-2023-12-05@sha256:3c70198e254daa6adb6fe9c8bf35827c94e182c5d0e4a735fadecd261bbb7c4b
    Port:           8500/TCP
    Host Port:      0/TCP
    State:          Running
      Started:      Tue, 05 Dec 2023 21:29:56 +0600
    Ready:          True
    Restart Count:  0
    Limits:
      cpu:     500m
      memory:  512Mi
    Requests:
      cpu:        500m
      memory:     512Mi
    Environment:  <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-s2kqv (ro)
Conditions:
  Type              Status
  Initialized       True 
  Ready             True 
  ContainersReady   True 
  PodScheduled      True 
Volumes:
  kube-api-access-s2kqv:
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
  Type    Reason     Age    From               Message
  ----    ------     ----   ----               -------
  Normal  Scheduled  2m24s  default-scheduler  Successfully assigned default/tf-serving-clothing-model-55d9b7586b-x5tkv to kind-control-plane
  Normal  Pulled     2m24s  kubelet            Container image "zoomcamp-10-model:xception-v4-001" already present on machine
  Normal  Created    2m24s  kubelet            Created container tf-serving-clothing-model
  Normal  Started    2m24s  kubelet            Started container tf-serving-clothing-model
```

## Port-forward
```
kubectl port-forward tf-serving-clothing-model-55d9b7586b-x5tkv 8500:8500
Forwarding from 127.0.0.1:8500 -> 8500
Forwarding from [::1]:8500 -> 8500
```

## Create Service
```
kubectl apply -f model-service.yaml 
kubectl get service
NAME                        TYPE           CLUSTER-IP     EXTERNAL-IP   PORT(S)        AGE
kubernetes                  ClusterIP      10.96.0.1      <none>        443/TCP        21h
tf-serving-clothing-model   ClusterIP      10.96.56.142   <none>        8500/TCP       14s
```

```
kubectl port-forward service/tf-serving-clothing-model 8500:8500
```

```
kind load docker-image zoomcamp-gateway:002
kubectl apply -f gateway-deployment.yaml 

kubectl port-forward gateway-675549d6bd-srpdv 9696:9696
kubectl logs gateway-675549d6bd-srpdv
```

```
kubectl apply -f gateway-service.yaml 
kubectl get service

kubectl port-forward service/gateway 8080:80