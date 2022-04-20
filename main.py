from re import A
from PIL import Image
import random
import json
import os

TOTAL_IMAGES = 50

## TRAITS

# gender = 6
# background = ["Blue", "Grey", "Red", "Yellow", "Green", "Cyber"]
background = ["Grey", "Red", "Teal", "White"]
# background_weights = [19,19,19,19,19,5]
background_weights = [25,25,25,25]
# background_files = {"Blue" : "background_blue", "Grey" : "background_grey", "Red" : "background_red", "Yellow" : "background_yellow", "Cyber" : "background_cyber", "Green" : "background_green", }
background_files = {"Grey" : "bg_grey", "Red" : "bg_red", "Teal" : "bg_teal", "White" : "bg_white", }

# 10
back = ["Battle Black", "Battle Green", "Battle Purple", "Battle Red", "Battle Yellow", "Machina Black", "Machina White", "Onmyouji Green", "Onmyouji Purple", "Onmyouji Yellow", "None"]
back_weights = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 50]
back_files = {"Battle Black" : "battle_black", "Battle Green" : "battle_green", "Battle Purple" : "battle_purple", "Battle Red" : "battle_red", "Battle Yellow" : "battle_yellow", "Machina Black" : "machina_black", "Machina White" : "machina_white", "Onmyouji Green" : "onmyouji_green", "Onmyouji Purple" : "onmyouji_purple", "Onmyouji Yellow" : "onmyouji_yellow", "None" : ""}

arm = ["Dagger", "None"]
arm_weights = [15, 85]
arm_files = {"Dagger" : "dagger", "None" : ""}

halo = ["Blue", "Teal", "Yellow", "None"]
halo_weights = [33, 33, 33, 1]q
halo_files = {"Blue" : "double_blue", "Teal" : "double_teal", "Yellow" : "double_yellow", "None" : ""}

ear_acc = ["Blue Earring", "Green Earring", "Red Earring", "Yellow Earring", "None"]
ear_acc = ["Round Blue", "Round Green", "Round Red", "Round Yellow", "Talis Black", "Talis Red", "Talis Teal", "Talis Yellow", "None"]
ear_acc_weights = [7, 7, 7, 7, 7, 7, 7, 7, 48]
ear_acc_files = {"Round Blue" : "round_blue", "Round Green" : "round_green", "Round Red" : "round_red", "Round Yellow" : "round_yellow", "Talis Black" : "talis_black", "Talis Red" : "talis_red", "Talis Teal" : "talis_teal", "Talis Yellow"  : "talis_yellow", "None" : ""}

mouth = ["Grin", "Smirk", "Aloof", "Sheepish", "Unimpressed", "Mischief"]
mouth_weights = [16,16,16,16,16,16]
mouth_files = {"Grin" : "mouth_grin", "Smile" : "mouth_smile", "Tongue Aloof" : "mouth_tongue_aloof", "Tongue Sheepish" : "mouth_tongue_sheepish", "Tongue Side" : "mouth_tongue_side", "Pout" : "mouth_pout"}
mouth_files = {"Grin" : "grin", "Smirk" : "smirk", "Aloof" : "aloof", "Sheepish" : "sheepish", "Unimpressed" : "unimpressed", "Mischief" : "mischief"}

head_acc = ["Blue Beast Ears", "Green Beast Ears", "Red Beast Ears", "Yellow Beast Ears", "None"]
head_acc_weights = [5, 5, 5, 5, 80]
head_acc_files = {"Blue Beast Ears" : "beastears_blue", "Green Beast Ears" : "beastears_green", "Red Beast Ears" : "beastears_red", "Yellow Beast Ears" : "beastears_yellow", "None" : ""}

mouth_acc = ["Blue Mask", "Green Mask", "Red Mask", "Yellow Mask", "None"]
mouth_acc = ["Cybermask Blue", "Cybermask Green", "Cybermask Red", "Cybermask Yellow", "Spike Mask Green", "Spike Mask Grey", "Spike Mask Pink", "Spike Mask Teal", "Veil Blue", "Veil Green", "Veil Grey", "Veil Teal", "None"]
mouth_acc_weights = [3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 3.5, 58]
mouth_acc_files = {"Cybermask Blue" : "cybermask_blue", "Cybermask Green": "cybermask_green", "Cybermask Red": "cybermask_red", "Cybermask Yellow": "cybermask_yellow", "Spike Mask Green": "spikemask_", "Spike Mask Grey": "spikemask_grey", "Spike Mask Pink": "spikemask_pink", "Spike Mask Teal": "spikemask_teal", "Veil Blue" : "veil_blue", "Veil Green" : "veil_green", "Veil Grey" : "veil_grey", "Veil Teal" : "veil_teal", "None" : ""}


