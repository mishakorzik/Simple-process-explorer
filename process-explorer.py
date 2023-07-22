import os, sys, subprocess, psutil, time, webbrowser, pyperclip
import threading
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
from tkinter.simpledialog import askstring

window = Tk()
window.title("He1Zen | process-explorer")
photo = PhotoImage(file='icons\\task.png')
window.wm_iconphoto(False, photo)
window.geometry('675x495')
window.resizable(False, False)
msg = Label(window, text="ID   | name                                                       pid:status               owner                                              location")
msg.place(x=1, y=1)
global infinity
global showall
infinity = True
showall = False

def window_cmdline(text):
    newWindow = Toplevel(window)
    newWindow.title("cmdline")
    newWindow.geometry("350x75")
    newWindow.resizable(False, False)
    photo = PhotoImage(file='icons\\task.png')
    newWindow.wm_iconphoto(False, photo)
    li = Listbox(newWindow, width=57, height=3, font=('Tahoma', 8))
    li.pack(expand=1, fill="both")
    li.place(x=1, y=1)
    li.insert(1, str(text))
    copy = Button(newWindow, text="copy", command=lambda: pyperclip.copy(str(text)), width=6).place(x=1, y=48)

def resetprocess():
    global proc_names
    global list
    global added
    global Lb1
    proc_names = []
    list = []
    added = []

def select_item(event):
    Lb1.selection_clear(0, END)
    Lb1.selection_set(Lb1.nearest(event.y))
    Lb1.activate(Lb1.nearest(event.y))

def listprocess():
    for proc in psutil.process_iter():
        try:
            processName = proc.name()
            processID = str(proc.pid)
            location = str(proc.exe())
            status = psutil.Process(proc.pid).status()
            if showall == False:
                owner = str(psutil.Process(int(processID)).username())
            num = 0
            nw = 0
            for i in processName:
                if i == "i":
                    nw += 1
                elif i == "j":
                    nw += 1
                elif i == "l":
                    nw += 1
                elif i == "r":
                    nw += 1
                elif i == "I":
                    nw += 1
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
                    location = "      " + location
                elif pnum == 2:
                    location = "     " + location
                elif pnum == 3:
                    location = "    " + location
                elif pnum == 4:
                    location = "   " + location
                elif pnum == 5:
                   location = "  " + location
                elif pnum == 6:
                    location = " " + location
                if num == 1:
                    processName = processName + "                                                            "
                elif num == 2:
                    processName = processName + "                                                          "
                elif num == 3:
                    processName = processName + "                                                        "
                elif num == 4:
                    processName = processName + "                                                      "
                elif num == 5:
                    processName = processName + "                                                    "
                elif num == 6:
                    processName = processName + "                                                  "
                elif num == 7:
                    processName = processName + "                                                "
                elif num == 8:
                    processName = processName + "                                              "
                elif num == 9:
                    processName = processName + "                                            "
                elif num == 10:
                    processName = processName + "                                          "
                elif num == 11:
                    processName = processName + "                                        "
                elif num == 12:
                    processName = processName + "                                      "
                elif num == 13:
                    processName = processName + "                                    "
                elif num == 14:
                    processName = processName + "                                  "
                elif num == 15:
                    processName = processName + "                                "
                elif num == 16:
                    processName = processName + "                              "
                elif num == 17:
                    processName = processName + "                            "
                elif num == 18:
                    processName = processName + "                          "
                elif num == 19:
                    processName = processName + "                        "
                elif num == 20:
                    processName = processName + "                      "
                elif num == 21:
                    processName = processName + "                    "
                elif num == 22:
                    processName = processName + "                  "
                elif num == 23:
                    processName = processName + "                "
                elif num == 24:
                    processName = processName + "              "
                elif num == 22:
                    processName = processName + "            "
                elif num == 23:
                    processName = processName + "          "
                elif num == 24:
                    processName = processName + "        "
                elif num == 25:
                    processName = processName + "      "
                else:
                    processName = processName + "    "
                if num < 30:
                    for i in range(nw):
                        processName = processName + " "
                if showall == True:
                    list.append(processName+'  '+processID+':'+status+'            '+location)
                else:
                    list.append(processName+'  '+processID+':'+status+'            '+owner+'            '+location)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

