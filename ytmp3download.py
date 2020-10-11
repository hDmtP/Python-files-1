import pafy
url = str(input("Enter yt vdo url:\n"))
video = pafy.new(url)
try:
    bestaudio = video.getbestaudio()
    bestaudio.download()
except:
    print("Error encountered. Check ur programm or connection")