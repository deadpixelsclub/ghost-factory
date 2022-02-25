# ghost-factory

Dead Pixels Club Ghost Factory is a Python program that selects images based on weights and combines them in a user-specified order.  The distinguishing feature of this program is that it allows the user to define traits that conflict with one another so that images with those traits do not get generated.

## How To:
- Check if you have Python3 installed on your machine by starting up your terminal and running the command `python3 --version`.  If you see Python 3 or greater, then proceed.  If not, you'll need to install Python3 (you may have to Google how until I can update this README).
- Once you have Python3 installed, `git clone` this repo somewhere locally.
- Open the config.py file and set all your configuration (see comments in config.py).
- Open your terminal, navigate to your local copy of this repo, and run the command `python3 run.py`

If you run into any issues or have questions, feel free to open an issue in Github and we'll look into it.

# weights
- The weights are pulled from the filenames in the traits directory.  The individual traits should be named as follows:  value#weight.png.  
