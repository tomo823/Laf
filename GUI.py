
import os
from tkinter import *
import tkinter.ttk as ttk
from summary import get_voice


root = Tk()
root.title("YouTubeのURLを入力してください")
root.geometry("640x480")






#Main
menu = Menu(root)

menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label = "終了", command=root.quit)
menu.add_cascade(label="ファイル", menu=menu_file)

menu_tool = Menu(menu, tearoff=0)
menu_tool.add_command(label = "プレイリストから動画を抽出する", )
menu.add_cascade(label="ツール", menu=menu_tool)

top_frame = Frame(root)
top_frame.pack(side="top",fill="both" ,expand=True, padx=5,pady=5)

lbl = Label(top_frame,text="YoutubeのURLを記述してください。")
lbl.pack(side="top",anchor = 'nw')

label_photo = Label(top_frame)
label_photo.pack(side="right",anchor = 'n')

#スクロールバー
scrollbar = Scrollbar(top_frame)
scrollbar.pack(side="right",fill="y")

txt = Text(top_frame, yscrollcommand=scrollbar.set)
txt.pack(side="left",fill="both",expand = True)

scrollbar.config(command=txt.yview)

#Progress Frame
progress_frame = LabelFrame(root,text="進行状況")
progress_frame.pack(fill="x", padx=5,pady=5,ipady=5)

p_var = DoubleVar()
progress_bar = ttk.Progressbar(progress_frame,maximum=100,variable=p_var)
progress_bar.pack(fill="x",padx=5,pady=5)

#Botton
run_frame = Frame(root)
run_frame.pack(fill="x", padx=5, pady=5)

btn_close = Button(run_frame, padx=5, pady=5, text="閉じる", width=12, command=root.quit)
btn_close.pack(side="right",padx=5,pady=5)

btn_start = Button(run_frame, padx=5,pady=5,text="ダウンロード開始",width=15, command=get_voice(s))
btn_start.pack(side="right",padx=5,pady=5)

root.config(menu=menu)
root.mainloop()



s = txt.get("1.0", "end")
lines = [x for x in s.splitlines(False) if x != ""]

print("■lines",lines)

p_var.set(1)
progress_bar.update()

for line in enumerate(lines):
    
    yt = None

    try:
        print("■line",line)

        yt = YouTube(line[1])

        #-----------------
        #global photo
        print(yt.thumbnail_url) 
        photo = getImageByUrl(yt.thumbnail_url)
        label_photo.config(image=photo)
        label_photo.update()
        #-----------------

        downlod_audio(yt)
        #downlod_video(yt)

        p_var.set(100 / len(lines) * (line[0]+1))
        progress_bar.update()

    except:
        print(sys.exc_info())
    finally:
        pass

p_var.set(100)

with open("LOG.txt", "w") as file:
    file.write(r.text)