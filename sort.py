 #!/usr/bin/python
# program that sorts your downloads folder and stores evrything in different folders like Mp3 in MP3folder .jpg in JPG folder and so on
# Author Akif Khan (akif500@gmail.com)
import os
import sys
import getpass
import shutil

_user = getpass.getuser()
dir="/home/"+_user+"/Downloads/"

def sort(f_type):
  try:  
      dirname=f_type.upper()
      os.chdir(dir)
      for files in os.listdir("."):
  
	  if files.endswith(f_type):
	
	      if os.path.isdir(dir+dirname):
		  shutil.move(dir+files,dir+dirname)
        
	      else:
		  os.mkdir(dir+dirname)
		  shutil.move(dir+files,dir+dirname)
		
      return	  
  
  except IOError:
      print "Error in reading file"
# ADD MORE EXTENSIONS HERE IF YOU WANT
sort("mp3")
sort("rpm")
sort("zip")
sort("pdf")
sort("doc")
sort("jpg")
sort("flv")
sort("tar")
