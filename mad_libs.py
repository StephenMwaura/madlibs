def mad_libs(): #creating my own function
    adjective_day = input("How was the day: ")
    adjective_monkey = input("How was the monkey behaviour: ")
    adjective_lion = input("How was the lion behaving: ")
    adjective_experience = input("How was the day: ")
#would be based on the adjective_experience
    if adjective_experience.lower() in ['exiciting', 'thrilling']:
        print("I cant wait to go back!")
    elif adjective_experience.lower() in ['boring', 'dull']:
        print("Hope next time it will be fun")
    else:
        print("A day to remember")
        
        story = (f"It was a beautiful {adjective_day} to see a {adjective_monkey} on a tree."
                 f" I was able to see a lion behaving in a {adjective_lion}"
                 f"It was a really {adjective_experience}")
        print("Here is the story")

        print(story)

mad_libs()


        

 


