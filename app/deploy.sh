#!/bin/bash

sudo docker-compose stop app-prometheus-division2
sudo docker-compose rm app-prometheus-division2
sudo docker rmi  app-prometheus-division2
sudo docker-compose build app-prometheus-division2
sudo docker-compose up --no-start app-prometheus-division2
sudo docker-compose start app-prometheus-division2
