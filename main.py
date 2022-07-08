from re import A
from PIL import Image
import random
import json
import os

TOTAL_IMAGES = 50

## TRAITS

# Back Ground
background = ["White", "Grey", "Dark", "Black"]
background_weights = [25,25,25,25]
background_files = {"White" : "1", "Grey" : "2", "Dark" : "3", "Black" : "4", }

# Middle Ground
middle = ["Dark", "Light", "None"]
middle_weights = [25,25,50]
middle_files = {"Dark" : "1", "Light" : "2", "None" : ""}

# Head Gear
headgear = ["Sword", "None"]
headgear_weights = [30, 70]
headgear_files = {"Sword" : "1", "None": ""}

# Gender
gender = ["Male", "Female"]
gender_weights = [50,50]

# ==========  MALE PARTS ========== 
## clothes
mclothes = ["1", "2", "3", "None"]
mclothes_weights = [30,30,30,10]
mclothes_files = {"1" : "1", "2" : "2", "3" : "3", "None" : ""}

## eyes
meye = ["1", "2", "3"]
meye_weights = [33,33,34]
meye_files = {"1" : "1", "2" : "2", "3" : "3"}

## hair
mhair = ["1", "2", "3", "4", "5", "6", "7", "None"]
mhair_weights = [14, 14, 14, 14, 14, 14, 14, 2]
mhair_files = {"1" : "1", "2" : "2", "3" : "3", "4" : "4", "5" : "5", "6" : "6", "7" : "7", "None" : ""}

## mouth
mmouth = ["1", "2", "3"]
mmouth_weights = [33,33,34]
mmouth_files = {"1" : "1", "2" : "2", "3" : "3"}

# ========== FEMALE PARTS ========== 
## clothes
fclothes = ["1", "2", "3"]
fclothes_weights = [33,33,34]
fclothes_files = {"1" : "1", "2" : "2", "3" : "3"}

## eyes
feye = ["1", "2", "3"]
feye_weights = [33, 33, 34]
feye_files = {"1" : "1", "2" : "2", "3" : "3"}

## hair
fhair = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
fhair_weights = [11, 11, 11, 11, 11, 11, 11, 11, 11]
fhair_files = {"1" : "1", "2" : "2", "3" : "3", "4" : "4", "5" : "5", "6" : "6", "7" : "7", "8" : "8", "9" : "9"}

## mouth
fmouth = ["1", "2", "3"]
fmouth_weights = [33,33,34]
fmouth_files = {"1" : "1", "2" : "2", "3" : "3"}

## IMAGE RANDOMISATION FUNCTION

all_images = []

def create_new_image():

    new_image = {}

    new_image ["Background"] = random.choices(background, background_weights)[0]
    new_image ["Middle"] = random.choices(middle, middle_weights)[0]
    new_image ["Headgear"] = random.choices(headgear, headgear_weights)[0]
    new_image ["Gender"] = random.choices(gender, gender_weights)[0]
    if new_image ["Gender"] == "Male":
        new_image ["Hair"] = random.choices(mhair, mhair_weights)[0]
        new_image ["Eye"] = random.choices(meye, meye_weights)[0]
        new_image ["Mouth"] = random.choices(mmouth, mmouth_weights)[0]
        new_image ["Clothes"] = random.choices(mclothes, mclothes_weights)[0]
    elif new_image ["Gender"] == "Female":
        new_image ["Hair"] = random.choices(fhair, fhair_weights)[0]
        new_image ["Eye"] = random.choices(feye, feye_weights)[0]
        new_image ["Mouth"] = random.choices(fmouth, fmouth_weights)[0]
        new_image ["Clothes"] = random.choices(fclothes, fclothes_weights)[0]

    print(new_image)

    if new_image in all_images:
        return create_new_image()
    else:
        return new_image

## CALL IMAGE RANDOMISATION FUNCTION

for i in range(TOTAL_IMAGES):

    new_trait_image = create_new_image()

    all_images.append(new_trait_image)


## TOKEN ID CREATION

i = 0
for item in all_images:
    item["tokenId"] = i
    i += 1

## IMAGE CREATION
# TODO - REFACTOR THE SKIN, GENDER ELIF CASES

for i, item in enumerate(all_images):
    print(i)

    im1 = Image.open(f'./assets/Background/{background_files[item["Background"]]}.png').convert('RGBA')
    try : im2 = Image.open(f'./assets/Middleground/{middle_files[item["Middle"]]}.png').convert('RGBA')
    except FileNotFoundError: im2 = ""
    if item["Gender"] == "Male":
        im3 = Image.open(f'./assets/{item["Gender"]}/Body/1.png').convert('RGBA')
        im4 = Image.open(f'./assets/{item["Gender"]}/Eye/{meye_files[item["Eye"]]}.png').convert('RGBA')
        im5 = Image.open(f'./assets/{item["Gender"]}/Mouth/{mmouth_files[item["Mouth"]]}.png').convert('RGBA')
        try: im6 = Image.open(f'./assets/{item["Gender"]}/Hair/{mhair_files[item["Hair"]]}.png').convert('RGBA')
        except FileNotFoundError: im6 = ""
        try : im7 = Image.open(f'./assets/{item["Gender"]}/Clothes/{mclothes_files[item["Clothes"]]}.png').convert('RGBA')
        except FileNotFoundError: im7 = ""
    elif item["Gender"] == "Female":
        im3 = Image.open(f'./assets/{item["Gender"]}/Body/1.png').convert('RGBA')
        im4 = Image.open(f'./assets/{item["Gender"]}/Eye/{feye_files[item["Eye"]]}.png').convert('RGBA')
        im5 = Image.open(f'./assets/{item["Gender"]}/Mouth/{fmouth_files[item["Mouth"]]}.png').convert('RGBA')
        im6 = Image.open(f'./assets/{item["Gender"]}/Hair/{fhair_files[item["Hair"]]}.png').convert('RGBA')
        im7 = Image.open(f'./assets/{item["Gender"]}/Clothes/{fclothes_files[item["Clothes"]]}.png').convert('RGBA')

    try : im8 = Image.open(f'./assets/Headgear/{headgear_files[item["Headgear"]]}.png').convert('RGBA')
    except FileNotFoundError: im8 = ""

    com1 = Image.alpha_composite(im1, im2).convert('RGBA') if im2 != "" else im1  # background + middleground
    com2 = Image.alpha_composite(com1, im3).convert('RGBA') # body
    com3 = Image.alpha_composite(com2, im4).convert('RGBA') # eye
    com4 = Image.alpha_composite(com3, im5).convert('RGBA') # mouth
    com5 = Image.alpha_composite(com4, im6).convert('RGBA') if im6 != "" else com4 # hair
    com6 = Image.alpha_composite(com5, im7).convert('RGBA') if im7 != "" else com5 # clothes
    com7 = Image.alpha_composite(com6, im8).convert('RGBA') if im8 != "" else com6 # headgear

    rgb_im = com7.convert('RGB')
    file_name = str(item["tokenId"]) + ".png"
    rgb_im.save("./generated/" + file_name)

    collage = Image.new("RGBA", (5000,2500), color=(255,255,255,255))
    max = 50
    l = list(range(0,max))
    random.shuffle(l)
    c=0

for i in range(0,5000,500):
    for j in range(0,2500,500):
        file = "./generated/"+str(l[c])+".png"
        photo = Image.open(file).convert("RGBA")
        photo = photo.resize((500,500))
        collage.paste(photo, (i,j))
        c+=1

collage.save("./collage/collage.png")
print("done!")