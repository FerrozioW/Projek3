#waking up

label act5:
    play music driving
    scene black
    nul "Wake Up"
    pi "[persistent.name]-Chan, Wake Up!!"
    scene cockpit
    show pio_a at show_char_bawah_ke_atas(0.5)
    with Dissolve (2.0)
    su "Uaaaghh...{w=1} Good morning [pio]-chan"
    pi "You sleep so well! it is not like you to be overslept"
    s "I just had a traumatic dream"
    pi "Really?? What dream?"
    s "A dream of a past where I was rejected from art school"
    pi "That must be sucks"
    s "It is"
    s "By the way, who's the one driving [tank]?"
    pfu "It's me"
    s "I apologize for making you the one to drive"
    pfu "It's okay"
    s "I will take the wheel from this point"
    s "[pf]-chan, switch with me"
    pfu "Ok"
    scene suzu_drive with dissolve
    s "Sit tight girls!! We are going to the frontline"
    s "(Driving) I'm kinda bored"
    s "Girls! Let's sing a song"
    pfu "{i}Every day, I imagine a future where I can be with you ~~~{/i}"
    pi "{i}In my hand, is a pen that will write a poem of me and you ~~~{/i}"
    s "{i}The ink flows down into the dark puddle ~~~{/i}"
    pi "{i}Just move your hand - write the way into his heart! ~~~{/i}"
    pfu "{i}But in this world of infinite choices ~~~{/i}"
    s "{i}What will it take just to find that special day? ~~~{/i}"
    pfu "{i}What will it take just to find that special day? ~~~{/i}"
    stop music fadeout 1.0

    play music bgm5
    scene cockpit with dissolve
    pi "What's wrong, [persistent.name]-chan"
    pfu "Why are you stopping the machine"
    s "We have reach the coordinate"
    s "Let me spot the area for little bit!"
    scene suzu_spot with dissolve
    s "(Pulls out the periscope)"
    s "Hmm. Let's see"
    scene trench with dissolve
    s "So this is the trenches"
    s "I wonder where the city of Belgorod is"
    scene city with dissolve
    s "Bingo! There you go"
    s "(writes down the coordinate)"
    scene cockpit with dissolve
    s "Girls! I have found out the enemy fortification at nearby trench and Belgorod"
    s "The coordinate is NE 69 SW 249"
    s "[pf]-chan, Make sure to report this to the Oberkommando"
    pfu "Noted!{w=0.5} I will talk to them via the radio"
    pfu "{i}Hallo Hallo!{w=0.5} This is Pzkwfg Ausf F2 No.69{w=0.5} We have spotted the garrison of the Red Army at NE 69 SW 249, Over!{/i}"
    pfu "{i}We are expecting an air support on those marked target, Over!{/i}"
    b "{i}Understandable, engagement permission granted!{/i}"
    s "How was it??"
    pfu "I have reported the position"
    pi "How was the respond?"
    pfu "[bf]-san told us to engage"
    s "Then let's do it!"
    scene trench with dissolve
    show p4_a:
        subpixel True
        xalign -1.6 yalign 1.0 alpha 0
        ease 3.0 xalign 0.5 alpha 1
    voice driving
    pi "It's surprisingly empty!"
    pfu "Did they flee?"
    s "I think they left for Belgorod"
    show p4_a:
        subpixel True
        ease 3.0 xalign 2.6 alpha 1
    voice driving
    s "Let's proceed!"
    scene city with dissolve
    show gri_a at show_char_kanan_ke_kiri(x=-0.8)
    show shock_a at show_char_kanan_ke_kiri(x=1.6)
    gt "We gonna defend this city"
    gt "Let's make Comrade Stolin proud"
    st "Not a single step back!"
    hide gri_a
    hide shock_a
    #shrinking
    show gri_a:
        subpixel True
        xalign -0.4 alpha 0
        ease 0.01 alpha 0
        "gri_b"
        zoom 1 alpha 0
        ease 2.0 zoom 0.375 xalign 0.5 yalign 0.8 alpha 1.0
        ease 0.01 alpha 0
        "gri_a"
        zoom 0.375 alpha 1
        ease 2.0 xalign 1.1
    pause 2.0
    show shock_a:
        subpixel True
        xalign 1.6 alpha 0
        ease 0.01 alpha 0
        "shock_b"
        zoom 1 alpha 0
        ease 2.0 zoom 0.375 xalign 0.5 yalign 0.8 alpha 1.0
        ease 0.01 alpha 0
        "shock_a"
        zoom 0.375 alpha 1
        ease 2.0 xalign 0.7
    window hide
    pause 3.0
    st "We are ready"
    show p4_b:
        subpixel True
        xalign -1.6 yalign 1.0 alpha 1
        ease 2.0 xalign -0.6 alpha 1
    s "Good afternoon! red bastards"
    gt "You will not move an inch from this point"
    play sound mg volume 0.5
    gt "(shoots machinegun){w=2}{nw}"
    play sound bounce
    pfu "Idiot!! your small bullet can't pierce through this metal beast"
    pi "[tank] is equipped with 80mm steel plating armor"
    s "It's our turn now"

    #shoot
    show bullet :
        subpixel True
        xalign 0.3 yalign 0.4 alpha 0.0
        parallel:
            ease  0.5 xalign 0.8 alpha 1.0
        parallel:
            ease_quad  0.5 yalign 0.7 alpha 1.0
        ease 0.05 alpha 0
        "smoke"
        xalign 0.52 yalign 0.6 zoom 0.1 alpha 1
        ease 0.08 zoom 1.0 xalign 1.0 alpha 1.0
        ease 5.0 xalign 1.4 alpha 0.5
    play sound firing volume 0.5
    queue sound tank_destroyed volume 0.75
    centered "{w=2.5}{nw}"
    hide bullet
    hide gri_a with moveoutright
    hide shock_a with moveoutright
    show p4_b:
        subpixel True
        ease 2.0 xalign 0.2 alpha 1
    pi "Did we get them??"
    s "I think??"
    pfu "Wait, There is more!!"
    show p4_b:
        subpixel True
        ease 2.0 xalign -0.6 alpha 1
    show normal_t34_a at show_char_kanan_ke_kiri(1.2):
        yalign 1.0
    pi "Oh [curse], here we go again"
    show blank with hpunch
    s "Th-{w=0.3}That's the legendary T-34"
    show blank with hpunch
    pfu "Whaaat????"
    s "Damn it!, it's a 1940 standard issued tank"
    s "It has 76 mm powerful Armor-Piercing round attached to the turret"
    s "To add salt to injury, it has a 90mm sloped armor!"
    s "I don't think our [tank] can be on par with it!!"
    #plane
    show stuka_down:
        subpixel True
        xalign -0.8 yalign -0.5 alpha 1
        parallel:
            ease 1.5 xalign 0.7 yalign 0.1
        "stuka_up"
        parallel:
            ease_quad 1.5 xalign 1.2 yalign -0.5
    play sound plane
    centered "{w=1.5}{nw}"
    show bomb:
        subpixel True
        xalign 0.7 yalign 0.1 alpha 0
        ease 1.0 yalign 1.0 alpha 1.0
        "smoke"
        xalign 0.52 yalign 0.75 zoom 0.1 alpha 1
        ease 0.08 zoom 1.0 xalign 1.0 alpha 1.0
        ease 8.0 xalign 1.6 alpha 0
    centered "{w= 1.0}{nw}"
    play sound tank_destroyed
    show normal_t34_b as normal_t34_a
    stop music fadeout 2.0
    centered "{w=1.5}{nw}"
    pi "What is that??"
    pfu "Finally she has arrived"
    p "{i}Sorry for the late girls! ~~~{/i}"
    s "The Stuka just saved our ass"
    pfu "Thank You, pilot-chan"
    p "Glad I could help"
    "pilot-chan lefts"
    play music bgm005 fadein 1.0
    pfu "They have retreated"
    pi "Does that mean we win???"
    pfu "Yes we are!"
    s "We did it girls! Belgorod is ours"
    hide normal_t34_a
    s "Quick, [pf]-chan contact the Oberkommando about our victory"
    s "We might even get a promotion for this"
    s "And more promotion = more money"
    pfu "You don't need to tell me that"
    pfu "{i}Hallo Hallo!{w=0.5} This is Pzkwfg Ausf F2 No.69{w=0.5} We have defeated the Red Army garrison and seized the town of Belgorod{/i}"
    b "{i}Understandable, good work girls{/i} "
    b "{i}However, I am really sorry to inform you that this operation has not finished yet{/i} "
    b "{i}The Group North has failed to capture Kursk{/i}"
    show blank with hpunch
    pfu "{i}What?? How could that be??{/i}"
    pfu "{i}Didn't they supplied by the legendary Tiger I tank??{/i}"
    b "{i}I couldn't believe it either..{/i}"
    b "{i}At first, I thought that it will be an easy victory for Group North{/i}"
    b "{i}But apparently, it seems that the Red Army has a trick of the sleeve{/i}"
    b "{i}The one who destroyed out Tiger tank are the enemy's Tank Ace{/i}"
    b "{i}It is a T-34 painted in white. That thing is really terrifying{/i}"
    b "{i}We called it,{w=0.5} 'The White Panzer'{/i}"
    pfu "{i}Understandable. We are waiting for your next order{/i}"
    b "{i}Group South, since the Northern front has suffered terrible losses{/i}"
    b "{i}You girls will replace their job{/i}"
    b "{i}Attack the city of Kursk from the South{/i}"
    pfu " {i}Affirmative{/i}"
    stop music fadeout 2.0
    scene black with ImageDissolve("tr-clockwipe",2,ramplen=123)
    jump act6
