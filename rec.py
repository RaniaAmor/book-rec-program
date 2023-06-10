import genres

favorite_genre = input("Please enter your favorite book genre: ")
recommendation = genres.get_book_recommendation(favorite_genre)
print("Book Recommendation:", recommendation)
