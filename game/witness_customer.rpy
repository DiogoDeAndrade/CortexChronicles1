label witness_customer:

    $ witness_customer = True

    scene bg court
    with None

    show prosecutor at right
    with dissolve

    prosecutor "The prosecution calls to the stand Mr. Eamon Baird..."

    hide prosecutor
    with dissolve
    show customer at left
    with dissolve
    show bailiff at right
    with dissolve

    bailiff "You swear by Cortex and the Prime Nexus to tell the truth, the whole truth, and nothing but the truth?"

    customer "I do!"

    hide bailiff
    with dissolve
    show prosecutor at right
    with dissolve

    prosecutor "Mr. Baird, you came forward when you saw the news of Mr. Reed's arrest, correct?"

    customer "That's correct, sir."

    prosecutor "Mr. Baird, can you recount your interaction with Mr. Reed at the library?"

    customer "Yes. I went to the library seeking some history books. Mr. Reed not only provided them but also insisted I read his manifesto against Cortex. He was very persistent about it."

    jump customer_decision1

label customer_decision1:

menu:
    "Object: What manifesto?" if knows_about_manifesto == False:
        jump what_manifesto

    "Object: Dont' remember the man" if not knows_about_library_data:
        jump customer_dont_remember

    "Stay silent":
        jump customer_stay_silent

label what_manifesto:
    
    player "Objection! What manifesto?! We haven't discussed any manifesto before!"

    prosecutor "Don't play coy, Mr. Reed. Your manifesto, the one you wrote!"

    $ knows_about_manifesto = True

    player "I didn't write any manifesto!"

    prosecutor "Oh yes you did, Mr. Reed... Not only did you write it, you pushed it's filth on innocent people in the library!"

    prosecutor "We found it in your home!"

    prosecutor "Mr. Baird, do you mind describing it?"

    customer "Certainly! It was a paper, about 20 pages long, with criticisms against Cortex and arguments for human governance. Quite radical, if you ask me."

    prosecutor "As you can see, your Honor, it's quite clear we will have to add authorship of seditious material to the accusations!"

    show judge at center
    with dissolve

    judge "Yes, it sure appears that way, Mr. Holt!"

    jump after_manifesto

label after_manifesto:

menu:
    "Protest" if dont_remember == False and not knows_about_baird_books:
        player "But... but... I don't recall!"

        $ dont_remember = True

        prosecutor "Your Honor, we will address the issue of Mr. Reed's memory later!"
        
        jump after_manifesto
        
    "Request library data" if knows_about_library_data and not knows_about_baird_books:
        jump request_library_data

    "Request cross examination":
        jump customer_cross_examine

    "Stay silent":
        player "..."        
        jump customer_no_more_questions

label customer_dont_remember:

    player "Objection! I've never met this man before in my life!"

    prosecutor "But he knows you, Mr. Reed! The library data attached to the process shows clearly that you provided Mr. Baird some books last week!"

    if dont_remember == False:

        player "But how can't I remember?! How?!"

        $ dont_remember = True

        prosecutor "We'll address that in a bit, Mr. Reed, please be patient..."

    $ knows_about_library_data = True

    jump customer_decision1

label customer_stay_silent:

    narrator "Rowan didn't recall any manifesto, but he decided against mentioning it...\nMaybe he had written a manifesto, or it's part of this elaborate play, but better not add more charges..."

    prosecutor "Mr. Baird, do you mind describing that manifesto?"

    customer "Certainly! It was a paper, about 20 pages long, with criticisms against Cortex and arguments for human governance. Quite radical, if you ask me."

    jump after_manifesto

label customer_cross_examine:

    player "May I question the witness, your Honor?"

    show judge at center
    with dissolve

    judge "Certainly, Mr. Reed, but be brief..."

    hide judge
    with dissolve
    hide prosecutor
    with dissolve

    player "Did you read this manifesto in its entirety, Mr. Baird?"

    customer "Not entirely. I skimmed through it but got the gist."

    player "Interesting. Now, can you recall any specific book titles or authors of the history books you borrowed that day?"

    customer "I... don't recall the exact titles. I just wanted something on the last century's events."

    if knows_about_baird_books:
        player "Mr. Baird, the library has a digital catalog and borrowing system. We retrieved records of your transactions that day. You borrowed two novels - none of which were history books. How do you explain this discrepancy?"

        customer "I... maybe I was mistaken about the genre..."

        player "Mistaken about borrowing history books when you actually borrowed novels? And yet, you claim to remember intricate details of a manifesto you just 'skimmed through'? Mr. Baird, it seems your memory is selective. Isn't it possible that your entire testimony about me pushing my alleged manifesto on you is just another one of these 'mistakes'?"

        customer "I... I just told you what I remembered."

        player "Or what you were told to remember..."

        player "No more questions, your Honor..."

        show judge at center
        with dissolve

        judge "You are excused, Mr. Baird, thank you..."

        $ score = score + 2

        hide customer
        with None
        hide judge
        with None
        hide prosecutor
        with None

        jump witness_loop    
    else:
        player "Do you have any idea on why I'd allegedly decided to press my alleged manifesto onto you? It seems curious, since I don't know who you are!"

        customer "Eh... Maybe I have one of those faces, and since I was interested in history books you thought I might have rebel thoughts like yours!"

        jump customer_cross_examine2

