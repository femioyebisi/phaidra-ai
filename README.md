# Scraper Service for Phaidra Technical Interview Project

This scraper service is a simple web service that accepts a URL as a JSON POST request and returns the HTTP GET code of the given URL. It also exposes
a Prometheus metric that increments every time the service performs an HTTP GET request. Web server is powered by Flask project is written in Python

## Requirements

- Python 3.x
- Flask
- prometheus-client
- Docker
- Kubernetes cluster (AWS EKS or minikube for local development)

## Installation

1. Clone the repository:

```bash
git clone https://github.com/femioyebisi/phaidra_scraper_service.git
```

1. Go to the `/app` directory

```
cd app
```

1. Run install requirements and run app locally

```
pip install -r requirements.txt

python3 scraper_service.py
```

## **Usage**

To get the HTTP GET code of a URL, send a POST request to the service with the URL in the request body:

```
curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"url": "http://example.com"}' \
  http://localhost:8080
```

To view the Prometheus metrics, visit `http://localhost:9095/metrics` in your browser or send a GET request to the same URL.

## **Testing**

Run functional tests on app

```
python3 functional_tests.py
```

if no error in your code proceed to the next step

## **Docker**

To run the service in a Docker container, build the Docker image:

```
docker build -t scraper_service .
```

Then run the image:

```
docker run -p 8080:8080 -p 9095:9095 scraper_service
```

## **Prometheus Configuration**

To query the service with Prometheus, add the following to your prometheus.yml:

To add to your docker container

```
docker exec -it {{container_name}} sh
```

Create a your `prometheus.yml` file in `/etc/prometheus`

```
vi /etc/prometheus/prometheus.yml
```

And add the file below

```
scrape_configs:
  - job_name: 'scraper_service'
    static_configs:
      - targets: ['localhost:9095']
```

## **PromQL Query**

To get the total number of HTTP GET requests performed by the service, use the following PromQL query:

```
sum(http_get)
```

To get the total number of HTTP GET requests for a specific URL, use the following query:

```
sum(http_get{url="http://example.com"})
```

## **Kubernetes**

Go to the `k8s` folder

```
kubectl apply -f scraper_service_deployment.yml
```

```
kubectl describe services
```

Navigate to the provided external ip address

```
curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"url": "http://example.com"}' \
  http://{{kubernetes_service_external_ip_address}}:{{kubernetes_nodePort}}
```
