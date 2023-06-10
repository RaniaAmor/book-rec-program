"""
book_recommendations.py

This module provides book recommendations based on the user's favorite genre.

Functions:
    get_book_recommendation(genre):
        Returns a book recommendation based on the provided genre.

"""

def get_book_recommendation(genre):
    """
    Returns a book recommendation based on the provided genre.

    Parameters:
        genre (str): The user's favorite book genre.

    Returns:
        str: A book recommendation corresponding to the genre.
        
    Raises:
        None

    Examples:
        >>> get_book_recommendation("Mystery")
        "The Girl with the Dragon Tattoo"

        >>> get_book_recommendation("Romance")
        "The Notebook"

    """

    # Add your logic here to provide a book recommendation based on the genre
    # You can use if/elif statements or any other logic to match the genre and return a recommendation
    
    if genre == "Mystery":
        return "The Girl with the Dragon Tattoo"  # Example recommendation for Mystery genre
    elif genre == "Romance":
        return "The Notebook"  # Example recommendation for Romance genre
    # Add more elif statements or other logic for additional genres
    
    # If no specific recommendation for the genre, you can provide a default recommendation
    return "Sorry, we don't have a specific recommendation for that genre."
