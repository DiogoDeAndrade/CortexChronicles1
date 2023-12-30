label gameover_outburst:

    scene bg court
    with None

    show prosecutor at right
    with dissolve

    prosecutor "Your Honor, this outburst is uncalled for and further proves the defendant's lack of control and respect for this court!"

    show judge at left
    with dissolve

    judge "I will agree with you, Mr. Holt."

    judge "It is obvious now that Mr. Reed is not capable of defending himself of the heinous crimes he's accused of, so it is better to move on to sentencing!"

    jump gameover
    

label gameover:

    show judge at left
    with dissolve

    judge "For the crime of sabotage, the court finds the defendent guilty as charged."

    if knows_about_manifesto:
        judge "For the crime of dissemination and authorship of seditious material, we also find the defendent guilty as charged."

    if score < 3:
        jump bad_ending
    else:
        jump good_ending

label bad_ending:
    judge "You will face the full consequences of your actions against this society and against Cortex."

    judge "Considering the threat you pose to societal stability and the heinous nature of your acts, the court hereby sentences you to death."

    judge "Guards, take him away..."

    if not plead_guilty:
        player "No! No! You have the wrong person! I didn't do anything!"

    scene bg black
    with longdissolve

    scene bg sunset
    with longdissolve

    narrator "The sun set..."

    narrator "The sun set...\nSilent..."

    narrator "The sun set...\nSilent...\nUnchanged..."

    scene bg coffin
    with longdissolve

    narrator "This day, Rowan Reed was killed by a system that feared him..."

    narrator "This day, Rowan Reed was killed by a system that feared him...\nFeared his thoughts... Feared his words..."

    narrator "This day, Rowan Reed was killed by a system that feared him...\nFeared his thoughts... Feared his words...\nFeared he would become tinder..."

    narrator "But they didn't put out the fire... they stoked it..."

    narrator "But they didn't put out the fire... they stoked it...\nMaybe one day Cortex will burn in it..."

    narrator "THE END"

    pause 1

    scene bg black
    with longfade

    narrator "Congratulations!\nYou've reached the end of The Trial of Rowan Reed, the first chapter of the Codex Chronicles.\nUnfortunately, you got the bad ending! Maybe try again?"

    return

label good_ending:
    judge "Although I consider you a threat to societal stability, the court couldn't find enough evidence to convict you to death."

    judge "As such, the court hereby sentences you to life imprisonment in the Tower, without the possibility of parole."

    judge "You may now believe this a mercy, but in time you might think it a curse..."

    judge "Guards, take him away..."
   
menu:

    "Cower":
        player "No! No! You have the wrong person! I didn't do anything!"
        jump good_ending_finale

    "Protest":
        player "This is unfair! It was all rigged! All rigged!"
        jump good_ending_finale

    "Threaten" if score >= 5:
        player "This isn't the end... We will rise!"
        player "Cortex will fall!"
        jump good_ending_finale    

label good_ending_finale:
    scene bg black
    with longdissolve

    scene bg sunset
    with longdissolve

    narrator "The sun set..."

    narrator "The sun set...\nSilent..."

    narrator "The sun set...\nSilent...\nUnchanged..."

    scene bg cell
    with longdissolve

    narrator "This day, Rowan Reed was locked away by a system that feared him..."

    narrator "This day, Rowan Reed was locked away by a system that feared him...\nFeared his thoughts... Feared his words..."

    narrator "This day, Rowan Reed was locked away by a system that feared him...\nFeared his thoughts... Feared his words...\nFeared he would become tinder..."

    narrator "But they didn't put out the fire... they stoked it..."

    narrator "But they didn't put out the fire... they stoked it...\nCortex will burn in it..."

    narrator "TO BE CONTINUED..."

    pause 1

    scene bg black
    with longfade

    narrator "Congratulations!\nYou've reached the end of The Trial of Rowan Reed, the first chapter of the Codex Chronicles.\nYou got the good ending! Good job!"

    return