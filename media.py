class Video():

    """ Class to store a video media type"""

    def __init__(self, video_title, video_duration):
        self.title = video_title
        self.duration = video_duration


class Movie(Video):

    """ Class to store movie related information """

    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, movie_title, movie_storyline, movie_duration,
                 poster_image, trailer_youtube, rating_index):
        self.title = movie_title
        self.storyline = movie_storyline
        self.duration = movie_duration
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.rating = self.VALID_RATINGS[rating_index]
