#!/bin/bash
# while true; do sleep 15 ; echo "background"; done &

while true; do python "urban-traffic/scheduler.py"; sleep 60 ; done
