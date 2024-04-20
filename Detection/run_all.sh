#!/bin/bash

python3 counting1.py &
python3 counting2.py &
python3 counting3.py &
python3 counting4.py &


wait

echo "All Python scripts have finished execution."