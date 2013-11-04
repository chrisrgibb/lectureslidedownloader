from bs4 import BeautifulSoup
import urllib2
import re
import sys

def get_file(link):

	# strips the link out of the tag
	text = link.get('href') 

	if(text.find('pdf') > 0): 	# text contains the word pdf so must be a file
		word = text.split(';') # some of the links have some extra words in them after a semi colon - not sure why
		url = word[0] #
			
		lengthOfWord = len(url)
		# finds last 3 letters of url
		n = lengthOfWord-3 
		extension =url[n:]
		prefix = url[:4]
		if extension == 'pdf' and prefix == 'http': # checks if link is valid
													# could have done this with a regex but this way is easier
			filename = url.split('/') 
			
			filetosave = str(filename[len(filename)-1]) 
		
			try: 
				#print filename
				req = urllib2.Request(url)
				response = urllib2.urlopen(req)
				
				print "TRYING TO DOWNLOAD {}".format(str(filetosave))
				#print open(os.path.basename(url), "wb")
				with open(filetosave, "wb") as localfile2:
					#req.read()
					localfile2.write(response.read())
			except:
				print "HTTP Error: ",sys.exc_info()
				print "couldn't download {}".format(str(filetosave))


############ main program ############

try:
	#u = urllib2.urlopen('http://ecs.victoria.ac.nz/Courses/NWEN301_2013T1/LectureSchedule')
	u = urllib2.urlopen('http://ecs.victoria.ac.nz/Courses/SWEN222_2013T2/LectureSchedule')

except:
	print "Problem connecting to url", sys.exc_info()
	exit()

filename = 'file.html'
localfile = open(filename, 'w') 
localfile.write(u.read())
localfile.close()

localfile = open(filename, 'r')

soup = BeautifulSoup(localfile)

# print(soup.prettify()) # prints the whole dom structure
print("FIND ALL HREFS")

list_of_links = soup.find_all('a', href=True)

for ffile in list_of_links:
	get_file(ffile)


localfile.close()