def showprocess():
    global list
    global proc_names
    list.sort(reverse=True)
    global Lb1
    Lb1 = Listbox(window, width=110, height=30, font=('Tahoma', 8))
    num = 0
    Lb1.delete(0, END)
    Lb1.pack(expand=1, fill="both")
    Lb1.place(x=1, y=21)
    Lb1.bind("<Button-3>", do_popup)
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
        if ":running" in t:
            added.append(n + "|" + i + "|running|C:" + str(o))
        elif ":stopped" in t:
            added.append(n + "|" + i + "|stopped|C:" + str(o))
        elif ":zombie" in t:
            added.append(n + "|" + i + "|zombie|C:" + str(o))
        elif ":sleeping" in t:
            added.append(n + "|" + i + "|zombie|C:" + str(o))
        elif ":waking" in t:
            added.append(n + "|" + i + "|zombie|C:" + str(o))
    for i in added:
        num, name, status, dir = i.split("|")
        num = int(num)
        num -= 1
        num = str(num)
        if status == "stopped":
            Lb1.itemconfig(num, bg='grey50')
        else:
            if name == "svchost.exe":
                if dir == "C:\Windows\System32\svchost.exe":
                    Lb1.itemconfig(num, bg='cyan3')
                else:
                    Lb1.itemconfig(num, bg='red1')
            if name == "smss.exe":
                if dir == "C:\Windows\System32\smss.exe":
                    Lb1.itemconfig(num, bg='green1')
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
                    pass
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
                elif dir == "C:\Windows\SysWOW64\dllhost.exe":
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
                    if "(x86" in dir:
                        Lb1.itemconfig(num, bg='yellow3')
                    else:
                        Lb1.itemconfig(num, bg='yellow2')
                elif "AppData" in dir:
                    if "Local" in dir:
                        Lb1.itemconfig(num, bg='yellow1')
                elif "Games" in dir:
                   Lb1.itemconfig(num, bg='orange2')
                elif "C:\Windows\System32\DriverStore" in dir:
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
            time.sleep(0.2)
        except:
            Lb2.delete(0, END)
            Lb2.insert(1, " ")
            Lb2.insert(2, " ")
            Lb2.insert(3, "")
            Lb2.itemconfig(0, bg="grey70")
            Lb2.itemconfig(1, bg="grey70")
            Lb2.itemconfig(2, bg="grey70")
            time.sleep(1)

def kill():
    try:
        global Lb1
        item = Lb1.get(Lb1.curselection())
        item = item.replace(":", "###", 1)
        item, _ = item.split("###")
        _, item = item.split("| ")
        item = item.replace("   ", "###", 1)
        _, item = item.split("###")
        item = item.replace(" ", "")
        PROCNAME = str(item)
        _, data = subprocess.getstatusoutput("tasklist")
        if PROCNAME in data:
            _, data = subprocess.getstatusoutput("taskkill /f /im " + str(PROCNAME))
            if "ERROR" in data:
                messagebox.showerror('Error', 'failed to kill process')
            else:
                threading.Thread(target=scan, kwargs={"sleep": 0}).start()
        else:
            messagebox.showerror('Error', 'process not found')
    except:
        messagebox.showerror('Error', 'failed to kill process')

def killall():
    global Lb1
    item = Lb1.get(Lb1.curselection())
    item = item.replace(":", "###", 1)
    item, _ = item.split("###")
    _, item = item.split("| ")
    item = item.replace("   ", "###", 1)
    item, _ = item.split("###")
    item = item.replace(" ", "")
    PROCNAME = str(item)
    if messagebox.askokcancel("Process Explorer", "Do you want to kill all processes related to "+PROCNAME):
        try:
            _, data = subprocess.getstatusoutput("tasklist")
            if PROCNAME in data:
                _, data = subprocess.getstatusoutput("taskkill /f /im " + str(PROCNAME))
                if "ERROR" in data:
                    messagebox.showerror('Error', 'failed to kill process')
                else:
                    threading.Thread(target=scan, kwargs={"sleep": 0}).start()
            else:
                messagebox.showerror('Error', 'process not found')
        except:
            messagebox.showerror('Error', 'failed to kill process')

def suspend():
    try:
        global Lb1
        item = Lb1.get(Lb1.curselection())
        item = item.replace(":", "###", 1)
        item, _ = item.split("###")
        _, item = item.split("| ")
        item = item.replace("   ", "###", 1)
        _, item = item.split("###")
        item = item.replace(" ", "")
        p = psutil.Process(int(item))
        p.suspend()
        threading.Thread(target=scan, kwargs={"sleep": 0}).start()
    except:
        messagebox.showerror('Error', 'failed to suspend process')

def resume():
    try:
        global Lb1
        item = Lb1.get(Lb1.curselection())
        item = item.replace(":", "###", 1)
        item, _ = item.split("###")
        _, item = item.split("| ")
        item = item.replace("   ", "###", 1)
        _, item = item.split("###")
        item = item.replace(" ", "")
        p = psutil.Process(int(item))
        p.resume()
        threading.Thread(target=scan, kwargs={"sleep": 0}).start()
    except:
        messagebox.showerror('Error', 'failed to resume process')

