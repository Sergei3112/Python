# Написать программу для установки видео с Youtube. 
# Можно использовать сторонние библиотеки, например, pytube.


# -*- coding: utf-8 -*-
"""
Pytube Video Download Tutorial
"""

# Importing YouTube Module from pytube library
from pytube import YouTube

# Prompting user for Youtube Video link
youtube_url = input("Введите ссылку YouTube :  ")

# Creating YouTube object with the link
myVideo = YouTube(youtube_url)

# Creating StreamQuery Object
myVideoStream = myVideo.streams

# Using Filters on the myVideoStream Object
webmStreams = myVideoStream.filter(file_extension = "webm")

# See the content in the webmStreams created using filter
print(webmStreams.all())
webmStreams.last().download()

# Filtering only audio streams
audioStream = myVideoStream.filter(type = "audio")

# Accessing first stream in the audio streams and Download it
audioStream = audioStream.first()
audioStream.download('G:\загрузки')

print("Your Files are downloaded successfully")
