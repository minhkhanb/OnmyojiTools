<img align="right" width="300" src="https://raw.githubusercontent.com/AcademicDog/myresource/master/usage.png" alt="copy URL to clipboard" />

This project forks to [https://github.com/AcademicDog/onmyoji_bot/](https://github.com/AcademicDog/onmyoji_bot/) and makes the following changes:

* Added packaging related configuration
* Added compatibility of virtual environment
* New features


### Features

-Yuhun
  -Single player
  -As a driver, team up with Yuhun and automatically invite
  -Team up as a passenger and automatically accept the invitation
  -Double open Yuhun
-The original fire
  -Automatically brush greed, hatred, and idiot
-Yuling
  -Automatically refresh Yuling
-Explore
  -Complete exploration, identify experience monsters, support automatic change of dog food
-Other
  -During the battle, the script will automatically reject all invitations to reward seals.
  -If there is no operation in the 60s program (card machine, stamina, etc.), it will be deemed as exhausted. In order to protect the bonus, YYS will be automatically closed.
  -This script only uses the functions of screen color finding and mouse background clicking, completely simulating the behavior of human players, without using any memory read and write functions. A uniformly distributed random time drift and random coordinate drift are added to sensitive locations. **But there may still be usage risks**.

### Use environment

> Onmyoji PC version client, default resolution (1136x640)
>
> Windows 10 and Windows 7, screen (1920x1080), display setting 100%
>
> To run the source code, Python3 32-bit is required
* * *

# Instructions

### Single player brush Yuhun/Yeyuanhuo/Yuling

1. Open this tool and switch to the Yuhun tab;

1. In the game, enter the main interface of Yuhun/Yeyuanhuo/Yu Ling (the page with the "challenge" button), please prepare the shikigami in advance and **lock the lineup**;

1. Click the "Start" button of this tool.

### Team up to brush the soul

1. Open this tool, switch to the Yuhun tab, and select "Single Driver" or "Single Passenger" according to your own situation;

1. To enter the team page in the game, please prepare the shikigami in advance and **lock the lineup**;

1. Click the "Start" button of this tool.

### Single player exploration

1. Open this tool and switch to the Explore tab;

1. Put the dog food captain in the middle of the Onmyoji in the game in advance, and **cancel the locked lineup**;

1. Click on the chapter to be explored in the game (that is, the page with the "Explore" button);

1. Click the "Start" button of this tool.

* * *

# Precautions

1. Requires Windows 10 or Windows 7, screen (1920x1080), display setting 100%".

1. When using Windows 7 system, you need to adjust the screen settings of the system: set the theme to the ugliest and most frustrating one. In Windows 10 system, there is no need to adjust the system screen settings.

1. You need to turn off the computer's automatic screen rest/hibernation.

1. The window can now be completely background and can be obscured, but **cannot be minimized**.

1. Don't turn on the "model stroke" in the game.

1. Do not move the game window.

1. When using a high-resolution screen, in the Onmyoji client program compatibility option, do not check "Alternate high-DPI scaling behavior", this option should be unchecked by default.

1. The exe file may be quarantined by anti-virus software. If it is quarantined, it needs to be restored and added to the trust zone.

1. When running the script in the command line mode, do not left-click on the command line to avoid selecting the text, which may cause the process to pause and cause other problems. If you accidentally pause, press the space to continue the script. (You can also turn off the quick edit mode of the command line window in the window properties panel to avoid accidental interruption)

1. Need to lock the lineup.

1. To brush the soul, the homeowner needs to open the script in the room, and the passengers can open it in the room or in battle.

1. Remember to close the script if you pause in the middle, because the script will close the game if the operation timeout.

1. It is not recommended to use the brush to explore, the current recognition of the experience monster is not successful. When the N card is at full level, it will automatically change the N card by dragging the 40% progress bar of the N card and then dragging and dropping, so the user needs to close the shikigami fold. To brush a 2-star 1-level white egg, you need to turn on the God fold. There are currently bugs in brushing advanced white eggs, and there is a problem with automatic material change.

1. When exploring dog food change, if you turn off the scroll card change and replace it with the first N card, be careful not to click "Like" on the N card, which will cause you to repeatedly change to a full-level dog food .

1. The function of marking shikigami will mark the second shikigami on the left, and you need to close the shikigami skill animation

1. If you don't want to install the operating environment, you can visit releases to download the latest [compiled] version, which has a graphical interface, and note that the .exe file and the /img folder should be placed in the same directory before running.

# Run uncompiled script
Install python3.7.0
Installation dependencies
~~~
pip install -r requirements.txt
~~~
Run run.bat (if a virtual environment is used, edit the virtual environment path in runInVirtualEnv.bat, and then run bat)

# Packing instructions
Install pyinstaller, if you are using a virtual environment, you need to install and package it in the virtual environment
~~~
pip install pyinstaller
~~~
Package exe
~~~
pyinstaller -F -w ui.py
~~~
or
~~~
pyinstaller -F omj.py
~~~

Attention, there is a pit! ! !
> If there is no error in the exe packaging process, but the packaged exe cannot be opened (for example, an error is reported: the volume where the file is located has been changed, and the opened file is no longer valid), you can close the antivirus software and package it again