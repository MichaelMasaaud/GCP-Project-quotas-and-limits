# GCP Project quotas and limits
## Introduction :

Quotas on GCP Projects are enforced for a variety of reasons: for example, they protect the community of Google Cloud users by preventing unforeseen spikes in usage. Quotas also help you with resource management: for instance, you can set your own caps on service usage within your Google-provided quota while developing and testing your applications. Each quota limit is expressed in terms of a particular countable resource, from requests per day to an API to the number of load balancers used by your application.

Not all projects have the same quotas for the same services. If you are using a free trial account to explore the platform, for example, you may have a very limited quota. Higher quotas for some services are available only after you have enabled billing for your project. As your use of Google Cloud expands over time, your quotas may increase accordingly. You can also request more quota if you need it, and set up monitoring and alerts in Cloud Monitoring to warn you about unusual quota usage behavior or when you're running out of quota.

## Problem description :
 
Currently, I'm working with a big financial institution migrating a massive workload from on-prem and other cloud platforms to Google Cloud Platform.
After kicking off the project and lots of teams start using GCP services and resources we start hitting some limits and quotas on those projects so we got lots of automation scripts fails due to " reaching the limits Error " and to fix that problem we used to wait for 24 - 48 hours on Google Support team to increase the quota for that specific resource .


## Solution : 

We start thinking how we can take proactive actions on this issue so business would not be affected whenever quota increases needed . So I created that Python script which collected all the network metrics from all the Project on the customer organization and post all the results on BigQuery then we can export all the data using Data studio and create alerts if a certain quotas passed 80% utilization which enable the operation team to open a support ticket early for quota request in advance .



