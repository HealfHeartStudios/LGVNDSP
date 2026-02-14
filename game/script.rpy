#w Code Project Start Date Nov 8 2025
#w This is a github test 2
#w ------------------------------------------------------------------------------------------------------------------------------------------------
#w Character definitions. setting var name, screen name, name color.
#w ------------------------------------------------------------------------------------------------------------------------------------------------
#w lara
define lu = Character("???", color="#ff0000")
define l = Character("Lara Chiba", color="#ff0000")
define l_shout = Character("Lara Chiba", who_color="#ff0000", what_size=50 )
define l_whisper = Character("Lara Chiba", who_color="#ff0000", what_size=18)
#w ghosty
define gu = Character("???", color="#a900af")
define g = Character("Ghosty O'hara", color="#a900af")
define g_shout = Character("Ghosty O'hara", who_color="#a900af", what_size=50)
define g_whisper = Character("Ghosty O'hara", who_color="#a900af", what_size=18)
define gf = Character("Saki O'hara", color="#a900af")
define gf_whisper = Character("Saki O'hara", who_color="#a900af", what_size=18)
#w ghostyfake/Saki
#w Side Characters
define f = Character("Fanta O'hara", who_color="#d47100")
define s = Character("Spirit O'hara", who_color="#c55ca6")
define sa = Character("Sakura", who_color="#ff8292")
define sas = Character("Sakura", who_color="#ff8292", what_size=18)
#w PC related Characters
define nar = Character(what_italic=True)
define pov = Character("[povname]", color="#faf0f0")
define fantasy = Character("[fantasy]", color="#faf0f0")
#w Defaualt PC before player chooses name for start
define sta = Character("You", color="#faf0f0")
define ph = Character("Phone", color="#faf0f0")
#w ------------------------------------------------------------------------------------------------------------------------------------------------
#w affection scores and other flags
#w ------------------------------------------------------------------------------------------------------------------------------------------------
default lara_love = 5
default ghosty_love = 5
default event = 0
default drink = 0
default lara_date_count = 0
default ghosty_date_count = 0
default wf = 0
#w ------------------------------------------------------------------------------------------------------------------------------------------------
#w May not be needed. do not delete just incase. I have no clue what the fuck im doing.
#w ------------------------------------------------------------------------------------------------------------------------------------------------
transform moveright:
    linear 0.4 xpos 0.9
transform moveleft:
    linear 0.4 xpos 0.1
#w ------------------------------------------------------------------------------------------------------------------------------------------------
#w Logo splash. Disable while testing 
#w ------------------------------------------------------------------------------------------------------------------------------------------------
label splashscreen:
    $ renpy.movie_cutscene("images/logo.webm")
    return

#w ------------------------------------------------------------------------------------------------------------------------------------------------
#w Game starts here.
#w ------------------------------------------------------------------------------------------------------------------------------------------------
label start:
    #w initalize the normal event flag, this should be done before and after every time it is used just incase.
    $ event = 0
    #w jump test
    #w jump to send to the tech demo, should be commented out for final build
    #w jump Beta
    scene message with dissolve

    l "This game is a work in progress started on 2025 Nov 8. last updated 2026 Feb 13th."
    g "Both full first dates are mostly complete. Backgrounds are unfinished and audio is still missing from the game confusing which Sadly means you don't get to hear my moans."
    l "Maybe next time ;)."
    g "Thank you for testing, please report any issues to SM_pai in DM's! remember this is a private test build! Do not post SS or any content from these builds in public places. We want the plot to be a surprise!"
    l "If you all behave maybe I'll give all the testers a little something special in game when the final build comes along~!"
    g "Welcome to the Valentines private test build! Thank you for your time."

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
    #w Into the main BBB room
    nar "Holy shit."
    show sak happy with dissolve

    sa "Right this way, we have a table prepared for you please take a seat and I'll be right back."
    nar "I nod, following her and take my seat at the small table for one."

    hide sak happy with dissolve

    nar "The club is full of beautiful women, that's for sure but the neon lights and general atmosphere... it's far more classy than I had expected."
    nar "I fumble through the menu Sakura had laid at my table in between glances at the surrounding scenery, trying to take it all in slow to not overwhelm myself."
    nar "If it wasn't for the pole dancing and ... interesting noises, this actually wouldn't be a bad place for a date."
    nar "Speaking of the pole dancing..."

    #w Cg with both looking at each other!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    scene lg cg 1
    sta "I can see why this place is so popular."
    nar "I had read in some of the online reviews that this place had interesting theming but after seeing Sakura I had assumed they just meant Bunny girls."
    nar "I can clearly see now I was mistaken, one of the girls on stage seems to be in a full costume, body paint and all."
    nar "I can't deny theres something alluring about the idea of a Demon girl."
    nar "The red head performing with her is far more what I was expecting but is no less beautiful."
    nar "There's something almost familiar about her I just can't put my finger on it..."
    #w Scarlet rose reference, may change or remove?
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
    #w fassion doll?
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
    #w Cg with both looking at each other!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    scene lg cg 1 with dissolve
    nar "I literally just saw these girls and haven't even talked to them, but it still kind of burns knowing I don't have even a small shot at a conversation with them."
    nar "This club has so much going on but my eyes seem stuck on the center stage, I can see why they're part of the 'golden trio' of the club."
    nar "Every single movement they make feels like it was perfectly practiced, the show they're putting on is almost hypnotic."
    nar "I feel like I'm watching two goddesses at work."
    scene bbb bar with dissolve
    nar "I stare into the red liquid filling the glass, I'm honestly a little worried Sakura could have put something in this..."
    nar "But if she was that kind of person I doubt she could work in a high profile club."
    #w Cg with eyes closed!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    scene lg cg 1 2 with dissolve
    nar "As I look back to the stage, to my dissapointment the show seems to be ending."
    nar "Curse that stupid wine glass and it's ability to make me lose my concentration."
    #w Cg with ghosty winking at camera lara looking at her worried!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    scene lg cg 1 3 with dissolve
    nar "As I'm thinking of ways to attempt to hurt an innanimate objects feelings, are they... looking at me?"
    nar "Before I can wonder too long, the demon girl locks eyes with me."
    scene lg cg 1 4 with dissolve
    nar "Is she... calling me up to her?"
    nar "Sakura said she's the owners daughter right? Oh shit did I do something wrong???"
    nar "I can feel my anxiety well up once more, Maybe you're NOT supposed to stare? How could you manage that? Is it what I'm wearing? Is it not classy enough?"
    nar "Could she sense my hostility towards the top heavy liquid holder? (still working on those insults)"
    nar "Maybe she's not..."
    #w ghosty annoyed...!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
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

#w------------------------------------------------------------------------------------------------------------------------------------------------
#w How to set flags // in this code it sets if you drink or not. '$ event = 0' . event is the defualt flag for this kind of action as outlined in the header code.
#w------------------------------------------------------------------------------------------------------------------------------------------------
label c2a1:
    $ drink = 0
    #you don't drink
    nar "I wouldn't dare touch that concoction, there's no telling what Sakura put in there."
    nar "That's totally the reason why... not because I'm still upset or anything."
    jump meetingthegirls

