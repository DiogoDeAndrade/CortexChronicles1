label courtroom_start:

    scene bg court
    with dissolve

    pause 2.0

    show bailiff at right
    with dissolve

    bailiff "All rise for Judge Orrin Malloy..."

    hide bailiff
    with dissolve
    show judge at left
    with irisout

    judge "Be seated..."

    judge "Bailiff, can you please read the charges?"

    hide judge 
    with None
    show bailiff at right
    with dissolve

    bailiff "In the matter before this court, the accused Rowan Reed stands charged with the following offenses: Sabotage resulting in the catastrophic failure of a powerplant, leading to multiple fatalities and citywide blackouts. How does the defendent plead?"

    jump plead

label plead:

menu:
    "Ask for lawyer" if ask_for_lawyer == False:
        jump ask_for_lawyer

    "Complaint of lack of memory" if dont_remember == False:
        jump dont_remember

    "Plead guilty":
        jump plead_guilty

    "Plead not guilty":
        jump plead_notguilty

label ask_for_lawyer:
    $ ask_for_lawyer = True

    player "This is a farce! What about a lawyer?!"

    hide bailiff
    with None
    show judge at left
    with None

    judge "Normally, yes, you would have the right to counsel, but considering the charges and the evidence against you, no lawyer wanted to be associated with this!"

    judge "Again, how do you plead?"

    jump plead

label dont_remember:
    $ dont_remember = True

    player "What?! I don't remember anything!!"

    hide bailiff
    with None
    show prosecutor at right
    with None

    prosecutor "Convenient, your Honor..."

    show judge at left
    with dissolve

    judge "The accused will state clearly how does he plead! He will have time for his defense!"

    prosecutor "Thank, your Honor..."

    hide prosecutor
    with dissolve

    jump plead

label plead_guilty:

    $ plead_guilty = True

    player "I plead guilty, your Honor..."

    show judge at left
    with dissolve

    judge "Thank you, Mr. Reed for your honesty. We will move to sentencing then..."

    jump gameover

    return

label plead_notguilty:

    player "I plead not guilty, your Honor... I didn't do anything! I couldn't!"
    
    show judge at left
    with dissolve

    judge "Silence! You will have time to present your case, Mr. Reed!"

    jump witness_loop

label witness_loop:

    scene bg court
    with None

    if not witness_doctor and dont_remember:
        jump witness_doctor

    if not witness_worker:
        jump witness_worker

    if not witness_customer:
        jump witness_customer

    show prosecutor at right
    with None

    prosecutor "The prosecution has no more witnesses, your Honor..."

    hide prosecutor
    with dissolve
    show judge at left
    with dissolve

    judge "Mr. Reed, do you have any closing remarks before I render my verdict?"

menu:
    "Say the trial is rigged":
        player "*tired* This entire trial... It's just a farce, isn't it?"

        player "*angry* Can't you see? It doesn't matter how many lies we expose. The system, Cortex — it has already decided my fate. This trial is just a performance for the masses, to give the illusion of justice."

        judge "You will stand down, Mr. Reed! I will not have any grandstanding in my courtroom!"

        $ score = score - 1

        judge "If you don't know how to behave, we will move to sentencing!"

        jump gameover

    "Try to appeal for mercy":
        player "Your Honor, I stand here, not as a threat to our society, but as a testament to the very human struggles that we all share. I'm accused of acts I have no memory of, acts that go against my very nature."

        player "I understand the gravity of the situation. But I beg you, Judge Malloy, for mercy."

        $ score = score + 1

        judge "That was a pretty speech, Mr. Reed. We shall now move to sentencing..."

        jump gameover

    "Do a manifesto":

        jump do_manifesto

        $ knows_about_manifesto = True
        $ score = score - 1

    "Say nothing":

        player "Nothing to add, your Honor..."

        jump gameover

label do_manifesto:

    player "I've dedicated my life to knowledge, to understanding our history, and to preserving the truths that get easily lost in the vast narratives Cortex tries to write. I've always believed in the potential for humanity to rise, learn, and evolve."

    player "I plead with you, Your Honor, to see beyond the fabricated evidence and testimonies. To see a man who simply sought to question, to learn, and to understand. My intentions have never been to bring harm but to shed light."

menu:
    "Call judge a lapdog":
        player "And if you prefer to be Cortex's lapdog instead of a beacon of human justice, so be it!"

        $ score = score - 1

        judge "Mr. Reed... It is a strange tactic, insulting the judge... You show yet again you don't know how to behave in court!"
        
        judge "We shall move now to sentencing..."

        jump gameover

    "Plead for tomorrow":
        player "I understand the gravity of the situation. But I beg you, Judge Malloy, for mercy. Not for my sake alone but for the sake of the truth and the future generations who deserve to know it."
        
        judge "That was a pretty eloquent speech, Mr. Reed. We shall now move to sentencing..."

        jump gameover
