#finale

label act6:
    play music bgm6
    scene black
    voice type
    centered "{color=#ffffff}Around the same time, Northen Front....{/color}"
    scene battlefield with dissolve
    show tiger_a:
        subpixel True
        xalign -1.6 yalign 1.5 alpha 1
        ease 2.0 xalign 0.0
    voice driving
    ti "What a good way to start a morning"
    ti "Just 50km more and we reach Kursk"
    show bullet_reversed :
        subpixel True
        xalign 2.0 yalign 0.6 alpha 0.0
        ease  0.5 xalign 0.4 alpha 1.0
        "explosion"

    centered "{w=0.5}{nw}"
    hide tiger_a
    hide bullet_reversed
    voice tank_destroyed
    show smoke:
        xalign 0.42 yalign 1.1 zoom 0.1 alpha 1
        ease 0.08 zoom 1.0 xalign 0.0 alpha 0.9
        ease 8.0 xalign -0.4 alpha 0

    show tiger_b behind smoke:
        subpixel True
        xalign 0.0
        yalign 1.5
    centered "{w=2}{nw}"
    nul "Die!!"
    show t34_a:
        subpixel True
        xalign 2.0 yalign 1.2 alpha 1
        ease 2.0 xalign 1.4
    nul "This Tiger is so weak"
    nul "It literally toasted in one shot"
    nul "It is an easy victory for the red army"
    scene suzu_spot with dissolve
    show blank with hpunch
    s "What the hell did I just saw??"
    s "Those things must be the so called 'White Panzer'"
    s "It even smacked those Tiger tank easily!"
    scene cockpit with dissolve
    show pio_a at show_char_kiri_ke_kanan(-0.4)
    show pf_a at show_char_kiri_ke_kanan(1.6)
    pi "How was it??"
    s "Damn it! {w=0.5} that was scary as hell"
    s "I saw it destroyed the Tiger in 1 shot"
    pfu "How could that be??"
    pfu "Didn't the Tiger has 152mm thick armor plating??"
    s "That's not the problem for them"
    s "They knew that they can't pierce the armor"
    s "So they aim for the turret"
    pi "How is that one-shot kill?"
    s "The turret has the weakest armor compared to the others"
    s "Yet it was the most vulnerable parts of the tank"
    s "Once the tank turret is hit, the shells of an Armor-Piercing round will scatter into pellets"
    s "Killing the tank crew inside it trough the turret hole"
    s "And Tiger is also no exception"
    pfu "That's scary!"
    pi "Can we really win against that beast?"
    s "I'm not sure"
    play sound firing
    queue sound bounce
    show blank with hpunch
    window hide
    pause 3.0
    s "Damn it! White Panzer spots us!"
    s "No other choice than to engage"
    scene battlefield with dissolve
    show t34_a:
        align (1.4,1.2)
    show p4_b:
        subpixel True
        xalign -1.6 yalign 1.2 alpha 1
        ease 2.0 xalign -0.6 alpha 1
    w "How was that fascisti??"
    w "Do you guys enjoy our welcome gift??"
    s "What a pleasant way to be greeted"
    s "As expected from the Red bastard"
    s "Now take this!"
    show bullet :
        subpixel True
        xalign 0.3 yalign 0.5 alpha 0.0
        ease  0.5 xalign 0.8 yalign 0.7 alpha 1.0
        "bullet_deflect"
        ease 0.4  xalign 1.5 yalign -1.0 alpha 1.0
    play sound firing volume 0.5
    play sound bounce
    s "Goddamit! it bounce"
    w "My turn!!"
    s "Shiit, We're done for!"
    show bullet_reversed:
        subpixel True
        xalign 0.7 yalign 0.57 alpha 0.0
        ease 0.5 xalign 0.1 alpha 1
        "explosion"
        zoom 4.0 xalign -0.6
    voice tank_destroyed
    window hide
    pause 2.0
    stop music fadeout 1.0
    scene  black
    centered "{w=2}{color=#ffffff}..............{/color}"
    show blank with hpunch
    scene danger
    show cockpit
    with Dissolve (3.0)
    play music danger
    s "Goddamit"
    s "You girls OK??"
    pfu "I'm fine"
    pi "Me too!"
    s "[pio], what's the status??"
    pi "Main Gun destroyed, and the track has been disabled"
    pi "Looks like This is the end"
    s "The White Panzer got us good"
    pfu "(Looks outside the window)"
    pfu "They are aiming at us"
    pfu "It's over"
    pi "Better say our prayers now"
    s "Damn I really wanted to be an artist"
    s "If only I got accepted at that time"
    pi "I regret that I didn't clear my browser history"
    pfu "I really want to play GTA VI"
    s "Oh come on! GTA VI will only be released after the death of Queen Elizabeth II"
    pi "Just give it up! She will never die since she is an immortal being"
    pfu "Guess you were right"
    s "[tank], sorry for not able giving the best for you"
    s "Sorry for not being a good owner"
    s "Girls! thank you for being my friends"
    s "And Mom, I apologize for not being a good daughter"
    scene black
    centered "{color=#ffffff}Goodbye!{/color}"
    stop music
    voice plane
    centered "{w=3.0}{nw}"
    play sound tank_destroyed
    jump ending
