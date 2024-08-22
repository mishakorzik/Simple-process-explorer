import os, sys, subprocess, psutil, webbrowser, time, pyperclip
import threading
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
from tkinter.simpledialog import askstring
from io import BytesIO
import base64

image = base64.b64decode('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')

window = Tk()
window.title("he1zen | process explorer")
photo = PhotoImage(data=image)
window.wm_iconphoto(False, photo)
window.geometry('725x490')
window.resizable(False, False)
msg = Label(window, text='ID   | name                                                                        pid:status                              owner                                                location')
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
    li = Listbox(newWindow, width=90, height=3, font=('Tahoma', 8))
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
            for i in processName:
                num += 1
            pnum = 0
            for _ in processID:
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
                location = " " * (10 - pnum) + location
                aditional = 0
                for add in processName:
                    if add == "i" or add == "I" or add == "l" or add == "t" or add == "r" or add == "f":
                        aditional += 1
                    elif add == "m" or add == "w" or add == "O":
                        aditional -= 1
                processName = processName + " "*((80+aditional)-(int(num)*2))
                if showall == True:
                    list.append(processName+'  '+processID+':'+status+'                   '+location)
                else:
                    owner = " " * (10 - pnum) + owner
                    list.append(processName+'  '+processID+':'+status+'                   '+owner+'            '+location)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

def showprocess():
    global list
    global proc_names
    list.sort(reverse=True)
    global Lb1
    Lb1 = Listbox(window, width=120, height=27, font=('Helvetica', 8))
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
        num = str(int(num) - 1)
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
            if name == "conhoz.exe" or name == "MEMZ.exe" or name == "tobi0a0c.exe":
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
    Lb2 = Listbox(window, width=30, height=4, font=('Tahoma', 8))
    Lb2.pack(expand=1, fill="both")
    Lb2.place(x=1, y=430)
    while infinity:
        try:
            if infinity == False: break
            net_io_1 = psutil.net_io_counters()
            time.sleep(1)
            net_io_2 = psutil.net_io_counters()
            sent = (net_io_2.bytes_sent - net_io_1.bytes_sent) / 1024
            recv = (net_io_2.bytes_recv - net_io_1.bytes_recv) / 1024
            if sent > 1024: sent = str(round(sent / 1024)) + " Mbytes"
            else: sent = str(round(sent)) + " KBytes"
            if recv > 1024: recv = str(round(recv / 1024)) + " Mbytes"
            else: recv = str(round(recv)) + " KBytes"
            memory = str(psutil.virtual_memory()[2])
            cpu = str(psutil.cpu_percent())
            Lb2.delete(0, END)
            Lb2.insert(1, "ram usage       : "+memory+"%")
            Lb2.insert(2, "cpu usage       : "+cpu+"%")
            Lb2.insert(3, "network sent  : "+sent)
            Lb2.insert(4, "network recv  : "+recv)
            Lb2.itemconfig(0, bg="grey70")
            Lb2.itemconfig(1, bg="grey70")
            Lb2.itemconfig(2, bg="grey70")
            Lb2.itemconfig(3, bg="grey70")
        except:
            pass

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
        check_cmd = subprocess.run(["cmd", "/c", "echo", "test"], capture_output=True, text=True)
        if check_cmd.returncode == 0:
            _, data = subprocess.getstatusoutput("tasklist")
            if PROCNAME in data:
                _, data = subprocess.getstatusoutput("taskkill /f /im " + PROCNAME)
                if "ERROR" in data:
                    messagebox.showerror('Error', 'failed to kill process')
                threading.Thread(target=scan, kwargs={"sleep": 0}).start()
            else:
                messagebox.showerror('Error', 'process not found')
        else:
            process = psutil.Process(int(PROCNAME))
            process.kill()
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
        check_cmd = subprocess.run(["cmd", "/c", "echo", "test"], capture_output=True, text=True)
        if check_cmd.returncode == 0:
            try:
                _, data = subprocess.getstatusoutput("tasklist")
                if PROCNAME in data:
                    _, data = subprocess.getstatusoutput("taskkill /f /im " + str(PROCNAME))
                    if "ERROR" in data:
                        if "Access is denied" in data:
                            messagebox.showerror('Error', 'failed to kill process. Access denied')
                        else:
                            messagebox.showerror('Error', 'failed to kill process')
                    threading.Thread(target=scan, kwargs={"sleep": 0}).start()
                else:
                    messagebox.showerror('Error', 'process not found')
                    threading.Thread(target=scan, kwargs={"sleep": 0}).start()
            except:
                messagebox.showerror('Error', 'failed to kill process')
                threading.Thread(target=scan, kwargs={"sleep": 0}).start()

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
            if "Access is denied" in data:
                messagebox.showerror('Error', 'failed to restart process. Access denied')
            else:
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
        showproc['text'] = 'show'
        msg['text'] = 'ID   | name                                                                        pid:status                              owner                                                location'
    else:
        showall = True
        showproc['text'] = 'hide'
        msg['text'] = 'ID   | name                                                                        pid:status                             location'
    threading.Thread(target=scan, kwargs={"sleep": 0}).start()

def do_popup(event):
    select_item(event)
    try:
        m.tk_popup(event.x_root, event.y_root)
    finally:
        m.grab_release()

def fmanager():
    try:
        subprocess.run(["file-manager.exe"])
    except:
        messagebox.showerror('Error', 'file manager not installed!')

b1 = Button(window, text="scan", command=lambda: threading.Thread(target=scan, kwargs={"sleep": 0}).start(), width=5).place(x=185, y=429)
b2 = Button(window, text="author", command=lambda: webbrowser.open('https://github.com/mishakorzik'), width=12).place(x=185, y=454)

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

showproc = Button(window, text="show", command=show, width=5)
showproc.place(x=227, y=429)
kill_proc = Button(window, text="kill", command=lambda: threading.Thread(target=kill).start(), width=8).place(x=665, y=454)
killall_proc = Button(window, text="kill-all", command=lambda: threading.Thread(target=killall).start(), width=8).place(x=665, y=430)
suspend_proc = Button(window, text="suspend", command=lambda: threading.Thread(target=suspend).start(), width=12).place(x=580, y=430)
resume_proc = Button(window, text="resume", command=lambda: threading.Thread(target=resume).start(), width=12).place(x=580, y=454)
files = Button(window, text="file manager", command=lambda: threading.Thread(target=fmanager).start(), width=14).place(x=470, y=430)

combobox = Combobox(window, values=["explorer.exe", "perfmon.exe", "regedit.exe", "taskmgr.exe"], state='normal', width=12)
combobox.place(x=470, y=456)
combobox.current(0)
def on_select(event):
    item = str(combobox.get())
    try:
        subprocess.run([item])
    except:
        messagebox.showerror('Error', 'failed to run. Access denied')

combobox.bind("<<ComboboxSelected>>", on_select)
notice1 = Label(window, text="run")
notice1.place(x=445, y=457)
notice2 = Label(window, text="system processes")
notice2.place(x=270, y=431)
window.protocol("WM_DELETE_WINDOW", close)
window.mainloop()