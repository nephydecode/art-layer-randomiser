from re import A
from PIL import Image
import random
import json
import os

TOTAL_IMAGES = 50

## TRAITS

# gender = 6
background = ["Blue", "Grey", "Red", "Yellow", "Green", "Cyber"]
background_weights = [19,19,19,19,19,5]
background_files = {"Blue" : "background_blue", "Grey" : "background_grey", "Red" : "background_red", "Yellow" : "background_yellow", "Cyber" : "background_cyber", "Green" : "background_green", }

body = ["White", "Tanned"]
body_weights = [50,50]
body_files = {"White" : "body_white", "Tanned" : "body_tanned"}

white_arm = ["White Dagger", "White Fist", "None"]
white_arm_weights = [5,20, 75]
white_arm_files = {"White Dagger" : "white_dagger", "White Fist" : "white_fist", "None": ""}

tanned_arm = ["Tanned Dagger", "Tanned Fist", "None"]
tanned_arm_weights = [5,20, 75]
tanned_arm_files = {"Tanned Dagger" : "tanned_dagger", "Tanned Fist" : "tanned_fist", "None" : ""}

ear_acc = ["Blue Earring", "Green Earring", "Red Earring", "Yellow Earring", "None"]
ear_acc_weights = [7, 7, 7, 7, 72]
ear_acc_files = {"Blue Earring" : "earring_blue", "Green Earring" : "earring_green", "Red Earring" : "earring_red", "Yellow Earring" : "earring_yellow", "None" : ""}

mouth = ["Grin", "Smile", "Tongue Aloof", "Tongue Sheepish", "Tongue Side", "Pout"]
mouth_weights = [16,16,16,16,16,16]
mouth_files = {"Grin" : "mouth_grin", "Smile" : "mouth_smile", "Tongue Aloof" : "mouth_tongue_aloof", "Tongue Sheepish" : "mouth_tongue_sheepish", "Tongue Side" : "mouth_tongue_side", "Pout" : "mouth_pout"}

head_acc = ["Blue Beast Ears", "Green Beast Ears", "Red Beast Ears", "Yellow Beast Ears", "None"]
head_acc_weights = [5, 5, 5, 5, 80]
head_acc_files = {"Blue Beast Ears" : "beastears_blue", "Green Beast Ears" : "beastears_green", "Red Beast Ears" : "beastears_red", "Yellow Beast Ears" : "beastears_yellow", "None" : ""}

mouth_acc = ["Blue Mask", "Green Mask", "Red Mask", "Yellow Mask", "None"]
mouth_acc_weights = [5, 5, 5, 5, 80]
mouth_acc_files = {"Blue Mask" : "facemask_blue", "Green Mask" : "facemask_green", "Red Mask" : "facemask_red", "Yellow Mask" : "facemask_yellow", "None" : ""}

gender = [ "Man", "Woman" ]
gender_weights = [ 50, 50 ]

# man clothes = 14    # woman clothes = 16
man_clothes = ["Black Jersey", "Blue Jersey", "Green Jersey", "Pink Jersey", "Black Scarved Jersey", "Blue Scarved Jersey", "Green Scarved Jersey", "Pink Scarved Jersey", "Black Uniform", "Blue Uniform", "Green Uniform", "Red Uniform", "Teal Uniform", "Yellow Uniform"]
man_clothes_weights = [4, 8, 8, 8, 4, 8, 8, 8, 4, 8, 8, 8, 8, 8 ] # black = 4%, others = 8%
man_clothes_files = {"Black Jersey" : "jersey_black", "Blue Jersey" : "jersey_blue", "Green Jersey" : "jersey_green", "Pink Jersey" : "jersey_pink", "Black Scarved Jersey" : "scarved_jersey_black", "Blue Scarved Jersey" : "scarved_jersey_blue", "Green Scarved Jersey" : "scarved_jersey_green", "Pink Scarved Jersey" : "scarved_jersey_pink", "Black Uniform" : "uniform_black", "Blue Uniform" : "uniform_blue", "Green Uniform" : "uniform_green", "Red Uniform" : "uniform_red", "Teal Uniform" : "uniform_teal", "Yellow Uniform" : "uniform_yellow"}
woman_clothes = ["Black Bikini Arm", "White Bikini Arm", "White Bikini", "Black Bikini", "Black Offshoulder", "Blue Offshoulder", "Green Offshoulder", "Pink Offshoulder", "Teal Offshoulder", "Yellow Offshoulder", "Black Uniform", "Blue Uniform", "Green Uniform", "Pink Uniform", "Teal Uniform", "Yellow Uniform"]
woman_clothes_weights = [3, 3, 3, 3, 3, 8, 8, 8, 8, 8, 3, 8, 8, 8, 8, 8] 
woman_clothes_files = {"Black Bikini Arm" : "bikini_armband_black", "White Bikini Arm" : "bikini_armband_white", "White Bikini" : "bikini_white", "Black Bikini" : "bikini_black", "Black Offshoulder" : "offshoulder_black", "Blue Offshoulder" : "offshoulder_blue", "Green Offshoulder" : "offshoulder_green", "Pink Offshoulder" : "offshoulder_pink", "Teal Offshoulder" : "offshoulder_teal", "Yellow Offshoulder" : "offshoulder_yellow", "Black Uniform" : "uniform_black", "Blue Uniform" : "uniform_blue", "Green Uniform" : "uniform_green", "Pink Uniform" : "uniform_pink", "Teal Uniform" : "uniform_teal", "Yellow Uniform" : "uniform_yellow"}

