from ProjectClass import Project

def main() :
    print("welcome to cozy crafts in the console! would you like to create a new project or resume a project?")
    print("\tr: resume\n \tn: new\n \te:exit")
    answer = input()
    
    if answer == 'r' :
        print("wahoo")
    elif answer == 'n' :
        print("yippie, new project!")
        testing = Project("testing", "crochet")
        testing.save_project_data()
    elif answer == "e" :
        print("byebye!")
        exit()
    else :
        print("try again :)")
    
if __name__ == '__main__' :
    main()