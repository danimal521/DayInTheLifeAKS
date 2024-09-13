# Module 4: Service
## Overview
The JokeAPI is now in production. It is a Python Flask app API and now we need to access it. To access our API we need to deploy a service. 



## Step 1: Examine service
We can look to see what services we have with get service.

```bash
kubectl get service -n production
```

Result: We currently do not have an services deployed.

```bash
No resources found in production namespace.
```

## Step 2: Deploy service

There is a service deployment in the In the JokeAPI_0.0.0 folder. There are several ways to route traffic to out pods, this will use the external load balancer and give us a public IP to access the API.

```bash
kubectl apply -f service.yaml -n production
```

Result: The service deploys correctly.

```bash
service/jokeapifront created
```

## Step 3: Getting IP
Now is the fun part! With the service deployed we just need to get the services.

```bash
kubectl get service -n production
```
Result: Yeah! We have an ipaddress we can use (under EXTERNAL-IP).

```bash
NAME           TYPE           CLUSTER-IP    EXTERNAL-IP     PORT(S)        AGE
jokeapifront   LoadBalancer   10.0.116.23   x.x.x.22   80:32142/TCP   46h
```

Next lets access our API! [Module 5](/Module5/README.md) 