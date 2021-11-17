import os
from datetime import datetime
from config import db
import sys
# insert at 1, 0 is the script path (or '' in REPL)
from models import Director, Movie

# Data to initialize database with
DIRECTOR = [
    {
        "name": "Yudha",
        "gender": 2,
        "uid": 124,
        "department": "departing",
        "movies": [
            {
                "original_title" : 'a',
                "budget": 237000000,
                "popularity": 100,
                "release_date" : '2009-12-10',
                "revenue" : 2787965087,
                "title" : 'a',
                "vote_average": 6.9,
                "vote_count" : 4500,
                "overview" : 'In the 22nd century, a paraplegic .',
                "tagline" : 'Enter the World of Pandora.',
                "uid" : 8321,
            },
        ],
    }
]

# Delete database file if it exists currently
if os.path.exists('final_proj.db'):
    os.remove('final_proj.db')

# Create the database
db.create_all()

# Iterate over the DIRECTOR structure and populate the database
for director in DIRECTOR:
    direct = Director(name=director.get("name"), gender=director.get("gender"), uid=director.get("uid"), department=director.get("department"))

#     # Add the movies for the director
    for movie in director.get("movies"):
        direct.movies.append(
            Movie(
                original_title = movie.get('original_title'),
                budget = movie.get('budget'),
                popularity = movie.get('popularity'),
                release_date = movie.get('release_date'),
                revenue = movie.get('revenue'),
                title = movie.get('title'),
                vote_average = movie.get('vote_average'),
                vote_count = movie.get('vote_count'),
                overview = movie.get('overview'),
                tagline = movie.get('tagline'),
                uid = movie.get('uid')
            )
        )
    db.session.add(direct)

db.session.commit()