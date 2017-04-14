from Tkinter import *
import tkMessageBox
import trainer as tr
import pandas
import utilities

root = Tk()
frame = Frame(root)
root.title("Malignant URL Checker")
frame.pack()
bottomframe = Frame(root)
bottomframe.pack( side = BOTTOM )

L1 = Label(frame, text="Enter the URL: ")
L1.pack( side = LEFT)
E1 = Entry(frame,bd =5, width=150)
E1.pack(side = RIGHT)

def submitCallBack():
	url=E1.get()

	flag=utilities.check_cache(url,'mycache.csv')

	if flag==0:
		tkMessageBox.showinfo( "URL Checker Result","The URL "+url+" is Benign")

	elif flag==1:
		tkMessageBox.showinfo( "URL Checker Result","The URL "+url+" is Malicious")
	
	elif flag==2:
		tkMessageBox.showinfo( "URL Checker Result","The URL "+url+" is Malware")

	else :

		utilities.features_to_csv(url,'test_features.csv')
		return_ans = tr.train_and_test('url_features.csv','test_features.csv')
		a=str(return_ans).split()

		if int(a[1])==0:
			flag=0
			utilities.append_result([url,flag],'mycache.csv')
			tkMessageBox.showinfo( "URL Checker Result","The URL "+url+" is Benign")

		elif int(a[1])==1:
			flag=1
			utilities.append_result([url,flag],'mycache.csv')
			tkMessageBox.showinfo( "URL Checker Result","The URL "+url+" is Malicious")
		else:
			flag=2
			utilities.append_result([url,flag],'mycache.csv')
			tkMessageBox.showinfo( "URL Checker Result","The URL "+url+" is Malware")

	   		   
B1 = Button(bottomframe, text ="Submit", command = submitCallBack)

B1.pack()

root.mainloop()