# man/woman eyes = 18
man_eyes = ["Black Confident", "Blue Confident", "Green Confident", "Pink Confident", "Teal Confident", "White Confident", "Black Droopy", "Blue Droopy", "Green Droopy", "Pink Droopy", "Teal Droopy", "White Droopy", "Black Worried", "Blue Worried", "Green Worried", "Red Worried", "Teal Worried", "White Worried"]
man_eyes_weights = [7.5, 7.5, 7.5, 7.5, 7.5, 5, 3.6, 3.6, 3.6, 3.6, 3.6, 2, 5.4, 5.4, 5.4, 5.4, 5.4, 3]
man_eyes_files = {"Black Confident" : "eye_confident_black", "Blue Confident" : "eye_confident_blue", "Green Confident" : "eye_confident_green", "Pink Confident" : "eye_confident_pink", "Teal Confident" : "eye_confident_teal", "White Confident" : "eye_confident_white", "Black Droopy" : "eye_droopy_black", "Blue Droopy" : "eye_droopy_blue", "Green Droopy" : "eye_droopy_green", "Pink Droopy" : "eye_droopy_pink", "Teal Droopy" : "eye_droopy_teal", "White Droopy" : "eye_droopy_white", "Black Worried" : "eye_worried_black", "Blue Worried" : "eye_worried_blue", "Green Worried" : "eye_worried_green", "Red Worried" : "eye_worried_pink", "Teal Worried" : "eye_worried_teal", "White Worried" : "eye_worried_white"}
woman_eyes = ["Black Confident", "Blue Confident", "Green Confident", "Pink Confident", "Teal Confident", "White Confident", "Black Droopy", "Blue Droopy", "Green Droopy", "Pink Droopy", "Teal Droopy", "White Droopy", "Black Worried", "Blue Worried", "Green Worried", "Red Worried", "Teal Worried", "White Worried"]
woman_eyes_weights = [7.5, 7.5, 7.5, 7.5, 7.5, 5, 3.6, 3.6, 3.6, 3.6, 3.6, 2, 5.4, 5.4, 5.4, 5.4, 5.4, 3]
woman_eyes_files = {"Black Confident" : "eye_confident_black", "Blue Confident" : "eye_confident_blue", "Green Confident" : "eye_confident_green", "Pink Confident" : "eye_confident_pink", "Teal Confident" : "eye_confident_teal", "White Confident" : "eye_confident_white", "Black Droopy" : "eye_droopy_black", "Blue Droopy" : "eye_droopy_blue", "Green Droopy" : "eye_droopy_green", "Pink Droopy" : "eye_droopy_pink", "Teal Droopy" : "eye_droopy_teal", "White Droopy" : "eye_droopy_white", "Black Worried" : "eye_worried_black", "Blue Worried" : "eye_worried_blue", "Green Worried" : "eye_worried_green", "Red Worried" : "eye_worried_pink", "Teal Worried" : "eye_worried_teal", "White Worried" : "eye_worried_white"}

