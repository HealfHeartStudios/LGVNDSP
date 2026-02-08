# Code Project Start Date Nov 8 2025
# This is a github test 2
#------------------------------------------------------------------------------------------------------------------------------------------------
# Character definitions. setting var name, screen name, name color.
#------------------------------------------------------------------------------------------------------------------------------------------------
#lara
define lu = Character("???", color="#ff0000")
define l = Character("Lara Chiba", color="#ff0000")
define l_shout = Character("Lara Chiba", who_color="#ff0000", what_size=50 )
define l_whisper = Character("Lara Chiba", who_color="#ff0000", what_size=18)
#ghosty
define gu = Character("???", color="#a900af")
define g = Character("Ghosty O'hara", color="#a900af")
define g_shout = Character("Ghosty O'hara", who_color="#a900af", what_size=50)
define g_whisper = Character("Ghosty O'hara", who_color="#a900af", what_size=18)
define gf = Character("Saki O'hara", color="#a900af")
define gf_whisper = Character("Saki O'hara", who_color="#a900af", what_size=18)
#ghostyfake/Saki
#Side Characters
define f = Character("Fanta O'hara", who_color="#d47100")
define s = Character("Spirit O'hara", who_color="#c55ca6")
define sa = Character("Sakura", who_color="#ff8292")
define sas = Character("Sakura", who_color="#ff8292", what_size=18)
#PC related Characters
define nar = Character(what_italic=True)
define pov = Character("[povname]", color="#faf0f0")
define fantasy = Character("[fantasy]", color="#faf0f0")
#Defaualt PC before player chooses name for start
define sta = Character("You", color="#faf0f0")
define ph = Character("Phone", color="#faf0f0")
#------------------------------------------------------------------------------------------------------------------------------------------------
#affection scores and other flags
#------------------------------------------------------------------------------------------------------------------------------------------------
default lara_love = 5
default ghosty_love = 5
default event = 0
default lara_date_count = 0
default ghosty_date_count = 0
default wf = 0
#------------------------------------------------------------------------------------------------------------------------------------------------
# May not be needed. do not delete just incase. I have no clue what the fuck im doing.
#------------------------------------------------------------------------------------------------------------------------------------------------
transform moveright:
    linear 0.4 xpos 0.9
transform moveleft:
    linear 0.4 xpos 0.1
#------------------------------------------------------------------------------------------------------------------------------------------------
#Logo splash. Disable while testing 
#------------------------------------------------------------------------------------------------------------------------------------------------
label splashscreen:
    $ renpy.movie_cutscene("images/logo.webm")
    return

#------------------------------------------------------------------------------------------------------------------------------------------------
#Game starts here.
#------------------------------------------------------------------------------------------------------------------------------------------------
label start:
    #initalize the normal event flag, this should be done before and after every time it is used just incase.
    $ event = 0
    #jump test
    #jump to send to the tech demo, should be commented out for final build
    #jump Beta
    scene black with fade

    l "This game is a work in progress started on 2025 Nov 8. last updated 2026 Feb 3rd."
    g "Since the last private build was released a lot of new writing and art has been added to the project."
    l "Both First dates now have nearly finished dialogue to read but the graphic data is not finished. That being said nearly everything is not final."
    g "Thank you for testing, please report any issues to SM_pai in DM's! remember this is a private test build! Do not post SS or any content from these builds in public places."
    l "If you all behave maybe I'll give you each a little something special when the final build comes along~"
    g "Welcome to the Valentines private test build!"

label Intro:

    scene bbb outside with fade

    nar "..."
    nar "My mind keeps yelling at me this was a bad idea. I can't believe I talked myself into this."
    nar "I've never visited any type of nightclub, much less somewhere this openly..."
    nar "'Explicit'"
    nar "There is no reason to be worried about it now, I'm already here. If I turned back now I would NEVER let myself live it down."
    nar "My heart is already beating out of my chest before I've even opened the door."

    scene bbb entrance with dissolve

    nar "This..."
    nar "Is not what I was expecting." 
    nar "The entrance hall is like a nice resturant's waiting room, it's nothing like the dark dirty room I had expected... maybe this won't be so bad."

    show sak happy with dissolve

    sa "Hello! Welcome to the BBB, my name is Sakura I'll be your hostess for the day."
    nar "Even in her lewd attire Sakura has a air of maturity to her, she seems to be all buisness. The juxtaposition is almost..."
    nar "Cute."
    sa "Did you come here alone love?"
    menu:
        "Did you come here alone love?"

        "Doesn't everyone? Why would you come to a place like this on a date?":
            $ lara_love = lara_love + 1
            $ ghosty_love = ghosty_love - 1
            jump c1a1

        "Yes, I'm actually here to get used to talking to new girls.": 
            $ ghosty_love = ghosty_love + 1
            jump c1a2
label c1a1:
    sta "Doesn't everyone? Why would you come to a place like this on a date?"
    hide sak happy
    show sak pout
    with dissolve
    nar "Sakura looks at me like I'm speaking an alien language, does she really not see how strange that would be?"
    hide sak pout
    show sak smug
    with dissolve
    sa "Many couples come here on dates, we offer lots of 'products' and even private rooms to help couples express their true desires."
    nar "Any 'cute' vibes I had gotten from her are instantly washed away."
    nar "I guess I shouldn't be surprised someone that works at a nightclub would feel so comfortable talking about sexual things..."
    hide sak smug
    show sak happy
    with dissolve
    jump intro2
label c1a2:
    sta "Yes, I'm actually here to get used to talking to new girls."
    hide sak happy
    show sak lewd
    with dissolve
    nar "Sakura looks at me with a... strange smile. I'm unsure what her exact expression is, it seems almost like a mix of pity and... hunger?"
    sa "I'm certain that you'll quickly warm up to the girls here. I wouldn't be surprised if you end the night physically satisfied, if you know what I mean."
    nar "Sakura ends her sentence with a wink like it's a completely normal thing to say to someone you just met."
    nar "My thoughts of her being cute are quickly being washed away with a wave of... thoughts of a different kind."
    hide sak lewd
    show sak happy
    with dissolve

    jump intro2
