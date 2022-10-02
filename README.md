*Previously part of [WMDE (https://github.com/WeaselOnaStick/map-data-editor)](https://github.com/WeaselOnaStick/map-data-editor).*

# SharMemIO Features:
  - Allows you to monitor: `(credit to Lucas for figuring out correct pointers for this)`
    - game version
    - game state
    - current character name
    - whether the player is in a car or not
  - Allows you to read, copy and use as drivers the following in-game variables: `(credit to Lucas for figuring out correct pointers for this)`
    - player's position,
    - player's rotation,
    - car's position,
    - car's rotation
  - Ability to change refresh rate at which the add-on reads in-game variables
  - Ability to drive 3D cursor's location and rotation using in-game values (also can be used as a driver but not as practical)
  - Ability to automatically insert keyframes (at the frequency specified above) to any given object
    - Also adds convenience operator for playing/pausing scene's animation
    - and a checkbox to automatically extend scene duration 
  - Operator that teleports the player to 3D cursor's position (warning: can cause clipping with tall cars)

[Youtube video demo:](https://www.youtube.com/watch?v=JTSPDk3QBmw)
![SMIO](https://i.imgur.com/XZAnEDl.png)


# This add-on requires pymem python module! Here are 2 ways of installing it to blender's python
## Automatically if you have python installed globally:
  1. Open command console
  2. Execute following `pip install pymem`
## Manually if previous method didn't work:
  1. Manually download [pymem from pypi.org here https://pypi.org/project/Pymem/#files](https://pypi.org/project/Pymem/#files) (download the source Pymem-***.tar.gz file)
  2. Inside the archive you should find "pymem" module folder (it should have init.py file inside of it!)
  3. Copy the folder into the folder where blender stores its modules. The path by default for blender 2.93 is C:\Program Files\Blender Foundation\Blender 2.93\2.93\python\lib\site-packages
  4. After restarting blender, the add-on should work. If not, contact me!

# How To Install the addon:
Latest stable release:
 * [Download latest zip from https://github.com/WeaselOnaStick/SharMemIO/releases/tag/Release](https://github.com/WeaselOnaStick/SharMemIO/releases/tag/Release)
 * In Blender: `Edit` > `Preferences` > `Add-ons` > `Install...`
 * Choose a ZIP you just downloaded
 * Enable the add-on