label c2a2: 
    $ drink = 1
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
#w------------------------------------------------------------------------------------------------------------------------------------------------
#w How to check an event flag / variables
#w------------------------------------------------------------------------------------------------------------------------------------------------
#w
#w
#w
#w
#w
#w
    if drink == 1:
        show bghosty tease at right
        with dissolve 

        gu "You okay there love? You looked like you were about to choke. Leave the swallowing to the big girls."
        nar "My brain nearly short circuts as she speaks... Holy shit they're even more attractive up close."
        show blara worry at left
        with dissolve
        lu "Saki!~ You're gonna make them actually choke."
        hide bghosty fsmile
        show bghosty smile at right
        with dissolve
    else:
        show blara at left
        with dissolve
        lu "You got up here quick, don't let Saki scare you~. She doesn't bite..."
        hide blara at left
        show blara smug at left
        with dissolve
        lu "Unless you ask her to."
        show bghosty fsmile at right
        with dissolve
        gf "I won't make any promises..."
        hide blara smug
        show blara at left
        with dissolve
        hide bghosty fsmile
        show bghosty smile at right
        with dissolve
    
    
    nar "They seem so... playful? Not the personalities I was expecting. Maybe I'm NOT in trouble?"
    hide blara worry
    show blara at left
    with dissolve
    if drink == 1:
        nar "Aw man.. I probably could have savored the spoils of my victory over the glass devil a little longer."
        hide bghosty smile
        show bghosty tease at right
        with dissolve
        gf "So, Lara do you want to tell our wine lover why you wanted them up here so bad?"

    else:
        hide bghosty smile
        show bghosty tease at right
        with dissolve
        gf"So Lara do you want to tell our runner about the grand-prize you want to give them?"
    hide blara
    show blara worryb at left
    with dissolve
    l "W-What?? You're the one who wanted them to come up here?!"
    nar "Lara's face flushes red, at first glance it's easy to tell she's these two get along well, but not without a little teasing"
    hide bghosty tease
    show bghosty at right
    with dissolve
    gf "{i}*Sigh*{/i}"
    gf "You're no fun red."

    if ghosty_love >= lara_love:
        hide blara worryb
        show blara pout at left
        with dissolve
        l "And you're way too forward with things."
        hide bghosty
        show bghosty judge at right
        with dissolve
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
#w------------------------------------------------------------------------------------------------------------------------------------------------
#w Code to ask for players name
#w------------------------------------------------------------------------------------------------------------------------------------------------
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

    if povname in ["Daddy"]:
        jump daddyname

    if povname in ["mlzrt"]:
        jump beta

    pov "My name is [povname]."

label sohedoeshaveaname:
#w this code checks which girl likes the player more at the moment based on actions up to this point.
    if ghosty_love >= lara_love:
        hide bghosty
        hide bghosty judge 
        show bghosty tease at right
        with dissolve
        gf "[povname]? That's a cute name, I'd bet you'd love to hear me moan it~"
        hide blara
        show blara worryb at left
        with dissolve
        l "S-Saki! We just met [povname], you can't be so...lewd. Or atleast not so quickly"
    else:
        l "[povname]..."
        l "I think it suits you. It's a great name."
        nar "Lara speaks with a soft smile, her words are genuine"
        


    hide bghosty
    hide bghosty judge 
    hide bghosty tease
    show bghosty fsmile at right
    with dissolve
    gf "Awww someones interested~. Guess that means it's time to cut to the good stuff!"
    hide blara
    hide blara worryb
    show blara conf at left
    with dissolve
    nar "Lara looks nearly as confused as I do, but I'm happy to know I misunderstood the situation. This seems far more lighthearted than the senarios I was expecting."
    hide bghosty fsmile
    show bghosty smile at right
    with dissolve
    gf "I couldn't help but notice you staring, I mean fuck, I could have sworn you were about to start drooling."
    gf "Hundreds of you pervs come in here every night so I'm sure you're wondering 'why me?' well..."
    hide blara conf
    show blara worry at left
    with dissolve
    hide bghosty smile
    show bghosty tease at right
    with dissolve
    gf "I couldn't help but notice Red kept sneaking glances back at you. I've known this bitch for over a year now and in all that time working together I've NEVER seen her stare at anyone so long."
    hide bghosty tease
    show bghosty fsmile at right
    with dissolve
    gf "Except maybe myself ofcour-"
    hide blara worry
    show blara mad at left
    hide bghosty fsmile
    show bghosty at right
    with dissolve
    l_shout "I-I was not!"
    nar "Lara's previous calm nature explodes, I could swear her eyes were glowing as she spoke from how the lights of the club reflected off them."
    hide blara mad
    show blara pout at left
    hide bghosty
    show bghosty smile at right
    with dissolve
    l_whisper "I-I mean I might of but I-"
    gf "It's okay doll, they are pretty cute. And if people get to stare at us all night long I think you've earned to take a few looks yourself."
    hide bghosty smile
    show bghosty tease at right
    with dissolve
    gf "That being said, if red has interest in you I just KNOW you've got some potential so I'm curious."
    hide bghosty tease
    show bghosty fsmile at right
    with dissolve
    gf "Who do you find more attractive [povname]?"
    hide blara pout
    show blara worryb at left
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

#w------------------------------------------------------------------------------------------------------------------------------------------------
#w  After this point the player has chosen Either Ghosty or Lara
#w------------------------------------------------------------------------------------------------------------------------------------------------

#r------------------------------------------------------------------------------------------------------------------------------------------------
#r Lara BBB Date 1
#r------------------------------------------------------------------------------------------------------------------------------------------------
label bbbl:

    pov "If I'm being honest, I think Lara is more my type"
    hide bghosty fsmile
    show bghosty at right
    with dissolve
    l_whisper "H-huh?"
    hide bghosty
    show bghosty judge at right
    with dissolve
    gf "Damn, succutiddies not your thing?"
    pov "N-no I mean you're really attractive too just... something about her."
    hide bghosty judge
    show bghosty smile at right
    with dissolve
    gf "You don't have to explain yourself love, Lara's got some impressive curves to her. I'm sure she would love to give you a better look at them~."
    l "W-w-wait... you're not joking right? I mean LOOK at her."
    show blara worry at left
    show blara worry at center
    with move
    nar "Lara cups Saki's ample chest with her hands."
    hide blara worry
    show blara shout at center 
    show bghosty smile at right
    with dissolve
    l_shout "LOOK AT THESE."
    hide blara shout
    show blara worry at center
    show bghosty smile at right
    with dissolve
    l "Y-you really find ME more attractive?"
    nar "Lara's eyes show true confusion... but also fear? Who hurt this girl?"
    pov "I mean..."
    
    menu:
        "Y-you really find ME more attractive?"

        "It's not just that, there's more to liking someone than just sex appeal.":
            hide bghosty smile
            show bghosty dis at right
            with dissolve
            pov "It's not just that, there's more to liking someone than just sex appeal."
            l "W-well yeah but Saki is so-"
            $ lara_love = lara_love + 1
            $ ghosty_love = ghosty_love - 1
            jump bbbl2

        "I'm not lying I really do find you more attractive.": 
            pov "I'm not lying I really do find you more attractive."
            hide bghosty smile
            show bghosty tease at right
            with dissolve
            g "Ignore her, she just wanted an excuse to grab my chest. Hers is just as big."
            hide blara worry
            show blara pout at center
            with dissolve
            l "N-no I wasn't I-"
            $ lara_love = lara_love + 1
            jump bbbl2