man_hair = ["Black Backcomb", "Blue Backcomb", "Green Backcomb", "Pink Backcomb", "White Backcomb", "Black Longcut", "Blue Longcut", "Green Longcut", "Pink Longcut", "White Longcut", "Black Shaggy", "Blue Shaggy", "Green Shaggy", "Pink Shaggy", "White Shaggy", "Black Spiked", "Blue Spiked", "Green Spiked", "Pink Spiked", "White Spiked"]
man_hair_weights = [5, 1.5, 1.5, 1.5, 0.5, 10, 3, 3, 3, 1, 15, 4.5, 4.5, 4.5, 1.5, 20, 6, 6, 6, 2]
man_hair_files = {"Black Backcomb" : "hair_backcombtail_black", "Blue Backcomb" : "hair_backcombtail_blue", "Green Backcomb" : "hair_backcombtail_green", "Pink Backcomb" : "hair_backcombtail_pink", "White Backcomb" : "hair_backcombtail_white", "Black Longcut" : "hair_longcut_black", "Blue Longcut" : "hair_longcut_blue", "Green Longcut" : "hair_longcut_green", "Pink Longcut" : "hair_longcut_pink", "White Longcut" : "hair_longcut_white", "Black Shaggy" : "hair_shaggy_black", "Blue Shaggy" : "hair_shaggy_blue", "Green Shaggy" : "hair_shaggy_green", "Pink Shaggy" : "hair_shaggy_pink", "White Shaggy" : "hair_shaggy_white", "Black Spiked" : "hair_spiked_black", "Blue Spiked" : "hair_spiked_blue", "Green Spiked" : "hair_spiked_green", "Pink Spiked" : "hair_spiked_pink", "White Spiked" : "hair_spiked_white"}
woman_hair = ["Black Bob", "Blue Bob", "Green Bob", "Pink Bob", "White Bob", "Black Lob", "Blue Lob", "Green Lob", "Pink Lob", "White Lob", "Black Long", "Blue Long", "Green Long", "Pink Long", "White Long", "Black Wave Bob", "Blue Wave Bob", "Green Wave Bob", "Pink Wave Bob", "White Wave Bob"]
woman_hair_weights = [15, 4.5, 4.5, 4.5, 1.5, 10, 3, 3, 3, 1, 10, 3, 3, 3, 1, 15, 4.5, 4.5, 4.5, 1.5]
woman_hair_files = {"Black Bob" : "hair_bob_black", "Blue Bob" : "hair_bob_blue", "Green Bob" : "hair_bob_green", "Pink Bob" : "hair_bob_pink", "White Bob" : "hair_bob_white", "Black Lob" : "hair_lob_black", "Blue Lob" : "hair_lob_blue", "Green Lob" : "hair_lob_green", "Pink Lob" : "hair_lob_pink", "White Lob" : "hair_lob_white", "Black Long" : "hair_longwave_black", "Blue Long" : "hair_longwave_blue", "Green Long" : "hair_longwave_green", "Pink Long" : "hair_longwave_pink", "White Long" : "hair_longwave_white", "Black Wave Bob" : "hair_wavebob_black", "Blue Wave Bob" : "hair_wavebob_blue", "Green Wave Bob" : "hair_wavebob_green", "Pink Wave Bob" : "hair_wavebob_pink", "White Wave Bob" : "hair_wavebob_white"}


## IMAGE RANDOMISATION FUNCTION

all_images = []

