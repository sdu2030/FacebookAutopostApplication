#11/7/2021
###############
# Tkinter Facebook Autopost Application

#Goal of this Application:

# - To improve the convenience of posting content to Facebook pages
# - To allow for the easy scheduling of Facebook page posts
#
try: 
   from tkinter import *
   import os
   import requests
   import time
   #import schedule
except:
   import pip
   pip.main(['install', 'tkinter'])
   pip.main(['install', 'os'])
   pip.main(['install', 'requests'])
   pip.main(['install', 'time'])
   #pip.main(['install', 'schedule'])
   from tkinter import *
   import os
   import requests
   import time
   
os.system('cls')
###################
#TKinter GUI

root = Tk()
root.title('Facebook Autopost')
#root.geometry('700x400')
root.config(bg='#1c4366')

###################
#Schedule Posts Function:
def reBind():
   PostB['state'] = 'normal'
   PostB['text'] = 'Post!'
   PostB['command'] = post
   PostA['state'] = 'disabled'
   
def unBind():
   pass
   
def postW():
   whenPost = post1.get()
   
#list for reference: ['Now', '10 minutes', '30 minutes', '1 hour', '1 day', '2 days', '7 days']
   
   tTime = [0, 600, 1800, 3600, 86400, 172800, 604800]
   #tTime = [0, 1, 2, 3, 4, 5, 6]
   x = postOp.index(whenPost)
   
   whenPost = tTime[x]

   
   save_inputs()
   # Disables the button so you can't post duplicates:
   PostB['text'] = 'Posting...'
   PostB['state'] = 'disabled'
   
   PostB['command'] = unBind 
   PostA['state'] = 'normal'
   root.after(whenPost*1000, unBind())
   

######


#Autopost Functions
def post():
   page_id_1 = pID.get()
   facebook_access_token_1 = FBT.get()
   msg = msgTxt.get('1.0','end-1c')
   
#  print(page_id_1)
#  print(msg)
   
   
   post_url = 'https://graph.facebook.com/{}/feed'.format(page_id_1)
   payload = {
   'message': msg,
   'access_token': facebook_access_token_1
   }
   
   postW()
   PostB['text']='Posted!'
   
   
   r = requests.post(post_url, data=payload)
   print(r.text)
   
def create_inputs():
   pepper = '|}{_+:{].<!@#$%^&*()(@#&$^@(!):<>?/.,;[]'

   text_file = open('inputSave.txt', 'w+')
   text_file.write(pepper+'Facebook Token:'+'\n')
   text_file.write(pepper+'Facebook Page ID:'+'\n')
   text_file.write(pepper+'Message:'+'\n')
   text_file.write(pepper+'Post in:')
   text_file.close()
   pass
   
def save_inputs():
   text_file = open('inputSave.txt', 'w+')
   
   
   #this 'pepper' is added onto the beggining of every label to prevent any confusion with the loading program because the loading program will break if the message in the text box contains words used for the label
   
   pepper = '|}{_+:{].<!@#$%^&*()(@#&$^@(!):<>?/.,;[]'
   text_file.write(pepper+'Facebook Token:'+FBT.get()+'\n')
   text_file.write(pepper+'Facebook Page ID:'+pID.get()+'\n')
   text_file.write(pepper+'Message:'+msgTxt.get(1.0, END)+'\n')
   text_file.write(pepper+'Post in:'+post1.get())

   #savedMsg = text_file.read()
   
   #msgTxt.insert(END, savedMsg)
   text_file.close()
   pass
   
def clear_inputs():
   FBT.delete(0, END)
   pID.delete(0, END)
   msgTxt.delete('1.0', END)
   pass
   
     
   
