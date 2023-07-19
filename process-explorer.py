import os, sys, subprocess, psutil, time, webbrowser
import threading
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
from tkinter.simpledialog import askstring

window = Tk()
window.title("He1Zen | process-explorer")
photo = PhotoImage(file='task.png')
window.wm_iconphoto(False, photo)
window.geometry('675x495')
window.resizable(False, False)
msg1 = Label(window, text="pid or name")
msg1.place(x=430, y=445)
msg = Label(window, text="ID   | name                       pid             location")
msg.place(x=1, y=1)
global infinity
infinity = True

process = Combobox(window, width=17)
def resetprocess():
    global proc_names
    global list
    global added
    proc_names = []
    list = []
    added = []

def listprocess():
    for proc in psutil.process_iter():
        try:
            processName = proc.name()
            processID = str(proc.pid)
            location = str(proc.exe())
            status = psutil.Process(proc.pid).status()
            #owner = str(psutil.Process(proc.pid).username())
            #print(owner)
            num = 0
            for i in processName:
                num += 1
            pnum = 0
            for i in processID:
                pnum += 1
            if "System" in processName:
                if location == "":
                    pass
            elif "Registry" in processName:
                if location == "Registry":
                    pass
            elif "MemCompression" in processName:
                if location == "MemCompression":
                    pass
            else:
                if pnum == 1:
                    location = "         " + location
                elif pnum == 2:
                    location = "      " + location
                elif pnum == 3:
                    location = "     " + location
                elif pnum == 4:
                    location = "   " + location
                elif pnum == 5:
                    location = " " + location
                elif pnum == 6:
                    location = "" + location
                if num == 1:
                    list.append(processName + '                           ' + processID + ':' + status + '         ' + location)
                elif num == 2:
                    list.append(processName + '                          ' + processID + ':' + status + '         ' + location)
                elif num == 3:
                    list.append(processName + '                         ' + processID + ':' + status + '         ' + location)
                elif num == 4:
                    list.append(processName + '                        ' + processID + ':' + status + '         ' + location)
                elif num == 5:
                    list.append(processName + '                       ' + processID + ':' + status + '         ' + location)
                elif num == 6:
                    list.append(processName + '                      ' + processID + ':' + status + '         ' + location)
                elif num == 7:
                    list.append(processName + '                     ' + processID + ':' + status + '         ' + location)
                elif num == 8:
                    list.append(processName + '                    ' + processID +':' + status + '         ' + location)
                elif num == 9:
                    list.append(processName + '                   ' + processID + ':' + status + '         ' + location)
                elif num == 10:
                    list.append(processName + '                  ' + processID + ':' + status + '         ' + location)
                elif num == 11:
                    list.append(processName + '                 ' + processID + ':' + status + '        ' + location)
                elif num == 12:
                    list.append(processName + '                ' + processID + ':' + status + '         ' + location)
                elif num == 13:
                    list.append(processName + '               ' + processID + ':' + status + '         ' + location)
                elif num == 14:
                    list.append(processName + '              ' + processID + ':' + status + '         ' + location)
                elif num == 15:
                    list.append(processName + '             ' + processID + ':' + status + '         ' + location)
                elif num == 16:
                    list.append(processName + '            ' + processID + ':' + status + '         ' + location)
                elif num == 17:
                    list.append(processName + '           ' + processID + ':' + status + '         ' + location)
                elif num == 18:
                    list.append(processName + '        ' + processID + ':' + status + '         ' + location)
                elif num == 19:
                    list.append(processName + '       ' + processID + ':' + status + '         ' + location)
                elif num == 20:
                    list.append(processName + '      ' + processID + ':' + status + '         ' + location)
                elif num == 21:
                    list.append(processName + '     ' + processID + ':' + status + '         ' + location)
                elif num == 22:
                    list.append(processName + '    ' + processID + ':' + status + '         ' + location)
                elif num == 23:
                    list.append(processName + '   ' + processID + ':' + status + '         ' + location)
                else:
                    list.append(processName + '  ' + processID + ':' + status + '         ' + location)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

