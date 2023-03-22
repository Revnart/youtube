from pytube import YouTube
yt = YouTube(input("Podaj link: ")).streams.get_highest_resolution().download()