label intro2:

    nar "Before I can say anything else Sakura has already grabbed a menu and has stepped out from behind the desk she was standing at."
    sa "If you could, please follow me."

    hide sak happy with dissolve

    sta "Oh, of course."
    nar "Maybe I was getting all worked up over nothing! I can already feel my heart calming down as I follow her to the crimson doors."

    scene bbb bar with fade
    #Into the main BBB room
    nar "Holy shit."
    show sak happy with dissolve

    sa "Right this way, we have a table prepared for you please take a seat and I'll be right back."
    nar "I nod, following her and take my seat at the small table for one."

    hide sak happy with dissolve

    nar "The club is full of beautiful women, that's for sure but the neon lights and general atmosphere... it's far more classy than I had expected."
    nar "I fumble through the menu Sakura had laid at my table in between glances at the surrounding scenery, trying to take it all in slow to not overwhelm myself."
    nar "If it wasn't for the pole dancing and ... interesting noises, this actually wouldn't be a bad place for a date."
    nar "Speaking of the pole dancing..."

    #Cg with both looking at each other!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    scene lg cg 1
    sta "I can see why this place is so popular."
    nar "I had read in some of the online reviews that this place had interesting theming but after seeing Sakura I had assumed they just meant Bunny girls."
    nar "I can clearly see now I was mistaken, one of the girls on stage seems to be in a full costume, body paint and all."
    nar "I can't deny theres something alluring about the idea of a Demon girl."
    nar "The red head performing with her is far more what I was expecting but is no less beautiful."
    nar "There's something almost familiar about her I just can't put my finger on it..."
    #Scarlet rose reference, may change or remove?
    scene bbb bar with dissolve
    show sak happy with dissolve
    with dissolve
    sa "Sorry for the wait, heres your complimentary free drink~! Don't worry it's fully on the house, we like to do something special for new faces."
    nar "As Sakura speaks she places a glass of red wine on the table but both her actions and voice are like background noise to my brain as I'm fully lost in thought."
    hide sak happy
    show sak smug
    with dissolve
    sa "Oh? Has my rookie ladykiller set their sights on someone already?"
    hide sak smug
    show sak pout
    with dissolve
    sa "And here I was hoping I would have a chance..."
    nar "Sakura fakes a frown before tracing my sight line to the center stage with a smile."
    hide sak pout
    show sak smug
    with dissolve
    sta "N-no I was just enjoying the show I-"
    
    sa "Oh that's good, no offense but I'm not sure you really have a chance. Those are Fanta's 'Star Girls'."
    sta "Fanta's... Star Girls?"
    sa "Fanta is the owner, those two along with a third who's rarely here are the 'golden trio' of the BBB"
    sa "The purple haired one is her daughter, and she liked the red head so much she let her live with her too."
    hide sak smug
    show sak pout
    with dissolve
    sas "Lucky..."
    sta "What was that?"
    hide sak pout
    show sak lewd
    with dissolve
    sa "Nothing, but yeah. They're like 'prized possessions' almost, 'look but don't touch' stuff you know?"
    hide sak lewd
    show sak smug
    with dissolve
    sa "Like your favorite toy."
    nar "Something tells me she doesn't mean a stuffed animal."
    #fassion doll?
    sta "So, I don't have a chance?"
    hide sak smug
    show sak lewd
    with dissolve
    sa "I didn't say that, the one in red has given private shows to a lucky few, I don't think the 'human' has though..."
    nar "That... was a strange way to word that but that means I might actually have a chance. I can't help but feel a little hopeful."
    hide sak lewd
    show sak smug
    with dissolve
    sa "Oh? Do I see hope in your eyes? What a brave pupal I've trained."
    nar "Okay, yeah she's a little weird."
    sa "Well, I'll leave you be for now~! Break a leg Ladykiller!"
    hide sak smug with dissolve
    sta "Thank you? I think?"
    nar "Sakura's words repeat in my head over and over."
    #Cg with both looking at each other!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    scene lg cg 1 with dissolve
    nar "I literally just saw these girls and haven't even talked to them, but it still kind of burns knowing I don't have even a small shot at a conversation with them."
    nar "This club has so much going on but my eyes seem stuck on the center stage, I can see why they're part of the 'golden trio' of the club."
    nar "Every single movement they make feels like it was perfectly practiced, the show they're putting on is almost hypnotic."
    nar "I feel like I'm watching two goddesses at work."
    scene bbb bar with dissolve
    nar "I stare into the red liquid filling the glass, I'm honestly a little worried Sakura could have put something in this..."
    nar "But if she was that kind of person I doubt she could work in a high profile club."
    #Cg with eyes closed!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    scene lg cg 1 2 with dissolve
    nar "As I look back to the stage, to my dissapointment the show seems to be ending."
    nar "Curse that stupid wine glass and it's ability to make me lose my concentration."
    #Cg with ghosty winking at camera lara looking at her worried!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    scene lg cg 1 3 with dissolve
    nar "As I'm thinking of ways to attempt to hurt an innanimate objects feelings, are they... looking at me?"
    nar "Before I can wonder too long, the demon girl locks eyes with me."
    scene lg cg 1 4 with dissolve
    nar "Is she... calling me up to her?"
    nar "Sakura said she's the owners daughter right? Oh shit did I do something wrong???"
    nar "I can feel my anxiety well up once more, Maybe you're NOT supposed to stare? How could you manage that? Is it what I'm wearing? Is it not classy enough?"
    nar "Could she sense my hostility towards the top heavy liquid holder? (still working on those insults)"
    nar "Maybe she's not..."
    #ghosty annoyed...!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    scene lg cg 1 5 with dissolve
    nar "No, she one-hundered percent is."
    nar "Okay okay, it's best to not keep a lady waiting right? 'If This Be My Destiny' and all that. I just wish I had something to help calm my nerves..."
    menu:
        "Should I calm my nerves with the wine?"

        "Hell No. I'm not going to touch that evil Vixen.":
            jump c2a1

        "Consume the blood of thy enemy.": 
            $ ghosty_love = ghosty_love + 2
            $ lara_love = lara_love + 1
            jump c2a2

