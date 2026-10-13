
movies = [
    {
        "name": "Inception",
        "genre": "Sci-Fi",
        "platform": "Netflix",
        "rating": 8.8
    },
    {
        "name": "Interstellar",
        "genre": "Sci-Fi",
        "platform": "Prime Video",
        "rating": 8.7
    },
    {
        "name": "The Dark Knight",
        "genre": "Action",
        "platform": "Netflix",
        "rating": 9.0
    },
    {
        "name": "Avengers Endgame",
        "genre": "Action",
        "platform": "Disney+",
        "rating": 8.4
    },
    {
        "name": "3 Idiots",
        "genre": "Comedy",
        "platform": "Prime Video",
        "rating": 8.4
    },
    {
        "name": "The Hangover",
        "genre": "Comedy",
        "platform": "Netflix",
        "rating": 7.7
    },
    {
        "name": "The Notebook",
        "genre": "Romance",
        "platform": "Netflix",
        "rating": 7.8
    },
    {
        "name": "La La Land",
        "genre": "Romance",
        "platform": "Prime Video",
        "rating": 8.0
    },
    {
        "name": "Joker",
        "genre": "Drama",
        "platform": "Prime Video",
        "rating": 8.3
    },
    {
        "name": "Forrest Gump",
        "genre": "Drama",
        "platform": "Netflix",
        "rating": 8.8
    },
    {
        "name": "Spider-Man No Way Home",
        "genre": "Action",
        "platform": "Netflix",
        "rating": 8.2
    },
    {
        "name": "The Martian",
        "genre": "Sci-Fi",
        "platform": "Disney+",
        "rating": 8.0
    }
]

print("=" * 55)
print("          MOVIE RECOMMENDATION SYSTEM")
print("=" * 55)

print("\nAvailable Platforms:")
print("1. Netflix")
print("2. Prime Video")
print("3. Disney+")

platform = input("\nEnter your preferred platform: ").strip()

print("\nAvailable Genres:")
print("1. Action")
print("2. Comedy")
print("3. Romance")
print("4. Sci-Fi")
print("5. Drama")

genre = input("\nEnter your preferred genre: ").strip()

recommendations = []

for movie in movies:
    if (movie["platform"].lower() == platform.lower()
            and movie["genre"].lower() == genre.lower()):
        recommendations.append(movie)

print("\n" + "=" * 55)

if recommendations:

    recommendations = sorted(
        recommendations,
        key=lambda movie: movie["rating"],
        reverse=True
    )

    print("             RECOMMENDED MOVIES")
    print("=" * 55)

    for i, movie in enumerate(recommendations, 1):
        print(f"\n{i}. {movie['name']}")
        print(f"   Genre    : {movie['genre']}")
        print(f"   Platform : {movie['platform']}")
        print(f"   Rating   : {movie['rating']}")

else:
    print("No movies found!")
    print("Please try another platform or genre.")

print("\n" + "=" * 55)
print("Thank you for using Movie Recommendation System!")
print("=" * 55)
