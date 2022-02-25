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
  value = filename.split("#")[0].split("$")[0]
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

def create_image_blueprint(image_blueprint_list, config):
    new_image_blueprint = {i['name']: random.choices(i["values"], i["weights"])[0] for i in config["trait_type_configs"]}
    
    for trait_a, conflict_list in config["conflicts"].items():
      for trait_b in conflict_list:
        if trait_a in str(new_image_blueprint) and trait_b in str(new_image_blueprint):
          return create_image_blueprint(image_blueprint_list, config)

    if new_image_blueprint in image_blueprint_list:
      return create_image_blueprint(image_blueprint_list, config)
    else:
      return new_image_blueprint

def main(config):
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
        attributes.append({"trait_type": key, "value": blueprint[key]})
    
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

  with open("./metadata/all-objects.json", "w") as outfile:
    json.dump(image_blueprint_list, outfile, indent=4)
  
  for item in image_blueprint_list:
    layers = [];
    for idx, trait in enumerate(item):
      if trait != "id":
        layers.append([])
        trait_path = os.path.join(config["trait_base_path"], config["trait_type_configs"][idx]["name"])
        trait_filename = trait_filenames[trait][item[trait]]
        layers[idx] = Image.open("{}/{}.png".format(trait_path, trait_filename))

    image = Image.new(mode="RGBA", size=config["image_size"], color="white")
    for layer in layers:
      image = Image.alpha_composite(image, layer.convert("RGBA"))
    
    filename = str(item["id"]) + ".png"
    image.save("./images/" + filename,"PNG")
    
    print("generated {} of {}".format(item["id"], config["n"]))

main(config)