gender = [ "Man", "Woman" ]
gender_weights = [ 50, 50 ]

body = ["White", "Tanned", "Red", "Blue", "Black"]
body_weights = [32.5,32., 12.5, 12.5, 10]
body_files = {"White" : "body_white", "Tanned" : "body_tanned", "Red" : "body_red", "Black" : "body_black", "Blue" : "body_blue"}

# man clothes = 14    # woman clothes = 16
man_clothes = ["Black Jersey", "Blue Jersey", "Green Jersey", "Pink Jersey", "Black Scarved Jersey", "Blue Scarved Jersey", "Green Scarved Jersey", "Pink Scarved Jersey", "Black Uniform", "Blue Uniform", "Green Uniform", "Red Uniform", "Teal Uniform", "Yellow Uniform"]
man_clothes_weights = [4, 8, 8, 8, 4, 8, 8, 8, 4, 8, 8, 8, 8, 8 ] # black = 4%, others = 8%
man_clothes_files = {"Black Jersey" : "jersey_black", "Blue Jersey" : "jersey_blue", "Green Jersey" : "jersey_green", "Pink Jersey" : "jersey_pink", "Black Scarved Jersey" : "scarved_jersey_black", "Blue Scarved Jersey" : "scarved_jersey_blue", "Green Scarved Jersey" : "scarved_jersey_green", "Pink Scarved Jersey" : "scarved_jersey_pink", "Black Uniform" : "uniform_black", "Blue Uniform" : "uniform_blue", "Green Uniform" : "uniform_green", "Red Uniform" : "uniform_red", "Teal Uniform" : "uniform_teal", "Yellow Uniform" : "uniform_yellow"}
woman_clothes = ["Black Bikini Arm", "White Bikini Arm", "White Bikini", "Black Bikini", "Black Offshoulder", "Blue Offshoulder", "Green Offshoulder", "Pink Offshoulder", "Teal Offshoulder", "Yellow Offshoulder", "Black Uniform", "Blue Uniform", "Green Uniform", "Pink Uniform", "Teal Uniform", "Yellow Uniform"]
woman_clothes_weights = [3, 3, 3, 3, 3, 8, 8, 8, 8, 8, 3, 8, 8, 8, 8, 8]  
woman_clothes_files = {"Black Bikini Arm" : "bikini_armband_black", "White Bikini Arm" : "bikini_armband_white", "White Bikini" : "bikini_white", "Black Bikini" : "bikini_black", "Black Offshoulder" : "offshoulder_black", "Blue Offshoulder" : "offshoulder_blue", "Green Offshoulder" : "offshoulder_green", "Pink Offshoulder" : "offshoulder_pink", "Teal Offshoulder" : "offshoulder_teal", "Yellow Offshoulder" : "offshoulder_yellow", "Black Uniform" : "uniform_black", "Blue Uniform" : "uniform_blue", "Green Uniform" : "uniform_green", "Pink Uniform" : "uniform_pink", "Teal Uniform" : "uniform_teal", "Yellow Uniform" : "uniform_yellow"}

