
# Title to slug converter by Function

def Slug_Maker(Title): #Takes title as argument
    try:
        Splitted_Title = Title.split(" ")  # Splits words apart which have spaces within

        Lower_Case_Title = [items.lower() for items in Splitted_Title]  # Gives list of words in lower case

        Slug = ("-").join(Lower_Case_Title)  # Joins words in list with "-" to make a slug
        return Slug
    except:
        return Title
    
A = Slug_Maker("How to do this")    # Pass str argument
print(A)  # Prints slug as a final result
