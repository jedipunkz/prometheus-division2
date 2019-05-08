#!/bin/bash

export dir=/home/thirai/prometheus-division2

if [ $# != 1 ]; then
    echo "Error, arg number must be 1."
    exit 1
fi

case "$1" in
    stop) forever stop -c python $dir/prometheus-division2.py ;;
    start) forever start -c python $dir/prometheus-division2.py ;;
    list) forever list ;;
esac
