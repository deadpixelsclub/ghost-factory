# Dead Pixels Club Ghost Factory

Dead Pixels Club Ghost Factory is a Python program that selects images based on weights and then stacks them to generate a specified number of unique images in png format.  The distinguishing feature of this program is that it allows the user to omit images that contain conflicting traits as well as images that may be unique but too similar.

## Install (MacOS)

1. Open `Terminal` or other command line tool and navigate to a location where you'd like to install the Ghost Factory.
2. Clone this repo via by running this command on the command line:  `git clone https://github.com/deadpixelsclub/ghost-factory-private.git`.
3. Mac may prompt you to install XCode or some other developer tools.  Yes, do that. 
4. In `Terminal` run this command: `python3 --version` to confirm that Python3 was installed on your machine.  If the output says Python 3 or greater, then proceed to step 5.  If not, you'll need to install Python3 (you may have to Google how until I have time to update this README).
5. In `Terminal` run this command: `python3 -m pip install --upgrade pip` to update the Python package manager (this is necessary for step 6 to complete successfully).
6. In `Terminal` run this command: `pip3 install -r requirements.txt` to install the package that has the image layering tools.
7. In `Terminal` navigate to your local copy of this repo and run this command: `python3 ghost_factory.py` to begin generating the test images.

If you run into any issues or have questions, feel free to open an issue in Github and we'll look into it.

## How To

1. Place image files associated with each trait (or "attributes" or "layers" or whatever you want to call them) in their respective trait type folder (i.e., background, eye, mouth, etc) inside of the `traits` folder.  You may set the relative weight of each trait by changing the filename to include a `#<weight>` at the end (see the Weights section below for more information).  The `traits` folder should have the following structure:

```
  .
  └── traits
      ├── background
      │   ├── red#1.png
      │   └── blue#1.png
      ├── eyes
      │   ├── blink#1.png
      │   └── squint#1.png
      └── mouth
          ├── smile#1.png
          └── smirk#1.png

```

2. Open the `config.py` file and set all your configurations (see Config below for instructions).
3. Open `Terminal`, navigate to your local copy of this repo, and run this command: `python3 ghost_factory.py` to begin generating your images.


### Weights

- The weights are pulled from the filenames in the traits directory.  The individual traits may be named as follows:  `name#weight.png`.
- The weights are relative to each other within each trait type.  For example, if we have 3 background trait files named red#1.png, blue#3.png, and yellow#5.png, then yellow will be selected more often than blue, and blue will be selected more often than red.  The exact weight methodology is determined by the `random.choice` function in the `random` package.  You can read about it here:  https://docs.python.org/3/library/random.html#random.choices.
- A `0` weight means the trait will NEVER be selected, so you can turn layers on/off by setting their weights to zero.
- If you do not include weights, each trait within a given trait type will have the same probability of being chosen.


### Config

This is an example `config.py` file:

```
{
  "n": 5, 
  "image_size": (1410, 1410)
  "name_prefix": "#", 
  "description": "Description of project.",
  "trait_base_path": "./traits/",
  "trait_type_order": ["background", "eyes", "mouth"], 
  "base_image_uri": "ipfs://NewUriToReplace/", 
  "conflicts": { 
      "solid_blue": ["expression_eyes", "expression_smirk"],
      "expression_smirk": ["eyewear_glasses_aviator"],
    },
  "skip_similar": "background",
  "additional_metadata": [{"creator": "Your Name"},
                          {"supply": 5}]
}
```

- `n` = Number of images to be generated.

- `image_size` = Pixel dimensions of the image (height, width).

- `name_prefix` = This gets prepended to the number of each generated image.  In the above config example, the images will be named `#1, #2, etc`, but if we set the `name_prefix` to "Ghost #", then the images will be named `Ghost #1, Ghost #2, etc`.

- `description` = Description of project.

- `trait_base_path` = Parent directory that contains the trait_type folders (e.g., background, eyes, mouth, etc).

- `trait_type_order` = The names in this list should be the same as the names of the folders in the `traits` folder.  The first trait type in the list will be treated as the lowest layer of the stacked images (typically, this would be the background).  The last trait type will be treated as the highest layer.

- `base_image_uri` = Base URI of image location.

- `conflicts` = Key-value pair where the key is a single trait name and the value is a list of one or more trait names that conflict with it.  In the above config example, images with a solid blue background will never contain the traits named `expression_eyes` or `expression_smirk`.  You may wish to configure `conflicts` for cases where two or more traits are not compatible, don't look good together, or for some other creative reason.

- `skip_similar` = If this key is in the config file, then the program will ignore the given trait type when determining if a given image has already been generated.  In the above config example, if image A and image B are identical in every way except for the `background` trait, then for the purposes of generating unique images they will be considered identical and one of them will NOT be generated.  

- `additional_metadata` = Anything that you may wish to include in the parent level of the metadata for each image.















