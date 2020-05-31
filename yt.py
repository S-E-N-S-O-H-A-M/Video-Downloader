from pytube import YouTube

# video_list=['https://www.youtube.com/watch?v=lUCNWfwBjy0','https://www.youtube.com/watch?v=KskbFT-RAIU']

video_list=open("sample.txt",'r')
#dv=yt.streams.get_by_itag(20)
# print(yt.streams.all())
for i in video_list:
    yt=YouTube(i)
    try:
         # dv=yt.streams.first()
        dv=yt.streams.first()
        dv.download("E:/")
        print("download completed:",i)
    except:
        print("download failed:",i)

