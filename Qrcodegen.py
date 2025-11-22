import os
import time
import qrcode # type: ignore
import subprocess
import sys
import tkinter as tk
from tkinter import messagebox

qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)

def makeqr():
    global qr
    url = url_entry.get()
    dir = dir_entry.get()
    name = name_entry.get()
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    if os.path.isdir(dir):
        img.save(f"{dir}/{name}.png")
        messagebox.showinfo("QR code has been saved", "Please open Finder or File Explorer to view your file")
        #if sys.platform in ['linux', 'darwin']:
         #   subprocess.run([f'cd {dir}', f'open {name}.png'])
        #elif sys.platform == 'win32':
          #  subprocess.run([f'cd {dir}', f'"{name}"'])
        #else:
         #   print("ERROR: Phantom process detected in cgroup '/user.slice/background'")
          #  time.sleep(.5)
           # print('CRITICAL: RestorePoint Δ#442 checksum mismatch (expected FD-22E9, got 00-00-00)')
           # time.sleep(5)
           # print("KernelScheduler::RebalanceThreads(a, t) failed due to an unexpected NULL handle returned by AsyncPipe::OpenChannel()")
           # time.sleep(1)
           # print("DiskController: WARNING - Sector remapper attempted to remap a sector that did not consent to being remapped.")
           # time.sleep(2)
           # print("Traceback (most likely):\n   File \"<startup\", line 1, in <module>\nSystemInternalFailureError: Python could not execute because machine-wide integrity grid dissolved during interpreter boot sequence.")
           # time.sleep(4)
           # print("CRITICAL: Memory parity mismatch.\n      Expected: 0x00\n        Found:  \"I can't keep doing this\"")
           # time.sleep(10)
            #sys.exit
    else:
        os.mkdir(dir)
        img.save(f"{dir}/{name}.png")
        messagebox.showinfo("Done!", "Please open Finder or File Explorer to access this file.\nThe generation process will now repeat.")  

window = tk.Tk()
window.title("QR Code Generator")
window.resizable(False, False)

url_label = tk.Label(window, text="Website URL")
url_label.pack()

url_entry = tk.Entry(window)
url_entry.pack()

dir_label = tk.Label(window, text="Destination directory")
dir_label.pack()

dir_entry = tk.Entry(window)
dir_entry.pack()

name_label = tk.Label(window, text="Image file name")
name_label.pack()

name_entry = tk.Entry(window)
name_entry.pack()

gen_button = tk.Button(window, text="Generate", command=makeqr)
gen_button.pack()

window.mainloop()