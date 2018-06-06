# Pavlok Brickout Game

This is a simple brickout-game. It's includes ball, paddle, brick wall
and additional collision detection between this objects. Furthermore logic for winning and losing and scoring.

The game runs at 60FPS.

I used a code sample for the basic structure of pygame from this site [http://programarcadegames.com/](http://programarcadegames.com/).

## Requirements

1. Python ~2.7
2. Pip

## Setup

```
# Run this command
sudo pip install -r requirements.txt

# Setup your secret key (Optional)
export SECRET_KEY="Your Secret key"
```

### Having troubles installing pygame on Mac OS?

```
# Assuming homebrew is installed already:
brew install mercurial
brew install sdl sdl_image sdl_mixer sdl_ttf portmidi
brew install smpeg

# You can new install Pygame
sudo -H pip install hg+http://bitbucket.org/pygame/pygame
```

## Running

```
# Run this command
sh run.sh
```
