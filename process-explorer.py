import os, sys, subprocess, psutil, webbrowser, time, pyperclip, threading, base64
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
from tkinter.simpledialog import askstring
from io import BytesIO

image = base64.b64decode('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')

processes = {
    "svchost.exe": {"path": [r"C:\Windows\System32\svchost.exe"], "level": 5},
    "WUDFHost.exe": {"path": [r"C:\Windows\System32\WUDFHost.exe"], "level": 3},
    "smss.exe": {"path": [r"C:\Windows\System32\smss.exe"], "level": 4},
    "services.exe": {"path": [r"C:\Windows\System32\services.exe"], "level": 4},
    "conhost.exe": {"path": [r"C:\Windows\System32\conhost.exe"], "level": 3},
    "cmd.exe": {"path": [r"C:\Windows\System32\cmd.exe"], "level": 2},
    "regedit.exe": {"path": [r"C:\Windows\regedit.exe"], "level": 2},
    "msconfig.exe": {"path": [r"C:\Windows\System32\msconfig.exe"], "level": 2},
    "spoolsv.exe": {"path": [r"C:\Windows\System32\spoolsv.exe"], "level": 4},
    "lsass.exe": {"path": [r"C:\Windows\System32\lsass.exe"], "level": 5},
    "csrss.exe": {"path": [r"C:\Windows\System32\csrss.exe"], "level": 5},
    "winlogon.exe": {"path": [r"C:\Windows\System32\winlogon.exe"], "level": 5},
    "sihost.exe": {"path": [r"C:\Windows\System32\sihost.exe"], "level": 4},
    "wininit.exe": {"path": [r"C:\Windows\System32\wininit.exe"], "level": 5},
    "AdminService.exe": {"path": [r"C:\Windows\System32\drivers\AdminService.exe"], "level": 4},
    "dwm.exe": {"path": [r"C:\Windows\System32\dwm.exe"], "level": 3},
    "RuntimeBroker.exe": {"path": [r"C:\Windows\System32\RuntimeBroker.exe"], "level": 3},
    "SecurityHealthService.exe": {"path": [r"C:\Windows\System32\SecurityHealthService.exe"], "level": 4},
    "ctfmon.exe": {"path": [r"C:\Windows\System32\ctfmon.exe"], "level": 2},
    "AggregatorHost.exe": {"path": [r"C:\Windows\System32\AggregatorHost.exe"], "level": 3},
    "explorer.exe": {"path": [r"C:\Windows\explorer.exe"], "level": 3},
    "fontdrvhost.exe": {"path": [r"C:\Windows\System32\fontdrvhost.exe"], "level": 4},
    "dllhost.exe": {"path": [r"C:\Windows\System32\dllhost.exe", r"C:\Windows\SysWOW64\dllhost.exe"], "level": 3},
    "smartscreen.exe": {"path": [r"C:\Windows\System32\smartscreen.exe"], "level": 4},
    "ShellHost.exe": {"path": [r"C:\Windows\System32\ShellHost.exe"], "level": 3},
    "taskhostw.exe": {"path": [r"C:\Windows\System32\taskhostw.exe"], "level": 3},
    "wuauserv.exe": {"path": [r"C:\Windows\System32\wuauserv.exe"], "level": 4},
    "taskmgr.exe": {"path": [r"C:\Windows\System32\taskmgr.exe"], "level": 1},
    "ntoskrnl.exe": {"path": [r"C:\Windows\System32\ntoskrnl.exe"], "level": 5},
    "audiodg.exe": {"path": [r"C:\Windows\System32\audiodg.exe"], "level": 1},
    "dasHost.exe": {"path": [r"C:\Windows\System32\dasHost.exe"], "level": 2}
}

suspicious = [
    "salinewin.exe",
    "conhoz.exe",
    "MEMZ.exe",
    "tobi0a0c.exe"
]

# Глобальні змінні
window = Tk()
window.title("he1zen | process explorer")
photo = PhotoImage(data=image)
window.wm_iconphoto(False, photo)
window.geometry('725x495')
window.resizable(False, False)
msg = Label(window, text=f'ID {' '*2} | name {' '*62} pid {' '*9} status {' '*13} owner {' '*58} location')
msg.place(x=1, y=1)

infinity = True
showall = False

