# ghost-factory

Dead Pixels Club Ghost Factory is a Python program that selects images based on weights and combines them in a user-specified order.  The distinguishing feature of this program is that it allows the user to define traits that conflict with one another so that images with those traits do not get generated.

## How To (MacOS):
1. Open `Terminal` or other command line tool and navigate to a location where you'd like to install the Ghost Factory.
2. Clone this repo via by running this command on the command line:  `git clone https://github.com/deadpixelsclub/ghost-factory-private.git`.
3. Mac may prompt you to install XCode or some other developer tools.  Yes, do that. 
4. In `Terminal` run this command: `python3 --version` to confirm that Python3 was installed on your machine.  If the output says Python 3 or greater, then proceed to step 5.  If not, you'll need to install Python3 (you may have to Google how until I have time to update this README).
5. In `Terminal` run this command: `python3 -m pip install --upgrade pip` to update the Python package manager (this is necessary for step 6 to complete successfully).
6.  In `Terminal` run this command: `pip3 install -r requirements.txt` to install the package that has the image layering tools.
7. Open the config.py file and set all your configuration (see comments in config.py).
8. In `Terminal` navigate to your local copy of this repo and run this command: `python3 run.py` to begin generating the images.

If you run into any issues or have questions, feel free to open an issue in Github and we'll look into it.

## weights
- The weights are pulled from the filenames in the traits directory.  The individual traits should be named as follows:  value#weight.png.
- The weights are relative to each other within each trait type.  For example, if we have 3 background trait files named red#1.png, blue#3.png, and yellow#5.png, then yellow will be selected more often than blue, and blue will be selected more often than red.  The exact weight methodology is determined by the `random.choice` function in the `random` package.  You can read about it here:  https://docs.python.org/3/library/random.html#random.choices.
- A `0` weight means the trait will NEVER be selected, so you can turn layers on/off by setting their weights to zero.
