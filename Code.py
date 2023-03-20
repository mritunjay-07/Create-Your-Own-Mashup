#importing libraries
import os
from pytube import YouTube
import sys
from moviepy.editor import *
from youtubesearchpython import *
from moviepy.editor import concatenate_audioclips


class ExtraParameterError(Exception):
  pass
class Videos(Exception):
  pass
class Compress(Exception):
  pass


def main():
  try:
    if(len(sys.argv)!=5):
      raise ExtraParameterError
    # singername= "Arjit Singh"
    # numberofvideos = 5
    # dur = 5
    # outputfile="102003030-output.mp3"

    singername=sys.argv[1]
    number1=sys.argv[2]
    number2=sys.argv[3]
    outputfile=sys.argv[4]

    numberofvideos = int(number1)
    dur = int(number2)

    if numberofvideos<10:
       raise Videos
    if dur<20:
       raise Compress
    
    #directory for downloading videos from youtube
    currentdir = os.getcwd()
    newdir1="102003030-initialdownload"
    path1 = os.path.join(currentdir, newdir1)
    os.mkdir(path1)
    #converting videos to audios
    currentdir = os.getcwd()
    newdir2="102003030-videostoaudios"
    path2 = os.path.join(currentdir, newdir2)
    os.mkdir(path2)

    #part1
    # singername= "Arjit Singh"
    # numberofvideos = 5
    def downloadingvideos(singername,numberofvideos,path1):
        list = []
        videoslink = CustomSearch(singername+' songs', VideoDurationFilter.short)
        # print(videoslink.result())
        count = 0
        x=numberofvideos+30

        for i in range(0,x):
            if count == numberofvideos:
                break
            if((((videoslink.result())["result"])[i])['publishedTime'])!=None:
                a = (((videoslink.result())["result"])[i])["link"]
                list.append(a)
                count = count+1
        # print(len(list))
        for i in list:
            yt = YouTube(i)
            yt = yt.streams.get_by_itag(18)
            yt.download(path1)


    downloadingvideos(singername,numberofvideos,path1)


    #part2
    def convertingvideos(root_dir):
        f=[]
        for filename in os.listdir(root_dir):
            f.append(os.path.join(root_dir, filename))
        # print(f)
        n=1
        for i in f:
            output_ext="mp3"
            filename, ext = os.path.splitext(i)
            clip = VideoFileClip(i)
            clip.audio.write_audiofile(f"102003030-videostoaudios\{n}.{output_ext}")
            n=n+1
    #part3
    def cut(root_dir,dur):
        # dur = 5
        f=[]
        for filename in os.listdir(root_dir):
            f.append(os.path.join(root_dir, filename))
        for file in f:
            output_ext="mp3"
            filename, ext = os.path.splitext(file)

            input_audio_clip = AudioFileClip(file)
            final_clip = input_audio_clip.subclip(0, dur)
            final_clip.write_audiofile(f"{filename}.{output_ext}")
    #part4
    def merge(root_dir,outputfile):
        f = []
        for filename in os.listdir(root_dir):
            f.append(os.path.join(root_dir, filename))

        mashupaudio=AudioFileClip(f[0])
        for file in range(1,len(f)):
            mashupaudio = concatenate_audioclips([AudioFileClip(f[file]),mashupaudio])
        mashupaudio.write_audiofile(outputfile)
        print("!!!Your Mashup is Ready!!!")


    convertingvideos(path1)
    cut(path2,dur)
    merge(path2,outputfile)


  except FileNotFoundError:
    print("File Not Found")
  except ExtraParameterError:
    print("Extra Number of Parameters Entered, ie parameters entered should be equal to 5")
  except Videos:
    print("Number of videos cannot be less than 10, ie , N should be greater than 10")
  except Compress:
    print("Compress Seconds cannot be less than 20, ie , Y should be greater than 20")

if __name__=="__main__":
  main() 


