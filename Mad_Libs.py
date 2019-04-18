def cap_name(nom):
    return nom.capitalize()

def lower_word(wordy):
    return wordy.lower()

def want_to_play():
    answer = input("Do you want to play MadLibs? (y/n): ")

    answer = answer.lower()

    if answer == "y":
        print("Yay!")
        return make_madlib()
    elif answer == "n":
        return print("Oh, ok. Have a nice day!")
    else:
        return print("That\'s not a 'y' or a 'n'.")


def make_madlib():

    

    name = input("Please provide a name: ")
    profession = input("Please provide a job title: ")
    animal = input("Please provide an animal: ")
    item = input("Please provide an inanimate item: ")
    group = input("Please provide a plural noun (ex: dogs): ")
    noun = input("Please provide a singular noun: ")

    fix_name = cap_name(name)
    fix_animal = lower_word(animal)
    fix_group = lower_word(group)
    fix_noun = cap_name(noun)

    
    return print("%s the %s defeated the %s with the %s and made the %s respect %s." % (fix_name, profession, fix_animal, item, fix_group, fix_noun))

want_to_play()