#------------------------------------------------------------------------------------------------------------------------------------------------
# How to set flags // in this code it sets if you drink or not. '$ event = 0' . event is the defualt flag for this kind of action as outlined in the header code.
#------------------------------------------------------------------------------------------------------------------------------------------------
label c2a1:
    $ event = 0
    #you don't drink
    nar "I wouldn't dare touch that concoction, there's no telling what Sakura put in there."
    nar "That's totally the reason why... not because I'm still upset or anything."
    jump meetingthegirls

label c2a2: 
    $ event = 1
    #you drink
    nar "I grab the great evil by it's stem and put it to my lips, it will never hurt another soul."
    nar "..."
    nar "I hate to admit it, but chugging that liquid from it's vile container so fast was incredibly painful."
    nar "That was by far the most expensive wine I had ever tasted, how much money does this place have to just give that out for free?"
    nar "There is sadly no time to question the bank roll of a nightclub right now."

    jump meetingthegirls   
label meetingthegirls:
    nar "With a deep breath I stand up and walk to the center stage."
    nar "Each step gets more difficult, I feel more nervous now than I ever have before."
    nar "Before I know it, Destiny arrives."
    scene bbb stage
#------------------------------------------------------------------------------------------------------------------------------------------------
# How to check an event flag / variables
#------------------------------------------------------------------------------------------------------------------------------------------------
#
#
#
#
#
#
    if event == 1:
        show bghosty at right
        with dissolve 

        gu "You okay there love? You looked like you were about to choke. Leave the swallowing to the big girls."
        nar "My brain nearly short circuts as she speaks... Holy shit they're even more attractive up close."
        show blara worry at left
        with dissolve
        lu "Saki!~ You're gonna make them actually choke."
    else:
        show blara at left
        with dissolve
        lu "You got up here quick, don't let Saki scare you~. She doesn't bite..."
        hide blara at left
        show blara smug at left
        with dissolve
        lu "Unless you ask her to."
        show bghosty at right
        with dissolve
        gf "I won't make any promises..."
        hide blara smug
        show blara at left
        with dissolve
    
    
    nar "They seem so... playful? Not the personalities I was expecting. Maybe I'm NOT in trouble?"
    hide blara worry
    show blara at left
    with dissolve
    if event == 1:
        nar "Aw man.. I probably could have savored the spoils of my victory over the glass devil a little longer."
        gf "So, Lara do you want to tell our wine lover why you wanted them up here so bad?"

    else:
        gf"So Lara do you want to tell our runner about the grand-prize you want to give them?"
    hide blara
    show blara worryb at left
    with dissolve
    l "W-What?? You're the one who wanted them to come up here?!"
    nar "Lara's face flushes red, at first glance it's easy to tell she's these two get along well, but not without a little teasing"
    gf "{i}*Sigh*{/i}"
    gf "You're no fun red."

    if ghosty_love >= lara_love:
        hide blara worryb
        show blara pout at left
        with dissolve
        l "And you're way too forward with things."
        gf"Fine, before we go any further what's your name love?"

    else:
        hide blara worryb
        show blara pout at left
        with dissolve
        l"I am fun."
        nar "Lara says with a pout"
        l "I just like to get to know someone before I start saying strange things to them."
        nar "My experience in this club so far tells me that seemingly normal thing makes her the outlier here."
        hide blara pout
        show blara at left
        with dissolve
        l "Okay well For starters... What's your name?"
#------------------------------------------------------------------------------------------------------------------------------------------------
# Code to ask for players name
#------------------------------------------------------------------------------------------------------------------------------------------------
        
label namecheckcode:

    $ povname = renpy.input("Okay, let's get this out of the way. What is your name?", length=25)
    $ povname = povname.strip()

    if not povname:
        $ povname = "The Slayer Of Wine Glasses"  

    if povname in [ "MKscorp", "Iffy", "Hatchet", "Reese", "AnimeGeorge2001", "SaiSuta", "Zero-Q", "SadBoiOnline", "Ricky Dupon", "Minner", "Befortuned", "Lxxi", "Staz", "Silvie", "Jorn"]:
        jump friendlyname


    if povname in [ "ScarletRose", "Scarlet Rose", "scarletrose", "scarlet rose", "Lara Chiba", "Ghosty O'hara", "Fanta O'hara", "Spirit O'hara", "Saki O'hara", "Skyla Chiba", "Sakura"]:
        jump usedname

    if povname in [ "Itzumi"]:
        jump itzuname

    if povname in [ "Mari"]:
        jump marname

    if povname in [ "Vega Chiba"]:
        jump veganame

    if povname in [ "Vincent E."]:
        jump vinname

    if povname in ["Angeline"]:
        jump angname

    if povname in ["Genie"]:
        jump geniename

    if povname in ["Shikki"]:
        jump shikkiname

    if povname in ["Genie"]:
        jump geniename

    if povname in ["Shiori Fujisaki","Monika","Yuri","Natsuki","Sayori"]:
        jump memoname

    if povname in ["MazHazPazzaz"]:
        jump mazname

    if povname in ["mlzrt"]:
        jump beta

    pov "My name is [povname]."

