# SharMemIO
Previously part of [WMDE (https://github.com/WeaselOnaStick/map-data-editor)](https://github.com/WeaselOnaStick/map-data-editor).

This add-on allows you to read player's position (in/out of car), use that data to drive blender animation, and also to write player's position by teleporting to 3D cursor's position.

[Youtube video demo:](https://www.youtube.com/watch?v=JTSPDk3QBmw)
![SMIO](https://i.imgur.com/XZAnEDl.png)


# This add-on requires pymem python module! Here are 2 ways of installing it toblender's python
## Automatically if you have python installed globally:
  1. Open command console
  2. Execute following `pip install pymem`
## Manually if previous method didn't work:
  1. Manually download [pymem from pypi.org here https://pypi.org/project/Pymem/#files](https://pypi.org/project/Pymem/#files (download the source Pymem-***.tar.gz file)
  2. Inside the archive you should find "pymem" module folder (it should have init.py file inside of it!)
  3. Copy the folder into the folder where blender stores its modules. The path by default for blender 2.93 is C:\Program Files\Blender Foundation\Blender 2.93\2.93\python\lib\site-packages
  4. After restarting blender, the add-on should work. If not, contact me!

# How To Install the addon:
Latest stable release:
 * [Download latest zip from https://github.com/WeaselOnaStick/SharMemIO/releases/tag/Release](https://github.com/WeaselOnaStick/SharMemIO/releases/tag/Release)
 * In Blender: `Edit` > `Preferences` > `Add-ons` > `Install...`
 * Choose a ZIP you just downloaded
 * Enable the add-on
