"""this is an exercise on fucntions"""

# def make_album(artist_name, artist_title):
#     """Fucntion to return a dictionary of the two paramenters"""
#     artist_dic = {'first': artist_name, 'title': artist_title}
#     return artist_dic

# artist_album = make_album('don meon', 'done me well')
# print(artist_album)


# """Print a simple greeting to each user in a list"""

# users = ['James', 'Jude','Judas', 'Jew']

# def greeting_message(users):
#     for names in users:
#         print(f"{names}, welcome to today's coaching class")

# greeting_message(users)

unprinted_designs = input("List your designers: ")

completed_models = [ ]

def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        unprinted_designs =+ 1
        
        current_design = unprinted_designs.pop()
        completed_models.append(current_design)

def show_completed_models(completed_models):
    for completed_models in completed_models:
        print(completed_model)

show_completed_models(completed_models)