proc_list = []
lb_index_to_proc = {}

def window_cmdline(text):
    newWindow = Toplevel(window)
    newWindow.title("cmdline")
    newWindow.geometry("350x75")
    newWindow.resizable(False, False)
    try:
        photo = PhotoImage(file='icons\\task.png')
        newWindow.wm_iconphoto(False, photo)
    except:
        pass
    li = Listbox(newWindow, width=90, height=3, font=('Tahoma', 8))
    li.pack(expand=1, fill="both")
    li.insert(1, str(text))
    Button(newWindow, text="copy", command=lambda: pyperclip.copy(str(text)), width=6).place(x=1, y=48)

def resetprocess():
    global proc_list, lb_index_to_proc
    proc_list = []
    lb_index_to_proc = {}

def listprocess():
    global proc_list
    for proc in psutil.process_iter():
        try:
            processName = proc.name()
            processID = str(proc.pid)
            location = proc.exe()
            status = psutil.Process(proc.pid).status()
            child = proc.children(recursive=True)
            if not showall:
                owner = psutil.Process(proc.pid).username()

            if "System" in processName and location == "":
                continue
            if "Registry" in processName and location == "Registry":
                continue
            if "MemCompression" in processName and location == "MemCompression":
                continue

            proc_data = {"name": processName, "id": processID, "child": child, "status": status, "location": location}
            if not showall:
                proc_data["owner"] = owner
            proc_list.append(proc_data)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

def showprocess():
    global proc_list, lb_index_to_proc, showall, Lb1
    lb_index_to_proc = {}
    Lb1 = Listbox(window, width=103, height=27, font=('Courier', 8))
    Lb1.delete(0, END)
    Lb1.pack(expand=1, fill="both")
    Lb1.place(x=1, y=21)
    Lb1.bind("<Button-3>", do_popup)
    proc_list.sort(key=lambda x: x["name"].lower())
    num = 0
    for proc in proc_list:
        if proc['name'] == '':
            continue
        display_index = num + 1
        if showall:
            info_str = f"{display_index:03d}| {proc['name']:<30} {proc['id']:<6} {proc['status']:<10}  {proc['location']:<10}"
        else:
            info_str = f"{display_index:03d}| {proc['name']:<30} {proc['id']:<6} {proc['status']:<10} {proc.get('owner',''):<28}  {proc['location']:<10}"
        Lb1.insert(END, info_str)
        lb_index_to_proc[num] = proc

        if proc["child"]:
            if proc["status"] in ("stopped"):
                p = processes.get(proc["name"])
                l = proc["location"]
                if p and any(path in l for path in p["path"]):
                    Lb1.itemconfig(num, bg='#765694')
                else:
                    Lb1.itemconfig(num, bg='#D46B9A')
            elif proc["name"] in suspicious:
                Lb1.itemconfig(num, bg='#CD3333')
            else:
                p = processes.get(proc["name"])
                l = proc["location"]
                if p and any(path in l for path in p["path"]):
                    Lb1.itemconfig(num, bg='#931FFF')
                else:
                    Lb1.itemconfig(num, bg='#DA70D6')
        elif proc["status"] in ("zombie", "sleeping", "waking", "stopped"):
            Lb1.itemconfig(num, bg='#7F7F7F')
        elif proc["name"] in suspicious:
            Lb1.itemconfig(num, bg='#FF0000')
        else:
            name = proc["name"]
            loc = proc["location"]
            p = processes.get(name)
            if p is None:
                if r"\Program Files (x86)" in loc:
                    Lb1.itemconfig(num, bg='#CCCC00')
                elif r"\Program Files" in loc:
                    Lb1.itemconfig(num, bg='#EEEE00')
                elif r"\AppData" in loc and r"\Local" in loc:
                    Lb1.itemconfig(num, bg='#FFFF00')
                elif r"\Games" in loc:
                   Lb1.itemconfig(num, bg='#FF8000')
            else:
                if any(path in loc for path in p["path"]):
                    if p["level"] == 5:
                        Lb1.itemconfig(num, bg='#00FF00')
                    elif p["level"] == 4:
                        Lb1.itemconfig(num, bg='#00CDCD')
                    elif p["level"] == 3:
                        Lb1.itemconfig(num, bg='#00FFFF')
                    elif p["level"] == 2:
                        Lb1.itemconfig(num, bg='#7AC5C5')
                    elif p["level"] == 1:
                        Lb1.itemconfig(num, bg='#A5B8B8')
                else:
                    Lb1.itemconfig(num, bg='#FF0000')
        num += 1

