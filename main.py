from pytube import YouTube
import os

# paste all the urls you want to download in links.txt file

#open the input file  by creating a file object
file_object = open('link.txt','r')

#read all the lines of links.txt file and store them inside a list, here, 'video_links'
video_links = file_object.readlines()

file_object.close()

#type of each url will be a string
#print(type(video_links[0]))


# url input from video_links list
for video_url in video_links:

    youtube_video = YouTube(video_url)


    # extract video
    video_stream = youtube_video.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()

    #comment the above line and uncomment the below to download audio file
    #video_stream = youtube_video.streams.filter(only_audio=True).first()

    #change below to your destination dir path
    download_directory = '/home/raghav/Music/bhajans'

    # download the file
    downloaded_file = video_stream.download(output_path=download_directory)

    # save the file
    file_name, file_extension = os.path.splitext(downloaded_file)
    
    #replace mp3 by mp4 for video downloads
    new_file_name = file_name + '.mp4'
    os.rename(downloaded_file, new_file_name)

    # result of success
    print(youtube_video.title + " has been successfully downloaded.")