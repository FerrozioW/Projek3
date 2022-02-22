label splashscreen:
    scene black
    $persistent.name = renpy.input("Enter your name (female)", length=12)
    $lower = (persistent.name).lower()

    if "lisa" in lower:
        "That is very similar to my mother's name! it's not my name"
        "I just remembered, I am Erika"
        $persistent.name = "Erika"
    elif "suzuran"  in lower:
        "That is very similar to my mother's name!, it's not my name"
        "I just remembered, I am Erika"
        $persistent.name = "Erika"
    voice type
    centered "{color=#ffffff}I have always aspired to be an artist since I was child{/color}"
    voice type
    centered "{color=#ffffff}However, life is not a fairytale{/color}"
    voice type
    centered "{color=#ffffff}It's my 690th day in the Eastern Front{/color}"
    voice type
    centered "{color=#ffffff}I can't even remember how do I got to this place in the first place{/color}"
    voice type
    centered "{color=#ffffff}It's like this muddy field has becoming a part of my life{/color}"
    voice type
    centered "{color=#ffffff}Tommorow is my 19th birthday{/color}"
    voice type
    centered "{color=#ffffff}Who would have guessed that my best day will be spent in this unending hellhole{/color}"
    voice type
    centered "{color=#ffffff}When I was 8th years old, my friend was caught stealing on the market{/color}"
    voice type
    centered "{color=#ffffff}When I got home, my mother scold me a lot{/color}"
    voice type
    centered "{color=#ffffff}However, I did not steal{/color}"
    voice type
    centered "{color=#ffffff}I briefly explained to my mother on how I did not steal{/color}"
    voice type
    centered "{color=#ffffff}Despite hearing that, my mother still insisted on lecturing me{/color}"
    voice type
    centered "{color=#ffffff}She said 'I knew that my precious daughter will not steal'{/color}"
    voice type
    centered "{color=#ffffff}'The reason why I scold you..'{/color}"
    voice type
    centered "{color=#ffffff}'Is because you were there..'{/color}"
    voice type
    centered "{color=#ffffff}My name is [persistent.name] {/color}.."
    voice type
    centered "{color=#ffffff}Eastern Front{vspace=30}Group South{vspace=30}2nd SS-Panzer Korps{vspace=30}1st Division{vspace=30}{i}PanzerIV Ausf. F2 No.69{/i}{/color}"
    voice type
    centered "{color=#ffffff}And I was there{/color}"
    scene white
    show splashscreen_1:
        subpixel True
        zoom 1.5 xalign 0.1 alpha 0.0
        ease 3.0 xalign 0.5 alpha 1.0
    centered "{w=3.0}{nw}"
    hide splashscreen_1
    show splashscreen_2:
        subpixel True
        zoom 0.375 xalign 0.9 alpha 0.0
        ease_quad 3.0 xalign 0.5 alpha 1.0
    centered "{w=3}{nw}"
    hide splashscreen_2
    scene white
    show menu_pic:
        subpixel True
        zoom 1.5 xalign 0.1 alpha 0.0
        ease_quad 3.0 xalign 0.5 alpha 1.0
    centered "{w=3}{nw}"
    show menu_pic:
        subpixel True
        zoom 1.5 xalign 0.1 alpha 0.0
        ease 0.1 xalign 0.5 alpha 0
        ease_quad 3.0 xalign 0.5 zoom 1 alpha 1.0
    centered "{w=3.1}{nw}"
return
