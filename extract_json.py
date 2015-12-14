"""
Description: Converts recipe images and titles to json file for training caption
generation with NeuralTalk2: https://github.com/mkorpusik/neuraltalk2
"""

import json

path = "/afs/csail.mit.edu/u/n/nhynes/vision_nick/data/recipes/allrecipes.com/"

allrecipes = open(path+"recipe_data.txt")
res = []
num_recipes = 0
for line in allrecipes:
    recipe = json.loads(line)
    if 'title' not in recipe or 'id' not in recipe or 'photos' not in recipe:
        continue
    title = recipe['title']
    recipe_id = recipe['id']
    num_recipes += 1
    for img in recipe['photos']:
        img_path = path + 'photos/' + img['id']
        res.append({"captions":[title], "id":recipe_id, "file_path":img_path})

print "Number photos:", len(res)
print "Number recipes:", num_recipes
with open('allrecipes.json', 'w') as outfile:
    json.dump(res, outfile)
outfile.close()