label bbbl2:
    nar "It seems Saki's offer of showing herself off finally caught up to Lara."
    hide bghosty dis
    hide bghosty tease
    show bghosty smile at right
    hide blara pout
    hide blara worry
    show blara yell at center
    with dissolve
    l "S-show them my curves a-are you crazy??? We just met?"
    hide bghosty smile
    show bghosty judge at right
    with dissolve
    gf "Oh? Well BBB policy deems that any customer who gets singled out by a stage performer is entitled to a private show."
    hide blara yell
    show blara shout at center
    with dissolve
    l "Y-You made that up right now!"
    hide bghosty judge
    show bghosty fsmile at right
    with dissolve
    gf "Huh? Red, I would NEVER do something like that... but you know."
    hide blara shout
    show blara worry at center
    hide bghosty fsmile
    show bghosty tease at right
    with dissolve
    gf "If you don't want to do it, I could. I'm sure I could give our new 'friend' a night to remember~."
    hide bghosty tease
    show bghosty smile at right
    hide blara worry
    show blara worry at center
    with dissolve
    l "N-no I'll do it!... I-if t-they want that of course..."
    pov "I-"
    hide bghosty tease
    show bghosty judge at right
    with dissolve
    gf "Lara. They're practically as red as your hair. They obivously want you. Come on girl I know you're not this oblivious."
    hide bghosty judge
    show bghosty at right
    with dissolve
    nar "I hadn't even noticed how red I was until Saki mentioned it. I feel like my heart is about to beat right out of my chest."
    nar "A PRIVATE SHOW? What does that even mean? Didn't sakura say Lara hadn't done any private shows? Does that mean..."
    nar "No. Brain calm down. This is literally her job."
    pov "I-I mean. If you want to I'd love t-"
    hide bghosty 
    show bghosty smile at right
    with dissolve
    gf "Great to hear! You two horny dogs go have fun in one of the private rooms, try not to break anything~!"
    hide blara worry
    show blara pout at center
    hide bghosty smile
    show bghosty fsmile at right
    with dissolve
    gf "Or each other~."
    show blara pout at left with move
    nar "Saki nearly shoves Lara off the stage after handing her a key that she had kept between the cleavage of her bunny suit. Saki seemed like she was far too prepared for this."
    hide blara pout
    show blara yell at left
    with dissolve
    l "W-wait but my shif-"
    hide bghosty fsmile
    show bghosty dis at right
    with dissolve
    gf "Lara. You and I both know Fanta would be lubing you up herself if she knew you were finally taking interest in someone. Go! I'll finish our shift alone."
    hide bghosty dis
    show bghosty wink at right
    with dissolve
    gf "But I expect to hear about EVERYTHING that happened. Got it?"
    hide blara yell
    show blara worry at left
    with dissolve
    l "I..."
#r all text before this point has been given a second read through as of 11/17/2025
    hide bghosty wink
    show bghosty judge at right
    with dissolve
    gf "No ifs, ands, or buts, not even your massive one. You cover for me whenever I'm in the mood for a snack, now it's my turn. Go! Have fun!"
    hide blara worry
    show blara pout at left
    hide bghosty judge
    show bghosty at right
    with dissolve
    l "My Butt is NOT massive."
    hide bghosty
    show bghosty tease at right
    with dissolve
    gf "So now you're lying to yourself and me? Go enjoy your time off before I call Fanta."
    hide blara pout
    show blara shout at left
    hide bghosty tease
    show bghosty smile at right
    with dissolve
    l_shout "UGHGHH. Fine."
    hide blara shout
    show blara pout at left
    with dissolve
#r how to hide characters and how to move character to center!!!
    hide bghosty smile with moveoutright
    show blara pout at center
    with move
    scene bbb stairs with dissolve
    nar "Without further warning Lara grabs my hand and begins leading me to a door with a sign reading 'Staff Only' "
    scene bbb stairs2 with dissolve
    nar "As she unlocks the door to the private room upstairs I can hear her breath becoming more heavy. Maybe I missread the conversation and Saki really was getting under her skin?"
#r LC1
    menu:
        "Should I say something?"

        "Hey, are you okay?":
            $ lara_love = lara_love + 1
            pov "Hey, are you okay?"
            l "Huh?"
            l_whisper "Oh, Oh gosh I'm sorry. I'm just a little nervous is all... I really do uhm."
            l "Nevermind, yes I'm okay."
            nar "That's a relief, I smile as we walk up the stairs. With how fast everything is going I can fully understand being nervous."
            jump bbbl3

        "Say nothing.": 
            nar "It's probably best I dont say anything..."
            nar "Her grip slowly on my hand tightens as she leads up the stairs, only releasing once the door to the private room has been opened."
            jump bbbl3
