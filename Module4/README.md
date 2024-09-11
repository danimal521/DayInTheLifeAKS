# Module 4: Service
## Overview





In this module we will deploy our backend API; the JokeAPI! This API was designed to use OpenAI to create jokes. As we said in module 1, AKS is all about running applications or deployments. We will deploy the API and explore some of the common tasks and commands you will use in AKS.

## Step 1: Let's create a namespace for our API
```bash
kubectl create ns production
```