def create_new_image():

    new_image = {}

    new_image ["Background"] = random.choices(background, background_weights)[0]
    new_image ["Body"] = random.choices(body, body_weights)[0]
    if new_image ["Body"] == "White":
        new_image ["Arm"] = random.choices(white_arm, white_arm_weights)[0]
    elif new_image ["Body"] == "Tanned":
        new_image ["Arm"] = random.choices(tanned_arm, tanned_arm_weights)[0]
    new_image ["Background"] = random.choices(background, background_weights)[0]
    new_image ["EarAccessories"] = random.choices(ear_acc, ear_acc_weights)[0]
    new_image ["Mouth"] = random.choices(mouth, mouth_weights)[0]
    new_image ["MouthAccessories"] = random.choices(mouth_acc, mouth_acc_weights)[0]
    new_image ["HeadAccessories"] = random.choices(head_acc, head_acc_weights)[0]
    new_image ["Gender"] = random.choices(gender, gender_weights)[0]
    if new_image ["Gender"] == "Man":
        new_image ["Hair"] = random.choices(man_hair, man_hair_weights)[0]
        new_image ["Eyes"] = random.choices(man_eyes, man_eyes_weights)[0]
        new_image ["Clothes"] = random.choices(man_clothes, man_clothes_weights)[0]
    elif new_image ["Gender"] == "Woman":
        new_image ["Hair"] = random.choices(woman_hair, woman_hair_weights)[0]
        new_image ["Eyes"] = random.choices(woman_eyes, woman_eyes_weights)[0]
        new_image ["Clothes"] = random.choices(woman_clothes, woman_clothes_weights)[0]

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

for item in all_images:

    im1 = Image.open(f'./assets/Background/{background_files[item["Background"]]}.png').convert('RGBA')
    im2 = Image.open(f'./assets/Body/{body_files[item["Body"]]}.png').convert('RGBA')
    if item["Body"] == "White":
        try : im3 = Image.open(f'./assets/Arm/{item["Body"]}/{white_arm_files[item["Arm"]]}.png').convert('RGBA')
        except FileNotFoundError: im3 = ""
    elif item["Body"] == "Tanned":
        try : im3 = Image.open(f'./assets/Arm/{item["Body"]}/{tanned_arm_files[item["Arm"]]}.png').convert('RGBA')
        except FileNotFoundError: im3 = ""
    im4 = Image.open(f'./assets/Mouth/{mouth_files[item["Mouth"]]}.png').convert('RGBA')
    try: im5 = Image.open(f'./assets/MouthAccessories/{mouth_acc_files[item["MouthAccessories"]]}.png').convert('RGBA')
    except FileNotFoundError: im5 = ""

    if item["Gender"] == "Man":
        im6 = Image.open(f'./assets/Clothes/{item["Gender"]}/{man_clothes_files[item["Clothes"]]}.png').convert('RGBA')
        im7 = Image.open(f'./assets/Eyes/{item["Gender"]}/{man_eyes_files[item["Eyes"]]}.png').convert('RGBA')
        im8 = Image.open(f'./assets/Hair/{item["Gender"]}/{man_hair_files[item["Hair"]]}.png').convert('RGBA')
    elif item["Gender"] == "Woman":
        im6 = Image.open(f'./assets/Clothes/{item["Gender"]}/{woman_clothes_files[item["Clothes"]]}.png').convert('RGBA')
        im7 = Image.open(f'./assets/Eyes/{item["Gender"]}/{woman_eyes_files[item["Eyes"]]}.png').convert('RGBA')
        im8 = Image.open(f'./assets/Hair/{item["Gender"]}/{woman_hair_files[item["Hair"]]}.png').convert('RGBA')

    try:  im9 = Image.open(f'./assets/HeadAccessories/{head_acc_files[item["HeadAccessories"]]}.png').convert('RGBA')
    except FileNotFoundError: im9 = ""
    try:  im10 = Image.open(f'./assets/EarAccessories/{ear_acc_files[item["EarAccessories"]]}.png').convert('RGBA')
    except FileNotFoundError: im10 = ""

    # im1 = background, im2 = body
    com1 = Image.alpha_composite(im1, im2) 
    # im3 = arm
    com2 = Image.alpha_composite(com1, im3) if im3 != "" else com1
    # im4 = mouth
    com3 = Image.alpha_composite(com2, im4)
    # im5 = mouth accessories
    com4 = Image.alpha_composite(com3, im5) if im5 != "" else com3
    # im6 = clothes, im7 = eyes, im8 = hair
    com5 = Image.alpha_composite(com4, im6)
    com6 = Image.alpha_composite(com5, im7)
    com7 = Image.alpha_composite(com6, im8)
    # im9 = mouth accessories
    com8 = Image.alpha_composite(com7, im9) if im9 != "" else com7
    # im10 = mouth accessories
    com9 = Image.alpha_composite(com8, im10) if im10 != "" else com8

    rgb_im = com9.convert('RGB')
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