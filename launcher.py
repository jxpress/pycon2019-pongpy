import sys
import subprocess
import tkinter
from tkinter import N, E, W, S
from tkinter import ttk

root = tkinter.Tk()
root.title(u"jx_pong - pyponjp2019 ")

main = tkinter.Frame(root, padx=10, pady=8, bg='#00A6BC')
main.grid()

tkinter.Label(main, text='Entry JX Pong', bg='#00A6BC', fg="white", font=("Helvetica", 20, "bold")).grid(row=0, column=0)

form = tkinter.Frame(main, padx=10, pady=16)
form.grid()

tkinter.Label(form, text='github').grid(row=1,column=0)
github = tkinter.Entry(form)
github.grid(row=1,column=1)

output = tkinter.Label(main, text='\n', font=("Helvetica", 10), bg='#eeeeee')
output.grid(row=3, column=0, sticky=(W, E))

def on_click_start():
    github_name = github.get()
    proc = subprocess.run([f'sh', 'start.sh', github_name],stdout = subprocess.PIPE, stderr = subprocess.PIPE)
    output['text'] = proc.stdout.decode("utf8") + proc.stderr.decode("utf8")

start_btn = ttk.Button(form, text='Start', command=on_click_start)
start_btn.grid(row=2, column=1, sticky=E)

root.mainloop()

