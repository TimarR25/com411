def escape_by(plan):
    if plan == "jumping over":
        print("We cannot escape that way! The boulder is too big!")
    elif plan == "running":
        print("We cannot escape that way! The boulder is moving too fast!")
    elif plan == "going deeper":
        print("That might just work! Lets go deeper!")
    else:
        print("Not sure about that plan!")

escape_by("jumping over")
escape_by("running around")
escape_by("going deeper")