label bbbl3:
    scene bbb privateroom with dissolve
    show blara with dissolve
    l "Well uhh... Welcome to the Bunny-Queen suite! Where I uhm, am gonna make all your fantasies come true."
    nar "Lara's words come out with the fakest confidence I have ever heard. This is obviously a script shes studied in her head a million times."
    nar "Maybe Sakura really was telling the truth when she said Lara has never done this before."
    nar "If the main floor just 'impressed' me with how classy it was, the 'private room' has nearly given me a stroke. The room has a bed, a couch, a minifridge, a tv, tables and chairs, even a full bathroom and shower. It's like a mini apartment."
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
        "I would love for you to be my first private show I'm just a little nervous is all..."

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
    nar "Before I can even think about reacting to what's happening Lara has crawled fully onto the bed."
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
    l "Y'know... I've been practicing for a new stage routine recently, Fanta's idea."
    l "Maybe I could show you it~."
    nar "Her confidence is building with each bounce of her hips, my eye's are locked to her motions as her words slowly connect in my mind, I can hear my own heartbeat in my ears. This ass might be the death of me."
    l "But first I'll need you to help me take off this unifo-"
    ph "'Buh duh duh ding'"
    scene bbb privateroom with dissolve
    hide l cg 1
    hide l cg 1 2
    hide l cg 1 3
    show blara yell with dissolve
    nar "Lara's eyes widen as she flips back to a seated position scrambling to pull her phone out of her uniform's top."
    nar "I would comment on how hypocritical it is that she keeps something in there, If I wasn't so brain melted from everything I had just experienced."
    hide blara yell
    show blara think
    with dissolve
    l "I s-sorry just uhm give me a minute I just uhm."
    hide blara think
    show blara worry
    with dissolve
    l "I just need to check this notification real quick It's uhm really important then I'll mute my phone, Promise."
    nar "as I watch her fidget with her phone it finally clicks in my brain what app that notification came from."
    pov "Wait, Was that a Quest Treasures Online notification? Oh! Is the new expansion coming out?"
    show laraphone1 with dissolve
    l "Huh, wait.... you play?"
    pov "Yeah, I have for years now. Not the biggest fan of QTO: New Beginings but I'm always excited to see new content for the main game!"
    show laraphone3 with dissolve
    l_whisper "Holy shit."
    nar "Wait. Was this a joke? I guess it would be kind of weird to stop everything just to check a notification for a game."
    nar "I was totally into it to, She probably thinks I'm a weirdo being so excited about a gam-"
    show laraphone2 with dissolve
    l "I never thought I would meet someone who like QTO like me! What class do you play? What do you play on?"
    nar "...Oh my God she's perfect."
    pov "I have a character for each class, and I usually play on my DV3"
    l "oooo a console player!~ I respect it. The game was built for controller so it makes since, I usually play on my desktop so I can record footage if I want to."
    nar "as my mind is slowly clearing from its fog and im realizing the situation i'm in, I'm not sure how we got here."
    nar "We went from a private show to talking about games but I can't complain, She looks so happy to be talking about this."
    pov "We should play together some time! What do you record for?"
    l "Oh uhm... totally! But I uh, usually just record for myself nothing big. What other kinds of games do you play?"
    #r game question! hint to secret ending.

    menu:
        "So what kinds of games do you play?"

        "Mostly just other MMO's and RPG's.":
            $ lara_love = lara_love + 3
            pov "Mostly just other MMO's and RPG's."
            pov "I play other kinds of games but story based games have always been a favorite."
            #Phantasy is spelt that way on purpose
            l "I respect that! I've played a ton of different rpgs over the years. From Lizard warrior to Last Dream. I love getting lost in a phantasy world and getting to escape reality for a while."
            l "I enjoy MMO's too, its nice getting to see comunities form around them even if they can be a little expensive sometimes."
            l "Looking at you Last Dream 14."
            l "Thankfully that's not an issue for me anymore, Fanta offered to start paying for all my subscriptions once I started working here."
            pov "Really? That's a... different employee benefit."
            l "I know! isn't it awesome?"
            jump bbbl6

        "I like casual things like life sims.": 
            $ lara_love = lara_love + 2
            pov "I guess it might sound basic but I mostly like casual things like life sims."
            l "Hey! that's not basic. Everyone has their own likes and dislikes."
            l "I love playing a nice relaxing game from time to time. you can't be collecting 4 crystals or avenging your dead brother by taking down a corrupt government in every game..."
            show laraphone3 with dissolve
            l "Well I guess you could but it would get boring."
            show laraphone2 with dissolve
            l "It's nice to get to just enjoy your time with a game and not feel like you have to do something in particular."
            l "besides everyone has their 1 month DIGBUILD phase from time to time."
            jump bbbl6       

        "I like competitive things like Shooters and fighting games.": 
            $ lara_love = lara_love + 1
            pov "I like competitive things like Shooters and fighting games."
            l "Oooo A competitive type. How good are you?"
            pov "I like to think I'm pretty good. I wouldn't say like, top tier but pretty good."
            l "And modest too? How sweet. I mostly play older Shooters when I'm in the competitive mood."
            l "Ring 2 and the original Ring are both super fun. When it comes to fighters I love the 'wanted' series. I love me a ninja girl."
            jump bbbl6     
label bbbl6:
    nar "Listening to her ramble on and on about games... It's kinda cute? I wonder how often she gets to do this kind of thing."
    pov "What kinds of games do you like?"
    show laraphone3 with dissolve
    l "Me? I like a little of everything to be honest..."
    l "Recently I've mostly been playing retro games. I picked up this cool Dating sim for the original DV1"
    pov "I didn't know they made dating sims for consoles back then?"
    l "Same! but its been super fun! I've seen people online complain it takes a long time to load your save file but I don't understand that."
    l "You're only loading once per play session anyway right? I guess some people like to go back to make sure they always pick the right option but that always felt..."
    l "weird to me? If you're playing a game where the challenge comes from making decisions why load when you make the wrong ones. isn't that kind of cheating? And what about the poor girls."
    l "They'll never know you're only saying what they want to hear... Maybe I'm just too emotional"
    pov "No I get it. why play the game If you're not going to 'PLAY' the game."
    l "Yeah! exactly that!"
    show laraphone2 with dissolve
    l "I hope you're not just saying that because you think it's what I want to hear~!"
    pov "I could never!"
    scene black with dissolve
    nar "We both laugh as we continue our conversation. With how it started the is far from how I expected the night to go, and even further from how I expected Lara to be."
    nar "She seems like such a fun person, I wish I had the time to get to know her better but all good things must come to an end."
    scene bbb privateroom with dissolve
    show blara worry with dissolve
    l "I uhm... Just wanted to say sorry for like, kind of half lying to you earlier when I got the QTO notification."
    hide blara worry
    show blara blush smile
    with dissolve
    l "I just didn't want you to think I was weird for being so excited about a game. I have a hard time believing people will accept certain parts of me... I should have known you would understand."
    nar "I can't help but smile at her words. Tonight was... an experience to say the least. It was far from what I expected but I enjoyed it."
    pov "I'm happy you decided to tell me. I would have never learned so much about you if you didn't."
    hide blara blush smile
    show blara worryb
    with dissolve
    l "I-I'm happy you enjoyed learning so much about me but... I'm sure this isn't what you expected from a private 'show'."
    l_whisper "More like a private yap sesh."
    hide blara worryb
    show blara blush smile
    with dissolve
    pov "You're fine! T-trust me even if it got cut short by our talk I saw MORE than enough to be satisfied."
    l "More than enough?..."
    hide blara blush smile
    show blara shout
    with dissolve
    l_shout "MY ASS IS N-"
    hide blara shout
    show blara pout
    with dissolve
    l "{i} Ahh never mind. {/i}"
    nar "That wasn't even what I meant, but it seems the truth always comes to the light."
    hide blara pout
    show blara worry
    with dissolve
    l "I uhm- I had a lot of fun tonight...Like uhm a LOT of fun."
    l "But uhm, I understand if you wanted something more... physical."
    nar "As Lara spoke she pulled a pair of cards out from the clevage of her uniform handing them to me with a smile."
    hide blara worry
    show blara
    with dissolve
    l "Here, these are Saki and my personal numbers. Sakura may not look like it but she's hard core. you're not going to be able to just call the front desk and ask for one of us."
    nar "Lara's words both stun me into near silence and fill my head with a million questions."
    pov "W-wait your personal phone numbers? Both of yours?"
    l "Yeah? Are you really that shocked? After everything tonight I would even give you my personal Xwit-r @"
    hide blara
    show blara smug
    with dissolve
    l "It's @LaraChiba by the way~!"
    hide blara smug
    show blara
    with dissolve
    pov "I-I guess that makes since but... Why would I call you?"
    l "I-I mean... I thought maybe you might want to try this whole Private show thing again some time, That's why I gave you Saki's number too."
    hide blara
    show blara worryb
    with dissolve
    l "She uhm... Is better at this than me. I feel we owe you a 'Real' private show after this..."
    hide blara worryb
    show blara blush smile
    with dissolve
    l "Though uhm if you ever want to just text and chat about games you could always use my number for that too."
    pov "I-I..."
    nar "I'm not sure even now how I got to this point But I've learned to not question good things tonight."
    pov "Thank you, I appreciate it."
    l "You're welcome. I- We look forward to hearing from you."
    l "It's uhm, almost closing time so I need to get downstairs to help Saki and the girls clean. I'll walk you out [povname]-"
    l_whisper "I-If that's okay with you?"
    pov "I'd love that"
    nar "Lara smiles as she takes my hand leading me back out the doors of the private room"
    scene black with fade    
    jump bbb_el
