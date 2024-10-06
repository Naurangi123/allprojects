# from pytube import Playlist

# url = input("Enter Playlist URL: ")
# playlist = Playlist(url)

# for video in playlist.videos:
#     video.streams.get_by_resolution()

# from pytube import Playlist

# # Function to filter streams by resolution
# def filter_by_resolution(streams, resolution):
#     # Iterate through available streams and find the one with the specified resolution
#     for stream in streams:
#         if stream.resolution == resolution:
#             return stream
#     return None

# # Input playlist URL
# url = input("Enter Playlist URL: ")

# # Initialize the playlist object
# playlist = Playlist(url)

# # Desired resolution
# desired_resolution = input("Enter desired resolution (e.g., '720p', '1080p'): ")

# # Iterate through videos in the playlist
# for video in playlist.videos:
#     # Get all streams for the video
#     video_streams = video.streams
    
#     # Filter streams by the desired resolution
#     stream = filter_by_resolution(video_streams, desired_resolution)
    
#     # If stream with desired resolution found, download it
#     if stream:
#         print(f"Downloading '{video.title}'...")
#         stream.download()
#     else:
#         print(f"No '{desired_resolution}' stream found for '{video.title}'. Skipping...")

from pytube import Playlist

# Input playlist URL
url = "https://www.youtube.com/watch?v=XWJ1sn3QC2c&list=RDXWJ1sn3QC2c&start_radio=1&ab_channel=WHALES"

yt=Playlist(url)

for video in yt.videos:
    stream=video.streams.get_by_resolution()
    stream.download()



