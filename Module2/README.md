# Module 2: Let's Deploy!
In this module we will deploy our backend API; the JokeAPI! This API was designed to use OpenAI to create jokes. As we said in module 1, AKS is all about running applications or deployments. We will deploy the API and explore some of the common tasks and commands you will use in AKS.

## Step 1: Let's create a namespace for our API
```bash
kubectl create ns production
```

Result: The namespace was created.


```bash
namespace/production created
```

Think of namespaces as isolation layers within AKS. We can now see the new namsepace with get namespaces

```bash
kubectl get namespaces
```

## Step 2: Let's deploy!

To deploy this application we need to tell AKS we want a deployment and describe what we want AKS to do. We do this with a yaml file and the deploy command. Navigate to the JokeAPI_0.0.0 folder and examine the deploy.yaml.

The basic yaml describes what needs to be deployed. Below is the basic example.

```bash
apiVersion: apps/v1
kind: Deployment
metadata:
  name: jokeapi
spec:
  selector:
    matchLabels:
      app: jokeapi
  replicas: 1
  template:
    metadata:
      labels:
        app: jokeapi
    spec:
      containers:
      - name: jokeapi
        image: youacr/jokeapi:0.0.0
```

To deploy, we need to "apply" a deployment, we use the following command:

```bash
kubectl apply -f deploy.yaml -n production
```

Result: The namespace was created.


```bash
deployment.apps/jokeapi configured
```

The first thing you normally do after you deploy a app to AKS is look at what pods are deployed. We can use the code below:

```bash
kubectl get pods -n production
```

Result: SUCCESS!... Oh wait a minute… what is "CreateContainerConfigError"?!

There are times when things do not go as planned (believe it or not)! What do we do when there is a deployment error? Let's mode to [Module 3](/Module3/README.md) and take a look!



```bash
NAME                       READY   STATUS                       RESTARTS   AGE
jokeapi-6d99b5c898-blfx5   0/1     CreateContainerConfigError   0          3m23s
```

