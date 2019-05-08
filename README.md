# Prometheus-Division2

Division2 フレンドの成績を Prometheus に突っ込んで Grafana で可視化

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

- Python3 modules.

```
pip install requests
pip install prometheus_client
```

- docker
- docker-compose

### Boot docker containers

A step by step series of examples that tell you how to get a running

Say what the step will be.

```bash
bash run.sh start
```

check the return by exectiong curl command as below.

```bash
curl http://localhost:8000
```

boot docker containers

```bash
docker-compose -f docker-compose.yml create
docker-compose -f docker-compose.yml start
```


## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* [prometheus_client](https://github.com/prometheus/client_python) - Prometheus instrumentation library for Python applications
* Python3
* requests module


## Contributing

Submitting pull requests to me, and I welcome.

## Authors

* **jedipunkz** -

See also the blog [ジェダイさんのブログ](https://jedipunkz.github.io) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