def pc_usage():
    Lb2 = Listbox(window, width=25, height=4, font=('Courier', 8))
    Lb2.pack(expand=1, fill="both")
    Lb2.place(x=1, y=430)
    while infinity:
        try:
            net_io_1 = psutil.net_io_counters()
            time.sleep(1)
            net_io_2 = psutil.net_io_counters()
            sent = (net_io_2.bytes_sent - net_io_1.bytes_sent) / 1024
            recv = (net_io_2.bytes_recv - net_io_1.bytes_recv) / 1024
            sent_str = f"{round(sent/1024)} MB/s" if sent > 1024 else f"{round(sent)} KB/s"
            recv_str = f"{round(recv/1024)} MB/s" if recv > 1024 else f"{round(recv)} KB/s"
            memory = str(psutil.virtual_memory()[2])
            cpu = str(psutil.cpu_percent())
            Lb2.delete(0, END)
            Lb2.insert(1, "ram usage     : " + memory + "%")
            Lb2.insert(2, "cpu usage     : " + cpu + "%")
            Lb2.insert(3, "network sent  : " + sent_str)
            Lb2.insert(4, "network recv  : " + recv_str)
            Lb2.itemconfig(0, bg="#B3B3B3")
            Lb2.itemconfig(1, bg="#B3B3B3")
            Lb2.itemconfig(2, bg="#B3B3B3")
            Lb2.itemconfig(3, bg="#B3B3B3")
        except:
            pass

def get_selected_proc():
    global showall, Lb1
    selected_indices = Lb1.curselection()
    if not selected_indices:
        messagebox.showerror('Error', 'No process selected')
        return None
    selected_index = selected_indices[0]
    if showall:
        return proc_list[selected_index+1]
    else:
        return proc_list[selected_index]

def kill():
    try:
        proc = get_selected_proc()
        if proc is None:
            return
        PROCNAME = proc['name']
        pid = int(proc['id'])
        if messagebox.askokcancel("Kill Process", f"Kill {PROCNAME} (PID: {pid})?"):
            p = psutil.Process(pid)
            p.kill()
            threading.Thread(target=scan, kwargs={"sleep": 0}).start()
    except Exception as e:
        messagebox.showerror('Error', f'failed to kill process: {e}')

def killall():
    try:
        proc_data = get_selected_proc()
        if proc_data is None:
            return
        selected_proc = psutil.Process(int(proc_data['id']))
        root_proc = selected_proc
        while True:
            parent = root_proc.parent()
            if parent is None:
                break
            root_proc = parent

        if messagebox.askokcancel("Process Explorer", f"Do you want to kill the entire process tree for {root_proc.name()} (PID: {root_proc.pid})?"):
            for child in root_proc.children(recursive=True):
                try:
                    child.kill()
                except Exception:
                    pass
            root_proc.kill()
            threading.Thread(target=scan, kwargs={"sleep": 0}).start()
    except Exception as e:
        messagebox.showerror('Error', f'Failed to kill process tree: {e}')

def suspend():
    try:
        proc = get_selected_proc()
        if proc is None:
            return
        if psutil.Process(int(proc['id'])).status() not in ("stopped"):
            psutil.Process(int(proc['id'])).suspend()
            threading.Thread(target=scan, kwargs={"sleep": 0}).start()
    except Exception as e:
        messagebox.showerror('Error', f'failed to suspend process: {e}')

def resume():
    try:
        proc = get_selected_proc()
        if proc is None:
            return
        psutil.Process(int(proc['id'])).resume()
        threading.Thread(target=scan, kwargs={"sleep": 0}).start()
    except Exception as e:
        messagebox.showerror('Error', f'failed to resume process: {e}')

def copypath():
    try:
        proc = get_selected_proc()
        if proc is None:
            return
        path = proc['location']
        pyperclip.copy(path)
    except Exception as e:
        messagebox.showerror('Error', f'select a process from list to copy path: {e}')

