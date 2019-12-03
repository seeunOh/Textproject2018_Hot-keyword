import tkinter
import datetime

window = tkinter.Tk()
window.title("언제 기사?")
window.geometry("300x300")

frame1 = tkinter.Frame(window,bg="white", relief='solid',bd=2)
frame1.pack(ipadx=100, ipady=2, padx=10,pady=10, side='top', fill='both')

tod = tkinter.Label(frame1, text="오늘날짜", bg="white")
tod.pack()

today =datetime.date.today().strftime("%Y/%m/%d")
todaylab = tkinter.StringVar()
todaylab.set(today)
label2 = tkinter.Label(frame1, textvariable=todaylab, font=("나눔바른펜", 13),bg="white")
label2.pack()

frame2 = tkinter.Frame(window,bg="white", relief='solid',bd=2)
frame2.pack(ipadx=100, ipady=60, padx=10,pady=10, side='top')

label = tkinter.Label(frame2, text="원하는 날짜를 입력하세요", font=("나눔바른펜", 15),bg="white")
label.pack(padx=20,pady=10)

ex = tkinter.Label(frame2,text="입력예시)20181206")
ex.pack()

dateStr = tkinter.StringVar()

def clickMe():
    window.destroy()
    import newsCrawling
    newsCrawling.crawl(dateStr.get())
    import newsGui
    newsGui.endGui()

textbox = tkinter.Entry(frame2, width=20, textvariable=dateStr)
textbox.pack()
action = tkinter.Button(frame2, text="입력", command=clickMe,font=("나눔바른펜", 10), width=5)
action.pack()

window.mainloop()




