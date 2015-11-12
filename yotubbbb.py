#C:\Users\Apache\Desktop\yoChannel
import os   
from time import sleep
import re 
import webbrowser

ph = raw_input("Enter the Account Name: ")

path = "C:\Users\\"+ph+"\Desktop\yoChannel\Channel"

files = list()
for filename in os.listdir(path):
	if re.findall("\S+html",filename):
		files.append(filename)
	linksum = 0

def html_to_txt(): 
    import urllib.request 
    url = str(path) 
    page = urllib.request.urlopen(url) 
    with open("test.txt", "w") as f: 
        for x in page: 
            f.write(str(x).replace('\\n','\n')) 
    s= 'Done' 
    return s

shandle = open("videoLink.txt","a")
for f in files:
	f = path + "\\"+f
	l = list()
	ihandle = open(f,"r")
	for a in ihandle:
		if re.findall("https://www.youtube.com\S+index=.",a):   
			link = re.findall("https://www.youtube.com\S+index=.",a)

			if link[0] not in l:
				l.append(link[0])
				shandle.write(link[0])
				shandle.write("\n")
	linksum += len(l)
	
	shandle.write("\n\n\n")
	ihandle.close()
shandle.close()


###########################################

handle = open("videoLink.txt","r")
leftfile = open("other.txt","a")
l = list()
r = ""
ser= list()
for a in handle:
	if a.find("watch") >= 0:
		r = a[a.find("www"):]
		ser.append(r.replace("\n",""))
	else:
		leftfile.write(a)
	#r+=a
#ser = r.split("\n")



for a in ser:
	dotl = a.find(".")
	url = a[:dotl+1]+"ss"+a[dotl+1:]
	print url
	webbrowser.open_new(url)
	raw_input("Press Enter to start the link")

handle.close()
leftfile.close()
#for filename in os.listdir(path):
#	handle = open(path+filename,a);
#	handle.write("\nNew line")
#	handle.close()
#	print "DONE"





def newLineRemover():# removes all the line that are there unnecessary betwwen the links
	count = 0
	for a in ser:
		if a =="":
			count+=1
	for a in range(count):
		ser.remove("")