#p
#p
#p
#p
#p
#p------------------------------------------------------------------------------------------------------------------------------------------------
#p Ghosty BBB Date 1 
#p------------------------------------------------------------------------------------------------------------------------------------------------
#p
#p
#p
#p
#p
label bbbs:
    hide bghosty 
    show bghosty smile at right
    with dissolve
    pov "I can't deny the alure of a Demon girl, Saki is more my type"
    hide blara worryb
    show blara at left
    with dissolve
    l_whisper "Agreed, Saki is pretty aluring.~"
    nar "Lara smiles, she's obviously being honest but suprisingly she seems a little dissapointed in my answer. It's obvious she doesn't take disapointment well."
    hide bghosty smile
    show bghosty wink at right
    with dissolve
    gf "I'm no regular demon, I'm a Succubus love."
    pov "Succubus?"
    hide bghosty wink
    show bghosty tease at right
    hide blara 
    show blara blush at left
    with dissolve
    gf "Semen demon. Soul-sucker. Vampire for cum. Whatever helps you imagine it."
    hide bghosty tease
    show bghosty fsmile at right
    hide blara blush
    show blara blush smile at left
    with dissolve
    gf "All that matters is that I'll give you the best night of your life."
    hide bghosty fsmile
    show bghosty at right
    with dissolve
    gf_whisper "or last..."
    pov "Should I be worried?"
    hide blara blush smile
    show blara think at left
    with dissolve
    l_whisper "Only if you're scared of losing your soul."
    hide blara think
    show blara at left
    with dissolve
    nar "Lara seems to have recovered well, she's back to smiling but her words have done anything but calm me, but before I can think too much Ghosty's voice brings me back to reality."
    hide bghosty 
    show bghosty wink at right
    with dissolve
    gf "Don't be scared, love. I will take very good care of you."
    nar "The flame eyed performer licks her teeth as she smiles, I can't help but feel like she's... Hungry."
    pov "Sorry, I'm just having a hard time mentally comprehending the situation i'm in. Everything is moving so fast."
    hide bghosty wink
    show bghosty at right
    with dissolve
    gf "You wouldn't be here if you weren't already looking for a little fun. "
    hide bghosty 
    show bghosty judge at right
    with dissolve
    gf "I'm just adding a touch of something... more exciting. Don't you want to let your imagination become reality?"
    hide bghosty judge
    show bghosty smile at right
    with dissolve
    nar "Saki's eyes glisten as she stares at me, it's almost like shes scanning my every desire. She's obviously far more experienced with this kind of thing than I could ever be."
    nar "this character she's playing feels so real. It's hard to believe she really isn't some kind of sex demoness."

    menu:
        "Don't you want to let your imagination become reality?"

        "What an amazing night to feel cursed.":
            pov  "What an amazing night to feel cursed."
            nar "The sentence slips out of my mouth without much thought especially not to how random it seems out of context. If this kind of 'Demon' is interested in me, Maybe curses aren't that bad."
            hide blara 
            show blara wink at left
            with dissolve
            l "Oooo, gaming references while talking to a hot girl? I like you."
            nar "Saki blankly stares as me and Lara go back and forth for a second about gaming."
            hide blara think
            show blara pout at left
            hide bghosty smile
            show bghosty judge at right
            with dissolve
            gf "You're both so... odd..."
            nar "Hmm, Guess gaming isn't Saki's thing."
            $ lara_love = lara_love + 1
            jump bbbs2

        "How much of my imagination, exactly?":
            $ ghosty_love = ghosty_love + 2
            pov "How much of my imagination, exactly?"
            nar "Part of me was afraid to find out the answer..."
            hide bghosty smile
            show bghosty wink at right
            with dissolve
            gf "Well, that's honestly up to you, love~"
            hide bghosty wink
            show bghosty tease at right
            with dissolve
            gf "You could let your mind run wild for all I care. I'm truly up for anything that dirty little brain can think of."
            hide blara pout
            show blara at left
            with dissolve
            l "Saki is very good at making dreams come true."
            hide blara smile
            show blara think at left
            with dissolve
            l_whisper "I wish she would do the same for me..."
            hide blara think
            show blara at left
            with dissolve
            gf "So tell me.. what is your wildest fantasy?"
            $ fantasy = renpy.input("So tell me.. what is your wildest fantasy?", length=45)
    $ fantasy = fantasy.strip()

    if not fantasy:
        $ fantasy = "Getting the soul sucked out of my body"

    jump bbbs2a
label bbbs2a:
    hide blara smile
    show blara blush smile at left
    hide bghosty tease
    show bghosty fsmile at right
    with dissolve
    pov "[fantasy]"

    gf "Hot."
    jump bbbs2  
