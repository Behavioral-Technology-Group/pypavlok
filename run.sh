#!/bin/bash
set -v

# Run both scripts parallel
python src/game.py & python src/services/PavlokServer.py && fg

# Can comment the above and comment either/or for debugging purposes
# python src/services/PavlokServer.py
# python src/game.py