def load_inputs():
   text_file = open('inputSave.txt', 'r')
   
   pepper = '|}{_+:{].<!@#$%^&*()(@#&$^@(!):<>?/.,;[]'
   
   savedMsg = text_file.read()
   
   FBTstart = savedMsg.index(pepper + 'Facebook Token:') + len(pepper + 'Facebook Token:')
   FBTend = savedMsg.index(pepper + 'Facebook Page ID:')
   
   pIDstart = savedMsg.index(pepper + 'Facebook Page ID:') + len(pepper + 'Facebook Page ID:')
   pIDend = savedMsg.index(pepper + 'Message:')
   
   msgTxtstart = savedMsg.index(pepper + 'Message:') + len(pepper + 'Message:')
   msgTxtend = savedMsg.index(pepper + 'Post in:')
   
   post1start = savedMsg.index(pepper + 'Post in:') + len(pepper + 'Post in:')
   post1end = len(savedMsg)
   
   
   FBT.insert(0, savedMsg[FBTstart:FBTend].strip())
   pID.insert(0, savedMsg[pIDstart:pIDend].strip())
   
   msgTxt.insert(END, savedMsg[msgTxtstart:msgTxtend].strip())
   
   #postOp.set(0, savedMsg[post1start:post1endend])
   
   text_file.close()
   pass
   
   
   
   
##########################################################
#Labels:

FBToken = Label(root, text =    'FB PAGE TOKEN:', bg = '#1c4366', fg = 'white', font=('Arial Black', 9, 'bold'))
PageID = Label(root, text =     'FB PAGE ID:',    bg = '#1c4366', fg = 'white', font=('Arial Black', 9, 'bold'))

PostB = Button(root, text =  'Post!', command=post, bg = 'aqua', fg = 'black',activebackground='blue')
PostA = Button(root, text =  'Post again!', command=reBind, bg = 'white', fg = 'black',activebackground='gray')

SaveB = Button(root, text =  'Save Inputs', command=save_inputs, bg = 'lime', fg = 'black',activebackground='green')
ClearB = Button(root, text =  'Clear Inputs', command=clear_inputs, bg = 'orange', fg = 'black',activebackground='red')


messageTxt = Label(root, text = 'MESSAGE:', bg = '#1c4366', fg = 'white', font=('Arial Black', 9, 'bold'))
postTime = Label(root, text =   'POST IN:', bg = '#1c4366', fg = 'white', font=('Arial Black', 9, 'bold'))
PostA['state'] = 'disabled'
#########################################################
#Text boxes:
FBT = Entry(root,width = 50, borderwidth = 5, )
pID = Entry(root, width = 50, borderwidth = 5)
msgTxt = Text(
    root,
    height=12,
    width=50,
    wrap='word',
    borderwidth = 3,
    font = ('Arial', 9, '')
)
# List Selection:
postOp = ['Now', '10 minutes', '30 minutes', '1 hour', '1 day', '2 days', '7 days']
rowx=0

post1 = StringVar(root)
post1.set(postOp[0]) # default value

postT = OptionMenu(root, post1, *postOp)

########################################Load inputs:

#this tries to load in inputs if there are any
try:
   load_inputs()
#if there are no inputs or no file for the inputs, this creates and sets up the input file.
except:
   create_inputs()
####################################################
#Packing Labels:
FBToken.grid(row=rowx, column = 0,sticky=W,padx = 15, pady = 10)
PageID.grid(row=rowx+3, column = 0,sticky=W,padx = 15, pady = 10)
messageTxt.grid(row=rowx+6, column = 0,sticky=W,padx = 15, pady = 10)
postTime.grid(row=rowx+9, column = 0,sticky=W,padx = 15, pady = 3)

#Inputs:
FBT.grid(row=rowx+1,column = 0,sticky=W,padx = 15, pady = 3)
pID.grid(row=rowx+4,column = 0,sticky=W,padx = 15, pady = 3)
msgTxt.grid(row=rowx+7,column = 0,sticky=W,padx = 15, pady = 10)
postT.grid(row=rowx+10,column = 0,sticky=W,padx = 15, pady = 3)



#Buttons:
PostB.grid(row=rowx+12, column = 4)
PostA.grid(row=rowx+12, column = 3)
SaveB.grid(row=rowx, column = 3)
ClearB.grid(row=rowx, column = 4)
##########################

root.mainloop()

##########################