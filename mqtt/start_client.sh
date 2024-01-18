#!/bin/bash

for script in client_requester.py client_receiver.py
do
  python3 "$script" &
done

wait
