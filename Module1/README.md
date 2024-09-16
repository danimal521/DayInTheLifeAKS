# Module 1: Getting to know your Guerrilla
<!-- ![guerrilla](/Images/g1.png) -->

## Overview
Azure Kubernetes Service is large and has many facets to it. There is a lot to learn and understand and this can be daunting and intimidating. Let's demystify this and get to know our guerrilla!

At its core, let's think of AKS as a simple virtual machine. Let's think of containers like a simple application. Now we just have to copy our application to the virtual macing to run the app. That’s it, at the core this is all we are doing and what the whole system is designed to do. 

Now, take many years of software evolution and design. Outages, software management and devops. Scale and cloud compute and you end up with an platform that can handle any compute/application need and at scale. This is where things get a little more complicated, but it does not have to be. Always remember it's just about running applications.

Let's jump in! In this module we will connect to an AKS cluster and look around.

## Step 1: Connect to Azure
Our first step is to login to Azure with the CLI

```bash
az login
```

Then we have to make sure we set the environment to the correct subscription

```bash
az account set --subscription <your sub>
```

## Step 2: Connect to AKS
From the portal, navigate to your AKS cluster. You will need the cluster name and the resource group it was created in.

![guerrilla](/Images/aksportal.png)

Then connect to your cluster.

```bash
az aks get-credentials --resource-group <your RG> --name <your cluster name>
```

## Step 3: Let's look around

One of the first things to look at in a cluster are the namespaces. Namespaces are isolation layers in AKS, think of different groupings of applications or subject areas. Many also use it for different deployment tiers such as Development, UAT and Production.

The tool we use to interact with AKS is kubectl. 

```bash
kubectl get namespaces
```

Result: This is a new, blank cluster. By default there will be a few namespaces deployed.

```bash
NAME                STATUS   AGE
default             Active   3h8m
gatekeeper-system   Active   3h8m
kube-node-lease     Active   3h8m
kube-public         Active   3h8m
kube-system         Active   3h8m
```

Now going back to the whole VMs and Apps, let's look at nodes and deployments.

```bash
kubectl get nodes
```

Result: In this example there are 2 node pools (agent and user), and they both have 2 nodes (4 total, think 4 VMs).

```bash
aks-agentpool-41166359-vmss000000   Ready    <none>   3h7m   vx.x.x
aks-agentpool-41166359-vmss000001   Ready    <none>   3h7m   vx.x.x
aks-userpool-41166359-vmss000000    Ready    <none>   3h7m   vx.x.x
aks-userpool-41166359-vmss000001    Ready    <none>   3h7m   vx.x.x
```

Let's look at thoes applications or deployments.

```bash
kubectl get deployments
```

Result: Nothing, what happened? In a default cluster there will probably not be any deployment. Once again, namespaces are a great way to isolate different workloads in the same cluster. Let's look across ALL namespaces.

```bash
No resources found in default namespace.
```

We can add the --all-namespaces=true

```bash
kubectl get deployments --all-namespaces=true
```

Result: Now we have some deployments! 

```bash
NAMESPACE           NAME                    READY   UP-TO-DATE   AVAILABLE   AGE
gatekeeper-system   gatekeeper-audit        1/1     1            1           3h23m
gatekeeper-system   gatekeeper-controller   2/2     2            2           3h23m
kube-system         ama-logs-rs             1/1     1            1           3h20m
kube-system         azure-policy            1/1     1            1           3h23m
kube-system         azure-policy-webhook    1/1     1            1           3h23m
kube-system         coredns                 2/2     2            2           3h23m
kube-system         coredns-autoscaler      1/1     1            1           3h23m
kube-system         konnectivity-agent      2/2     2            2           3h23m
kube-system         metrics-server          2/2     2            2           3h23m
```

We have now looked at the basic parts of AKS in that we are ready to deploy our application! On to [Module 2](/Module2/README.md)!