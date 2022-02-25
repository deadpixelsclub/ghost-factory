config = {
  "trait_type_order": ["background", "eyes", "mouth"], # Change to reflect your projects trait types
  "n": 5, # Number of images to generate
  "conflicts": { 
      "trait_name": ["conflicting_trait_name_1", "conflicting_trait_name_2", "conflicting_trait_name_3"], # Images where trait_name appears with any of the conflicting_trait_names will not be generated
      "trait_name2": ["conflicting_trait_name_1", "conflicting_trait_name_2", "conflicting_trait_name_3"],
    },
  "trait_base_path": "./traits/", # Name of folder containing trait types and their respective trait files
  "base_image_uri": "ipfs://NewUriToReplace/", 
  "image_size": (1410, 1410), #(height, width)
  "name_prefix": "#", # Can be anything
  "description": "Description of project.",
  "additional_metadata": [{"creator": ""},  # Values may be added or removed from this list.  The entire field may also be removed.
                          {"category": ""},  
                          {"supply": 100},
                          {"properties": {
                              "catalog": [],
                              "extras": [],
                              }
                            }
                          ]
}
