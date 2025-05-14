from PIL import Image, ImageFont, ImageDraw

white = (255,255,255,255)
black = (0,0,0,255)

font = ImageFont.truetype("MinecraftStandard.otf", 24)

def draw_note(draw, note, scale_pos):
    match note:
        case 0:
            draw.text((10,148-14), scale_pos, font=font, fill=black)
        case 1:
            draw.text((28,84-13), scale_pos, font=font, fill=white)
        case 2:
            draw.text((47,148-14), scale_pos, font=font, fill=black)
        case 3:
            draw.text((66,84-13), scale_pos, font=font, fill=white)
        case 4:
            draw.text((85,148-14), scale_pos, font=font, fill=black)
        case 5:
            draw.text((122,148-14), scale_pos, font=font, fill=black)
        case 6:
            draw.text((141,84-13), scale_pos, font=font, fill=white)
        case 7:
            draw.text((160,148-14), scale_pos, font=font, fill=black)
        case 8:
            draw.text((178,84-13), scale_pos, font=font, fill=white)
        case 9:
            draw.text((197,148-14), scale_pos, font=font, fill=black)
        case 10:
            draw.text((216,84-13), scale_pos, font=font, fill=white)
        case 11:
            draw.text((235,148-14), scale_pos, font=font, fill=black)


def note_to_number(root): # WIP
    #C is 0, C#/Db is 1, D is 2, etc. C is 0 because the images use C as the left-most note.
    if root == "C":
        return 0
    elif root == "C#" or root == "Db":
        return 1
    elif root == "D":
        return 2
    elif root == "D#" or root == "Eb":
        return 3
    elif root == "E":
        return 4
    elif root == "F":
        return 5
    elif root == "F#" or root == "Gb":
        return 6
    elif root == "G":
        return 7
    elif root == "G#" or root == "Ab":
        return 8
    elif root == "A":
        return 9
    elif root == "A#" or root == "Bb":
        return 10
    elif root == "B":
        return 11
    else:
        raise Exception("Invalid Note")
    
    
def add_steps(root_num, half_step_count):
    root_num += half_step_count
    if root_num > 11:
        root_num -= 12
    
    return root_num
    

def generate_scales(root): # WIP
    #major = w, w, h, w, w, w, h
    major = (2, 2, 1, 2, 2, 2, 1)
    #natural minor = w, h, w, w, h, w, w
    natural_minor = (2, 1, 2, 2, 1, 2, 2)
    
    labels = ("R", "2", "3", "4", "5", "6", "7")

    root_n = note_to_number(root)
    major_scale = [root_n]
    natural_minor_scale = [root_n]
    
    for steps in major:
        stepped = add_steps(major_scale[len(major_scale)-1], steps)
        major_scale.append(stepped)
    for steps in natural_minor:
        stepped = add_steps(natural_minor_scale[len(natural_minor_scale)-1], steps)
        natural_minor_scale.append(stepped)
    print(major_scale)
    print(natural_minor_scale)
    
    base_piano_image = Image.open("SMALL_PIANO_SCALE.png")
    piano_draw = ImageDraw.Draw(base_piano_image)
    for i, note in enumerate(major_scale):
        if i < 7:
            draw_note(piano_draw, note, labels[i])
    base_piano_image.save(root+" Major.png")
    base_piano_image.close()
    
    base_piano_image = Image.open("SMALL_PIANO_SCALE.png")
    piano_draw = ImageDraw.Draw(base_piano_image)
    for i, note in enumerate(natural_minor_scale):
        if i < 7:
            draw_note(piano_draw, note, labels[i])
    base_piano_image.save(root+" Minor.png")
    base_piano_image.close()

notes = ("C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B")
for note in notes:
    generate_scales(note)