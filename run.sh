#!/bin/bash
set -v

# Run both scripts parallel
# python src/game.py & python src/services/PavlokServer.py && fg

python src/services/PavlokServer.py