# NEW : man clothes = 15   # woman clothes = 17
man_clothes = ["Avenger Green", "Avenger Purple", "Avenger Yellow", "Forcewalker Green", "Forcewalker Purple", "Forcewalker Yellow", "Lineros Green", "Lineros Purple", "Lineros Yellow", "Robe Green", "Robe Purple", "Robe Red", "Trainers Green", "Trainers Purple", "Trainers Red", "None"]
man_clothes_weights = [6.5, 6.5, 6.5, 6.5, 6.5, 6.5, 6.5, 6.5, 6.5, 6.5, 6.5, 6.5, 6.5, 6.5, 6.5, 2.5]
man_clothes_files = {"Avenger Green" : "avenger_green", "Avenger Purple" : "avenger_purple", "Avenger Yellow" : "avenger_yellow", "Forcewalker Green" : "forcewalker_green", "Forcewalker Purple" : "forcewalker_purple", "Forcewalker Yellow" : "forcewalker_yellow", "Lineros Green" : "lineros_green", "Lineros Purple" : "lineros_purple", "Lineros Yellow" : "lineros_yellow", "Robe Green" : "robe_green", "Robe Purple" : "robe_purple", "Robe Red" : "robe_red", "Trainers Green" : "trainers_green", "Trainers Purple" : "trainers_purple", "Trainers Red" : "trainers_red", "None" : ""}
woman_clothes = ["Barbay Black", "Barbay White", "Beach Black", "Beach White", "Choro Black", "Choro White", "Cybikini Black", "Cybikini White", "Kismet Green", "Kismet Purple", "Kismet Yellow", "Linnex Green", "Linnex Purple", "Linnex Red", "Ribbon Green", "Ribbon Purple", "Ribbon Red"]
woman_clothes_weights = [5.8, 5.8, 5.8, 5.8, 5.8, 5.8, 5.8, 5.8, 5.8, 5.8, 5.8, 5.8, 5.8, 5.8, 5.8, 5.8, 5.8]
woman_clothes_files = {"Barbay Black" : "barbay_black", "Barbay White" : "barbay_white", "Beach Black" : "beach_black", "Beach White" : "beach_white", "Choro Black" : "choro_black", "Choro White" : "choro_white", "Cybikini Black" : "cybikini_black", "Cybikini White" : "cybikini_white", "Kismet Green" : "kismet_green", "Kismet Purple" : "kismet_purple", "Kismet Yellow" : "kismet_yellow", "Linnex Green" : "linnex_green", "Linnex Purple" : "linnex_purple", "Linnex Red" : "linnex_red", "Ribbon Green" : "ribbon_green", "Ribbon Purple" : "ribbon_purple", "Ribbon Red" : "ribbon_red"}

# # man/woman eyes = 18
# man_eyes = ["Black Confident", "Blue Confident", "Green Confident", "Pink Confident", "Teal Confident", "White Confident", "Black Droopy", "Blue Droopy", "Green Droopy", "Pink Droopy", "Teal Droopy", "White Droopy", "Black Worried", "Blue Worried", "Green Worried", "Red Worried", "Teal Worried", "White Worried"]
# man_eyes_weights = [7.5, 7.5, 7.5, 7.5, 7.5, 5, 3.6, 3.6, 3.6, 3.6, 3.6, 2, 5.4, 5.4, 5.4, 5.4, 5.4, 3]
# man_eyes_files = {"Black Confident" : "eye_confident_black", "Blue Confident" : "eye_confident_blue", "Green Confident" : "eye_confident_green", "Pink Confident" : "eye_confident_pink", "Teal Confident" : "eye_confident_teal", "White Confident" : "eye_confident_white", "Black Droopy" : "eye_droopy_black", "Blue Droopy" : "eye_droopy_blue", "Green Droopy" : "eye_droopy_green", "Pink Droopy" : "eye_droopy_pink", "Teal Droopy" : "eye_droopy_teal", "White Droopy" : "eye_droopy_white", "Black Worried" : "eye_worried_black", "Blue Worried" : "eye_worried_blue", "Green Worried" : "eye_worried_green", "Red Worried" : "eye_worried_pink", "Teal Worried" : "eye_worried_teal", "White Worried" : "eye_worried_white"}
# woman_eyes = ["Black Confident", "Blue Confident", "Green Confident", "Pink Confident", "Teal Confident", "White Confident", "Black Droopy", "Blue Droopy", "Green Droopy", "Pink Droopy", "Teal Droopy", "White Droopy", "Black Worried", "Blue Worried", "Green Worried", "Red Worried", "Teal Worried", "White Worried"]
# woman_eyes_weights = [7.5, 7.5, 7.5, 7.5, 7.5, 5, 3.6, 3.6, 3.6, 3.6, 3.6, 2, 5.4, 5.4, 5.4, 5.4, 5.4, 3]
# woman_eyes_files = {"Black Confident" : "eye_confident_black", "Blue Confident" : "eye_confident_blue", "Green Confident" : "eye_confident_green", "Pink Confident" : "eye_confident_pink", "Teal Confident" : "eye_confident_teal", "White Confident" : "eye_confident_white", "Black Droopy" : "eye_droopy_black", "Blue Droopy" : "eye_droopy_blue", "Green Droopy" : "eye_droopy_green", "Pink Droopy" : "eye_droopy_pink", "Teal Droopy" : "eye_droopy_teal", "White Droopy" : "eye_droopy_white", "Black Worried" : "eye_worried_black", "Blue Worried" : "eye_worried_blue", "Green Worried" : "eye_worried_green", "Red Worried" : "eye_worried_pink", "Teal Worried" : "eye_worried_teal", "White Worried" : "eye_worried_white"}

