# About
_Press Stitch_ is a set of Python scripts for the Press Switch visual novels by Skeigh. The scripts will stitch together content from earlier versions of the game to create one single game with paths from multiple versions.

The scripts do not contain any of Skeigh's content. You have to download the zip file for v0.5c of Press Switch and the scripts will patch it.

# Current status
The script patches Press Switch 0.5c to additionally contain:

* All paths from Press Switch 0.4, i.e. the main Eliza path and everything leading off it
* The Ciel path from Press Switch 0.3
* The Eliza / Elena clone path from Press Switch 0.3
* The Nurse path and ending from Press Switch 0.3
* The Nick paths from Press Switch 0.3

The resulting game has all paths fully playable, including the 0.5 paths.

## Content from 0.4
The 0.4 Eliza route starts with Eliza in her bedroom, but in 0.5 Eliza comes in to your room in the evening instead. So to access the 0.4 routes you must first kick Eliza out of your room, and then you will get a choice to reconsider. This leads to the 0.4 content.

This is also the way to access the Eliza / Elena cloning path.

## Content from 0.3
In 0.3 Ciel had blue hair and blue name text, but in 0.5 she is a brunette with brown name text. In the combined game she will appear as she does in 0.5 at all times, so this will look different to how it did in 0.3.

## Testing
Currently the scripts are beta-quality. Content from earlier versions appears to work and be graphically very close to the original games, but more play testing is needed. Bug reports and pull requests are gratefully received!

The scripts are developed and tested primarily on Linux, but they should work equally well on Windows. If you have any problems please submit a bug report.

# Download and Installation

## Windows
1. If you don't have Python installed, download it from [python.org](https://www.python.org/downloads/) and install it. While installing, check the "add to PATH" box.
2. Download the ZIP file for the project - press the green "Code" button above and select "Download ZIP".
3. Unzip it somewhere, this should create a folder called `press-stitch-main`.
4. Download the `Press-SwitchV0.5c-pc.zip` file from [TFGames](https://tfgames.site/index.php?module=viewgame&id=282) and put it in the `press-stitch-main` folder.
5. In the `press-stitch-main` folder, double-click the `press_stitch.py` script, and you should see it start to run in a command window. It will print lots of numbers and statistics as it runs, this is normal and you can ignore this. _PLEASE NOTE!_ This will take a long time, sometimes up to 15 minutes depending on your PC speed.
7. If everything completes correctly, there will now be a new folder called `Press-SwitchV0.5c-pc` which contains the patched game. Go into there and click on the `Press-Switch` application to play the game.

Note that you only need to do the steps above once! If you want to come back and play the game again, you can just run it like in step 6.

## Linux
On Linux you can use the system's Python 3, ensure it's installed using your system's package manager. For example, on Ubuntu you'd use `sudo apt install python3`. Otherwise the steps are the same as for Windows and the patched game can be run using the `Press-Switch.sh` script.
