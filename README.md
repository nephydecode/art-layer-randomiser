# art-layer-randomiser

Creates a collection of random artwork with different art layers &amp; defined weighted probability

## Defining Traits

Each trait represents a layer of image - Background Layer / Body layer / Hair Layer. For each trait, the following are defined :

- (1) Trait Name (2) Trait Rarity (Weighted Probability) (3) Dictionary / Key-Value pair of Trait Name - File Name

For Optional Traits, include the weighted probability of not getting a trait & assign an empty string to that key-value pair.

```
mouth_acc = ["Blue Mask", "Green Mask", "Red Mask", "Yellow Mask", "None"]
mouth_acc_weights = [5, 5, 5, 5, 80]
mouth_acc_files = {"Blue Mask" : "facemask_blue", "Green Mask" : "facemask_green", "Red Mask" : "facemask_red", "Yellow Mask" : "facemask_yellow", "None" : ""}
```

## Image Traits Randomisation

This step creates & saves a List of the traits the randomised image has.

```
new_image = {}
new_image ["MouthAccessories"] = random.choices(mouth_acc, mouth_acc_weights)[0]
```

For traits that are dependent on other traits, they can also be defined or grouped together like the following.

```
    if new_image ["Body"] == "White":
        new_image ["Arm"] = random.choices(white_arm, white_arm_weights)[0]
    elif new_image ["Body"] == "Tanned":
        new_image ["Arm"] = random.choices(tanned_arm, tanned_arm_weights)[0]
```

To ensure that ALL generated images are UNIQUE, all the traits of a newly generated image is checked against previously generated images.

```
    if new_image in all_images:
        return create_new_image()
    else:
        return new_image
```

Based on the defined total no. of images, the image creation function is repeatedly called and aded into a list of `all_images`.

```
for i in range(50):
    new_trait_image = create_new_image()
    all_images.append(new_trait_image)
```

## TOKEN ID CREATION

For each generated image, a Token ID should also be generated along & assigned to identify the different images in the collection.

## IMAGE COMPOSITION

To create the image, the generated List of traits for each image will be taken and the corresponding image layers are opened layer by layer.

```
im1 = Image.open(f'./assets/Background/{background_files[item["Background"]]}.png').convert('RGBA')
```

For optional traits, remember to include a `try except` to catch the `FileNotFoundError` and assign an empty string to the image layer.

```
    try: im5 = Image.open(f'./assets/MouthAccessories/{mouth_acc_files[item["MouthAccessories"]]}.png').convert('RGBA')
    except FileNotFoundError: im5 = ""
```

Each of the layers are then composed in a procedural manner. Checks for empty layers or images are also done.

```
    com1 = Image.alpha_composite(im1, im2)
    com2 = Image.alpha_composite(com1, im3) if im3 != "" else com1
```

Once the entire image with all the layers / traits is composed, the image is converted into RGB format & saved as a filename corresponding to the token ID.

```
    rgb_im = com9.convert('RGB')
    file_name = str(item["tokenId"]) + ".png"
    rgb_im.save("./generated/" + file_name)
```

## OPTIONAL : COLLAGE CREATION

To make a collage of a series of the generated art, a new Image file with defined size & color is created. The no. of images to be included in the collage will also be defined. From the folder where the generated Images are located, the files will be opened, converted into RGBA, resized & pasted into the next available space (defined pixels & dimensions) in the collage. Once the entire collage is completed, it will be saved to defined directory.

```
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
```