def showprocess(animation):
    global list
    global proc_names
    list.sort(reverse=True)
    Lb1 = Listbox(window, width=110, height=30, font=('Tahoma', 8))
    num = 0
    Lb1.delete(0, END)
    Lb1.pack(expand=1, fill="both")
    Lb1.place(x=1, y=21)
    for i in list:
        num += 1
        n = str(num)
        if num > 99:
            Lb1.insert(num,n + " | " + i)
        elif num > 9:
            Lb1.insert(num, "0" + n + " | " + i)
        else:
            Lb1.insert(num, "00" + n + " | " + i)
        i = i.replace(" ", "|", 1)
        i, o = i.split("|")
        t, o = o.split("C:")
        if "running" in t:
            added.append(n + "|" + i + "|running|C:" + str(o))
        elif "stopped" in t:
            added.append(n + "|" + i + "|stopped|C:" + str(o))
        elif "zombie" in t:
            added.append(n + "|" + i + "|zombie|C:" + str(o))
    for i in added:
        _, name, _, _ = i.split("|")
        proc_names.append(name)
    proc_names = [*set(proc_names)]
    proc_names.sort()
    process['values'] = proc_names
    #list.sort()
    for i in added:
        if animation == True:
            time.sleep(0.01)
        num, name, status, dir = i.split("|")
        num = int(num)
        num -= 1
        num = str(num)
        if status == "stopped":
            Lb1.itemconfig(num, bg='grey60')
        else:
            if name == "svchost.exe":
                if dir == "C:\Windows\System32\svchost.exe":
                    Lb1.itemconfig(num, bg='cyan3')
                else:
                    Lb1.itemconfig(num, bg='red1')
            if name == "smss.exe":
                if dir == "C:\Windows\System32\smss.exe":
                    Lb1.itemconfig(num, bg='blue2')
                else:
                    Lb1.itemconfig(num, bg='red1')
            if name == "services.exe":
                if dir == "C:\Windows\System32\services.exe":
                    Lb1.itemconfig(num, bg='cyan3')
                else:
                    Lb1.itemconfig(num, bg='red1')
            if name == "conhost.exe":
                if dir == "C:\Windows\System32\conhost.exe":
                    Lb1.itemconfig(num, bg='CadetBlue2')
                else:
                    Lb1.itemconfig(num, bg='red1')
            if name == "cmd.exe":
                if dir == "C:\Windows\System32\cmd.exe":
                    Lb1.itemconfig(num, bg='pink3')
            if name == "regedit.exe":
                if dir == "C:\Windows\\regedit.exe":
                    Lb1.itemconfig(num, bg='pink3')
            if name == "msconfig.exe":
                if dir == "C:\Windows\System32\\msconfig.exe":
                    Lb1.itemconfig(num, bg='pink3')
            if name == "powershell.exe":
                if "C:\Windows\System32\WindowsPowerShell" in dir:
                    Lb1.itemconfig(num, bg='pink3')
            if name == "spoolsv.exe":
                if dir == "C:\Windows\System32\spoolsv.exe":
                    Lb1.itemconfig(num, bg='cyan1')
            if name == "lsass.exe":
                if dir == "C:\Windows\System32\lsass.exe":
                    Lb1.itemconfig(num, bg='cyan2')
                else:
                    Lb1.itemconfig(num, bg='red1')
            if name == "csrss.exe":
                if dir == "C:\Windows\System32\csrss.exe":
                    Lb1.itemconfig(num, bg='CadetBlue1')
                else:
                    Lb1.itemconfig(num, bg='red1')
            if name == "winlogon.exe":
                if dir == "C:\Windows\System32\winlogon.exe":
                    Lb1.itemconfig(num, bg='green1')
                else:
                    Lb1.itemconfig(num, bg='red1')
            if name == "sihost.exe":
                if dir == "C:\Windows\System32\sihost.exe":
                    Lb1.itemconfig(num, bg='blue2')
                else:
                    Lb1.itemconfig(num, bg='red2')
            if name == "wininit.exe":
                if dir == "C:\Windows\System32\wininit.exe" in dir:
                    Lb1.itemconfig(num, bg='cyan2')
                else:
                    Lb1.itemconfig(num, bg='red1')
            if name == "AdminService.exe":
                if dir == "C:\Windows\System32\drivers\AdminService.exe":
                    Lb1.itemconfig(num, bg='blue2')
                else:
                    Lb1.itemconfig(num, bg='red1')
            if name == "dwm.exe":
                if dir == "C:\Windows\System32\dwm.exe":
                    Lb1.itemconfig(num, bg='blue2')
                else:
                    Lb1.itemconfig(num, bg='red1')
            if name == "SgrmBroker.exe":
                if dir == "C:\Windows\System32\Sgrm\SgrmBroker.exe":
                    Lb1.itemconfig(num, bg='blue1')
                else:
                    Lb1.itemconfig(num, bg='red1')
            if name == "SecurityHealthService.exe":
                if dir == "C:\Windows\System32\SecurityHealthService.exe":
                    Lb1.itemconfig(num, bg='cyan2')
                else:
                    Lb1.itemconfig(num, bg='red1')
            if name == "RuntimeBroker.exe":
                if dir == "C:\Windows\System32\RuntimeBroker.exe":
                    Lb1.itemconfig(num, bg='blue1')
                else:
                    Lb1.itemconfig(num, bg='red1')
            if name == "ctfmon.exe":
                if dir == "C:\Windows\System32\ctfmon.exe":
                    Lb1.itemconfig(num, bg='blue1')
                else:
                    Lb1.itemconfig(num, bg='red1')
            if name == "AggregatorHost.exe":
                if dir == "C:\Windows\System32\AggregatorHost.exe":
                    Lb1.itemconfig(num, bg='blue1')
                else:
                    Lb1.itemconfig(num, bg='red1')
            if name == "explorer.exe":
                if dir == "C:\Windows\explorer.exe":
                    Lb1.itemconfig(num, bg='green1')
            if name == "fontdrvhost.exe":
                if dir == "C:\Windows\System32\\fontdrvhost.exe":
                    Lb1.itemconfig(num, bg='cyan4')
                else:
                   Lb1.itemconfig(num, bg='red1')
            if name == "WUDFHost.exe":
                if dir == "C:\Windows\System32\WUDFHost.exe":
                    pass
                else:
                    Lb1.itemconfig(num, bg='red1')
            if name == "dllhost.exe":
                if dir == "C:\Windows\System32\dllhost.exe":
                    Lb1.itemconfig(num, bg='cyan3')
                else:
                    Lb1.itemconfig(num, bg='red1')
            if name == "smartscreen.exe":
                if dir == "C:\Windows\System32\smartscreen.exe":
                    Lb1.itemconfig(num, bg='cyan1')
            if dir == __file__:
                Lb1.itemconfig(num, bg='green1')
            if name in dir:
                if "Program Files" in dir:
                    if "Application" in dir:
                        Lb1.itemconfig(num, bg='yellow2')
                    else:
                        Lb1.itemconfig(num, bg='yellow1')
                elif "AppData" in dir:
                    if "Local" in dir:
                        if "Programs" in dir:
                            Lb1.itemconfig(num, bg='yellow1')
                elif "Games" in dir:
                   Lb1.itemconfig(num, bg='orange2')
                elif "C:\Windows\System32\DriverStore\FileRepository" in dir:
                    Lb1.itemconfig(num, bg='purple1')
            if "javaw.exe" in dir:
                if "bin" in dir:
                    Lb1.itemconfig(num, bg='pink2')
            if "python.exe" in dir:
                if "Python" in dir:
                    Lb1.itemconfig(num, bg='pink2')

