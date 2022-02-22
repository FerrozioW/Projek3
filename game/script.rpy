# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# perpendek nama karakter.
$pio = "Pioneer"
$pf = "Spotter"
$bf = "Officer"

#define karakter
define nul = Character("???")
define c = Character("{i}Cherino-Chan{/i}",image = "cherino")
define b = Character("{i}[bf]-Chan{/i}", image = "brigadefuhrer")
define s = Character("{i}[persistent.name]{/i}", image = "lisa")
define su = Character("{i}[persistent.name]{/i}", image = "suzu")
define pfu = Character("{i}[pf]{/i}-Chan",image = "pf")
define pi = Character("{i}Pioneer-Chan{/i}",image = "pio")
define p = Character ("{i}Stuka pilot-Chan{/i}",image = "pilot")
define m = Character("{i}Suzuran{/i}",image = "suzuran")
define t = Character("{i}Teacher{/i}")
define atr = Character("{i}Art School Instructor{/i}")
define gt = Character ("{i}Guards-Chan{/i}",image = "gri")
define st = Character ("{i}Shock Troops-Chan{/i}",image = "shock")
define ti = Character ("{i}Tiger crew-Chan{/i}",image = "tiger")
#dekralasi image
image rain = Movie(fps=30, size=(1280, 720), channel='movie', play='rain.mpg', mask='rain.mpg', mask_channel=None, loop=True)
image repair2 = "effect_tank/repair.png"
image repair3 = "effect_tank/repair.png"
image arrow_reversed = im.Flip("arrow.png",vertical = "True")
image bullet_reversed = im.Flip("bullet.png", horizontal="True")
image pio_a_reversed = im.Flip("pio_a.png", horizontal="True")
image pio_b_reversed = im.Flip("pio_b.png", horizontal="True")
image p4_b reversed = im.Flip("p4/p4_b.png",horizontal = "True")
image pf_b = im.MatrixColor("pf_a.png", im.matrix.brightness(+2.0))
image gri_b = im.MatrixColor("gri_a.png", im.matrix.brightness(+2.0))
image shock_b = im.MatrixColor("shock_a.png", im.matrix.brightness(+2.0))
#fungsi atl
transform show_char_bawah_ke_atas(y = 1.0):
    subpixel True
    yalign (y-0.08) alpha 0
    ease 1.5 yalign y alpha 1
transform show_char_kiri_ke_kanan(x = 0.5):
    subpixel True
    xalign (x-0.08) alpha 0.0
    ease 1.3 xalign x alpha 1.0
transform show_char_kanan_ke_kiri(x = 0.5):
    subpixel True
    xalign (x+0.08) alpha 0.0
    ease 2.0 xalign x alpha 1.0

# The game starts here.