label sohedoeshaveaname:
    #this code checks which girl likes the player more at the moment based on actions up to this point.
    if ghosty_love >= lara_love:
        gf "[povname]? That's a cute name, I'd bet you'd love to hear me moan it~"
        hide blara
        show blara worryb at left
        with dissolve
        l "S-Saki! We just met [povname], you can't be so...lewd. Or atleast not so quickly"
    else:
        l "[povname]..."
        l "I think it suits you. It's a great name."
        nar "Lara speaks with a soft smile, her words are genuine"

    gf "Awww someones interested~. Guess that means it's time to cut to the good stuff!"
    hide blara
    hide blara worryb
    show blara conf at left
    with dissolve
    nar "Lara looks nearly as confused as I do, but I'm happy to know I misunderstood the situation. This seems far more lighthearted than the senarios I was expecting."
    gf "I couldn't help but notice you staring, I mean fuck, I could have sworn you were about to start drooling."
    gf "Hundreds of you pervs come in here every night so I'm sure you're wondering 'why me?' well..."
    hide blara conf
    show blara worry at left
    with dissolve
    gf "I couldn't help but notice Red kept sneaking glances back at you. I've known this bitch for over a year now and in all that time working together I've NEVER seen her stare at anyone so long."
    gf "Except maybe myself ofcour-"
    hide blara worry
    show blara mad at left
    with dissolve
    l_shout "I-I was not!"
    nar "Lara's previous calm nature explodes, I could swear her eyes were glowing as she spoke from how the lights of the club reflected off them."
    hide blara mad
    show blara pout at left
    with dissolve
    l_whisper "I-I mean I might of but I-"
    gf "It's okay doll, they are pretty cute. And if people get to stare at us all night long I think you've earned to take a few looks yourself."
    gf "That being said, if red has interest in you I just KNOW you've got some potential so I'm curious."
    gf "Who do you find more attractive [povname]?"
    hide blara pout
    show blara worry at left
    with dissolve
    l "G-Saki! You can't just ask that!"
    nar "Lara's tone seems less upset and more... anxious. My mother warned me about questions like this. It's times like these I wish I paid attention to what she said."
    pov "Well... if I had to choose..."
    menu:
        "Who do you find more attractive [povname]?"

        "That damn smile and those scarlet eyes, Lara is more my Type.":
            $ lara_love = lara_love + 3
            $ ghosty_love = ghosty_love + 1
            $ lara_date_count = lara_date_count + 1
            jump bbbl

        "I can't deny the alure of a Demon girl, Saki is more my type.": 
            $ ghosty_love = ghosty_love + 2
            $ ghosty_date_count = ghosty_date_count + 1
            jump bbbs

#------------------------------------------------------------------------------------------------------------------------------------------------
# After this point the player has chosen Either Ghosty or Lara
#------------------------------------------------------------------------------------------------------------------------------------------------

#------------------------------------------------------------------------------------------------------------------------------------------------
# Lara BBB Date 1
#------------------------------------------------------------------------------------------------------------------------------------------------
label bbbl:

    pov "If I'm being honest, I think Lara is more my type"
    hide blara pout
    show blara worry at left
    with dissolve
    l_whisper "H-huh?"
    gf "Damn, succutiddies not your thing?"
    pov "N-no I mean you're really attractive too just... something about her."
    gf "You don't have to explain yourself love, Lara's got some impressive curves to her. I'm sure she would love to give you a better look at them~."
    l "W-w-wait... you're not joking right? I mean LOOK at her."
    show blara worry at left
    show blara worry at center
    with dissolve
    with move
    nar "Lara cups Saki's ample chest with her hands."
    hide blara worry
    show blara shout at center 
    with dissolve
    l_shout "LOOK AT THESE."
    hide blara shout
    show blara worry at center
    with dissolve
    l "Y-you really find ME more attractive?"
    nar "Lara's eyes show true confusion... but also fear? Who hurt this girl?"
    pov "I mean..."
    
    menu:
        "Y-you really find ME more attractive?"

        "It's not just that, there's more to liking someone than just sex appeal.":
            pov "It's not just that, there's more to liking someone than just sex appeal."
            l "W-well yeah but Saki is so-"
            $ lara_love = lara_love + 1
            $ ghosty_love = ghosty_love - 1
            jump bbbl2

        "I'm not lying I really do find you more attractive.": 
            pov "I'm not lying I really do find you more attractive."
            g "Ignore her, she just wanted an excuse to grab my chest. Hers is just as big."
            hide blara worry
            show blara pout at center
            with dissolve
            l "N-no I wasn't I-"
            $ lara_love = lara_love + 1
            jump bbbl2
label bbbl2:
    hide blara pout
    hide blara worry
    show blara yell at center
    with dissolve
    nar "It seems Saki's offer of showing herself off finally caught up to Lara."
    l "S-show them my curves a-are you crazy??? We just met?"
    gf "Oh? Well BBB policy deems that any customer who gets singled out by a stage performer is entitled to a private show."
    hide blara yell
    show blara shout at center
    with dissolve
    l "Y-You made that up right now!"
    gf "Huh? Red, I would NEVER do something like that... but you know."
    hide blara shout
    show blara worry at center
    with dissolve
    gf "If you don't want to do it, I could. I'm sure I could give our new 'friend' a night to remember~."
    l "N-no I'll do it!... I-if t-they want that of course..."
    pov "I-"
    gf "Lara. They're practically as red as your hair. They obivously want you. Come on girl I know you're not this oblivious."
    nar "I hadn't even noticed how red I was until Saki mentioned it. I feel like my heart is about to beat right out of my chest."
    nar "A PRIVATE SHOW? What does that even mean? Didn't sakura say Lara hadn't done any private shows? Does that mean..."
    nar "No. Brain calm down. This is literally her job."
    pov "I-I mean. If you want to I'd love t-"
    gf "Great to hear! You two horny dogs go have fun in one of the private rooms, try not to break anything~!"
    hide blara worry
    show blara pout at center
    with dissolve
    gf "Or each other~."
    show blara pout at left with move
    nar "Saki nearly shoves Lara off the stage after handing her a key that she had kept between the cleavage of her bunny suit. Saki seemed like she was far too prepared for this."
    hide blara pout
    show blara yell at left
    with dissolve
    l "W-wait but my shif-"
    gf "Lara. You and I both know Fanta would be lubing you up herself if she knew you were finally taking interest in someone. Go! I'll finish our shift alone."
    gf "But I expect to hear about EVERYTHING that happened. Got it?"
    hide blara yell
    show blara worry at left
    with dissolve
    l "I..."
    #all text before this point has been given a second read through as of 11/17/2025
    gf "No ifs, ands, or buts, not even your massive one. You cover for me whenever I'm in the mood for a snack, now it's my turn. Go! Have fun!"
    hide blara worry
    show blara pout at left
    with dissolve
    l "My Butt is NOT massive."
    gf "So now you're lying to yourself and me? Go enjoy your time off before I call Fanta."
    hide blara pout
    show blara shout at left
    with dissolve
    l_shout "UGHGHH. Fine."
    hide blara shout
    show blara pout at left
    with dissolve
