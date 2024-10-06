import json


# This function will help to load the data or details stored in the file or in the retrieving of data of the file..
def load_data():
    try:
        with open('movie_manager.txt', 'r') as file:
            test = json.load(file)
            return test
    except FileNotFoundError:
        return []

#This function will help to store the elements in the file... 
def save_data_helper(movies):
    with open('movie_manager.txt', 'w') as file:
        json.dump(movies, file)


# This function will help to print or show all the movie details
def list_all_movie(movies):
    print("\n")
    print("*" * 70)
    for index, movie in enumerate(movies, start=1):   
        #The enumerate function in Python converts a data collection object into an enumerate object. Enumerate returns an object that contains a counter as a key for each value within an object, making items within the collection easier to access.
        print(f"{index}. Name: {movie['name']}, Year: {movie['Year']} ")
    print("\n")
    print("*" * 70)

# This Function will help to add movies in the list..
def add_movie(movies):
    name = input("Enter Movie name: ")
    Year = input("Enter Year: ")
    movies.append({'name': name, 'Year': Year})
    save_data_helper(movies)
    print(f"\nMovie Added Successfully!!!")

# This function will help to update the movie or any details about the movie...
def update_movie(movies):
    list_all_movie(movies)
    index = int(input("Enter the movie number to update: "))
    if 1 <= index <= len(movies):
        name = input("Enter the new Movie name: ")
        Year = input("Enter Year: ")
        movies[index-1] = {'name':name, 'Year': Year}
        save_data_helper(movies)
        print("\nList Successfully updated.....")
    else:
        print("Invalid index selected!!!!")


# This function will help to delete a movie from the file....
def delete_movie(movies):
    list_all_movie(movies)
    index = int(input("Enter the Movie number to be deleted: "))
    
    if 1<= index <= len(movies):
        del movies[index-1]
        save_data_helper(movies)
        print("\nMovie deleted successfully!!!")
        
    else:
        print("Invalid Movie index selected.....")


# Main  function from where the execution will start
def main():
    movies = load_data()
    while True:
        print("\nWelcome to Movie Manager App  \n")
        print("1. List All Favourite Movies ")
        print("2. Add a Movie ")
        print("3. Update a Movie or details ")
        print("4. Delete a Movie ")
        print("5. Exit the App ")
        choice = input("Enter your choice: ")

        match choice:
            case '1':
                list_all_movie(movies)
            case '2':
                add_movie(movies)
            case '3':
                update_movie(movies)
            case '4':
                delete_movie(movies)
            case '5':
                print("\nSuccessfully Exited Movie Manager App!!!")
                break
            case _:
                print("\nInvalid Choice  \nPlease Enter Valid Option....")


# Calling the main function....
if __name__ ==  "__main__":  # __name__ this is called as dunder(that underscore underscore part)..
    main()