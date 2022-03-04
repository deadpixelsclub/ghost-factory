from PIL import Image
import random
import json
import os
from config import config

def listdir_nohidden(path):
  for f in os.listdir(path):
    if not f.startswith("."):
      yield f

def parse_filename(filename):
  value = filename.split("#")[0]
  filename_no_ext = filename.split(".")[0]
  weight = int(filename_no_ext.split("#")[1])
  return value, filename_no_ext, weight 

def get_trait_type_config(trait_base_path, trait_type):
  filepath = os.path.join(trait_base_path, trait_type) 
  trait_type_config = {}
  trait_type_config["name"] = trait_type
  trait_type_config["values"] = [parse_filename(f)[0] for f in listdir_nohidden(filepath)] 
  trait_type_config["filenames"] = [parse_filename(f)[1] for f in listdir_nohidden(filepath)]
  trait_type_config["weights"] = [parse_filename(f)[2] for f in listdir_nohidden(filepath)]
  return trait_type_config

def remove_key(d, key):
  r = dict(d)
  del r[key]
  return r

def create_image_blueprint(image_blueprint_list, config):
  
  # config['trait_type_configs']  -->  [{'name': 'background', 'values': ['blue', 'orange']}, {}. {}, ...]
  # new_image_blueprint           -->  {'background: 'blue', 'skin': 'white', ...}
  # config["conflicts"]           -->  [{'trait_type': 'background', 'value': 'blue', 'conflicts': ['hat_blue', ...]}, {}, {}, ...]

  new_image_blueprint = {i['name']: random.choices(i["values"], i["weights"])[0] for i in config["trait_type_configs"]}

  # skip conflicts
  for c in config["conflicts"]:
    for trait in new_image_blueprint:
      if c["value"] in new_image_blueprint[c["trait_type"]] and new_image_blueprint[trait] in c["conflicts"]:
        return create_image_blueprint(image_blueprint_list, config)

  # skip duplicates
  if new_image_blueprint in image_blueprint_list:
    return create_image_blueprint(image_blueprint_list, config)

  # skip similar
  if "skip_similar" in config:
    _new_image_blueprint = remove_key(new_image_blueprint, config['skip_similar'])
    _image_blueprint_list = [remove_key(i, config['skip_similar']) for i in image_blueprint_list]
    if _new_image_blueprint in _image_blueprint_list:
      return create_image_blueprint(image_blueprint_list, config)

  return new_image_blueprint

def reset_directory(path):
  for f in os.listdir(path):
    os.remove(os.path.join(path, f))

def main(config, metadata_only=False, color="white"):
  reset_directory("./metadata/")
  reset_directory("./images/")

  config["trait_type_configs"] = [get_trait_type_config(config["trait_base_path"], trait_type) for trait_type in config["trait_type_order"]]

  trait_filenames = {}
  
  for i in config["trait_type_configs"]:
    trait_filenames[i["name"]] = {}
    for idx, key in enumerate(i["values"]):
      trait_filenames[i["name"]][key] = i["filenames"][idx];
  
  image_blueprint_list = []
  for i in range(config["n"]):
    image_blueprint = create_image_blueprint(image_blueprint_list, config)
    image_blueprint_list.append(image_blueprint)

  i = 1
  for item in image_blueprint_list:
      item["id"] = i
      i += 1

  for blueprint in image_blueprint_list:
    attributes = []
    for key in blueprint:
      if key != "id":
        attributes.append({"trait_type": key, "value": blueprint[key].split("$")[0]})
    
    metadata = {
        "name":  config["name_prefix"] + str(blueprint["id"]),
        "description": config["description"],
        "image": config["base_image_uri"] + str(blueprint["id"]) + ".png",
        "id": blueprint["id"],        
        "attributes": attributes}

    if "additional_metadata" in config:
      for item in config["additional_metadata"]:
        metadata.update(item)

    metadata.update({"compiler": "Dead Pixels Club Ghost Factory"})
    
    with open("./metadata/" + str(blueprint["id"]) + ".json", "w") as outfile:
        json.dump(metadata, outfile, indent=4)

  with open("./all-objects.json", "w") as outfile:
    json.dump(image_blueprint_list, outfile, indent=4)
  
  if metadata_only:
    return

  print("Generating...")
  for count, item in enumerate(image_blueprint_list):
    layers = [];
    for idx, trait in enumerate(item):
      if trait != "id":
        layers.append([])
        trait_path = os.path.join(config["trait_base_path"], config["trait_type_configs"][idx]["name"])
        trait_filename = trait_filenames[trait][item[trait]]
        layers[idx] = Image.open("{}/{}.png".format(trait_path, trait_filename))

    image = Image.new(mode="RGBA", size=config["image_size"], color=color)
    for layer in layers:
      image = Image.alpha_composite(image, layer.convert("RGBA"))
    
    filename = str(item["id"]) + ".png"
    image.save("./images/" + filename,"PNG")
    
    if (count + 1) % 100 == 0:
      print("generated {} of {}".format(count + 1, config["n"]))

  print("Finished.  {} of {} generated".format(count + 1, config["n"]))

if __name__ == "__main__":
  main(config)