#how to hide characters and how to move character to center!!!
    hide bghosty with moveoutright
    show blara pout at center
    with move
    scene bbb stairs with dissolve
    nar "Without further warning Lara grabs my hand and begins leading me to a door with a sign reading 'Staff Only' "
    scene bbb stairs2 with dissolve
    nar "As she unlocks the door to the private room upstairs I can hear her breath becoming more heavy. Maybe I missread the conversation and Saki really was getting under her skin?"
#LC1
    menu:
        "Should I say something?"

        "Hey, are you okay?":
            $ lara_love = lara_love + 1
            pov "Hey, are you okay?"
            l "Huh?"
            l_whisper "Oh, Oh gosh I'm sorry. I'm just a little nervous is all... I really do uhm."
            l "Nevermind, yes I'm okay."
            nar "I smile as we walk up the stairs, I can fully understand being nervous."
            jump bbbl3

        "Say nothing.": 
            nar "It's probably best I dont say anything..."
            nar "Her grip on my hand tightens as we walk up the stairs."
            jump bbbl3
label bbbl3:
    scene bbb private room with dissolve
    show blara with dissolve
    l "Well uhh... Welcome to the Queen suite!"
    nar "Lara's words come out with the fakest confidence I have ever heard. Maybe Sakura really was telling the truth when she said Lara has never done this before."
    nar "If the main floor just 'impressed' me with how classy it was, the 'private room' has nearly given me a stroke. The room has a bed, a couch, a minifridge, a tv, tables and chairs, It's like a mini apartment."
    nar "In fact, this room is FAR NICER than my own. I find myself once again questioning just how much money this club has?"
    pov "It is really nice."
    l "I know right? I usually come up here for my breaks, It's way better than sitting in the public break room having to make small talk with people I barely know in my 'relaxation' time y'know?"
    nar "As Lara sits down on the soft matress in the corner of the room removing the heels she had been wearing, she smiles softly to herself."
    hide blara
    show blara worry at center
    with dissolve
    l "Sorry for being so... tense... I've never really done this before so I'm not exactly super ready-"
    nar "Lara pauses mid sentence looking up at me."
    hide blara worry
    show blara yell at center
    with dissolve
    l "N-Not to say I don't want to do this. I really do uhm... "
    hide blara yell
    show blara at center
    with dissolve
    l "I would love for you to be my first private show I'm just a little nervous is all..."
    menu:
        "?"

        "That's okay we all get nervous sometimes.":
            $ lara_love = lara_love + 2
            pov "That's okay we all get nervous sometimes."
            l "Thank you, for real. Knowing that you're chill with me being anxious honestly makes me feel a lot better."
            pov "Of course, I was really anxious just to walk into the club in the first place."
            l "Oh same, I was sweating bullets the first time I came here."
            pov "Really? I wouldn't expect a woman as attractive as you to be so anxiety filled."
            l "I've gotten a lot better since I started working here. Saki took interest in me the first day we met, once she heard my story and got to know me a bit she introduced me to her mom."
            l "One thing lead to another and now I get to work with my best friend and get to live in a mansion with her mom. Stepping out of your comfort zone can be really rewarding sometimes."
            pov "So, you went from being anxious about your first visit to working here?"
            hide blara
            show blara think at center
            with dissolve
            l "Hmm..."
            nar "Lara adjusts her top as she thinks. It's nice to feel like someone is actually considering my questions and not judging me for finding this all a little jarring."
            hide blara think
            show blara at center
            with dissolve
            l "I mean, Saki was already offering me a job as soon as we started talking. She just saw something special in me I guess."
            l "Once I met Fanta I basically had no hope of turning her down, not that it matters I enjoy working here."
            pov "I can see why they wanted you so bad. Watching you on stage it seemed almost unreal how mesmerizing you were."
            pov "I mean, it must have taken you forever to learn all those movements."
            l "It did take a pretty long time."
            nar "Lara's smile grows as she responds, having such a casual conversation seems to be calming us both down."
            l "Saki is a really good friend, even if we do argue sometimes. It's all in good spirit."
            pov "Like about your butt earlier?"
            hide blara
            show blara worry at center
            with dissolve
            nar "Lara's eyes widen at my words. I seem to have struck a cord."
            l "I-I mean, I guess so... You don't agree with her do you?"
            pov "W-what do you mean?"
            hide blara worry
            show blara shout at center
            with dissolve
            l "Like, my butt is nothing special. She acts like its HUGE. I swear hers is almost the same size as mine."
            nar "I'm not sure what the right thing to say here is. I mean it's not like I'm some ass expert, and as much as I was staring I don't think I got a good look at it earlier."
            pov "Well I mean I haven't really gotten that good of a-"
            l "Oh, well here look."
            jump bbbl4

        "Did what Saki said make you anxious?": 
            pov "Did what Saki said make you anxious?"
            hide blara
            show blara worry at center
            with dissolve
            l "What? Oh, no. I'm still just not used to really being y'know... Like this with people yet."
            pov "I unders-"
            hide blara worry
            show blara pout at center
            with dissolve
            l_shout "Wait."
            nar "Lara's expression darkens."
            hide blara pout
            show blara mad at center
            with dissolve
            l "Are you talking about that last thing she said?"
            nar "I tilt my head in confusion. I can't seem to remember what Saki had said before we left, I think by that point my brain was already fried."
            l "My butt is NOT that fat."
            pov "Oh, That I mean I ca-"
            hide blara mad
            show blara shout at center
            with dissolve
            l "Wait, here look."
            jump bbbl4
