# from youtubesearchpython import SearchVideos
from youtubesearchpython import SearchPlaylists

# search = SearchVideos("Battlefield 5", offset=2, mode="json", max_results=3)
search = SearchPlaylists("Battlefield 5", offset=2, mode="json", max_results=3)
print(search.result())