# man/woman eyes = 9
man_eyes = ["Blue Confident", "Green Confident", "Pink Confident", "Blue Droopy", "Pink Droopy", "Yellow Droopy", "Blue Worried", "Pink Worried", "Yellow Worried"]
man_eyes_weights = [11, 11, 11, 11, 11, 11, 11, 11, 11]
man_eyes_files = {"Blue Confident" : "confident_blue", "Green Confident" : "confident_green", "Pink Confident" : "confident_pink", "Blue Droopy" : "droopy_blue", "Pink Droopy" : "droopy_pink", "Yellow Droopy" : "droopy_yellow", "Blue Worried" : "worried_blue", "Pink Worried" : "worried_pink", "Yellow Worried" : "worried_yellow"}
woman_eyes = ["Black Confident", "Blue Confident", "Pink Confident", "Blue Droopy", "Pink Droopy", "Black Droopy", "Blue Worried", "Pink Worried", "Black Worried"]
woman_eyes_weights = [11, 11, 11, 11, 11, 11, 11, 11, 11]
woman_eyes_files = {"Black Confident" : "confident_black", "Blue Confident" : "confident_blue", "Pink Confident" : "confident_pink", "Blue Droopy" : "droopy_blue", "Pink Droopy" : "droopy_pink", "Black Droopy" : "droopy_black", "Blue Worried" : "worried_blue", "Pink Worried" : "worried_pink", "Black Worried" : "worried_black"}

man_hair = ["Black Backcomb", "Blue Backcomb", "Green Backcomb", "Pink Backcomb", "White Backcomb", "Black Longcut", "Blue Longcut", "Green Longcut", "Pink Longcut", "White Longcut", "Black Shaggy", "Blue Shaggy", "Green Shaggy", "Pink Shaggy", "White Shaggy", "Black Spiked", "Blue Spiked", "Green Spiked", "Pink Spiked", "White Spiked"]
man_hair_weights = [5, 1.5, 1.5, 1.5, 0.5, 10, 3, 3, 3, 1, 15, 4.5, 4.5, 4.5, 1.5, 20, 6, 6, 6, 2]
man_hair_weights = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
man_hair_files = {"Black Backcomb" : "hair_backcombtail_black", "Blue Backcomb" : "hair_backcombtail_blue", "Green Backcomb" : "hair_backcombtail_green", "Pink Backcomb" : "hair_backcombtail_pink", "White Backcomb" : "hair_backcombtail_white", "Black Longcut" : "hair_longcut_black", "Blue Longcut" : "hair_longcut_blue", "Green Longcut" : "hair_longcut_green", "Pink Longcut" : "hair_longcut_pink", "White Longcut" : "hair_longcut_white", "Black Shaggy" : "hair_shaggy_black", "Blue Shaggy" : "hair_shaggy_blue", "Green Shaggy" : "hair_shaggy_green", "Pink Shaggy" : "hair_shaggy_pink", "White Shaggy" : "hair_shaggy_white", "Black Spiked" : "hair_spiked_black", "Blue Spiked" : "hair_spiked_blue", "Green Spiked" : "hair_spiked_green", "Pink Spiked" : "hair_spiked_pink", "White Spiked" : "hair_spiked_white"}

