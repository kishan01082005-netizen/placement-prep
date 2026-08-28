class movie:
    def __init__(self, title, rating):
        self.title = title
        self.rating = rating
    
    def display_info(self):
        return f"Movie: {self.title}, Rating: {self.rating}"
    
yash_movie=movie("toxic", 8.5)
yash_movie_info = yash_movie.display_info()
print(yash_movie_info)