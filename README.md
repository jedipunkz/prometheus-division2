# Prometheus-Division2

Division2 フレンドの成績を Prometheus に突っ込んで Grafana で可視化

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

- Linux OS or macos
- python3
- docker
- docker-compose

### Boot docker containers

Say what the step will be.

```bash
docker-compose build
docker-compose up --no-start
docker-compose start
```

Check the return by exectiong curl command as below.

```bash
curl http://localhost:8000
```

And now you can access grafana with a url as below.

http://<your_server_ip>:3000/

### re-deploy applications

Create new branch for new application

```bash
git checkout -b some_new_branch
```

Modify your application.

```bash
${EDITOR} app/prometheus-division2.py
```

Commit, Push, Merge,  and git pull all new applications. and execute `deploy.sh`.

```bash
bash deploy.sh
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