man_hair = ["Black Backcomb", "Blue Backcomb", "Green Backcomb", "Yellow Backcomb", "White Backcomb", "Black Wave", "Blue Wave", "Green Wave", "Yellow Wave", "White Wave", "Black Shaggy", "Blue Shaggy", "Grey Shaggy", "Yellow Shaggy", "White Shaggy", "Black Spiked", "Blue Spiked", "Green Spiked", "Yellow Spiked", "White Spiked"]
man_hair_files = {"Black Backcomb" : "backcombtail_black", "Blue Backcomb" : "backcombtail_blue", "Green Backcomb" : "backcombtail_green", "Yellow Backcomb" : "backcombtail_yellow", "White Backcomb" : "backcombtail_white", "Black Wave" : "wave_black", "Blue Wave" : "wave_blue", "Green Wave" : "wave_green", "Yellow Wave" : "wave_yellow", "White Wave" : "wave_white", "Black Shaggy" : "shaggy_black", "Blue Shaggy" : "shaggy_blue", "Grey Shaggy" : "shaggy_grey", "Yellow Shaggy" : "shaggy_yellow", "White Shaggy" : "shaggy_white", "Black Spiked" : "spiked_black", "Blue Spiked" : "spiked_blue", "Green Spiked" : "spiked_green", "Yellow Spiked" : "spiked_yellow", "White Spiked" : "spiked_white"}

woman_hair = ["Black Bob", "Blue Bob", "Green Bob", "Pink Bob", "White Bob", "Black Lob", "Blue Lob", "Green Lob", "Pink Lob", "White Lob", "Black Long", "Blue Long", "Green Long", "Pink Long", "White Long", "Black Wave Bob", "Blue Wave Bob", "Green Wave Bob", "Pink Wave Bob", "White Wave Bob"]
woman_hair_weights = [15, 4.5, 4.5, 4.5, 1.5, 10, 3, 3, 3, 1, 10, 3, 3, 3, 1, 15, 4.5, 4.5, 4.5, 1.5]
woman_hair_weights = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
woman_hair_files = {"Black Bob" : "hair_bob_black", "Blue Bob" : "hair_bob_blue", "Green Bob" : "hair_bob_green", "Pink Bob" : "hair_bob_pink", "White Bob" : "hair_bob_white", "Black Lob" : "hair_lob_black", "Blue Lob" : "hair_lob_blue", "Green Lob" : "hair_lob_green", "Pink Lob" : "hair_lob_pink", "White Lob" : "hair_lob_white", "Black Long" : "hair_longwave_black", "Blue Long" : "hair_longwave_blue", "Green Long" : "hair_longwave_green", "Pink Long" : "hair_longwave_pink", "White Long" : "hair_longwave_white", "Black Wave Bob" : "hair_wavebob_black", "Blue Wave Bob" : "hair_wavebob_blue", "Green Wave Bob" : "hair_wavebob_green", "Pink Wave Bob" : "hair_wavebob_pink", "White Wave Bob" : "hair_wavebob_white"}

woman_hair = ["Black Bob", "Blue Bob", "Green Bob", "Brown Bob", "White Bob", "Black Lob", "Blue Lob", "Green Lob", "Yellow Lob", "White Lob", "Black Long", "Blue Long", "Green Long", "Yellow Long", "White Long", "Black Bobwave", "Blue Bobwave", "Green Bobwave", "Red Bobwave", "White Bobwave"]
woman_hair_files = {"Black Bob" : "bob_black", "Blue Bob" : "bob_blue", "Green Bob" : "bob_green", "Brown Bob" : "bob_brown", "White Bob" : "bob_white", "Black Lob" : "lob_black", "Blue Lob" : "lob_blue", "Green Lob" : "lob_green", "Yellow Lob" : "lob_yellow", "White Lob" : "lob_white", "Black Long" : "longwave_black", "Blue Long" : "longwave_blue", "Green Long" : "longwave_green", "Yellow Long" : "longwave_yellow", "White Long" : "longwave_white", "Black Bobwave" : "bobwave_black", "Blue Bobwave" : "bobwave_blue", "Green Bobwave" : "bobwave_green", "Red Bobwave" : "bobwave_red", "White Bobwave" : "bobwave_white"}

## IMAGE RANDOMISATION FUNCTION

all_images = []

def create_new_image():

    new_image = {}

    new_image ["Background"] = random.choices(background, background_weights)[0]
    new_image ["Back"] = random.choices(back, back_weights)[0]
    if new_image ["Back"] == "None":
        new_image["Halo"] = "None"
    else:
        new_image["Halo"] = random.choices(halo, halo_weights)[0]
    new_image ["Body"] = random.choices(body, body_weights)[0]
    # if new_image ["Body"] == "White":
    #     new_image ["Arm"] = random.choices(white_arm, white_arm_weights)[0]
    # elif new_image ["Body"] == "Tanned":
    #     new_image ["Arm"] = random.choices(tanned_arm, tanned_arm_weights)[0]
    new_image ["Arm"] = random.choices(arm, arm_weights)[0]
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

