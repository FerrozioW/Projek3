#finale

label act6:
    scene black
    voice type
    centered "{color=#ffffff}Around the same time, Northen Front....{/color}"
    scene battlefield with dissolve
    show tiger_a:
        subpixel True
        xalign -1.6 yalign 1.0 alpha 1
        ease 2.0 xalign 0.0
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
        xalign 0.42 yalign 0.6 zoom 0.1 alpha 1
        ease 0.08 zoom 1.0 xalign 0.0 alpha 0.9
        ease 8.0 xalign -0.4 alpha 0

    show tiger_b behind smoke:
        subpixel True
        xalign 0.0
        yalign 1.0
    centered "{w=2}{nw}"
    nul "Die!!"
    show t34_a:
        subpixel True
        xalign 1.6 yalign 1.0 alpha 1
        ease 2.0 xalign 1.0
    window hide
    pause 
