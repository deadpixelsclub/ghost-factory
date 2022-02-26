# ghost-factory

Dead Pixels Club Ghost Factory is a Python program that selects images based on weights and then stacks them to generate a specified number of unique images in png format.  The distinguishing feature of this program is that it allows the user to omit images that contain conflicting traits as well as images that may be too similar despite being technically unique.

## How It Works

Coming soon...

## Steps (MacOS)

1. Open `Terminal` or other command line tool and navigate to a location where you'd like to install the Ghost Factory.
2. Clone this repo via by running this command on the command line:  `git clone https://github.com/deadpixelsclub/ghost-factory-private.git`.
3. Mac may prompt you to install XCode or some other developer tools.  Yes, do that. 
4. In `Terminal` run this command: `python3 --version` to confirm that Python3 was installed on your machine.  If the output says Python 3 or greater, then proceed to step 5.  If not, you'll need to install Python3 (you may have to Google how until I have time to update this README).
5. In `Terminal` run this command: `python3 -m pip install --upgrade pip` to update the Python package manager (this is necessary for step 6 to complete successfully).
6.  In `Terminal` run this command: `pip3 install -r requirements.txt` to install the package that has the image layering tools.
7. Open the config.py file and set all your configurations (see comments in config.py).
8. In `Terminal` navigate to your local copy of this repo and run this command: `python3 ghost_factory.py` to begin generating the images.

If you run into any issues or have questions, feel free to open an issue in Github and we'll look into it.


### Weights

- The weights are pulled from the filenames in the traits directory.  The individual traits should be named as follows:  value#weight.png.
- The weights are relative to each other within each trait type.  For example, if we have 3 background trait files named red#1.png, blue#3.png, and yellow#5.png, then yellow will be selected more often than blue, and blue will be selected more often than red.  The exact weight methodology is determined by the `random.choice` function in the `random` package.  You can read about it here:  https://docs.python.org/3/library/random.html#random.choices.
- A `0` weight means the trait will NEVER be selected, so you can turn layers on/off by setting their weights to zero.


### Config

This is an example `config.py` file:

```
{
  "trait_type_order": ["background", "eyes", "mouth"], 
  "n": 9, 
  "conflicts": { 
      "trait_name1": ["trait_name_2", "trait_name_3"],
      "trait_name2": ["trait_name_4", trait_name_5],
    },
  "skip_similar": "background",
  "trait_base_path": "./traits/",
  "base_image_uri": "ipfs://NewUriToReplace/", 
  "image_size": (1410, 1410), #(height, width)
  "name_prefix": "#", 
  "description": "Description of project.",
  "additional_metadata": [{"creator": ""},
                          {"category": ""},  
                          {"supply": 100},
                          {"properties": {
                              "catalog": [],
                              "extras": [],
                              }
                            }
                          ]
}
```

- `trait_type_order` = List where the first element is the lowest layer of the stacked images.
- `n` = Number of images to be generated.
- `conflicts` = Key-value pair where the key is a single trait name and the value is a list of one or more trait names that conflict with it.
- `skip_similar` = If this key is in the config file, then the program will ignore the given trait type when determining if a given image has already been generated.  For example, if image A and image B have different background colors but are otherwise identical, they will be considered identical if the value in this field is `background`.
- `trait_base_path` = Parent directory that contains the trait_type folders (e.g., background, eyes, mouth, etc).
- `base_image_uri` = Base URI of image location.
- `image_size` = Pixel dimensions of trait files.
- `name_prefix` = This gets prepended to the number of each generated image.
- `description` = Description of project.
- `additional_metadata` = A list of dictionary items that you may wish to include in the parent level of the metadata for each image.















