# About
_Press Stitch_ is a set of Python scripts for the Press Switch visual novels by Skeigh. The scripts will stitch together content from earlier versions of the game to create one single game with paths from multiple versions.

The scripts do not contain any of Skeigh's content. You have to download the zip file for v0.5c of Press Switch and the scripts will patch it.

# Current status
The script patches Press Switch 0.5c to contain the content from Press Switch 0.4, i.e. the main Eliza path. The resulting game has all paths from both 0.4 and 0.5 fully playable. The 0.4 game starts with Eliza in her bedroom, so to access the 0.4 routes you must first kick Eliza out of your room, and then you will get a choice to reconsider. This leads to the 0.4 content.

Currently the scripts are beta-quality. The game appears to work and be graphically very close to the 0.4 game, but more play testing is needed. Bug reports and pull requests are gratefully received!

The scripts are developed and tested primarily on Linux, but they should work equally well on Windows. If you have any problems please submit a bug report.

# Download and Installation
1. Clone the git repository
2. Download the `Press-SwitchV0.5c-pc.zip` file from [TFGames](https://tfgames.site/index.php?module=viewgame&id=282) and put in the base of the cloned repository
3. Run the `press_stitch.py` file using Python3. On Linux this should be as easy as: `python3 ./press_stitch.py`
4. The script will unzip, extract and patch the game into the directory `Press-SwitchV0.5c-pc`
5. If everything completes correctly, the game will be playable in that directory.