label bbbs2:
    hide blara pout
    hide blara blush smile
    show blara  at left
    hide bghosty fsmile
    hide bghosty judge
    show bghosty wink at right
    with dissolve
    gf "Anyways, if you're interested, I can treat you to a little private show~"
    nar "Sakura said Saki was the owners daughter right? I'm not sure my heart could handle something like that but..."
    nar "I would be CRAZY to refuse her offer, I doubt many people get a chance like this."
    hide bghosty wink
    show bghosty smile at right
    with dissolve
    pov "Well... if you're offering-"
    hide bghosty smile
    show bghosty fsmile at right
    with dissolve
    gf "Great!"
    nar "Before I could even finish she was already pulling a key out from between the cleavage of her bunny suit."
    l "You.. you just have that in there..?!"
    hide bghosty fsmile
    show bghosty smile at right
    with dissolve
    gf "Duh! A key to a room this special can not just be left out anywhere!~ Do you have the rest of the shift covered or should I call someone to come help?"
    hide blara
    show blara worry at left
    with dissolve
    l "Oh, Uhm no I'll be fine, Go have your fun!~"
    hide blara worry
    show blara at left
    hide bghosty smile
    show bghosty wink at right
    with dissolve
    gf "Thanks Red!~ I'll pay you back later, Promise!~"
    nar "The way the two are talking this seems to happen pretty often. Is ending your shift early really not that big of a deal for them
    ?"
    hide bghosty wink
    show bghosty at right
    hide blara 
    show blara worryb at left
    with dissolve
    l "It's okay Saki Just don't be too rough with them..."
    nar "Lara's words come out with an emotion I can't quite place, is she just sad I didn't pick her or... Actually worried?"
    hide blara worryb
    show blara pout at left
    hide bghosty
    show bghosty fsmile at right
    with dissolve
    gf "I can't make any promises~ Now, Follow me love.~"
    nar "Saki's words are followed with a wink, every little thing she does is just so... perfect. It almost feels like shes magic with how easily she's making my heart race."
    hide blara pout with moveoutleft
    show bghosty fsmile at center
    with move
    scene bbb stairs with dissolve
    nar "As my mind continues it's attempt to catch up with everything that's going on, Saki grabs my hand and begins leading me to a door with a sign reading 'Staff Only' "
    scene bbb stairs2 with dissolve
    nar "As I followed behind her, the costumes tail seeming to sway in slow motion as we climed the stairs to the second floor. I can hear my heart pounding in my chest louder with each step."
    nar "Before I know it Saki has opened the door to the room where all my anxiety will hopefully soon be replaced with pleasure."
    #p
    #p
    #p
    #p
    #p private show room with ghosty starts here
    #p
    #p
    #p
    scene bbb privateroom with dissolve
    show bghosty smile with dissolve
    gf "Make yourself comfortable, Hun."
    nar "If the main floor just 'impressed' me with how classy it was, the 'private room' has nearly given me a stroke. The room has a bed, a couch, a minifridge, a tv, tables and chairs, even a full bathroom and shower. It's like a mini apartment."
    pov "This is room is just for private shows? It's amazing."
    hide bghosty smile
    show bghosty judge
    with dissolve
    gf "Oh? I mean it's nothing special. You should see the rooms back at the mansion."
    nar "Saki was incredibly calm about this ordeal... Though I suppose this is fairly normal for her. If they spend this much on a private room, I can't even begin to imagine what her home looks like"
    hide bghosty judge
    show bghosty smile
    with dissolve
    gf "I can tell you're nervous. There's no need to be shy, love. I'm not going to hurt you..."
    hide bghosty smile
    show bghosty 
    with dissolve
    gf_whisper "Unless you want me to."
    nar "Every time she whispers I wonder if she knows I can still hear her.."
    pov "Sorry, I just don't know how to process this whole... situation. I'm still catching my breath."
    hide bghosty 
    show bghosty smile
    with dissolve
    gf "Whole situation? You scored a private show with one of the stage girls. I'm not sure what more you could hope for coming to a club like this."
    hide bghosty smile
    show bghosty tease
    with dissolve
    nar "theres no arguing against her words, There's no sense in being bashful now."
    gf "Did you expect a tea party instead? Ooo, or maybe you're sad you had to choose between us? So selfish~!"
    pov "W-what no you are this is far more than I expected already I-I guess I just didn't expect this much attention. Especially so quickly."
    hide bghosty smile
    show bghosty tease
    with dissolve
    gf "We here at the BBB pride ourselves at being full of surprises~! Besides, Red obviously saw something special in you and she has an AMAZING eye for this kind of thing."
    hide bghosty tease
    show bghosty smile
    with dissolve
    gf "Plus, I love making guests feel welcome~! And what better way can a woman of my tallents do that then getting 'personal'."
    nar "As she speaks Saki closes the space between us, placing her hands against chest causing a soft shiver to run through my body. I swear she's like a living aphrodisiac."
    hide bghosty smile
    show bghosty wink
    with dissolve
    gf "Now... How about we get comfortable?"
    nar "Saki pushes into me softly, as I step back I bump into a chair sat in the corner of the room"
    gf "Go ahead, take a seat.~"
    nar "I did as told and sat on the soft chair, my arms awkwardly falling to the sides."
    hide bghosty wink
    show bghosty
    with dissolve
    pov "The sign in the front said thought this place has a 'look but don't touch' policy?"
    gf "Mmm..."
    hide bghosty 
    show bghosty smile
    with dissolve
    nar "There was a mischevious glint in Saki's eyes as she let my question hang in the air for a moment."
    gf "That's for the stage shows love. We can't have all you naughty women and men interupting the routine."
    gf "But I want to give you a true taste of what the BBB can provide~! It's the least I could do as the owner's daughter. If you'll allow me of course."
    nar "I shake my head in a gentle nod as I stare into the flaming eyes of the woman before me."
    nar "Without further warning Saki moved into my lap, Her soft thighs wrapping around my waist "
    nar "The sudeen heat of her body against mine is nearly too much. The sensation making my mind blur for a moment before I came back to the reality of whats happening."

    show g cg 1 with fade:
        yalign 1.0
    nar "my breath hitches as I study Saki's form sitting atop me. It's more than enough to fully short circut my brain, I can't form a thought much less words."
    gf "ahem."
    gf "My eyes are up here love."
    show g cg 1 :
        subpixel True
        yalign 1.0
        linear 2.0 yalign 0.6
    gf "..."
    gf "A little higher babe."
    show g cg 1 :
        subpixel True
        yalign 0.6
        linear 2.0 yalign 0.1
    gf "..."
    gf "there you go!~"
    show g cg 1 2 with dissolve:
        yalign 0.1
    gf "That wasn't so hard now was it?"
    nar "Saki's smile quickly fades into a pout as my response time fails to meet her needs."
    show g cg 1 with dissolve:
        yalign 0.1
    gf "I hope I don't weight too much for you.."
    pov "No! Not at all!"
    show g cg 1 2 with dissolve:
        yalign 0.1
    nar "Saki giggled, It was obvious even in my dazed state 'playing with her food' is something she obviously enjoyed."
    gf "Well that's good to hear."
    nar "Her tone of her voice shifted to something much more... sultry."
    gf "I was joking earlier about having to look me in the eye love. I'm making a rare exception giving a new client a free private show so take full advantage of it, darling."

    menu:
        "Go ahead, Enjoy the view."

        "Continue to look her in the eyes":
            $ lara_love = lara_love + 2
            $ ghosty_love = ghosty_love + 2
            show g cg 1 with dissolve:
                yalign 0.1
            nar "despite her offer I can't seem to look away from her eyes. something about them is mesmerizing."
            gf "Aww still a little shy? Here let me help you with that."

        "Her chest calls to me.": 
            $ ghosty_love = ghosty_love + 2
            $ lara_love = lara_love + 2
            nar"well if she's offering..."
            show g cg 1 2 with move:
                yalign 0.6
            nar"As my head snaps to her chest Saki lets out a small laugh."
            gf "I love when they know what they want."
            gf "I should have guessed, I saw you staring at them from the stage..."
            gf "you know, you don't have to JUST stare."


        "I can't help but look at those killer thighs.":
            $ ghosty_love = ghosty_love + 2
            nar"well if she's offering..."
            show g cg 1 2 with move:
                yalign 1.0
            nar"As my head snaps to her thighs Saki lets out a small laugh."
            gf "I love it when they know what they want."
            gf "Although if you're a thigh person I'm truly shocked you picked me over Lara. It must have been for some other reason~!"
            gf "You got a kink for demon girls?"
            nar "I feel it's in my best interest to not answer that."
            gf "Let me show you what we do best~."
            



    nar "Saki guided my hands all across her body, my palms caressing each inch she lead me to touch."
    gf "You're so shaky~. It's kinda cute."
    pov "Can you blame me? I'm still having a hard time believing I'm not dreaming."
    gf "This? If that's how you feel I can give you so much more than you could ever dream of~."
    pov "More?"
    nar "A chill ran down my spine. I have no idea what she is capable of... but I feel so drawn to find out."
    gf "Well, if you think you're ready that is."
    pov "Please... I want more."
    gf "Aww~ I like the sound of desperation from you."
    nar "I'm not sure where my sudden boost of confidence is coming from but Saki was clearly getting more and more excited by the second. She bounced against my lap softly as she spoke."
    gf "Enough foreplay then, lets get to the good part~."
    scene bbb privateroom with dissolve
    show bghosty smile with dissolve
    nar "Without a moment's notice Saki lifted herself off my lap and pulled me to stand up."
    hide bghosty smile
    show bghosty fsmile 
    with dissolve
    gf "I did promise you a show, didn't I? You make yourself comfortable and allow me to fuel your deepest desires~!"
    nar "Saki moved to The center of the room, working the pole as she had in the show room earlier."
    nar "The show quickly became far more revealing, going from a basic dance routine to strip teasing."
    nar "My heart rate continued to climb as each piece of the uniform hit the floor, finally her nearly her entire body was bare to my eyes leaving only her wings, tail, and a pair of sheer thigh highs."
    scene g cg 2 with dissolve
    pov "Holy."
    pov "Shit."
    nar "Saki laughed at my incredibly flustered response. The uniform barely consealed her figure underneath but now, nothing was left to the imagination."
    gf "I'm going to assume you like what you see?"
    nar "As I took in every inch of her skin the answer to her question was about as easy to come to as she was."
    pov "Y-yes! Of course!"
    nar "She smiled, I'm sure she knew how amazing she looked but teasing me was obviously something she enjoyed at this point."
    gf "Good. So now... What was that thing you said earlier"
    pov "?"
    scene g cg 2 2 with dissolve
    gf "You know, your biggest fantasy. I mean I think we could start with something smaller, don't want to end our fun too quick."
    gf "But '[fantasy]'... I think I can find a way to satisfy that craving of yours in my own special way~."
    nar "The next few minutes are a blur, Saki may truly be the best there is at what she does."
    nar "Every movement she makes feels rehersed to a masterful level. It's like she was made for this."
    scene black with dissolve
    nar "Before the night is over, She kept her word."
    nar "she was far more than I could ever dream of."
    scene bbb privateroom with dissolve
    nar "Once we've finished, Saki went to the restroom to take a hot shower, I can hear the water pouring over her body as I lay in the bed, the events that just unfolding playing on loop in my head."
    nar "One thing is for sure. If Demon girls weren't a kink of mine before tonight they are now."
    show bghosty smile
    with dissolve
    nar "Soon Saki returns to the bed side, She's so full of energy even while I'm still trying to catch my breath. She's truly on a different level."
    gf "Sorry it took so long, Had to fix up my body makeup after the shower, it's supposed to be water proof but It still runs from time to time. gotta keep up the illusion four the audience you know?"
    pov "You...You're fine I'm just now catching my breath."
    hide bghosty smile
    show bghosty wink
    with dissolve
    gf "Aww, I'm sure you're fine. after all I took Red's advice and took it easy on you!~"
    nar "T-That was going easy on me? Any more and I may have actually died. These girls are serious."
    hide bghosty wink
    show bghosty 
    with dissolve
    gf "Speaking of Red. Lara has some actual interest in you, Which believe it or not is rare. She's not the kind to fall for someone so easily. You're a lucky person to have caught her eye."
    gf "I'm not going to tell you what you have to do but maybe think about giving her a call or something..."
    hide bghosty 
    show bghosty wink
    with dissolve
    gf "It may not be as physical as our time here tonight but I'm sure she would treat you to an amazing time. Plus have you seen her ass? I'm pretty sure it claps when she blinks."
    hide bghosty wink
    show bghosty judge
    with dissolve
    gf "don't tell her I said that. I'll never hear the end of it."
    hide bghosty judge
    show bghosty smile
    with dissolve
    gf "that being said I wouldn't be opposed to another Night of fun aswell. It's not often Someone stays awake once I'm finished with them!~"
    nar "That is 100 percent believable. I can feel my body begging for sleep as I listen to her speak."
    gf "Here. hand me your phone."
    nar "I do as I'm told, I'm not gonna argue with the woman that just showed me nirvana. Even so I'm curious what she could need it for."
    pov "What for?"
    hide bghosty smile
    show bghosty tease
    with dissolve
    gf "Sakura may not look it but she's hard core. you're not going to be able to just call the front desk and ask for one of us. I'm putting our personal numbers in here."
    nar "As she speaks she snaps a picture of herself, winking with her tongue out. filling out her contact information."
    pov "Your personal numbers? are you sure that's okay?"
    hide bghosty tease
    show bghosty judge
    with dissolve
    gf "I wouldn't do something I'm not sure I want to do."
    hide bghosty judge
    show bghosty smile
    with dissolve
    gf "Besides, I got to blow off some steam tonight. It's the least I could do to re-pay you~!"
    gf "The club will be closing soon So I probably need to help the girls clean up."
    gf " I'll walk you downstairs just remember to give what I said a thought hun."
    scene black with dissolve
    jump bbb_gl
    #p
    #p 2/12/2026 Ghosty date 1 first pass finished. somehow before Lara's??? I've betrayed my girl.
