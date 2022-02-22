
#act2 will focused on mc's past
label act2:
    scene black with ImageDissolve("tr-clockwipe",3,ramplen = 123)
    voice type
    centered "{color=#ffffff}5 years ago{/color}"
    play music bgm2 fadein 2.0
    show classroom:
        subpixel True
        zoom 1.5 xalign 0.1 alpha 0.0
        ease 3.0 zoom 1.0 xalign 0.5 alpha 1.0
    window hide
    pause 3.0
    t "Welcome to today's class of Database System"
    t "My Name is {s}Mel*sa{/s} and today's topic is database security"
    t "So Database Security is.....{w=1} You can see it yourself on the slide"
    su "This Class is so boring!"
    t "Make sure to write your student notes about this material and submit it in the end of the class"
    su "(Damn Bitch! You didn't even teach us anything)"
    su "Cherino-Chan, do you write your note?"
    c "Nyet, I didn't even understand what she said"
    t "Okay, what is the main purpose of backup files in database??"
    t "let's see..{w=1} Dimas can you answer it"
    "Dimas" "I did not know it Miss"
    show blank with hpunch
    t "THEN WHAT THE HELL ARE YOU DOING IN THIS CLASS?"
    t "EVEN THOUGH I SPEND SO MUCH TIME TEACHING YOU"
    t "AND YOU STILL THERE NOT DOING ANYTHING"
    t "DO YOU EVEN WRITE YOUR STUDENT NOTE?"
    "Dimas" "(Moves hand)"
    show blank with hpunch
    t "OHHHH!{w=1} YOU ARE SHOWING ME MIDDLE FINGER NOW?"
    "Dimas" "No.. Miss, I just try to scratch my ear"
    t "YOU THINK I WILL BELEIVE THAT?"
    t "YOU INSOLENT CHILD!"
    t "BACK ON MY DAY IN {s}BINUS{/s}, I STUDIED HARD ALONE FOR THIS COURSE"
    t "YOU ARE LUCKY ENOUGH TO BE TAUGHT BY ME, AND STILL YOU DON'T APPRECIATE IT"
    c "(Whisper) damn, I feel sorry for this guy"
    su "His luck is just bad right now, this morning he probably pulled three 6 {image=emoji/star.png}{alt}star{/alt} operator or something"
    c "Pfft! sucks to be him"
    play sound bell
    "bell rings"
    su "Finally the class is over!"
    t "Okay that is today's class! thank you for attending and don't forget to submit your student notes"
    t "And Dimas!!{w=0.5} see me after school!!"
    show out_class:
        subpixel True
        zoom 1.0 xalign 0.1 alpha 0.0
        ease 3.0 zoom 1.0 xalign 0.5 alpha 1.0
    su "School has ended"
    su "What are we gonna do, Cherino-Chan?"
    show cherino_a:
        subpixel True
        xalign 0.5 yalign 0.0 alpha 0
        ease 2.0 alpha 1
    su "{i}(This is Renkawa Cherino-Chan, she is a transfer student from Red Winter Federation. We have been friends since we are 6){/i}"
    c "[persistent.name]-Chan, what are we gonna do now that the school is over?"
    su "I just bought Doki Doki Literature Club 2 . You want to come over and play?"
    c "Wooooah.. Can I play it?"
    su "Of course!!"
    c "Well then, let's go!!"
    hide cherino_a
    show house with dissolve
    su "Let's get Inside"
    scene livingroom with dissolve
    show suzuran_a at show_char_bawah_ke_atas (0.8):
        xalign 0.5
    m "Welcome Home my child!"
    su "I'm home"
    c "Good afternoon Suzuran-san"
    m "Oh Cherino-Chan is here too"
    c "Sorry to interupt~~~"
    m "It's okay.. just make yourself at home"
    hide suzuran_a
    play sound se002
    scene room with dissolve
    "They began to play the game"
    scene black with ImageDissolve("tr-clockwipe",1,ramplen = 123)
    voice type
    centered "{color=#ffffff} 5 hours later {/color}"
    scene room with dissolve
    show cherino_a at show_char_bawah_ke_atas (0.0):
        xalign 0.5
    su "Wow we finally beat the game"
    c "It sure is tiresome to clear all the possible route"
    su "The plot is very good though, the storyline is just awesome and unpredictable"
    su "Still, I can't believe that monika hang herself!"
    c "And Sayori is the one behind every strange things"
    su "I'm glad that I asked you to play with me"
    su "Otherwise, I will never beats the game alone"
    c "(Looks at clock)"
    su "What's wrong, Cherino-Chan??"
    c "Wow, time sure flies. It is 7 p.m. already"
    su "Now that you mention it"
    c "It's time for me to get home"
    su "Yep, I will walk you home"
    hide cherino_a
    play sound se002
    scene livingroom with dissolve
    show suzuran_a at show_char_bawah_ke_atas:
        xalign 0.5
    m "Leaving already, Cherino-chan??"
    c "Yes I am. Moreover, it is late already!"
    m "Indeed it is, but tomorrow is a holiday. Why don't you stay over for tonight?"
    c "No I can't. I have plans for tomorrow"
    m "Oh..  Okay then!"
    m "[persistent.name] !! Make sure you walk Cherino-Chan to home!"
    su "Okay Mom!"
    stop music fadeout 2.0
    hide suzuran_a
    scene road with dissolve
    show cherino_a at show_char_bawah_ke_atas (0.0):
        xalign 0.5
    su "Cherino-Chan. Thanks for today!"
    hide cherino_a
    scene cherino_smile with dissolve
    play music bgm2_2
    c "[persistent.name]-Chan. Thank you for all this time"
    c "Thank you for being my first and only best friend"
    su "What are you talking about...{w=1} Why are you talking like that??"
    c "[persistent.name]-Chan. Do you still remember?"
    c "When we were 8, I got caught stealing at Mr.Hans market??"
    c "At that time, he really got angry and ended up almost reporting us to the police?"
    c "It was sure a horrifying experience"
    "Cherino tries to hold her tears"
    su "Just tell me what happened??{w=1} What is the reason of your behavior just now?"
    c "[persistent.name]-Chan. I had to go back to the federation tomorrow"
    scene road with dissolve
    show cherino_a at show_char_bawah_ke_atas (0.0):
        xalign 0.5
    show blank with hpunch
    su ".{w=0.5}.{w=0.5}.{w=0.5} Why so sudden??"
    c "My father was a victim of {i}The Great Purge{/i}. He was charged for treason and found guilty"
    c "I don't have any memory about him. All I remember was when he told me that he will go outside to buy vodka"
    c "But he never returned since then"
    c "Even though we are not related anymore, I am still his daughter"
    c "And my scholarship got revoked and I was deported back tommorow"
    show blank with hpunch
    su "No..{w=0.5}No..{w=0.5}No.. You can't just leave me like that"
    show blank with hpunch
    su "How about our promise?? Didn't we agree that we will get into an art school together"
    su "And becoming the best artist in the world??"
    c "I'm sorry [persistent.name]-Chan. I can't keep the promise"
    hide cherino_a
    scene black with ImageDissolve("tr-clockwipe",1,ramplen = 123)
    voice run
    centered "{color=#ffffff}[persistent.name] can't cope with the situation. Then proceeds to run away{/color}"
    scene road with dissolve
    show blank with hpunch
    su "{image=emoji/sob.png}{alt}sob{/alt}  {image=emoji/sob.png}{alt}sob{/alt}  {image=emoji/sob.png}{alt}sob{/alt}  {image=emoji/sob.png}{alt}sob{/alt}  {image=emoji/sob.png}{alt}sob{/alt}  {image=emoji/sob.png}{alt}sob{/alt}  {image=emoji/sob.png}{alt}sob{/alt}  {image=emoji/sob.png}{alt}sob{/alt}  {image=emoji/sob.png}{alt}sob{/alt}  {image=emoji/sob.png}{alt}sob{/alt}  {image=emoji/sob.png}{alt}sob{/alt}{image=emoji/sob.png}  {alt}sob{/alt}{image=emoji/sob.png}{alt}sob{/alt}"
    su "Cherino-Chan Bakkaaa!! {image=emoji/sob.png}  {alt}sob{/alt}{image=emoji/sob.png}  {alt}sob{/alt}  {image=emoji/sob.png}{alt}sob{/alt}  {image=emoji/sob.png}{alt}sob{/alt}  {image=emoji/sob.png}{alt}sob{/alt}  {image=emoji/sob.png}{alt}sob{/alt}"
    scene house with dissolve
    $sob = "{image=emoji/sob.png}{alt}sob{/alt}"
    show blank with hpunch
    su "YOU SAID THAT YOU WILL ENTER ART SCHOOL TOGETHER WITH ME! [sob][sob][sob]"
    su "BUT YOU LIE!!![sob][sob][sob] YOU LIEE!!!! [sob][sob][sob]"
    play sound se002
    scene livingroom with dissolve
    show suzuran_a at show_char_bawah_ke_atas (0.5):
        xalign 0.5
    m "My lovely child, what's wrong??"
    su "[sob][sob][sob][sob][sob][sob][sob][sob][sob]"
    play sound se002
    scene room with dissolve
    su "[sob][sob][sob][sob][sob][sob][sob][sob][sob][sob][sob][sob][sob][sob][sob][sob][sob][sob][sob][sob][sob][sob][sob][sob][sob][sob][sob][sob][sob][sob][sob][sob][sob][sob][sob][sob]"
    m "[persistent.name]!!! may I come in??"
    su "........"
    play sound se002
    "(Suzuran open's the door)"
    show suzuran_a with dissolve
    m "My child, What is happening to you??"
    su "..........{w=1} Cherino-Chan lied to me!![sob] [sob] [sob] [sob]"
    su "She said that we will be an artist together [sob] [sob] [sob] [sob]. But she left me!!"
    m "[persistent.name],{w=1} I think you already know"
    m "Cherino-Chan also has her own circumstances"
    m "By acting like this, you will only burden her and yourself"
    m "However, did you know that you are still very lucky.."
    m "When I was your age, I spend all of my childhood inside the basement of my house"
    m "Everyday was a same routine for me"
    m "I woke up, take a shower, eat, watching TV, and goes back to sleep"
    m "Even though sometimes Onii-san goes downstair to play, It is still very lonely for me"
    m "Given the circumstance, that is the reason why I never had any friends"
    m "Only when I reached 18 years old that I was allowed to go upstairs and sleep in my own room"
    m "That's why [persistent.name], you need to respect her decision"
    m "Whatever happens you are still my cute child that I know"
    m "So..{w=1}Make sure to wish her a safe trip"
    su "O-{w=0.5}Okay mom"
    stop music fadeout 2.0
    scene black
    voice type
    centered "{color=#ffffff}And that was the last time I met her"
    jump act3
