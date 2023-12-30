label witness_doctor:

    $ witness_doctor = True

    scene bg court
    with None

    show prosecutor at right
    with dissolve

    prosecutor "Since the defendant mentioned his memory issues, the prosecution calls to the stand Doctor Elara Mercer..."

    hide prosecutor
    with dissolve
    show doctor at left
    with dissolve
    show bailiff at right
    with dissolve

    bailiff "You swear by the Cortex and the Prime Nexus to tell the truth, the whole truth, and nothing but the truth?"

    doctor "Of course!"

    hide bailiff
    with dissolve
    show prosecutor at right
    with dissolve

    prosecutor "Doctor Mercer, you examined Mr. Reed after he claimed to have no memory, that's correct?"

    doctor "That is correct, Counselor."

    prosecutor "Can you relate your findings?"

    doctor "Of course. After conducting several cognitive assessments and neuroimaging scans, it's my professional opinion that Mr. Reed is exhibiting symptoms consistent with Post-Traumatic Stress Disorder, or PTSD."

    prosecutor "And how, Dr. Mercer, does PTSD relate to memory loss or gaps in memory?"

    doctor "PTSD can manifest in various ways, one of which includes disruptions in memory recall. It's not uncommon for individuals with PTSD to experience dissociative amnesia, where they cannot remember crucial events, especially those related to the trauma. This can result in gaps in their memory or even a complete inability to recall the traumatic event."

    prosecutor "So, is your opinion that even Mr. Reed felt his actions were so horrific that he blocked them out?"

    doctor "Yes."
    
menu:
    "Object: Memory issues were caused by Doctor Mercer":
        jump doctor_is_lying

    "Object: PTSD might not be caused by self actions":
        jump ptsd_not_caused_by_reed

    "Object: Request second opinion":
        jump second_opinion

    "Request cross examinination":
        jump doctor_cross_examine

    "Stay silent":
        jump doctor_stay_silent

label doctor_is_lying:
    
    player "Objection! I remember a conversation earlier where the doctor told the prosecution she made me forget!"

    hide doctor
    show judge at center
    with dissolve

    judge "Those are very serious allegations, Mr. Reed...\nDo you have any proof of you're saying?!"

    player "Er... No, I just know what I saw!"

    judge "Then in that case I believe you're just trying to descredit the witness and will strike your comments from the record!"

    $ noise = noise + 1

    if noise == 2:
        judge "One more outburst like this and you'll forfeit your opportunity to defend yourself, Mr. Reed!"

    if noise == 3:
        jump gameover_outburst

    jump doctor_no_more_questions

label ptsd_not_caused_by_reed:

    player "Objection! Even if I'm suffering from PTSD, there is no way of figuring out what's the source of PTSD. It might be completely unrelated to the current case!"

    show judge right at center
    with dissolve

    judge "Is this true, doctor?"

    doctor "Well... er... yes, we can't be sure... but it would be a coincidence, right?"

    hide doctor
    with dissolve
    show prosecutor left at left
    with dissolve

    prosecutor "This is complete speculation, your Honor!"

    judge "Well, it seems to be speculation either way... I will allow it!"

    $ score = score + 1

    jump doctor_no_more_questions

label second_opinion:

    player "Objection! I request a second opinion, your Honor!"

    hide doctor
    show judge at center
    with dissolve

    judge "And then a third? And a fourth after that?! On what grounds do you want a second opinion? Doctor Mercer is a well respected physician!"

    player "Not saying she isn't, your Honor, but..."

    judge "But nothing, Mr. Reed! The court is not here to indulge you!"

    $ noise = noise + 1

    if noise == 2:
        judge "One more outburst like this and you'll forfeit your opportunity to defend yourself, Mr. Reed!"

    if noise == 3:
        jump gameover_outburst

    jump doctor_no_more_questions

label doctor_cross_examine:

    player "Your Honor, may I ask a question to the good doctor?"

    hide prosecutor
    with None
    show judge right at center
    with dissolve

    judge "Go right ahead, Mr. Reed..."

    player "Doctor Mercer, you are a doctor of psychology, correct?"

    doctor "Er... I don't know why is that relevant..."

    player "Yes or no, doctor?"

    doctor "..."

    doctor "Actually no... I'm a pharmacologist."

    player "Ah! So, why is a pharmacologist diagnosing PTSD and such, which is usually the task of a psychologist?"

    show prosecutor at right
    with None

    prosecutor "Objection, your Honor! Doctor Mercer's credentials aren't in question here!"

    show judge right at center
    with None

    judge "I'll allow it, Mr. Holt... Please answer the question, Doctor Mercer."

    doctor "Er... I don't... I mean... Probably because..."

    player "So, it seems you would not be the first choice to analyze a patient with my issues... but would be excelent to cause the issues in the first place?"

    show prosecutor at right
    with None

    prosecutor "Objection, your Honor! Speculation!"

    player "Withdrawn, your Honor. No further questions..."

    $ score = score + 2

    hide prosecutor
    with None
    show judge right at center
    with dissolve

    judge "You are excused, Doctor Mercer, thank you!"

    hide doctor
    with None
    hide judge
    with None
    hide prosecutor
    with None

    jump witness_loop

label doctor_stay_silent:

    player "*say nothing*"

    $ noise = noise - 1

    jump doctor_no_more_questions

label doctor_no_more_questions:

    scene bg court
    with None

    show prosecutor at right
    with None

    prosecutor "I have no more questions, your Honor..."

    show judge at center
    with dissolve

    judge "You are excused, Doctor Mercer, thank you!"

    hide doctor
    with None
    hide judge
    with None
    hide prosecutor
    with None

    jump witness_loop