#w_________________________________________________________________
#w_________________________________________________________________
#w Endings for first dates.________________________________________
#w_________________________________________________________________
#w_________________________________________________________________
#r lara ending
label bbb_el:
    scene bbb entrance with dissolve
    nar "As we reach the entrance, Lara releases my hand and turns to face me"
    show blara blush smile with dissolve 
    l "W-well I guess It's time we say our goodbyes."
    
    if drink == 0:
        show sak pout at left
        show bghosty wink at right
        with dissolve 
        sa "Not so fast wine abandoner!"
        sa "I mean, who leaves a FREE drink at their table."
        show sak lewd at left
        with dissolve 
        sa "Anyways, you're not leaving here without giving us all the details!~"
        

    else:
        show sak smug at left
        show bghosty wink at right
        with dissolve 
        sa "Not so fast ladykiller!~"
        hide sak smug
        show sak lewd at left
        with dissolve 
        sa "you're not leaving here without giving us all the details!~"
        
        # sakura done
        # lara done 
        # ghosty done
    hide blara blush smile   
    show blara worryb
    with dissolve
    l "S-sakura! Y-you can wait till they've left to ask."
    hide sak lewd
    show sak pout at left
    with dissolve 
    sa "No way. I need every detail right now."
    hide sak pout
    show sak smug at left
    with dissolve 
    sa "Every. Detail."
    hide bghosty wink
    show bghosty fsmile at right
    with dissolve 
    gf "Sakura I want to know too but if we make Lara explain in front of [povname] I think she might melt into a puddle of embarasment."
    hide sak smug
    show sak pout at left
    hide bghosty fsmile 
    show bghosty smile at right
    with dissolve 
    sa "hmpf. fine."
    hide blara worryb 
    show blara blush smile
    hide bghosty smile 
    show bghosty at right
    with dissolve
    l "It wasn't anything crazy anyway..."
    hide sak pout
    show sak smug at left
    hide bghosty
    show bghosty judge at right
    with dissolve
    gf "I never said it was, But I have GOT to know every little thing."
    hide bghosty judge
    show bghosty fsmile at right
    with dissolve
    gf "But I also love to hear about every big thing."
    nar "Ghosty's wink sends a chill down my spine. I feel if I had chosen to have my private show with her it wouldn't have ended with a talk about video games..."
    hide blara blush smile   
    show blara 
    with dissolve
    l "I promise I'll tell you everything once we have the club closed for the night."
    hide sak smug
    show sak happy at left
    hide bghosty fsmile
    show bghosty at right
    with dissolve 
    sa "Oh my god I can't wait. Did you use any toy-"
    hide blara   
    show blara pout
    with dissolve
    l "Sakura. Once. They. Are. Gone."
    hide sak happy
    show sak lewd at left
    hide blara pout 
    show blara think
    with dissolve 
    sa "Yes mommy."
    hide sak lewd
    show sak smug at left
    hide blara think 
    show blara blush smile
    hide bghosty
    show bghosty smile at right
    with dissolve 
    gf "Sakura's just excited about the idea of little miss red finally showing interest in someone."
    hide blara blush smile
    show blara blush
    with dissolve 
    l "Alright, t-thats enough talking for now. we gotta get things cleaned up for the night."
    hide blara blush
    show blara blush smile
    with dissolve 
    l "[povname], Thank you for visiting the BBB, I really hope you enjoyed everything..."
    pov "I did, Thank you"
    if drink == 0:
        hide sak smug
        show sak pout at left
        with dissolve 
        sa "You sure didn't enjoy the FREE drink..."
        hide sak pout
        show sak smug at left
        with dissolve 
    #o could be an issue. unsure atm 2/13/2026
    l "And uh, Remember to think about those numbers I gave you... both of them. please?"
    pov "I will, thank you again. I had a lot of fun tonight"
    scene black with dissolve
    nar "As the conversation died out I left the doors of the building I had been so scared to enter just hours before now a little sad to be leaving."
    nar "..."

    jump end

