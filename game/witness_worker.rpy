label witness_worker:

    $ witness_worker = True

    scene bg court
    with None

    show prosecutor at right
    with dissolve

    prosecutor "The prosecution calls to the stand Mr. Milo Travers..."

    hide prosecutor
    with dissolve
    show worker at left
    with dissolve
    show bailiff at right
    with dissolve

    bailiff "You swear by the Prime Nexus to tell the truth, the whole truth, and nothing but the truth?"

    worker "I do!"

    hide bailiff
    with dissolve
    show prosecutor at right
    with dissolve

    prosecutor "Mr. Travers, you are a worker in the Northcore Powerplant, correct?"

    worker "That's right, sir."

    prosecutor "Can you tell the court what you saw on the night of the incident?"

    worker "Yes. It was around 9 PM, and I was just finishing up my shift, ansious to get home... The late shift in the winter is very cold, so me and the boys are always anxious to wrap things up!"
    
    worker "I saw that man over there *points at Rowan* near the north entrance of the powerplant, acting suspiciously. He kept looking around, as if making sure no one was watching."

    prosecutor "And you didn't think of confronting him?"

    worker "Oh no, sir. It was cold, and I didn't want to get home later!"

    worker "Now I wish I had..."

menu:
    "Object: Don't know where the powerplant is":
        jump worker_is_lying

    "Accuse worker":
        jump worker_accuse

    "Request cross examinination":
        jump worker_cross_examine

    "Stay silent":
        jump worker_stay_silent

label worker_is_lying:
    
    player "Objection! I don't even know where that powerplant is!"

    show judge at center
    with dissolve

    judge "Mr. Reed, if that's your best defense, I don't think this is going to go your way..."

    $ noise = noise + 1

    if noise == 2:
        judge "One more outburst like this and you'll forfeit your opportunity to defend yourself, Mr. Reed!"

    if noise == 3:
        jump gameover_outburst

    jump worker_no_more_questions

label worker_accuse:

    player "Ah! It seems you didn't do your job and now you want me to take the fall for it!"

    show judge at center
    with dissolve

    judge "Mr. Reed, it's not Mr. Travers job to provide security for the powerplant, and even if it was he would just be incompetent, not part of a conspiracy against you!"

    player "But he's saying it was me, and it wasn't! Maybe it was him that bombed the place!"

    prosecutor "This is complete speculation, your Honor!"

    judge "Yes, it seems so, Mr. Holt... Mr. Reed, you are out of order!"

    $ noise = noise + 1

    if noise == 2:
        judge "One more outburst like this and you'll forfeit your opportunity to defend yourself, Mr. Reed!"

    if noise == 3:
        jump gameover_outburst

    jump worker_no_more_questions

label worker_cross_examine:

    hide prosecutor
    with dissolve

    player "Your Honor, I assume I can ask some questions?"

    show judge at center
    with dissolve

    judge "All right, Mr. Reed, but thread carefully..."

    player "Mr. Travers, you said it was around 9 PM, correct?"

    worker "That's right."

    player "Could you describe the lighting conditions for the court? Was it dark? I assume so, since it is winter..."

    worker "Well, there's a streetlamp near the north entrance, so it was fairly well-lit. But yeah, the sun had set, so it was dark elsewhere."

    player "Interesting. And can you tell us what that person was wearing?"

    worker "He was wearing some sort of red shirt and I think a cap..."

menu:
    "Question clothes":
        jump worker_cross_examine_clothes

    "Question visibility":
        jump worker_cross_examine_visibility

label worker_cross_examine_clothes:

    player "See, your Honor? I have no red shirts and I never wore a cap!"

    show prosecutor at right
    with None

    prosecutor "Actually, your Honor, searches in the defendant's home yielded exactly the type of clothers Mr. Travers reported seeing in that night!"

    show judge at center
    with None

    judge "Interesting... So you will also claim they're not yours, Mr. Reed?"

    player "..."

    $ score = score - 1

    jump worker_no_more_questions

label worker_cross_examine_visibility:
    
    player "So, you can clearly identify my face in the distance, but you think I was wearing 'some sort of shirt' and you think maybe a cap?"

    player "I don't think you saw anything, Mr. Travers..."

    player "Did someone put you up to this?"

    show prosecutor at right
    with None

    prosecutor "Objection, your Honor! Badgering the witness!"

    show judge at center
    with None

    judge "He raises some good points, Mr. Holt... Is there any other proof Mr. Reed was there that night?"

    prosecutor "..."

    player "Mr. Travers, I have one more question... In such an important powerplant, was there any kind of security cameras?"

    worker "Er... What?"

    show judge right at center
    with None

    judge "Answer, Mr. Travers..."

    worker "Er, yes... there are cameras all around..."

    player "Even in the north entrance?"
    
    worker "Yes, sir..."

    player "And did the cameras pick up any picture of me or indeed anybody else?"

    worker "No sir... I was told they malfunctioned..."

    player "Told? Told by who?"

    worker "Mr. Holt, sir..."

    player "Mr. Holt? That seems odd...\nThank you, I have no more questions..."

    show judge at center
    with None

    judge "Odd indeed... Mr. Holt, care to explain?"

    prosecutor "Nothing odd, your Honor... I'm the attorney in charge, I was informed by the police and I informed Mr. Travers afterwards..."

    $ score = score + 2

menu:
    "Accuse Holt":
        jump accuse_holt

    "Stay silent":
        jump worker_stay_silent2

label accuse_holt:

    player "Informed by the police, or informed of the police, Holt?"

    judge "That will be enough, Mr. Reed! Mr. Holt is not on trial here, you are!"

    $ noise = noise + 1

    if noise == 2:
        judge "One more outburst like this and you'll forfeit your opportunity to defend yourself, Mr. Reed!"

    if noise == 3:
        jump gameover_outburst

    judge "You are excused, Mr. Travers, thank you!"

    hide doctor
    with None
    hide judge
    with None
    hide prosecutor
    with None

    jump witness_loop

label worker_stay_silent2:

    player "..."

    judge "You are excused, Mr. Travers, thank you!"

    hide doctor
    with None
    hide judge
    with None
    hide prosecutor
    with None

    jump witness_loop

label worker_stay_silent:

    player "*say nothing*"

    $ noise = noise - 1

    jump worker_no_more_questions

label worker_no_more_questions:

    show prosecutor at right
    with None

    prosecutor "I have no more questions, your Honor..."

    show judge at center
    with dissolve

    judge "You are excused, Mr. Travers, thank you... And please, be more vigilant next time!"

    hide worker
    with None
    hide judge
    with None
    hide prosecutor
    with None

    jump witness_loop
