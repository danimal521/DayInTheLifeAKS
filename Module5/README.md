# Module 5: Run and Upgrade!
## Overview
This is the exciting module! We can now run the application! In this module, we will also update the application with a new version. There are several ways to do this. Ultimately you will want to do this with a DevOps pipe but there will be times where you might need to manually update the deployment. 

The easiest way is to simply update the deployment. AKS as a system wants to maintain deployments with a desired state. You declare how you want the deployment to look like and AKS will make it so.

In the previous modules we deployed the JokeAPI. The application was set to create jokes about a programmer using AKS.

## Step 1: Let's run the application
Using the IP address from the previous step, lets open a browser and navigate to the Joke endpoint.

```bash
http://xxx.xxx.xxx.xxx/Joke
```

Result: A joke!

![ss](/Images/ss1.png)

## Step 2: Upgrade
There are several ways to upgrade the deployments. The most direct is to set the image.

```bash
kubectl set image deployments/jokeapi jokeapi=oceacr.azurecr.us/jokeapi:0.0.1 -n production
```

Result: Deployment updated.

```bash
deployment.apps/jokeapi image updated
```

AKS wants to manage these application with a desired state. You have now told AKS the desires state has changed. In that AKS will now reconcile the deployed images and you can see this happen.

If we quickly look at the pods we can see the update happening.

```bash
kubectl get pods -n production
```

The result (if we are fast enough) is one pod will be terminating and a new one will be starting or running. The new pod has the image we set above, thus upgraded.

```bash
NAME                       READY   STATUS        RESTARTS   AGE
jokeapi-5f69d74995-v2bsl   1/1     Terminating   0          61s
jokeapi-96b6b6c6-vmnxv     1/1     Running       0          5s
```

Now our JokeAPI take a parameter that is the joke prompt.
```bash
http://xxx.xxx.xxx.xxx/Joke?tell me a joke about a programmer using AKS
```

Result: A joke!

![ss](/Images/ss1.png)

We can always switch back to older versions. This is helpful if there is a production issue and we need to roll back.

```bash
kubectl set image deployments/jokeapi jokeapi=oceacr.azurecr.us/jokeapi:0.0.0 -n production
```

After the upgrade we will be back to the 0.0.0 version! Easy!