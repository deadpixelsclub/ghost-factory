config = {
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