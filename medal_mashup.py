
from lib import lib
import pandas as pd
from PIL import Image
import requests
from io import BytesIO
import os.path
import sys

if len(sys.argv) < 2:
    print("Please provide a gamertag")
    sys.exit(1)

lib = lib({
    'token': "insert your token here"
})

version = "@1.4.0"
gamertag = sys.argv[1]
def getAllMedals(gamertag, season=None):
    medals = pd.DataFrame(lib.halo.infinite[version].metadata.multiplayer.medals()['data'])
    medals['image_urls'] = medals['image_urls'].apply(lambda x: x['large'])
    medals['count'] = 0

    result = lib.halo.infinite[version].stats.players['service-record'].multiplayer.matchmade.all({
        'gamertag': gamertag,
        'season': season,
    })
    medal_count = pd.DataFrame(result['data']['core']['breakdowns']['medals'])
    for i in range(len(medal_count)):
        medals.loc[medals['id'] == medal_count['id'][i], 'count'] = medal_count['count'][i]
    
    return medals

medals = getAllMedals(gamertag)

print(medals)

if len(sys.argv) == 3 and sys.argv[2] == "--save-images":

    for i in range(len(medals)):
        response = requests.get(medals['image_urls'][i])
        img = Image.open(BytesIO(response.content))
        img.save('.\images\\' + medals['name'][i] + '.png')

    path = ".\images"
    dirs = os.listdir(path)

    def crop():
        for item in dirs:
            if item not in ['Killing Spree.png']:
                fullpath = os.path.join(path, item)
                if os.path.isfile(fullpath):
                    im = Image.open(fullpath)
                    f, e = os.path.splitext(fullpath)
                    imCrop = im.crop((20, 20, 236, 236))
                    imCrop.save(f + 'Cropped.png', "png")

    crop()

    # delete all images but the cropped ones
    for item in dirs:
        if item not in ['Killing Spree.png']:
            fullpath = os.path.join(path, item)
            if os.path.isfile(fullpath):
                f, e = os.path.splitext(fullpath)
                if f + 'Cropped.png' not in os.listdir(path):
                    os.remove(fullpath)
        else:
            # rename the image by adding Cropped
            fullpath = os.path.join(path, item)
            f, e = os.path.splitext(fullpath)
            os.rename(fullpath, f + 'Cropped.png')

gephi = pd.DataFrame(columns=['source', 'weight', 'type', 'image'])
gephi['source'] = medals[medals['count'] != 0]['name']
gephi['weight'] = medals[medals['count'] != 0]['count']
gephi['type'] = medals[medals['count'] != 0]['type']
gephi['image'] = medals[medals['count'] != 0]['name']
gephi['image'] = gephi['image'].apply(lambda x: x + 'Cropped.png')

with open('halo.csv', 'w') as f:
    f.write('id')
gephi.to_csv('halo.csv', mode='a')

print("Done! Go to gephi and follow the rest of the tutorial.")