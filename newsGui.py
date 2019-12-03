from keywordExtraction import hotkey

class endGui:
    hotkeylist = hotkey
    import tkinter

    window = tkinter.Tk()
    window.title("분야별 기사")
    window.geometry("980x500")
    window.config(bg="white")

    mainLabel = tkinter.Label(window, text="핫 키워드", font=("나눔바른펜", 20))
    mainLabel.pack(padx=10, pady=10)

    frame1 = tkinter.Frame(window, bg="white", relief='solid', bd=2)
    frame1.pack(ipadx=40, ipady=20, padx=10, side='left')
    label = tkinter.Label(frame1, text="정치", font=("나눔바른펜", 15), bg="yellow")
    label.pack(pady=5)
    for i in range(0, 10):
        label = tkinter.Label(frame1, text=str(i + 1) + "." + hotkeylist[0][i], font=("나눔바른펜", 13), bg="white")
        label.pack()

    frame1 = tkinter.Frame(window, bg="white", relief='solid', bd=2)
    frame1.pack(ipadx=40, ipady=20, padx=10, side='left')
    label = tkinter.Label(frame1, text="경제", font=("나눔바른펜", 15), bg="yellow")
    label.pack(pady=5)
    for i in range(0, 10):
        label = tkinter.Label(frame1, text=str(i + 1) + "." + hotkeylist[1][i], font=("나눔바른펜", 13), bg="white")
        label.pack()

    frame1 = tkinter.Frame(window, bg="white", relief='solid', bd=2)
    frame1.pack(ipadx=40, ipady=20, padx=10, side='left')
    label = tkinter.Label(frame1, text="사회", font=("나눔바른펜", 15), bg="yellow")
    label.pack(pady=5)
    for i in range(0, 10):
        label = tkinter.Label(frame1, text=str(i + 1) + "." + hotkeylist[2][i], font=("나눔바른펜", 13), bg="white")
        label.pack()

    frame1 = tkinter.Frame(window, bg="white", relief='solid', bd=2)
    frame1.pack(ipadx=40, ipady=20, padx=10, side='left')
    label = tkinter.Label(frame1, text="생활", font=("나눔바른펜", 15), bg="yellow")
    label.pack(pady=5)
    for i in range(0, 10):
        label = tkinter.Label(frame1, text=str(i + 1) + "." + hotkeylist[3][i], font=("나눔바른펜", 13), bg="white")
        label.pack()

    frame1 = tkinter.Frame(window, bg="white", relief='solid', bd=2)
    frame1.pack(ipadx=40, ipady=20, padx=10, side='left')
    label = tkinter.Label(frame1, text="세계", font=("나눔바른펜", 15), bg="yellow")
    label.pack(pady=5)
    for i in range(0, 10):
        label = tkinter.Label(frame1, text=str(i + 1) + "." + hotkeylist[4][i], font=("나눔바른펜", 13), bg="white")
        label.pack()

    window.mainloop()