for i, item in enumerate(all_images):

    im1 = Image.open(f'./assets/Background/{background_files[item["Background"]]}.png').convert('RGBA')
    try : im2 = Image.open(f'./assets/Back/{back_files[item["Back"]]}.png').convert('RGBA')
    except FileNotFoundError: im2 = ""
    if item["Gender"] == "Man":
        im3 = Image.open(f'./assets/Body/Man/{body_files[item["Body"]]}.png').convert('RGBA')
    elif item["Gender"] == "Woman":
        im3 = Image.open(f'./assets/Body/Woman/{body_files[item["Body"]]}.png').convert('RGBA')
    try : 
        im4 = Image.open(f'./assets/Arm/{item["Body"]}/{arm_files[item["Arm"]]}.png').convert('RGBA')
    except FileNotFoundError: im4 = ""
    # if item["Body"] == "White":
    #     try : im4 = Image.open(f'./assets/Arm/{item["Body"]}/{arm_files[item["Arm"]]}.png').convert('RGBA')
    #     except FileNotFoundError: im4 = ""
    # elif item["Body"] == "Tanned":
    #     try : im4 = Image.open(f'./assets/Arm/White/{item["Body"]}/{arm_files[item["Arm"]]}.png').convert('RGBA')
    #     except FileNotFoundError: im4 = ""
    im5 = Image.open(f'./assets/Mouth/{mouth_files[item["Mouth"]]}.png').convert('RGBA')
    try: im6 = Image.open(f'./assets/MouthAccessories/{mouth_acc_files[item["MouthAccessories"]]}.png').convert('RGBA')
    except FileNotFoundError: im6 = ""

    if item["Gender"] == "Man":
        try : im7 = Image.open(f'./assets/Clothes/{item["Gender"]}/{man_clothes_files[item["Clothes"]]}.png').convert('RGBA')
        except FileNotFoundError: im7 = ""
        im8 = Image.open(f'./assets/Eyes/{item["Gender"]}/{man_eyes_files[item["Eyes"]]}.png').convert('RGBA')
        im9 = Image.open(f'./assets/Hair/{item["Gender"]}/{man_hair_files[item["Hair"]]}.png').convert('RGBA')
    elif item["Gender"] == "Woman":
        im7 = Image.open(f'./assets/Clothes/{item["Gender"]}/{woman_clothes_files[item["Clothes"]]}.png').convert('RGBA')
        im8 = Image.open(f'./assets/Eyes/{item["Gender"]}/{woman_eyes_files[item["Eyes"]]}.png').convert('RGBA')
        im9 = Image.open(f'./assets/Hair/{item["Gender"]}/{woman_hair_files[item["Hair"]]}.png').convert('RGBA')

    try:  im10 = Image.open(f'./assets/HeadAccessories/{head_acc_files[item["HeadAccessories"]]}.png').convert('RGBA')
    except FileNotFoundError: im10 = ""
    try:  im11 = Image.open(f'./assets/EarAccessories/{ear_acc_files[item["EarAccessories"]]}.png').convert('RGBA')
    except FileNotFoundError: im11 = ""
    try:  im12 = Image.open(f'./assets/Halo/{halo_files[item["Halo"]]}.png').convert('RGBA')
    except FileNotFoundError: im12 = ""

    com1 = Image.alpha_composite(im1, im2) if im2 != "" else im1  # bg + wing
    com2 = Image.alpha_composite(com1, im3)  # body
    com3 = Image.alpha_composite(com2, im4) if im4 != "" else com2  # arm
    com4 = Image.alpha_composite(com3, im5) # mouth
    com5 = Image.alpha_composite(com4, im6) if im6 != "" else com4 # im5 = mouth accessories
    com6 = Image.alpha_composite(com5, im7) if im7 != "" else com5 # im6 = clothes, im7 = eyes, im8 = hair
    com7 = Image.alpha_composite(com6, im8)
    com8 = Image.alpha_composite(com7, im9)
    com9 = Image.alpha_composite(com8, im10) if im10 != "" else com8 # im9 = mouth accessories
    com10 = Image.alpha_composite(com9, im11) if im11 != "" else com9 # im10 = mouth accessories
    com11 = Image.alpha_composite(com10, im12) if im12 != "" else com10 # im12 = halo

    rgb_im = com11.convert('RGB')
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