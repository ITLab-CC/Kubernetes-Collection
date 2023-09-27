
FROM python:3.7-alpine as builder
RUN apk add --no-cache git
COPY requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt
COPY . /docs
WORKDIR /docs
RUN mkdocs build

FROM nginx:alpine
COPY --from=builder /docs/site /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
