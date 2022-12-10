class Series:
    def __init__(self, name: str, seasons: int, genres: list):
        self.title=name
        self.seasons= seasons
        self.genres=genres
        self.rating=0
        self.rating_count=0
        self.rating_total=0
    
    def rate(self,rating: int):
        self.rating_count+=1
        self.rating_total+= rating
        self.rating= self.rating_total/self.rating_count
        return self.rating

    def __str__(self) :
        genres_list = ", ".join(self.genres)
        if self.rating_count > 0:
            return f"{self.title} ({self.seasons} seasons)\ngenres: {genres_list}\n{self.rating_count} ratings, average {self.rating:.1f} points "
        
        elif self.rating_count == 0 :
            return f"{self.title} ({self.seasons} seasons)\ngenres: {genres_list}\nno ratings"
def minimum_grade(grade: float, series: list):
    min_grade=[]
    for a in series:
        if a.rating >= grade:
            min_grade.append(a)

    return min_grade

def includes_genre(genre: str, series_list: list):
    include_genre=[]
    for b in series_list:
        for g in b.genres:
            if g == genre:
                include_genre.append(b)
    return include_genre
if __name__ == "__main__":

    s1 = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
    s1.rate(5)

    s2 = Series("South Park", 24, ["Animation", "Comedy"])
    s2.rate(3)

    s3 = Series("Friends", 10, ["Romance", "Comedy"])
    s3.rate(2)

    series_list = [s1, s2, s3]

    print("a minimum rating of 4.5:")
    for series in minimum_grade(4.5, series_list):
        print(series.title)

    print("genre Comedy:")
    for series in includes_genre("Comedy", series_list):
        print(series.title)