#w_________________________________________________________________
#w_________________________________________________________________
#w_________________________________________________________________
#w_________________________________________________________________
#w_________________________________________________________________
#w_________________________________________________________________
#w_________________________________________________________________
#w_________________________________________________________________

#p ghosty ending
label bbb_gl:
    scene bbb entrance with dissolve
    nar "As we reach the entrance the fog in my mind finally begins to clear."
    show bghosty wink with dissolve
    gf "Okay love, I had a lot of fun tonight but It's time you head home.~"
    
    
    if drink == 0:
        show sak pout at right
        with dissolve 
        sa "Not so fast wine abandoner!"
        show sak lewd at right
        with dissolve 
        sa "I mean, who leaves a FREE drink at their table."
        sa "Anyways, you're not leaving here without giving me ALL the details!~"
        
    
        

    else:
        show sak smug at right
        with dissolve 
        sa "Not so fast ladykiller!~"
        show sak lewd at right
        with dissolve 
        sa "you're not leaving here without giving me ALL the details!~"
        
        # sakura done
        # lara
        # ghosty
    hide bghosty wink
    show bghosty smile
    show blara worryb at left
    with dissolve
    l "S-sakura! C-can't you wait till they've left to ask Saki?"
    hide sak lewd
    show sak pout at right
    show blara blush smile
    with dissolve 
    sa "No way. I need every detail right now."
    hide sak pout
    show sak lewd at right
    with dissolve 
    sa "Every. Detail."
    hide bghosty smile
    show bghosty fsmile
    with dissolve
    gf "Mmmm, Sorry Sakura I think you'll need to wait. If you want every detail we're gonna be here all night!~"
    hide sak lewd
    show sak smug at right
    with dissolve 
    sa "Ooooo I'm excited!!"
    hide blara blush smile
    show blara worryb at left
    with dissolve
    l "I just hope you weren't too rough..."
    hide bghosty fsmile
    show bghosty tease
    with dissolve
    gf "Don't worry Red I was gentle!~ Right [povname]?"
    nar "I'm not sure If I would consider what we did gentle, but I'm not about to argue."
    pov "yeah-"
    hide bghosty tease
    show bghosty smile
    with dissolve
    gf "See!~"
    hide blara worryb
    show blara blush smile at left
    with dissolve
    l "As long as [povname] enjoyed themselves..."
    sa "Oh I'm sure they did. I could hear them down here over the speakers"
    hide blara blush smile
    show blara shoutb at left
    with dissolve
    l "S-Sakura."
    sa "Don't pretend like you couldn't."
    hide blara shoutb
    show blara poutb at left
    hide bghosty smile
    show bghosty 
    with dissolve
    gf "Alright, that's enough chatting babes,we need to get things cleaned up for the night."
    hide bghosty 
    show bghosty wink
    with dissolve
    gf "[povname], Thank you for visiting the BBB, we hope you enjoyed your time here."
    pov "Thank you, I uhm... appreciated the service?"
    hide sak smug
    show sak lewd at right
    with dissolve 
    sas "I'm sure you did."
    hide bghosty wink
    show bghosty smile
    with dissolve
    gf "Visit again any time hun, And give what I said a thought."
    pov "I will, thank you again."
    scene black with dissolve
    nar "As the conversation died out I left the doors of the building I had been so scared to enter just hours before now a little sad to be leaving."
    nar "..."
    jump end





#nar "The programmer has a nap. Hold out! Programmer!"

#w Ending of the game, put credits here in the future!
    label end:
    #y__________________________Text For Valentines Demo_______________________________________
    scene message with dissolve
    l "This concludes the Valentines test demo."
    l "We here at HHS hope you enjoyed what's been presented. It's not much but this was a few months of learning and work"
    g "I'm sure they enjoyed what you 'Presented' to them on the bed."
    l "..."
    l_whisper"... I'm going to ignore that."
    l "Hopefully from this point on development time will be far faster as SM understands MOSTLY how the engine works."
    l "Anyways. Keep in mind nothing was final and it all still needs polish, but please report any major issues, thoughts, or suggestions to SM_pai as well as if you would like to be sent future demos."
    #y -----------------------------------------------------------------------------------------
    nar "Please send a screen shot of this text box to @SM_pai. Lara love is [lara_love]. Ghosty love is [ghosty_love]. Lara date count is [lara_date_count]. Ghosty date count is [ghosty_date_count]. "
    nar "Thank you for playing<3! Tester can now has a nap. Rest Well! Tester!"
    nar "..."
    if lara_date_count >= ghosty_date_count:
        l "Psst... Hey you still there [povname] ?"
        l "There's a lot of name easter eggs to find!"
        l "Here are 2 of the most interesting ones. Sm told me to tell you about them."
        l "Try naming yourself 'Mlzrt' or 'Daddy'"
        l "Okay. thank you for playing my route! Love you~! B-bye!"
    scene black with dissolve
    #r this ends the game do not add anything after this point.
    return
#y ------------------------------------------------------------------------------------------------------------------------------------------------
#r End of game above, next is sub systems used for special events
#y ------------------------------------------------------------------------------------------------------------------------------------------------




#w name checker output for Final
    label friendlyname:
        l "Oh! You have the same name as one of my friends"
        l "What a coincidence."
        l "..."
        l ";)"
        jump sohedoeshaveaname

    label daddyname:
        $ renpy.movie_cutscene("images/no.webm")
        $ renpy.quit()

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
        $ povname = "Mari"
        l "Huh..."
        l "You don't really look like a fox girl to me..."
        g "why would you say something so strange to someone we just met?"
        l "It's basic procedure."
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
        l "Nice of you to visit ME at work for a change!~"
        jump sohedoeshaveaname

    label mazname:
        l "Maz! It's been a while!"
        l "How are Willow and Morgan? Still hot?"
        jump sohedoeshaveaname
    #Name Ch
















#wBETA CODE LEFT IN WITH mlzrt EASTER EGG DO NOT TOUCH OR ADD CODE.
#b Original test code, might leave this in as an easter egg? maybe have pn "test" send you here?
    label beta:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bbb bar test
 

    # These display lines of dialogue.
#b name select, makes MC annon if no name is chosen
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
#b question choice path
    menu:
        "?"

        "huh, that was pretty easy to get to work!":
            jump yes1

        "why are you a sketch?": 
            jump no1
#b Huh, That was pretty easy to get to work!

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
#b Why Are You A Sketch?
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
#b beta name check
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