---
tags: [kubernetes, sharelatex, latex, overleaf]
---

# Overleaf / ShareLaTeX

- Create an MongoDB Replica Set by following the instructions in the [MongoDB Replica Set](/databases/mongodb) section.
- Create an Redis Standalone by following the instructions in the [Redis Standalone](/databases/redis) section. (We need to create a Redis Standalone because the Redis Cluster is not supported by ShareLaTeX)

## Installation

First you need to create a namespace for ShareLaTeX.

```bash
kubectl create namespace sharelatex-ns
```

Then you need to adjust the environment variables in the `sharelatex-deployment.yaml` file.

Set the following environment variables:

| Variable                      | Description                                      |
| ----------------------------- | ------------------------------------------------ |
| SHARELATEX_MONGO_URL          | The MongoDB connection string                    |
| SHARELATEX_REDIS_HOST         | The Redis host                                   |
| SHARELATEX_EMAIL_FROM_ADDRESS | The email address from which the emails are sent |
| SHARELATEX_EMAIL_SMTP_HOST    | The SMTP host                                    |
| SHARELATEX_EMAIL_SMTP_PORT    | The SMTP port                                    |
| SHARELATEX_EMAIL_SMTP_SECURE  | The SMTP secure flag                             |
| SHARELATEX_EMAIL_SMTP_USER    | The SMTP user                                    |
| SHARELATEX_EMAIL_SMTP_PASS    | The SMTP password                                |
| SHARELATEX_APP_NAME           | The name of the ShareLaTeX instance              |
| SHARELATEX_SITE_URL           | The URL of the ShareLaTeX instance               |
| SHARELATEX_ADMIN_EMAIL        | The email address of the admin                   |
| SHARELATEX_BEHIND_PROXY       | The behind proxy flag                            |
| SHARELATEX_SECURE_COOKIE      | The secure cookie flag                           |

Also adjust the `host` in the `sharelatex-ingress.yaml` file.

Then you can deploy ShareLaTeX.

```bash
kubectl apply -f .
```
