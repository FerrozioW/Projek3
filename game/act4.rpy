#back to the past again
label act4:
    #play bgm
    show room with dissolve
    su "Today is the day of the art school entrance exam"
    su "Better be going fast"
    play sound se002
    scene livingroom with dissolve
    show suzuran_a at show_char_bawah_ke_atas (0.0):
        xalign 0.5
    m "Oh! Leaving already"
    su "Yes Mom, I will be attending the entrance exam for the art school"
    m "I'm sure my daughter will be admitted in no time"
    su "Just you see mom! I will definitely became the best artist to ever live"
    m "I can't wait to see [persistent.name]-chan become a renowned artist"
    su "Then I will be going now"
    m "Good luck [persistent.name]!! Take care"
    play sound se002
    scene black with ImageDissolve("tr-clockwipe",2,ramplen = 123)
    voice type
    centered "{color=#ffffff}30 minutes later{/color}"
    play sound se002
    scene art_school with dissolve
    su "Finally I'm here!"
    show squidward at show_char_kiri_ke_kanan(0.5):
        yalign 0.0
    atr "State your name and number"
    su "My name is [persistent.name], and my participant number is 069"
    su "This time I will definitely success"
    atr "Whatever, you may start now"
    su "Ok!"
    hide squidward
    su "Let's see"
    su "Maybe I will draw a plane"
    scene black with ImageDissolve("tr-clockwipe",2,ramplen = 123)
    centered "{color=#ffffff}much later{/color}"
    scene drawing with dissolve
    su "Done!"
    su "This is indeed a good scenery of a plane"
    su "Let's submit this to the instructor"
    su "I can't wait to see his reaction"
    scene art_school with dissolve
    show squidward at show_char_kiri_ke_kanan(0.5):
        yalign 0.0
    "[persistent.name] submits her result"
    su "Instructor, how was my drawing??"
    atr "This drawing of planes"
    atr "How should I put this"
    atr "It is very goo-{w=0.5} no it's bad,very bad"
    show blank with hpunch
    atr "You think you can get admitted by drawing this??"
    show blank with hpunch
    atr "You can't just draw on your own like this"
    show blank with hpunch
    atr "You need to follow the art book!"
    show blank with hpunch
    atr "Ugghhh!! I don't want to see your face anymore"
    show blank with hpunch
    atr "Get out!!"
    show blank with hpunch
    su "[sob] [sob] [sob] [sob] [sob] [sob]"
    su "Maybe I'm not suited to be a painter [sob] [sob] [sob]"
    su "If only this is Siracusa where I can bribe to get in"
    atr "You are more suited to be a dictator"
    hide squidward
    "[persistent.name] left the room"
    play sound se002
    show black with dissolve
    jump act5