label customer_cross_examine2:
    
menu:
    "Press on friendly face":
        player "So I risked my life showing forbidden literature because you have a friendly face?"
        player "It seems unlikely!"

        customer "Well, who knows what makes rebels tick!"

        player "..."

        jump customer_no_more_questions

    "Press on history books":
        jump customer_history

    "Say nothing":
        player "So, no more question, Mr. Baird. Thank you."

        jump customer_no_more_questions

label customer_history:
    player "What kind of history are you interested in, Mr. Baird?"

    customer "Oh, you know... anything, really!"

    player "That seems really vague, I think... Last centuries? The wars? Social political? Art?"

    customer "Oh, a bit of everything..."

    player "So, as a history generalist, you have some ideas on the reasons for the War of Knives 50 years ago, right?"

    customer "Oh... Well, there's so many reasons..."

    show prosecutor at right
    with dissolve

    prosecutor "Objection, your Honor! What's the relevance of this?!"

menu:
    "Credibility":
        player "It speaks to his credibility as a witness, your Honor!"

        show judge at center
        with dissolve

        judge "I will allow it... Please answer the question, Mr. Baird..."

        customer "So, as I was saying, there's so many reasons..."

        player "EXCEPT! There was no such thing as a War of Knives!"

        player "Someone who studies history would never think there was one!"

        customer "Er... But... What..."

        $ score = score + 1

        player "You are lying, Mr. Baird... I don't know why, but you are lying!"

        judge "That's enough, Mr. Reed..."

        $ noise = noise + 1

        if noise == 2:
            judge "One more outburst like this and you'll forfeit your opportunity to defend yourself, Mr. Reed!"

        if noise == 3:
            jump gameover_outburst

        player "Sorry, your Honor... No more questions"

        judge "You are excused, Mr. Baird, thank you..."

        jump witness_loop

    "Accuse Baird of being the author of the manifesto":
        player "The fact you're hesitating so much shows a guilty conscience, Mr. Baird."

        player "Maybe it wasn't me that pushed my manifesto onto you... Maybe it was you that pushed it onto me!"

        customer "What?! Preposterous!"

        show judge at center
        with dissolve
  
        judge "Indeed, Mr. Reed, that's enough... Mr. Baird is not on trial here, you are!"

        $ noise = noise + 1

        if noise == 2:
            judge "One more outburst like this and you'll forfeit your opportunity to defend yourself, Mr. Reed!"

        if noise == 3:
            jump gameover_outburst

        player "Sorry, your Honor... No more questions"

        judge "You are excused, Mr. Baird, thank you..."

        jump witness_loop

    "Withdraw question":
        player "I withdraw the question, your Honor... No further questions..."

        show judge at center
        with dissolve

        judge "You are excused, Mr. Baird, thank you..."

        jump witness_loop

label request_library_data:

    player "Your Honor, I require access to the library data."

    show judge at center
    with dissolve

    judge "Of course, it should be on your terminal..."

    narrator "Rowan quickly skims the library data. The data for Baird shows the following:\nRequested 'Romance in the Rain: A Steamy Novel' - 1 wk ago\nRequested 'Traders of the Heart' - 1 wk ago\nReturned 'Loving Love: A Horse Tale' - 1 wk ago\nRequested 'Loving Love: A Horse Tale' - 2 wk ago"

    $ knows_about_baird_books = True

    narrator "The books requested weren't history books, but romance novels... Strange..."

    jump after_manifesto

label customer_no_more_questions:

    show prosecutor at right
    with dissolve

    prosecutor "I have no more questions, your Honor..."

    show judge at center
    with dissolve

    judge "You are excused, Mr. Baird, thank you... And be sure to put anything you've read out of your mind!"

    hide customer
    with None
    hide judge
    with None
    hide prosecutor
    with None

    jump witness_loop