def pc_usage():
    global infinity
    Lb2 = Listbox(window, width=20, height=3, font=('Tahoma', 8))
    Lb2.pack(expand=1, fill="both")
    Lb2.place(x=1, y=445)
    while infinity:
        try:
            if infinity == False:
                break
            memory = str(psutil.virtual_memory()[2])
            cpu = str(psutil.cpu_percent())
            Lb2.delete(0, END)
            Lb2.insert(1, "RAM usage: "+memory+"%")
            Lb2.insert(2, "CPU usage: "+cpu+"%")
            Lb2.insert(3, "")
            Lb2.itemconfig(0, bg="grey70")
            Lb2.itemconfig(1, bg="grey70")
            Lb2.itemconfig(2, bg="grey70")
            time.sleep(1)
        except:
            Lb2.delete(0, END)
            Lb2.insert(1, " ")
            Lb2.insert(2, " ")
            Lb2.insert(3, "")
            Lb2.itemconfig(0, bg="grey70")
            Lb2.itemconfig(1, bg="grey70")
            Lb2.itemconfig(2, bg="grey70")
            time.sleep(1)

def all_kill():
    try:
        PROCNAME = str(process.get())
        _, data = subprocess.getstatusoutput("tasklist")
        if PROCNAME in data:
            _, data = subprocess.getstatusoutput("taskkill /f /im " + str(PROCNAME))
            if "ERROR" in data:
                messagebox.showerror('Error', 'failed to kill process')
            else:
                if ".exe" in PROCNAME:
                    messagebox.showinfo('Info', 'successful killed process ' + PROCNAME)
                    threading.Thread(target=scan, kwargs={"animation": False}).start()
                else:
                    messagebox.showinfo('Info', 'successful killed process pid ' + PROCNAME)
                    threading.Thread(target=scan, kwargs={"animation": False}).start()
        else:
            messagebox.showerror('Error', 'process not found')
    except:
        messagebox.showerror('Error', 'failed to kill process')