def copypid():
    try:
        proc = get_selected_proc()
        if proc is None:
            return
        pyperclip.copy(proc['id'])
    except Exception as e:
        messagebox.showerror('Error', f'select a process from list to copy pid: {e}')

def cmdline():
    try:
        proc = get_selected_proc()
        if proc is None:
            return
        p = psutil.Process(int(proc['id']))
        cmdlist = p.cmdline()
        text = " ".join(cmdlist)
        window_cmdline(text)
    except Exception as e:
        messagebox.showerror('Error', f'failed to get cmdline from process: {e}')

def restart():
    try:
        proc = get_selected_proc()
        if proc is None:
            return
        path = proc['location']
        pid = int(proc['id'])
        PROCNAME = proc['name']

        p = psutil.Process(pid)
        p.kill()
        threading.Thread(target=scan, kwargs={"sleep": 1}).start()
        os.system(f'"{path}"')
    except Exception as e:
        messagebox.showerror('Error', f'failed to restart process: {e}')

def close():
    if messagebox.askokcancel("Process Explorer", "Do you want to quit from process explorer?"):
        global infinity
        infinity = False
        window.destroy()

def scan(sleep):
    if sleep:
        time.sleep(int(sleep))
    resetprocess()
    listprocess()
    showprocess()

def show():
    global showall
    showall = not showall
    threading.Thread(target=scan, kwargs={"sleep": 0}).start()
    time.sleep(0.5)
    if showall:
        showproc['text'] = 'hide'
        msg['text'] = f'ID {' '*2} | name {' '*62} pid {' '*9} status {' '*16} location'
    else:
        showproc['text'] = 'show'
        msg['text'] = f'ID {' '*2} | name {' '*62} pid {' '*9} status {' '*13} owner {' '*58} location'

def do_popup(event):
    try:
        Lb1.selection_clear(0, END)
        Lb1.selection_set(Lb1.nearest(event.y))
        Lb1.activate(Lb1.nearest(event.y))
        m.tk_popup(event.x_root, event.y_root)
    finally:
        m.grab_release()

def fmanager():
    try:
        subprocess.run(["file-manager.exe"])
    except:
        messagebox.showerror('Error', 'file manager not installed!')

# Кнопки і меню
b1 = Button(window, text="scan", command=lambda: threading.Thread(target=scan, kwargs={"sleep": 0}).start(), width=5)
b1.place(x=180, y=429)
b2 = Button(window, text="author", command=lambda: webbrowser.open('https://github.com/mishakorzik'), width=12)
b2.place(x=180, y=454)

m = Menu(window, tearoff=0)
m.add_command(label="Copy path", command=lambda: threading.Thread(target=copypath).start())
m.add_command(label="Copy pid", command=lambda: threading.Thread(target=copypid).start())
m.add_command(label="Cmd line", command=lambda: threading.Thread(target=cmdline).start())
m.add_separator()
m.add_command(label="Restart", command=lambda: threading.Thread(target=restart).start())

showproc = Button(window, text="show", command=show, width=5)
showproc.place(x=222, y=429)
kill_proc = Button(window, text="kill", command=lambda: threading.Thread(target=kill).start(), width=8)
kill_proc.place(x=666, y=454)
killall_proc = Button(window, text="kill-all", command=lambda: threading.Thread(target=killall).start(), width=8)
killall_proc.place(x=666, y=430)
suspend_proc = Button(window, text="suspend", command=lambda: threading.Thread(target=suspend).start(), width=12)
suspend_proc.place(x=581, y=430)
resume_proc = Button(window, text="resume", command=lambda: threading.Thread(target=resume).start(), width=12)
resume_proc.place(x=581, y=454)
files = Button(window, text="file manager", command=lambda: threading.Thread(target=fmanager).start(), width=14)
files.place(x=472, y=430)

combobox = Combobox(window, values=["explorer.exe", "perfmon.exe", "regedit.exe", "taskmgr.exe", "sysdm.cpl"], state='normal', width=12)
combobox.place(x=471, y=456)
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
notice2.place(x=265, y=431)

window.protocol("WM_DELETE_WINDOW", close)

resetprocess()
listprocess()
threading.Thread(target=showprocess).start()
threading.Thread(target=pc_usage).start()

window.mainloop()