label start:
    stop music
    #play bgm
    scene black
    voice type
    centered "{color=#ffffff}11 Mar 1943, in a small town named Kharkov{/color}"
    show field:
        subpixel True
        xalign 0.1 alpha 0.0
        ease_quad 3.0 xalign 0.5 alpha 1.0
    centered "{w=3}{nw}"
    s "Phew, finally we arrived!"
    show p4_b at show_char_kiri_ke_kanan(-0.2):
        yalign 1.0

    s "Damn! it's so hot inside this metal can"
    s "Might as well open up the hatch"
    show atas_p4:
        zoom 0.9
        subpixel True
        align(0.11,0.32) alpha 0.0
        ease 0.8 yalign 0.27 alpha 1.0
    s "Arrgh, much better"
    s "Let's see..."
    hide p4_b
    hide atas_p4
    show p4_b:
        subpixel True
        xalign -0.2 yalign 1.0 alpha 1.0
        ease_quad 2.0 zoom 1.5 xalign 0.5
    $tank = renpy.input("Enter your tank's name (remember, tank is gendered as female)", length=12)
    $temp_tank = (tank).lower()
    if "lisa" in temp_tank:
        s "Who would use their mother's name to name a tank"
        s "Let's just name her Cunnie, it's a good name"
        $tank = "Cunnie"
    elif "suzuran"  in temp_tank:
        s "That is very similar to my mother's name!, it's not my name"
        s "I just remembered, I am Suzurina"
        $tank = "Cunnie"
    s "Hmmm... Something is wrong with [tank]"
    s "It's just doesn't feel good when I drive her"
    s "(Looks closer) No wonder"
    s "The track is dislocated"
    s "Uwoooh, this is bad"
    s "The front armor is damaged"
    hide p4_b
    $pio = "Pioneer"
    s "I need someone to repair this tank for me"
    s "[pio]!! you there?"
    show pio_a_reversed at show_char_kanan_ke_kiri(1.0) :
        yalign 0.0
    pi "You called??"
    s "Thank god you are here!"
    s "As you can see, the front plating and the track are damaged"
    s "Can you repair [tank] for me??"
    pi "No problem"
    show p4_b at show_char_kiri_ke_kanan(-0.2):
        yalign 1.0


    #pioneer shrinking
    show pio_a_reversed:
        subpixel True
        xalign 0.8 yalign 0.0 alpha 0
        ease 0.01 alpha 0
        "pio_b_reversed"
        zoom 4.0 alpha 0
        ease 2.0 zoom 2 yalign 1.0 alpha 1.0
        ease 0.01 alpha 0
        "pio_a_reversed"
        zoom 0.5 alpha 1
    "([pio]-Chan shrinks her body)"
    pi "Perfect!!, now let's get to work"
    show pio_a_reversed as pio_a_reversed behind p4_b:
        subpixel True
        zoom 0.5 alpha 1
        xalign 0.8, yalign 1.0
        ease_quad 2.0 xalign 0.5 blur 0.2
    $curse = "scheiße"
    pi "Oh [curse], this looks bad"
    pi "It will take a very long time to repair this"
    s "I don't care how long it will take, just take care of [tank] for me"
    pi "Affirmative! I will start repairing it now"
    show repair:
        subpixel True
        xalign 0.39 yalign 0.7 alpha 0.0
        parallel:
            ease 0.6 zoom 0.8 xalign 0.39 yalign 0.7 alpha 0.4
            ease 0.6 zoom 0.86 xalign 0.39 yalign 0.7 alpha 0.7
            repeat

    show repair2 :
        subpixel True
        xalign 0.19 yalign 0.6 alpha 0.0
        parallel:
            ease 0.9 zoom 0.8   alpha 0.4
            ease 0.7 zoom 0.86  alpha 0.7
            repeat
    show repair3:
        subpixel True
        xalign 0.05 yalign 0.55 alpha 0.0
        parallel:
            ease 1.2 zoom 0.8   alpha 0.4
            ease 0.9 zoom 0.86  alpha 0.7
            repeat
    play music welding
    s "On the meantime, I should change to more comfortable clothing"
    show lisa_b:
        subpixel True
        zoom 0.5 xalign -0.8 yalign 1.0 alpha 0
        easein 2.0 zoom 0.225 xalign 0.1 yalign 0.2 alpha 1.0

    #show tiger_a at show_char_kiri_ke_kanan(x = 0.0):
        #yalign 1.0

    su "I'm feeling much comfier now"
    su "[pio]-Chan, how was your day?"
    pi "Usually I woke up at 6 a.m. and do my morning work out"
    pi "And proceed to build fortification along the coastline and digging out trenches"
    pi "You know, since I am an engineer"
    $pf = "Spotter"
    $bf = "Officer"
    pi "Lucky for me, today [pf]-Chan reported that heavy rain is happening in the outskirt of the town"
    su "How is that lucky?"
    pi "Well, the rain causes the ground to become muddy, making the movement done by foot or vehicle engine much slower"
    pi "Most people will not march in this condition"
    pi "If the enemy aren't going to march, then it means that I was supposed to enjoy my holiday because I don't need to construct sandbags and other stuff"
    pi "But thanks to {b}Certain Someone{/b}, I had to repair this tin can"
    hide repair
    hide repair2
    hide repair3
    stop music fadeout 1.0
    pi "It's done"
    show lisa_b:
        subpixel True
        ease 0.8 yalign 0.29 alpha 0.0
    su "Let me get my tank out"
    show p4_b reversed as p4_b:
        subpixel True
        ease 2.3 xalign -0.6 alpha 0.0
    su "(drives out the tank)"
    show pio_a_reversed:
        subpixel True
        ease_quad 2.0 xalign 0.5
    pi "Now that I'm done, let's get back to my original form"
    show pio_a_reversed:
        subpixel True
        "pio_b_reversed"
        zoom 2.0 alpha 0.0
        ease 2.0 zoom 4 xalign 0.5 yalign 0.0 alpha 1.0
        "pio_a_reversed"
        zoom 1 alpha 1
    pi "(goes back to her original form)"
    su "How should I say this...{w=1} Thank you!{w=1} and I apologize for making you work on your holiday"
    pi "Nein, don't sweat it!!{w=1} Honestly I kinda like doing my job"
    pi "Since I was born, I know that I'm destined to be an engineer"
    pi "I love doing engineering stuff like what I am doing right now"
    pi "However somethimes I just hate it"
    su "Why is that?"
    pi "Some jerk ass superior just demand that I finished it in a certain time"
    su "I know right!{w=1} Indeed deadline is just very annoying"
    pi "Sometimes those deadlines are just inhumane"
    pi "Imagine being told to place barbed wire on 2 km wide frontline and they just gave you 30 minutes to do so"
    su "What? that's crazy!!"
    pi "Yep, somethimes I just want to give them my shovel and told them to do it so they can understande the pain"
    pi "But I managed to hold myself back"
    pi "Since if I do it for real then I will definitely got hanged, just like my friend Sayori"
    su "Wrong game!"
    su "But I do get you though! at least you got to do your dream job"
    su "When I was little, I was aspired to be an artist"
    pi "Wait! What?"
    su "Strange isn't it!"
    su "It is a long story though"
    jump act2

    #show tiger_a at show_char_kiri_ke_kanan(x = 0.0):
        #yalign 1.0
    show bullet_reversed :
        subpixel True
        xalign 2.0 yalign 0.6 alpha 0.0
        ease  0.5 xalign 0.4 alpha 1.0
        "explosion"

    centered "{w=0.5}{nw}"
    #show explosion as bullet
    hide tiger_a
    hide bullet_reversed
    #show burning:
        #subpixel True
    voice tank_destroyed
    show smoke:
        xalign 0.42 yalign 0.6 zoom 0.1 alpha 1
        ease 0.08 zoom 1.0 xalign 0.0 alpha 0.9
        ease 8.0 xalign -0.4 alpha 0

    show tiger_b behind smoke:
        subpixel True
        xalign 0.0
        yalign 1.0
    centered "{w=2}{nw}"

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.



    # These display lines of dialogue.

    b "Die You Bitch"
    hide smoke
    hide tiger_b
    show gri_a:
        align (0.5,0.0)

    b "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