def suspend():
    try:
        try:
            pid = int(process.get())
            p = psutil.Process(pid)
            p.suspend()
        except:
            PROCNAME = str(process.get())
            _, data = subprocess.getstatusoutput("tasklist")
            if PROCNAME in data:
                for proc in psutil.process_iter():
                    if proc.name() == PROCNAME:
                        p = psutil.Process(proc.pid)
                        p.suspend()
                threading.Thread(target=scan, kwargs={"animation": False}).start()
                #messagebox.showinfo('Info', 'successful suspend process ' + PROCNAME)
            else:
                messagebox.showerror('Error', 'process not found')
    except:
        messagebox.showerror('Error', 'failed to suspend process')

def resume():
    try:
        try:
            pid = int(process.get())
            p = psutil.Process(pid)
            p.resume()
        except:
            PROCNAME = str(process.get())
            _, data = subprocess.getstatusoutput("tasklist")
            if PROCNAME in data:
                for proc in psutil.process_iter():
                    if proc.name() == PROCNAME:
                        p = psutil.Process(proc.pid)
                        p.resume()
                threading.Thread(target=scan, kwargs={"animation": False}).start()
                #messagebox.showinfo('Info', 'successful resume process '+PROCNAME)
            else:
                messagebox.showerror('Error', 'process not found')
    except:
        messagebox.showerror('Error', 'failed to resume process')

def scan(animation):
    resetprocess()
    listprocess()
    if animation == True:
        time.sleep(0.2)
    showprocess(animation)

b1 = Button(window, text="scan", command=lambda: threading.Thread(target=scan, kwargs={"animation": True}).start(), width=12)
b1.place(x=126, y=444)
b2 = Button(window, text="author", command=lambda: webbrowser.open('https://github.com/mishakorzik'), width=12)
b2.place(x=126, y=468)

resetprocess()
listprocess()
showprocess(False)
th1 = threading.Thread(target=pc_usage)
th1.start()

process.place(x=502, y=446)
kill_proc = Button(window, text="kill", command=all_kill, width=4)
kill_proc.place(x=629, y=444)
suspend_proc = Button(window, text="suspend", command=suspend, width=12)
suspend_proc.place(x=500, y=469)
resume_proc = Button(window, text="resume", command=resume, width=12)
resume_proc.place(x=581, y=469)
window.mainloop()
infinity = False
