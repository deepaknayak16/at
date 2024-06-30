##Auto message to whatsapp
# importing the module
import pywhatkit
  
# using Exception Handling to avoid 
# unprecedented errors
try:
    
  # sending message to receiver
  # using pywhatkit
  pywhatkit.sendwhatmsg("+918088310484", 
                        "Hello from GeeksforGeeks", 
                        22, 28)
  print("Successfully Sent!")
  
except:
    
  # handling exception 
  # and printing error message
  print("An Unexpected Error!")



