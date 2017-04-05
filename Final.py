#Assignment 2
#Anna Lang (5839881)
#Worked with: Caleb Nelson (5847850)

def assignment2A():
 count = 0 
 while count < 5: 
   import random
   number = random.randrange(1,101)  
   ans = raw_input("Is " + str(number) + " even or odd? --> ").lower()
   count = count + 1
   
   if number%2 == 0:
      if ans!="odd" and ans!="even" and ans!="e" and ans!="o":
       print "Please answer even, odd, e, or o. Thank you in advance!"
      if ans=="even" or ans == "e":
       print "correct"
      if ans=="odd" or ans == "o":
       print "wrong"
      
   else:
     if ans!="odd" and ans!="even" and ans!="e" and ans!="o":
       print "Please answer even, odd, e, or o. Thank you in advance!"
     if ans=="odd" or ans == "o":
       print "correct"
     if ans=="even" or ans =="e":
       print "wrong"
     

def assignment2B(text,spaces):
  #this is the function that is spliting the sentence apart
  test = text.split()
     
  while True: 
  #this is for when nothing is entered for text
    if (len(text)<=0):
      print "Null phrase. Enter at least one character, a word, or words separated by a space or spaces"
      break
  #this is nothing is entered in for spaces       
    elif (len (spaces) <=0):
      print "Padding must be between 1 and 5 characters. You had 0 characters"
      break
  #this is for when the person has entered more than 6 things in for spaces 
    elif (len (spaces) >= 6):
      print "Padding must be between 1 and 5 characters. You had more than 5 characters"
      break
    else: 
  #this is joining the sentence back together and added the spaces the person has inputted 
      extra = spaces.join(test)   
  #this will print the joined sentenece with the additional spaces added
      print extra
      break
  
  
                