label bbbl4:
    hide blara with dissolve
    nar "Before I can even think about reacting to whats  happening Lara has crawled fully onto the bed."
    show l cg 1 with dissolve
    l "Look, It's not that big, right?"
    nar "Holy."
    nar "Shit."
    nar "My mother warned me about a lot of things, this situation is not one of them."
    nar "I mean, we went up here for a private show but with how casual thing had been I was not mentally prepared to be greeted by easily the nicest ass I have ever seen in my life."
    l "Hello?~ Earth to [povname]? You still in there?"
    pov "I uhm-"
    menu:
        "Look, It's not that big, right?"

        "In the nicest way, I think I agree with Saki.":
            $ ghosty_love = ghosty_love + 1
            pov "In the nicest way, I think I agree with Saki."
            l "HUH?"
            pov "N-no Like it's fat in a good way. like you're really hot-"
            nar "My words escape my mouth before I realize what I'm saying. It's not untrue but damnit thats such a bad way to tell someone unprompted they're Attractive for the first time."
            l "Y-You... Really think I'm hot?"
            nar "Or maybe not? Lara seems surprised, but happy with my very forward comment. Maybe she's not as shy as she lets on?"
            show l cg 1 4 with dissolve
            l "I think I understand now... "
            jump bbbl5

        "Say nothing.": 
            nar "I can't bring myself to lie to her, Her ass is pretty big but in the best possible way."
            l "Hello? Did you like, blue screen or somethin-"
            show l cg 1 4 with dissolve
            nar "Lara's determined expresion is quickly replaced with a smirk as realization hits her."

            jump bbbl5           
label bbbl5:

    show l cg 1 2 with dissolve
    l "This is doing something for you isn't it?~"
    nar "I wonder what gave me away first? My silence, the fact my face is burning up, or..."
    l "It's okay to be shy, trust me It takes a while to get used to this kind of thing."
    nar "Something about getting me flustered seems to have lit a fire inside Lara, it's like all the anxiety and fear she had building up inside her melted away."
    pov "I mean I-I can't say it isn't"
    l "aww, but you're not able to say it is? Am I not good enough for you?"
    nar "Damnit she's good at this. for someone who's inexperienced she's doing a VERY good job."
    pov "Y-you are more than good enough for me."
    show l cg 1 3 with dissolve
    l "mmh~ I'm happy to hear you say that."
    nar "Her soft moan sends a shock through my body, my voice feels like its caught in my throat. Every movement she makes is making it harder to think straight."
    l "you know, Maybe you could help me take this o-"
    ph "'Buh duh duh ding'"
    scene bbb private room with dissolve
    hide l cg 1
    hide l cg 1 2
    hide l cg 1 3
    show blara yell with dissolve
    nar "Lara's eyes widen as she flips back to a seated position scrambling to pull her phone out of her uniform's top."
    hide blara yell
    show blara think
    with dissolve
    l "I s-sorry just uhm give me a minute I just uhm."
    hide blara think
    show blara worry
    with dissolve
    l "I just need to check this notification real quick It's uhm really important then I'll mute my phone, Promise."
    nar "as I watch her fidget with her phone it finally clicks in my brain what app that notification came from."
    pov "Wait, Was that a Quuest Treasures Online notification?"
    show laraphone1 with dissolve
    l "Huh, wait.... you play?"
    nar "The programmer has a nap. Hold out! Programmer!"
    jump end







#------------------------------------------------------------------------------------------------------------------------------------------------
# Ghosty BBB Date 1
#------------------------------------------------------------------------------------------------------------------------------------------------
label bbbs:
    pov "I can't deny the alure of a Demon girl, Saki is more my type"
    l_whisper "Agreed, Saki is pretty aluring.~"
    nar "Lara smiles, she's obviously being honest but suprisingly she seems a little dissapointed in my answer. She must not take dissapointment well."
    gf "I'm no regular demon, I'm a Succubus love."
    nar "Succubus?"
    gf "Semen demon. Soul-sucker. Vampire for cum. Whatever helps you imagine it."
    gf "All that matters is that I'll give you the best night of your life."
    gf_whisper "or last..."
    pov "Should I be worried?"
    l_whisper "Only if you're scared of losing your soul."
    nar "Lara seems to have recovered well, she's back to smiling but her words have done anything but calm me, but before I can think too much Ghosty's voice brings me back to reality."
    gf "Don't be scared, love. I will take very good care of you."
    nar "The flame eyed performer licks her teeth as she smiles"
    pov "I feel like I'm walking into a trap."
    gf "You wouldn't be here if you weren't already looking for a little fun. "
    gf "I am just adding a touch of something... more exciting. Don't you want to let your imagination become reality?"
    nar "Saki's eyes glisten as she stares at me, its almost like shes pleading. She's obviously very experienced in this kind of thing."
    nar "the character she's playing feels so real. It's hard to believe she really isn't some kind of sex demoness."

    menu:
        "Don't you want to let your imagination become reality?"

        "What an amazing night to feel cursed.":
            pov  "What an amazing night to feel cursed."
            nar "The sentence slips out of my mouth without much thought especially not to how random it seems out of context. If this kind of 'Demon' is interested in me, Maybe curses aren't that bad."
            l "Oooo, gaming references while talking to a hot girl? I like you."
            nar "Saki blankly stares as me and Lara go back and forth for a second about gaming."
            gf "You're both so... odd..."
            nar "Saki was clearly dumbfounded by the two making gaming references."
            $ lara_love = lara_love + 1
            jump bbbs2

        "How much of my imagination, exactly?":
            $ ghosty_love = ghosty_love + 2
            pov "How much of my imagination, exactly?"
            nar "Part of me was afraid to find out the answer..."
            gf "Well, that's honestly up to you, love~"
            gf "You could let your mind run wild for all I care. I'm truly up for anything that dirty little brain can think of."
            l "Saki is very good at making dreams come true."
            l_whisper "I wish she would do the same for me..."
            gf "So tell me.. what is your wildest fantasy?"
            $ fantasy = renpy.input("So tell me.. what is your wildest fantasy?", length=45)
    $ fantasy = fantasy.strip()

    if not fantasy:
        $ fantasy = "Getting the soul sucked out of my body"

    jump bbbs2a

