#Assignment 4
#Anna Lang 5839881

def assignment4A():
  #getting the file
  file = pickAFile() 
  
  lengthOfFile = len(file) 
  #finding the dot within the file
  dot = file.rfind('.') 
  #if the file is a picture then this will happen
  if file.endswith(".jpg") : 
    print("This is a picture") 
    show(makePicture(file)) 
    print("type is : .jpg") 
  #if the file is a audio file then this will happen
  elif file.endswith(".wav") :
    print("This is a sound") 
    play(makeSound(file)) 
    print("type is : .wav") 
  #if the file is not .wav or .jpg
  else : 
    print("You did not pick a picture or sound file") 
    print("file is : ."+file[dot+1:lengthOfFile])
 



def getClip(file, startPoint, endPoint):
#getting the file
  file = pickAFile()
  #This is to check if it is a music file 
  if not file.endswith(".wav") :
    print ("Please choose a music or '.wav' file.")
    return None; 
  else
    print ("this is not a music file")
  #find clip size
  sampRate = int(getSamplingRate(makeSound(file)))
  startindex = int(startPoint * sampRate)
  endindex = int(endPoint * sampRate)
  if endindex > getNumSamples(makeSound(file)):
    endindex = getNumSamples(makeSound(file))
  numSamp = endindex - startindex
  #copy the clip into the empty sound
  sound = makeEmptySound(numSamp, sampRate)
  index = 0;
  while index < numSamp:
   value = getSampleValueAt(makeSound(file), (index + startindex))
   setSampleValueAt(sound, index, value)
   index = index + 1
   
  return sound


