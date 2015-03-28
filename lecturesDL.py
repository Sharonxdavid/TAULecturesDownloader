### easy to download lectures from TAUVideo ###
################Sharon David###################
###############################################
import urllib.request

def find_all_indices(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += len(sub)
        
course=input('Enter course name')
WELCOME=input('Enter course sourcecode')

PREFIX=list(find_all_indices(WELCOME,"files"))
SUFFIX=list(find_all_indices(WELCOME,".jpg"))
PREFIX.reverse(),SUFFIX.reverse()
urls=[]

for i in range(0,len(PREFIX)):
    temp='http://video.tau.ac.il/'+WELCOME[PREFIX[i]:SUFFIX[i]]+'.wmv'
    urls.append(temp)

#print(urls)
print('starting!')

for i in range(0,len(urls)):
    newI=str(i+1)
    fileName=course+newI+'.wmv'
    print('file #'+newI+':')
    try: urllib.request.urlretrieve(urls[i],fileName)
    except:
        print("Skipping")
        continue
    print('yay! next lecture.')

print('Download complete!')
