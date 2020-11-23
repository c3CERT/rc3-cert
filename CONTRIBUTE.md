# How-to Contribute

* Take a look on https://howto.rc3.world/maps.html
* Read the README as well.

## Install pre-push hook for image checks.
* pip3 install -p requirements.txt
* ln scripts/check_imgs.py .git/hooks/pre-commit

## What to contribute
### Sprites
* Only commit sprites you created yourself.
* Only single sprites, we will (re)generate the spritesheets for you.
* Make sure your sprite is dividable by 32px on both axis.
* We generate our spritesheets in alphabetical order, would be nice if your new sprites are already named to take their place at the end of the list.

### Maps
* No changes to main.json, basement.json or hackcenter.json
* Check if your new map is cert-related, there will be a huge (and unlimited) cluster of rc3 locations, you can create a independent map as well!
* Don't test map creation/editing in this repository, clone https://github.com/thecodingmachine/workadventure-map-starter-kit instead.

## Get your stuff in this repository
* Create a pull request (preferred)
* Send a mail to deinkoks@cert.ccc.de if your not familiar with git