def copypath():
    try:
        global Lb1
        item = Lb1.get(Lb1.curselection())
        _, item = item.split("C:\\")
        item = "C:\\"+str(item)
        pyperclip.copy(item)
    except:
        messagebox.showerror('Error', 'select a process from list to copy path')

def restart():
    try:
        global Lb1
        item = Lb1.get(Lb1.curselection())
        _, item = item.split("C:\\")
        item = "C:\\"+str(item)
        path = f'"{item}"'
        item = Lb1.get(Lb1.curselection())
        item = item.replace(":", "###", 1)
        item, _ = item.split("###")
        _, item = item.split("| ")
        item = item.replace("   ", "###", 1)
        item, _ = item.split("###")
        item = item.replace(" ", "")
        PROCNAME = str(item)
        _, data = subprocess.getstatusoutput("taskkill /f /im " + str(PROCNAME))
        if "ERROR" in data:
            messagebox.showerror('Error', 'failed to restart process')
        else:
            threading.Thread(target=scan, kwargs={"sleep": 1}).start()
            os.system(path)
    except:
        messagebox.showerror('Error', 'select a process from list to restart')

def copypid():
    try:
        global Lb1
        item = Lb1.get(Lb1.curselection())
        item = item.replace(":", "###", 1)
        item, _ = item.split("###")
        _, item = item.split("| ")
        item = item.replace("   ", "###", 1)
        _, item = item.split("###")
        item = item.replace(" ", "")
        pyperclip.copy(str(item))
    except:
        messagebox.showerror('Error', 'select a process from list to copy pid')

def cmdline():
    try:
        global Lb1
        item = Lb1.get(Lb1.curselection())
        item = item.replace(":", "###", 1)
        item, _ = item.split("###")
        _, item = item.split("| ")
        item = item.replace("   ", "###", 1)
        _, item = item.split("###")
        item = item.replace(" ", "")
        p = psutil.Process(int(item))
        cmdlist = p.cmdline()
        text = ""
        for i in cmdlist:
            text = text + i + " "
        window_cmdline(text)
    except:
        messagebox.showerror('Error', 'failed to get cmdline from process')

def close():
    if messagebox.askokcancel("Process Explorer", "Do you want to quit from process explorer?"):
        global infinity
        infinity = False
        window.destroy()

def scan(sleep):
    if sleep == 0:
        pass
    else:
        time.sleep(int(sleep))
    resetprocess()
    listprocess()
    showprocess()

def show():
    global showall
    if showall == True:
        showall = False
        showproc['text'] = 'Show'
        msg['text'] = 'ID   | name                                                       pid:status                owner                                              location'
    else:
        showall = True
        showproc['text'] = 'Hide'
        msg['text'] = 'ID   | name                                                       pid:status                   location'
    threading.Thread(target=scan, kwargs={"sleep": 0}).start()

def do_popup(event):
    select_item(event)
    try:
        m.tk_popup(event.x_root, event.y_root)
    finally:
        m.grab_release()

b1 = Button(window, text="scan", command=lambda: threading.Thread(target=scan, kwargs={"sleep": 0}).start(), width=5).place(x=126, y=444)
b2 = Button(window, text="author", command=lambda: webbrowser.open('https://github.com/mishakorzik'), width=12).place(x=126, y=468)

m = Menu(window, tearoff=0)
m.add_command(label="Copy path", command=lambda: threading.Thread(target=copypath).start())
m.add_command(label="Copy pid", command=lambda: threading.Thread(target=copypid).start())
m.add_command(label="Cmd line", command=lambda: threading.Thread(target=cmdline).start())
m.add_separator()
m.add_command(label="Restart", command=lambda: threading.Thread(target=restart).start())

resetprocess()
listprocess()
threading.Thread(target=showprocess).start()
threading.Thread(target=pc_usage).start()

showproc = Button(window, text="Show", command=show, width=5)
showproc.place(x=167, y=444)
kill_proc = Button(window, text="kill", command=lambda: threading.Thread(target=kill).start(), width=8).place(x=605, y=469)
killall_proc = Button(window, text="kill-all", command=lambda: threading.Thread(target=killall).start(), width=8).place(x=605, y=444)
suspend_proc = Button(window, text="suspend", command=lambda: threading.Thread(target=suspend).start(), width=12).place(x=520, y=444)
resume_proc = Button(window, text="resume", command=lambda: threading.Thread(target=resume).start(), width=12).place(x=520, y=469)

notice = Label(window, text="system processes")
notice.place(x=207, y=446)
window.protocol("WM_DELETE_WINDOW", close)
window.mainloop()