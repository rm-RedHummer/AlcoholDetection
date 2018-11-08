import Tkinter,tkFileDialog

root = Tkinter.Tk()
filez = tkFileDialog.askopenfilenames(parent=root,title='Choose a file')
for file in filez:
# print root.tk.splitlist(filez)
