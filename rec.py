import genres.py

favorite_genre = input("Please enter your favorite book genre: ")
recommendation = book_recommendations.get_book_recommendation(favorite_genre)
print("Book Recommendation:", recommendation)
