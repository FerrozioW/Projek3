
#back to the present
label act3:
    #play bgm
    scene field with dissolve
    show pio_a at show_char_bawah_ke_atas(0.0):
        xalign -0.4
    pi "That was actually a very interesting story though"
    s "I know right?"
    s "I wonder what she is doing right now"
    s "I'm sure she has become a great artist now"
    s "Unlike me"
    pi "It's ok [persistent.name]-Chan"
    pi "Once the war is over, you can try as many times as you can"
    s "Thanks, [pio]-Chan"
    play music  run
    "(someone is approaching)"
    nul "Heyy Guyyys!"
    stop music
    show pf_a:
        subpixel True
        xalign 2.6 yalign 0.0 alpha 0
        ease 2.0 xalign 1.6 alpha 1
    pfu "(Panting){w=0.5} Haah. Haah.{w=0.5} I have been searching for both of you"
    s "Oh hello [pf]-Chan"
    pi "Glad to see you again, [pf]-Chan"
    s "What brings you here today?"
    pfu "Where the hell have you guys been??"
    pfu "[bf]-Chan has something to tell us"
    pfu "She told us to meet at the HQ in 15 minutes"
    s "We still got time, why hurry?"
    pi "Yeah that's right, 15 minutes is still a lot of time"
    pfu "That is not the problem"
    s "Then what is it??"
    pfu "She tells that 30 minutes ago"
    show blank with hpunch
    pi "[curse]!!, better hurry up!"
    s "Let's run"
    scene plain with dissolve
    show hq_b at show_char_kanan_ke_kiri(0.5):
        yalign 0.0
    pi "Let's get in"
    window hide
    show pio_a:
        subpixel True
        xalign 0.0 yalign 0.0 alpha 0
        ease 0.01 alpha 0
        "pio_b"
        zoom 4.0 alpha 0
        ease 2.0 zoom 1.5 yalign 0.8 alpha 1.0
        ease 0.01 alpha 0
        "pio_a"
        zoom 0.375 alpha 1
        ease 2.0 xalign 0.5
        ease 1.0 alpha 0
    pause 2.0
    show pf_a:
        subpixel True
        xalign 0.0 yalign 0.0 alpha 0
        ease 0.01 alpha 0
        "pf_b"
        zoom 1 alpha 0
        ease 2.0 zoom 0.375 yalign 0.8 alpha 1.0
        ease 0.01 alpha 0
        "pf_a"
        zoom 0.375 alpha 1
        ease 2.0 xalign 0.5
        ease 1.0 alpha 0
    window hide
    pause 3.0
    "You are now inside the hq"
    scene tent with dissolve
    show brigadefuhrer_a at show_char_kanan_ke_kiri(0.5):
        yalign 0.0
    show blank with hpunch
    b "Where the hell you all have been to??"
    b "You guys are late !!!"
    s "We're very sorry!"
    b "Whatever! let's cut chase to the point"
    b "The Oberkommando just issued an order"
    b "I will thoroughly explain on the map"
    scene map with dissolve
    show chibi_p4 at show_char_kiri_ke_kanan(0.44):
        yalign 0.75
    b "As you can see, we are now in the small town of Kharkov"
    b "Luckily, we had successfully mantained communication with the Group North"
    b "It seems they resided in the rural village of Konotop"
    show chibi_tiger at show_char_kiri_ke_kanan(0.24):
        yalign 0.25
    pause 2.0
    b "Our mission is to enricle enemy's center pocket"
    show arrow:
        subpixel True
        xalign 0.3 yalign 0.2  alpha 0
        ease_quad 2.0 xalign 0.38 yalign 0.2 rotate 0 alpha 1
    b "Group North will attempt breaktrough to capture Kursk"
    show arrow_reversed:
        subpixel True
        xalign 0.55 yalign 0.75 alpha 0
        ease_quad 2.0 rotate -90 alpha 1
    b "While we are expected to attack from the south and seize Belgorod"
    hide arrow
    hide arrow_reversed
    show chibi_tiger:
        subpixel True
        ease_quad 2.0 xalign 0.56
    show chibi_p4:
        subpixel True
        ease_quad 2.0 xalign 0.52 yalign 0.45
    pause 2.0
    b "By successfully doing that, their entire pocket will be encircled and forced to surrender"
    scene tent with dissolve
    show brigadefuhrer_a at show_char_kanan_ke_kiri(0.5):
        yalign 0.0
    b "We call this mission {i}Operation UwU{/i}"
    b "We will began to dispatch tommorow morning"
    b "Any question??"
    pfu "No, Ma'am!"
    b "Good! that is for today's meeting"
    b "You are allowed to leave"
    play sound se002
    hide brigadefuhrer_a
    "Officer-Chan has left the meeting session"
    s "Let's get going shall we??"
    pfu "Good night guys!"
    pi "See you tomorrow"
    play sound se002
    scene field with dissolve
    s "Now let's get some sleep"
    scene black with ImageDissolve("tr-clockwipe",2,ramplen = 123)
    voice type
    centered "{color=#ffffff}4 Years Ago{/color}"
    jump act4