label bbbs2a:
    pov "[fantasy]"
    gf "Hot."
jump bbbs2
    
label bbbs2:
    gf "Anyways, if you're interested, I can treat you to a little private show~"
    nar "Sakura said Saki was the owners daughter right? I'm not sure my heart could handle something like that but..."
    nar "I would be CRAZY to say no, this could be a once in a life time chance."
    pov "Well.. if you're offering-"
    gf "Great!"
    nar "Before I could even finish she was already pulling a key out from between the cleavage of her bunny suit."
    l "You.. you just have that in there..?!"
    gf "Duh! A key to a room this special can not just be left out anywhere!~ Do you have the rest of the shift covered or should I call someone to come help?"
    l "Oh, Uhm no I'll be fine, Go have your fun!~"
    gf "Thanks Red!~ I'll pay you back later, Promise!~"
    nar "The way the two are talking this seems to happen pretty often."
    l "It's okay Saki Just don't be too rough with them..."
    nar "Lara's words come out with an emotion I can't quite place, is she just sad I didn't pick her or... Actually worried?"
    gf "I can't make any promises~ Now, Follow me love.~"
    nar "Saki's words are followed with a wink that causes my heart to race, its like she has me under a spell with how every little thing she does is just so... perfect."
    nar "As my mind continues its attempt to catch up with everything that's going on, Saki grabs my hand and begins leading me to a door with a sign reading 'Staff Only' "
    nar "As I followed behind her, the costumes tail seeming to sway in slow motion as we climed the stairs to the second floor. I can hear my heart pounding in my chest louder with each step."
    nar "Before I know it Saki has opened the door to the room where all my anxiety will hopefully soon be replaced with pleasure."
    gf "Make yourself comfortable, Hun."
    nar "If the main floor just 'impressed' me with how classy it was, the 'private room' has nearly given me a stroke. The room has a bed, a couch, a minifridge, a tv, tables and chairs, It's like a mini apartment."
    nar "This is just a room for private shows? It's amazing."
    gf "Oh? I mean it's nothing special. You should see the rooms back at the mansion."
    nar "Saki was incredibly calm about this ordeal... Though I suppose this is the norm for her. If the clubs private rooms are like this, I can't even begin to imagine what her home looks like"
    gf "I can tell you're nervous. There's no need to be shy, love. I I'm not going to hurt you..."
    gf_whisper "Unless you want me to."
    nar "Every time she whispers I wonder if she knows I can still hear her.."
    pov "I just don't know what to think about this whole... situation. I'm still catching my breath."
    gf "Well, what did you expect walking into the place?"
    nar "theres no arguing against her words, There's no sense in being bashful now."
    pov "I guess I just didn't expect this much attention. Especially so quickly"
    gf "But it's nice, isn't it? Besides, Red obviously saw something special in you and she has an AMAZING eye for this kind of thing."
    gf "Plus, I love making guests feel welcome~"
    nar "without further warning Saki Places her hands on my chest causing a soft shiver to run through my body. I swear she's like a living aphrodisiac."
    gf "Now... How about we get comfortable?"
    nar "Saki pushes into me softly, as I step back I bump into the bed sat in the corner of the room"
    gf "Go ahead, take a seat love.~"
    nar "I could feel the heat of her body against mine. The sensation making my mind blur for a moment before I snapped back."
    nar "I did as told and sat on the bed, my palms awkwardly fell to my sides on the mattress."
    pov "Um.. I thought this place was about 'look don't touch?'"
    gf "Mmm.."
    nar "There was a mischevious glint in Saki's eyes as she let my question hang in the air for a moment."
    gf "You're right.. but I can make exceptions."
    gf "I want to give you a once in a life time expereience after all~"
    nar "Without another thought Saki's body moved on to my lap. "
    nar "I could barely form a sentence feeling Saki on top of me."
    # Lap CG pov
    gf "I hope I don't weight too much for you.."
    pov "No! Not at all!"
    nar "Saki giggled. She wasn't worried at all but it was entertaining to see them get so frantic."
    gf "Well that's good to hear."
    nar "The tone of her voice shifted to something much more.. sultry."
    gf "Don't be shy. I'm making a rare exception, so take advantage of it, darling."
    nar "Saki guided my hand all across her body, the palms of my hand caressing each inch she allowed me to touch."
    gf "You're so shaky~"
    pov "Can you blame me? It's not like I expected to be put in this situation."
    gf "I can give you so much more than this~"
    pov "More?"
    nar "A chill ran down my spine. I have no idea what she is capable of.. but I felt so drawn to find out."
    pov "Please.. I want more"
    gf "Aww~ I like the sound of desperation from you."
    nar "Saki was clearly getting more and more excited by the second. Her hips were practically grinding against my lap."
    nar "The heat of her body was making my mind swirl."
    nar "Without a moment's notice Saki lifted herself off my lap and pulled me to stand up."
    gf "I did promise you a show, didn't I?"
    nar "Saki moved to be on the bed, slowly strip teasing me. She tosssed each piece of clothing to the side until her body was bare to my eyes."
    nar "My brain could barely wrap my head around the sight in front of me."
    gf "I'm going to assume you like what you see"
    nar "I couldn't even form a sentence as I took in every inch of her skin."
    pov "Y-yes! Of course!"
    gf "Good. Join me, darling, or do you need me to help you?"

    # Bed CG pov
    
    nar "The programmer has a nap. Hold out! Programmer!"

    jump end


