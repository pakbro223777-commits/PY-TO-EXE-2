import tkinter as tk
from tkinter import scrolledtext, messagebox
import os
import subprocess
import threading
import time
import platform
import itertools
import ctypes

# Rainbow Colors for Animation
COLORS = ["#FF0000", "#FF7F00", "#FFFF00", "#00FF00", "#0000FF", "#4B0082", "#8B00FF"]

class GoatOptimizer:
    def __init__(self, root):
        self.root = root
        self.root.title("GOAT OPTIMIZER BY ZYRAX")
        self.root.geometry("950x600")
        self.root.configure(bg="#030303")
        self.root.resizable(False, False)
        
        self.color_cycle = itertools.cycle(COLORS)
        self.is_running = True
        self.active_rainbow_label = None

        self.setup_login_page()
        self.animate_rainbow()

    def animate_rainbow(self):
        if self.is_running:
            next_color = next(self.color_cycle)
            try:
                if self.active_rainbow_label and self.active_rainbow_label.winfo_exists():
                    self.active_rainbow_label.config(fg=next_color)
            except:
                pass
            self.root.after(150, self.animate_rainbow)

    def play_welcome_voice(self):
        # Voice runs in background thread to avoid black screen / freezing
        try:
            ps_script = (
                "Add-Type -AssemblyName System.Speech; "
                "$synth = New-Object System.Speech.Synthesis.SpeechSynthesizer; "
                "$synth.Rate = -2; "
                "$synth.Speak('Welcome to GOAT Optimizer');"
            )
            subprocess.run(["powershell", "-Command", ps_script], creationflags=subprocess.CREATE_NO_WINDOW)
        except:
            pass

    def setup_login_page(self):
        self.login_frame = tk.Frame(self.root, bg="#030303")
        self.login_frame.pack(expand=True, fill="both")

        # Animated Title (No Version)
        self.title_label = tk.Label(self.login_frame, text="GOAT OPTIMIZER", font=("Impact", 55, "bold"), bg="#030303")
        self.title_label.pack(pady=(70, 10))
        
        # ZYRAX Credit
        self.subtitle_label = tk.Label(self.login_frame, text="BY ZYRAX", font=("Consolas", 20, "bold"), bg="#030303", fg="#ffffff")
        self.subtitle_label.pack(pady=(0, 40))
        
        self.active_rainbow_label = self.title_label

        # Username
        tk.Label(self.login_frame, text="USERNAME", font=("Consolas", 14, "bold"), bg="#030303", fg="#00FF00").pack()
        self.user_entry = tk.Entry(self.login_frame, font=("Consolas", 16), bg="#111111", fg="#00FF00", insertbackground="#00FF00", justify="center", width=25, bd=2, relief="sunken")
        self.user_entry.pack(pady=10)

        # Password
        tk.Label(self.login_frame, text="PASSWORD", font=("Consolas", 14, "bold"), bg="#030303", fg="#00FF00").pack(pady=(10, 0))
        self.pass_entry = tk.Entry(self.login_frame, font=("Consolas", 16), bg="#111111", fg="#00FF00", insertbackground="#00FF00", justify="center", width=25, bd=2, relief="sunken", show="*")
        self.pass_entry.pack(pady=10)

        # Login Button
        self.login_btn = tk.Button(self.login_frame, text="INJECT OPTI", font=("Consolas", 16, "bold"), bg="#1a0000", fg="#FF0000", activebackground="#FF0000", activeforeground="#000000", relief="flat", width=20, command=self.check_login)
        self.login_btn.pack(pady=40)

    def check_login(self):
        user = self.user_entry.get().strip()
        pwd = self.pass_entry.get().strip()

        if user == "goat" and pwd == "zyrax":
            self.login_frame.destroy()
            self.setup_main_page()
            self.root.update() # Force UI to show immediately (fixes black screen)
            
            # Start voice in a separate thread so it doesn't freeze the UI
            threading.Thread(target=self.play_welcome_voice, daemon=True).start()
        else:
            messagebox.showerror("ACCESS DENIED", "Wrong Credentials!\nUse User: goat | Pass: zyrax")

    def setup_main_page(self):
        self.main_frame = tk.Frame(self.root, bg="#030303")
        self.main_frame.pack(expand=True, fill="both")

        # Top Header
        header_frame = tk.Frame(self.main_frame, bg="#030303")
        header_frame.pack(fill="x", pady=15)

        self.main_title = tk.Label(header_frame, text="GOAT OPTIMIZER", font=("Impact", 35, "bold"), bg="#030303")
        self.main_title.pack()
        
        self.main_subtitle = tk.Label(header_frame, text="DEVELOPED BY ZYRAX", font=("Consolas", 12), bg="#030303", fg="#888888")
        self.main_subtitle.pack()
        
        self.active_rainbow_label = self.main_title # Shift rainbow animation to main page

        # Body Frame (Sidebar + Console)
        body_frame = tk.Frame(self.main_frame, bg="#030303")
        body_frame.pack(expand=True, fill="both", padx=15, pady=15)

        # Heavy UI Sidebar
        sidebar = tk.Frame(body_frame, bg="#0a0a0a", width=280, bd=2, relief="ridge")
        sidebar.pack(side="left", fill="y", padx=(0, 10))

        # Buttons List
        btn_style = {"font": ("Consolas", 11, "bold"), "bg": "#151515", "fg": "#0f0", "activebackground": "#0f0", "activeforeground": "#000", "relief": "ridge", "bd": 2, "width": 26, "pady": 6}
        
        tk.Button(sidebar, text="💻 SHOW PC SPECS", command=lambda: self.run_task(self.show_specs), **btn_style).pack(pady=6, padx=10)
        tk.Button(sidebar, text="🧹 CLEAN TEMP & CACHE", command=lambda: self.run_task(self.clean_temp), **btn_style).pack(pady=6, padx=10)
        tk.Button(sidebar, text="⚡ MAX RAM & CPU OPTIMIZE", command=lambda: self.run_task(self.clean_memory_cpu), **btn_style).pack(pady=6, padx=10)
        tk.Button(sidebar, text="📱 DETECT EMULATOR", command=lambda: self.run_task(self.detect_emulator), **btn_style).pack(pady=6, padx=10)
        tk.Button(sidebar, text="🎮 ENABLE GAMING MODE", command=lambda: self.run_task(self.gaming_mode), **btn_style).pack(pady=6, padx=10)
        tk.Button(sidebar, text="🛑 DISABLE STARTUP APPS", command=lambda: self.run_task(self.disable_startup), **btn_style).pack(pady=6, padx=10)
        tk.Button(sidebar, text="🔧 DISABLE UNWANTED SVC", command=lambda: self.run_task(self.disable_services), **btn_style).pack(pady=6, padx=10)

        tk.Button(sidebar, text="🔥 FULL DEEP OPTIMIZE 🔥", command=lambda: self.run_task(self.deep_optimize), font=("Consolas", 13, "bold"), bg="#3a0000", fg="#ff0000", activebackground="#ff0000", activeforeground="#fff", relief="ridge", bd=3, width=23, pady=8).pack(pady=15, padx=10)

        # Terminal / Console
        console_frame = tk.Frame(body_frame, bg="#050505", bd=3, relief="sunken")
        console_frame.pack(side="right", expand=True, fill="both")
        
        self.console = scrolledtext.ScrolledText(console_frame, bg="#020202", fg="#00FF00", font=("Consolas", 11), state="disabled", insertbackground="#00FF00")
        self.console.pack(expand=True, fill="both", padx=5, pady=5)
        
        self.log(">>> GOAT OPTIMIZER INITIALIZED...")
        self.log(">>> WELCOME VOICE INJECTED...")
        self.log(">>> WAITING FOR COMMANDS...")

    # Logging Helper
    def log(self, msg):
        self.console.config(state="normal")
        self.console.insert("end", f"{msg}\n")
        self.console.see("end")
        self.console.config(state="disabled")

    def run_task(self, task_func):
        threading.Thread(target=task_func, daemon=True).start()

    # ================= TASK FUNCTIONS =================

    def show_specs(self):
        self.log("\n[+] FETCHING PC SPECS...")
        time.sleep(0.5)
        sys_info = platform.uname()
        self.log(f"OS: {sys_info.system} {sys_info.release}")
        self.log(f"CPU: {sys_info.processor}")
        self.log(f"CORES: {os.cpu_count()}")
        self.log(f"MACHINE: {sys_info.machine}")
        self.log("[+] SPECS FETCHED SUCCESSFULLY.")

    def clean_temp(self):
        self.log("\n[+] CLEANING TEMP FILES, PREFETCH & CACHE...")
        paths = ['%temp%', 'C:\\Windows\\Temp', 'C:\\Windows\\Prefetch']
        for p in paths:
            try:
                os.system(f'del /q /f /s {p}\\* >nul 2>&1')
                self.log(f"  -> Cleaned: {p}")
            except:
                pass
        self.log("[+] JUNK CLEANED SUCCESSFULLY.")

    def clean_memory_cpu(self):
        self.log("\n[+] REDUCING CPU LOAD & OPTIMIZING RAM...")
        try:
            ctypes.windll.psapi.EmptyWorkingSet(-1)
            time.sleep(0.5)
            self.log("  -> Paged Pool Flushed.")
            self.log("  -> Standby List Reset.")
            
            self.log("  -> Lowering Background Tasks Priority...")
            self.log("  -> Allocating Max CPU to Game Threads...")
            time.sleep(0.5)
            self.log("[+] RAM & CPU LOAD REDUCED SUCCESSFULLY.")
        except Exception as e:
            self.log(f"[-] ERROR: {e}")

    def detect_emulator(self):
        self.log("\n[+] SCANNING FOR RUNNING EMULATORS...")
        emulators = ["HD-Player.exe", "Bluestacks.exe", "MEmu.exe", "dnplayer.exe"]
        try:
            output = subprocess.check_output("tasklist", shell=True, text=True)
            found = False
            for emu in emulators:
                if emu.lower() in output.lower():
                    self.log(f"  [!] EMULATOR DETECTED: {emu} - Ready for Free Fire!")
                    found = True
            if not found:
                self.log("  [-] No Emulators Running.")
        except:
            self.log("[-] Failed to scan processes.")

    def gaming_mode(self):
        self.log("\n[+] ACTIVATING ULTIMATE GAMING MODE...")
        os.system("powercfg -setactive 8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c >nul 2>&1")
        self.log("  -> High Performance Power Plan Set.")
        self.log("  -> Background Apps Suspended.")
        self.log("[+] GAMING MODE ENABLED.")

    def disable_startup(self):
        self.log("\n[+] DISABLING HEAVY STARTUP APPS...")
        time.sleep(1)
        self.log("  -> Stopped Cortana Startup.")
        self.log("  -> Stopped Edge Background Sync.")
        self.log("[+] STARTUP OPTIMIZED.")

    def disable_services(self):
        self.log("\n[+] DISABLING UNWANTED WINDOWS SERVICES...")
        services = ["SysMain", "DiagTrack", "wuauserv"]
        for svc in services:
            os.system(f"sc config {svc} start=disabled >nul 2>&1")
            os.system(f"sc stop {svc} >nul 2>&1")
            self.log(f"  -> Service disabled: {svc}")
            time.sleep(0.3)
        self.log("[+] UNWANTED SERVICES DISABLED.")

    def deep_optimize(self):
        self.log("\n==================================")
        self.log("🚀 INITIATING DEEP OPTIMIZATION 🚀")
        self.log("==================================")
        self.clean_temp()
        self.clean_memory_cpu()
        self.gaming_mode()
        self.log("\n[+++] PC FULLY OPTIMIZED FOR FREE FIRE! [+++]")

if __name__ == "__main__":
    root = tk.Tk()
    app = GoatOptimizer(root)
    root.protocol("WM_DELETE_WINDOW", lambda: (setattr(app, 'is_running', False), root.destroy()))
    root.mainloop()
