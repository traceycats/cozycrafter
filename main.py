from ProjectLibrary import Project
from sqlalchemy import create_engine

engine = create_engine("sqlite:///projects.db", echo=True) # echo means it logs all the data to the console

def main() :
    with engine.connect() as conn :
        print("welcome to cozy crafts in the console! would you like to create a new project or resume a project?")
        answer = input("\tr: resume\n \tn: new\n \te:exit")
        
        if answer == 'r' :
            print("wahoo, here is your last active project")
        elif answer == 'n' :
            print("yippie, new project!")
            # this will eventually be one form to fill out before making the project. for now, just using prompts then making the object
            name = input("what would you like to name your project?")
            type = input("if your project knit or crochet?")
            pattern = input("what's the name of the pattern you are using?") # this will be changed to be inputting a pdf of the pattern
        elif answer == "e" :
            print("bye bye!")
            exit()
        else :
            print("try again :)")
    
if __name__ == '__main__' :
    main()