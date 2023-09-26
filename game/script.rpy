define player = Character("Me", what_size=26, color="#8de3e3")
define prosecutor = Character("Prosecutor", what_size=26, color="#da7070")
define doctor = Character("Doctor", what_size=26,  color="#6bac78")
define worker = Character("Worker", what_size=26,  color="#c7d15b")
define customer = Character("Customer", what_size=26,  color="#5fd15b")
define judge = Character("Judge", what_size=26,  color="#836bac")
define bailiff = Character("Bailiff", what_size=26,  color="#743ed1")
define narrator = Character("", what_size=26,  color="#bebebe")

define longfade = Fade(2.0, 1.0, 2.0)
define longdissolve = Dissolve(2.0)

default score = 0
default noise = 0
default ask_for_lawyer = False
default dont_remember = False
default knows_about_manifesto = False
default knows_about_library_data = False
default knows_about_baird_books = False
default plead_guilty = False

default witness_doctor = False
default witness_worker = False
default witness_customer = False

label start:
    jump intro
    #jump courtroom_start
