# Module 3: Troubleshooting a deployment and Security
## Overview

In this module we will look at how to troubleshoot a deployment and get your pods up and running. We will also talk about security as, spoiler alert, the configuration issue we have is security related. In applications we have secrets. Things like connection strings and other app configurations have to live somewhere where we can manage but they also need to be secure. An easy service to use is Azure Key Vault! This allows us to manage our application keys in a secure fashion and gives us an easy UI to rotate and manage these secrets.

In AKS we run our containers in pods. These pods have a configuration. These configuration settings are set in the yaml deployments, like the one we did in module 2. In that, we could set all the secrets in that deployment file. However if someone was able to get that file, all our secrets would be in there. We could also set all the settings in the that same deployment file but that makes it harder to add new values. A great answer to this is having the settings to Azure Key Vault (KV) in the deployment, then having all the other keys in KV. If you app needs a new key, you just open KV and add it. If you need to change it you change it there as well. 

Here is a visual on this architecture.

![Arch](/Images/kv.png)


Going back to our troubled deployment, let's see if we can understand why out pod did not start. In  our previous step, we deployed the JokeAPI and did a get pods. This shows us the pods that are running in that namespace.


```bash
NAME                       READY   STATUS                       RESTARTS   AGE
jokeapi-6d99b5c898-pmjjx   0/1     CreateContainerConfigError   0          17m
```

Going back to our troubled deployment, let's see if we can understand why out pod did not start. In  our previous step, we deployed the JokeAPI and did a get pods. This shows us the pods that are running in that namespace.

Looking at the output, we have one pod (jokeapi-6d99b5c898-pmjjx) that has failed due to a configuration issue. Note the pod name is the name of the container (jokeapi) and a generated ID. This is the name of the pod, jokeapi-6d99b5c898-pmjjx. When we are troubleshooting pods, the two go to methods are logs and describe. Let's first use logs. 

Note: Most functions in kubectl use verbs like get and set. Logs does not use this as it’s a retrieval of running data as to meta data. Remember AKS is a desired state configuration environment. In essence we are pulling meta data about the deployment with get, I know confusing!

With this in mind, we run the following command, remember to use your pod name.

```bash
kubectl logs jokeapi-6d99b5c898-pmjjx -n production
```

Results: OK so whats this now? Bad requests and something about "waiting to start". If you look at the column ready, it shows 0/1. This pod is not running, so how can there be logs? In this scenario, the pod never started so there are no logs yet. As there is no logs lets go to the next troubleshooting method with "describe".

```bash
Error from server (BadRequest): container "jokeapi" in pod "jokeapi-6d99b5c898-pmjjx" is waiting to start: CreateContainerConfigError
```


```bash
kubectl describe pods jokeapi-6d99b5c898-pmjjx -n production
```

Result: OK now we have some information. Let look at a few things here. Toward the top we can see the image that was deployed. In this case 0.0.0. If we scroll to the bottom and look at the events we see the error. Error: secret "vaulturl" not found

If we go back to the deployment, we can is see in the env section, this deployment required a few settings (to KV above). Things like the vault URL and the ClientID.

There many ways to connect to KV. In this workshop, your IT team will provide you 4 pieces of information. We need: the Vault URL, Client ID, Client Secret and the Tenant ID. What is going to happen here is we will push these secrets to AKS. Then the deployment will securely take these secrets and push them to the pods. Then in the pod will have access to the KV, thus access to application secrets!