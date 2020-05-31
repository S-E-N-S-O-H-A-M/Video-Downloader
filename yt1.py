import pytube 

# pytube.YouTube("https://www.youtube.com/watch?v=tzei6YoqQeM").streams.first().download("E:/")
pytube.Playlist("https://www.youtube.com/channel/UCQHLxxBFrbfdrk1jF0moTpw/playlists").download_all("E:/")