#end the game and return player to title
    label end:

    nar "thank you for play testing the demo <3"
    #this ends the game do not add anything after this point.
    return
#------------------------------------------------------------------------------------------------------------------------------------------------
# End of game above, next is sub systems used for special events
#------------------------------------------------------------------------------------------------------------------------------------------------
#name checker output for Final
    label friendlyname:
        l "Oh! You have the same name as one of my friends"
        l "What a coincidence."
        l "..."
        l ";)"
        jump sohedoeshaveaname

    label usedname:
        l "..."
        l "Nice try. Don't you think that might get a little confusing?"
        jump namecheckcode

    label veganame:
        l "Don't."
        $ lara_love = 0
        $ povname = "Dumb Bitch <3"
        jump sohedoeshaveaname

    label geniename:
        l "Hey! its been a while."
        l "I hope Angeline has been doing well!"
        jump sohedoeshaveaname

    label itzuname:
        l "Oh! Itzumi!"
        gf "Hey mommy ;)!"
        jump sohedoeshaveaname

    label vinname:
        l "Do you happen to be scottish?"
        gf "And or an incubus?"
        jump sohedoeshaveaname

    label marname:
        l "Huh..."
        l "You don't really look like a fox girl to me..."
        g "why would you say something so strange to someone we just met?"
        l "It's basic procedure"
        jump sohedoeshaveaname

    label memoname:
        l "Oh! Like the dating sim character!"
        l "Promise not to love bomb me and I'm sure we will get along fine!"
        gf "?"
        jump sohedoeshaveaname

    label shikkiname:
        l_shout "OH MY GOD"
        l "It's Shikki the creator of the hit RPG series final f-"
        gf "Hun. Calm down you're gonna get us copyright struck."
        jump sohedoeshaveaname

    label angname:
        l "Angel! it's been so long!~"
        l "We have got to catch up with each other more often!"
        l "Nice of you to visit me at work for a change!~"
        jump sohedoeshaveaname

    label mazname:
        l "Maz! It's been a while!"
        l "How are Willow and Morgan? Still hot?"
        jump sohedoeshaveaname
    #Name Ch
















#BETA CODE LEFT IN WITH mlzrt EASTER EGG DO NOT TOUCH OR ADD CODE.
#Original test code, might leave this in as an easter egg? maybe have pn "test" send you here?
    label beta:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bbb bar test
 

    # These display lines of dialogue.
#name select, makes MC annon if no name is chosen
    $ povname = renpy.input("Okay, lets get this out of the way. What is your name?", length=20)
    $ povname = povname.strip()

    if not povname:
        $ povname = "Annon"  

    if povname in [ "Itzumi", "Vincent E.", "Mari", "Iffy",  "Shikki", "Hatchet", "AnimeGeorge2001", "Shiori Fujisaki", "SaiSuta", "Zero-Q", "SadBoiOnline", "MazHazPazzaz", "Rdup", "Minner", "Befortuned", "Dasani"]:
        jump huh

    if povname in [ "Vega", "ScarletRose", "Scarlet Rose", "scarletrose", "scarlet rose", "Lara Chiba", "Ghosty O'hara", "Fanta O'hara", "Spirit O'hara", "Saki O'hara", "skyla", "Sakura"]:
        jump huh2

    label passbeta:

        show ghosty test with dissolve:
            xalign 0.9
            yalign 1.0

        show lara test with dissolve:
            xalign 0.1
            yalign 1.0

        l "Welcome to the next Level [povname]!"
        #new line added post beta
        l "I'm happy to see you here again... We've been so lonely... so very lonely... won't you join us?"
        g "Is that some kind of reference?"
#question choice path
    menu:
        "?"

        "huh, that was pretty easy to get to work!":
            jump yes1

        "why are you a sketch?": 
            jump no1
#Huh, That was pretty easy to get to work!

    label yes1:

    l "Tech is truly amazing! I'm in a visual novel!"

    pov "How do you know that..."

    l_whisper "Don't ask questions you don't want to learn the answers to."

    pov "What was that?"

    l_shout "Don't pretend like you didn't get as much time as you wanted to read that."

    pov "What?"
    hide lara test
    show lara test sad:
            xalign 0.1
            yalign 1.0
    l "..."

    l_whisper "Pre written MC dialogue in visual novels piss me off. Why is the player fill in always such a dumb ass..."


    jump end
#Why Are You A Sketch?
    label no1:

        l_shout "HUH?!"
        
        hide lara test
        show lara test sad:
            xalign 0.1
            yalign 1.0
        

        l "It's rude to ask a girl a question like that y'know..."

        l "I think I'm pretty well defined for this point in development..."

        pov "certain parts of you are well defined that's for sure..."

        g_shout "truth"

        hide lara test sad
        show lara test:
            xalign 0.1
            yalign 1.0

        l "I'll take that as a compliment <3"

        l "Maybe all Annonymous player characters aren't annoying"

        pov "Sweet! does that mean I get a CG of us having ''some fun'' togehter?"

        hide lara test
        show lara test sad:
            xalign 0.1
            yalign 1.0

        l "And you ruined it..."

   
        jump end
#beta name check
    label huh:

        l "Oh! You have the same name as one of my friends"

        l "What a coincidence"

        l "..."

        l ";)"

        jump passbeta

    label huh2:

        l "..."

        l "Nice try. Don't you think that might get a little confusing?"
        jump passbeta