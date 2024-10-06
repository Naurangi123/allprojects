from pytube import YouTube


url=input("Enter a Video to download Audio")

yt=YouTube(url)
audio_streams=yt.streams.filter(only_audio=True).first()
audio_streams.download()