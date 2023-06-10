genres = ['Fiction',
'Non-Fiction',
'Mystery',
'Thriller',
'Romance',
'Science Fiction',
'Fantasy',
'Horror',
'Historical Fiction',
'Biography',
'Autobiography',
'Memoir',
'Self-Help',
'Travel',
'Poetry',
'Drama',
'Comedy',
'Satire',
'Children Literature',
'Young Adult', ]

book_data=[ ['Fiction:', "To Kill a Mockingbird", 'by Harper Lee'],
           ['Non-Fiction:', "Sapiens: A Brief History of Humankind",  'by Yuval Noah Harari'],
           ['Mystery:' ,"Gone Girl" ,'by Gillian Flynn'],
           ['Thriller:' ,"The Girl on the Train", 'by Paula Hawkins'],
           ['Romance:', "Pride and Prejudice" ,'by Jane Austen'],
           ['Science Fiction:' ,"Dune", 'by Frank Herbert'],
           ['Fantasy:' ,"The Hobbit", 'by J.R.R. Tolkien'],
           ['Horror:', "The Shining", 'by Stephen King'],
           ['Historical Fiction:', "The Book Thief", 'by Markus Zusak'],
           ['Biography:', "The Diary of a Young Girl" ,'by Anne Frank'],
           ['Autobiography:',"The Autobiography of Malcolm X" ,'by Malcolm X and Alex Haley'],
           ['Memoir:', "Educated" ,'by Tara Westover'],
           ['Self-Help:', "The 7 Habits of Highly Effective People", 'by Stephen R. Covey'],
           ['Travel:', "Eat, Pray, Love", 'by Elizabeth Gilbert'],
           ['Poetry:', "Milk and Honey", 'by Rupi Kaur'],
           ['Drama:', "Romeo and Juliet" ,'by William Shakespeare'],
           ['Comedy:',"The Hitchhiker's Guide to the Galaxy" ,'by Douglas Adams'],
           ['Satire:', "Animal Farm" ,'by George Orwell'],
           ['Childrens Literature:', "Harry Potter and the Sorcerers Stone", 'by J.K. Rowling'],
           ['Young Adult (YA):', "The Fault in Our Stars" ,'by John Green']
           ]
def get_book_recommendation(genre):
    # Add your logic here to provide a book recommendation based on the genre
    # You can use if/elif statements or any other logic to match the genre and return a recommendation
    
    if genre == "Mystery":
        return "The Girl with the Dragon Tattoo"  # Example recommendation for Mystery genre
    elif genre == "Romance":
        return "The Notebook"  # Example recommendation for Romance genre
    # Add more elif statements or other logic for additional genres
    elif genre == "Fiction":
        return "To Kill a Mockingbird by Harper Lee"
    elif genre == "Non-Fiction":
        return "Sapiens: A Brief History of Humankind by Yuval Noah Harari" 
    elif genre == "Thriller":
        return "The Girl on the Train by Paula Hawkins" 
    elif genre == "Science Fiction":
        return "Dune by Frank Herbert" 
    elif genre == "Fantasy":
        return "The Hobbit by J.R.R. Tolkien" 
    elif genre == "Horror":
        return "The Shining by Stephen King " 
    elif genre == "Historical Fiction":
        return "The Book Thief by Markus Zusak" 
    elif genre == "Biography":
        return "The Diary of a Young Girl by Anne Frank " 
    elif genre == "Autobiography":
        return "The Autobiography of Malcolm X by Malcolm X and Alex Haley" 
    elif genre == "Memoir":
        return "Educated by Tara Westover " 
    elif genre == "Self-Help":
        return "The 7 Habits of Highly Effective People by Stephen R. Covey" 
    elif genre == "Travel":
        return "Eat, Pray, Love by Elizabeth Gilbert" 
    elif genre == "Poetry":
        return "Milk and Honey by Rupi Kaur" 
    elif genre == "Drama":
        return "Romeo and Juliete by William Shakespeare" 
    elif genre == "Comedy":
        return "The Hitchhiker's Guide to the Galaxy by Douglas Adams " 
    elif genre == "Satire":
        return "Animal Farm by George Orwell" 
    elif genre == "Children's Literature":
        return "Harry Potter and the Sorcerers Stone by J.K. Rowling" 
    elif genre == "Poetry":
        return "Milk and Honey by Rupi Kaur" 
    elif genre == "Young Adult":
        return "The Fault in Our Stars by John Green" 
       
       
    
    # If no specific recommendation for the genre, you can provide a default recommendation
    return "Sorry, we don't have a specific recommendation for that genre."

# You can add more functions or code to handle the book recommendations in this file
