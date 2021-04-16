# About
_Press Stitch_ is a set of Python scripts for the Press Switch visual novels by Skeigh. The scripts will stitch together content from earlier versions of the game to create one single game with paths from multiple versions.

The scripts do not contain any of Skeigh's content. You have to download the zip file for v0.5c of Press Switch and the scripts will patch it.

# Current status
The script patches Press Switch 0.5c to additionally contain:

* All paths from Press Switch 0.4, i.e. the main Eliza path and everything leading off it
* The Ciel path from Press Switch 0.3

The resulting game has all paths fully playable, including the 0.5 paths.

## Content from 0.4
The 0.4 Eliza route starts with Eliza in her bedroom, but in 0.5 Eliza comes in to your room in the evening instead. So to access the 0.4 routes you must first kick Eliza out of your room, and then you will get a choice to reconsider. This leads to the 0.4 content.

## Content from 0.3
In 0.3 Ciel had blue hair and blue name text, but in 0.5 she is a brunette with brown name text. In the combined game she will appear as she does in 0.5 at all times, so this will look different to how it did in 0.3.

## Testing
Currently the scripts are beta-quality. Content from earlier versions appears to work and be graphically very close to the original games, but more play testing is needed. Bug reports and pull requests are gratefully received!

The scripts are developed and tested primarily on Linux, but they should work equally well on Windows. If you have any problems please submit a bug report.

# Download and Installation
The script is written for Python 3 and you should ensure this is installed first.

1. Download the ZIP file for the project (in the green "Code" button above) and unzip it somewhere. Alternatively you can clone the git repository, 
2. Download the `Press-SwitchV0.5c-pc.zip` file from [TFGames](https://tfgames.site/index.php?module=viewgame&id=282) and put it in the uncompressed project folder (or the base of the cloned repository if you've done that).
3. Run the `press_stitch.py` file using Python3. On Linux this should be as easy as: `python3 ./press_stitch.py`.
4. The script will unzip, extract and patch the game into the directory `Press-SwitchV0.5c-pc`. PLEASE NOTE! This will take a long time, sometimes up to 15 minutes depending on your PC speed.
5. If everything completes correctly, the game will be playable in that directory.
