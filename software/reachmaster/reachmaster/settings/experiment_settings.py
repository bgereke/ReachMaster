from .. import config
import Tkinter as tk 
import tkMessageBox

class ExperimentSettings(tk.Toplevel):

    def __init__(self, parent):
        #create window
        tk.Toplevel.__init__(self, parent)
        self.transient(parent) 
        self.grab_set()
        self.title("Experiment Settings") 
        self.configure(bg="white")
        self.protocol("WM_DELETE_WINDOW", self.on_quit) 
        #initialize tk variables from config
        self.cfg = config.json_load_byteified(open('./temp/tmp_config.txt'))
        self.lights_on_dur = tk.StringVar()
        self.lights_on_dur.set(str(self.cfg['ExperimentSettings']['lights_on_dur']))
        self.lights_off_dur = tk.StringVar()
        self.lights_off_dur.set(str(self.cfg['ExperimentSettings']['lights_off_dur']))
        self.reward_win_dur = tk.StringVar()
        self.reward_win_dur.set(str(self.cfg['ExperimentSettings']['reward_win_dur']))
        self.max_rewards = tk.StringVar()
        self.max_rewards.set(str(self.cfg['ExperimentSettings']['max_rewards']))
        self.solenoid_open_dur = tk.StringVar()
        self.solenoid_open_dur.set(str(self.cfg['ExperimentSettings']['solenoid_open_dur']))
        self.solenoid_bounce_dur = tk.StringVar()
        self.solenoid_bounce_dur.set(str(self.cfg['ExperimentSettings']['solenoid_bounce_dur']))
        self.flush_dur = tk.StringVar()
        self.flush_dur.set(str(self.cfg['ExperimentSettings']['flush_dur']))
        self.reach_delay = tk.StringVar()
        self.reach_delay.set(str(self.cfg['ExperimentSettings']['reach_delay']))
        #configure window
        self.configure_window()

    def on_quit(self):
        self.cfg['ExperimentSettings']['lights_on_dur'] = int(self.lights_on_dur.get())
        self.cfg['ExperimentSettings']['lights_off_dur'] = int(self.lights_off_dur.get())
        self.cfg['ExperimentSettings']['reward_win_dur'] = int(self.reward_win_dur.get())
        self.cfg['ExperimentSettings']['max_rewards'] = int(self.max_rewards.get()) 
        self.cfg['ExperimentSettings']['solenoid_open_dur'] = int(self.solenoid_open_dur.get())
        self.cfg['ExperimentSettings']['solenoid_bounce_dur'] = int(self.solenoid_bounce_dur.get())
        self.cfg['ExperimentSettings']['flush_dur'] = int(self.flush_dur.get())
        self.cfg['ExperimentSettings']['reach_delay'] = int(self.reach_delay.get())
        config.save_tmp(self.cfg)
        self.destroy()

    def configure_window(self):
        tk.Label(self,text="Lights On (ms):", font='Arial 10 bold', bg="white",width=23,anchor="e").grid(row=1, column=0)   
        tk.Entry(self,textvariable=self.lights_on_dur,width=17).grid(row=1, column=1)
        tk.Label(self,text="Lights Off (ms):", font='Arial 10 bold', bg="white",width=23,anchor="e").grid(row=2, column=0)   
        tk.Entry(self,textvariable=self.lights_off_dur,width=17).grid(row=2, column=1)
        tk.Label(self,text="Reward Window (ms):", font='Arial 10 bold', bg="white",width=23,anchor="e").grid(row=3, column=0)   
        tk.Entry(self,textvariable=self.reward_win_dur,width=17).grid(row=3, column=1)
        tk.Label(self,text="# Rewards/Trial:", font='Arial 10 bold', bg="white",width=23,anchor="e").grid(row=4, column=0)   
        tk.Entry(self,textvariable=self.max_rewards,width=17).grid(row=4, column=1)
        tk.Label(self,text="Solenoid Open (ms):", font='Arial 10 bold', bg="white",width=23,anchor="e").grid(row=5, column=0)   
        tk.Entry(self,textvariable=self.solenoid_open_dur,width=17).grid(row=5, column=1)
        tk.Label(self,text="Solenoid Bounce (ms):", font='Arial 10 bold', bg="white",width=23,anchor="e").grid(row=6, column=0)   
        tk.Entry(self,textvariable=self.solenoid_bounce_dur,width=17).grid(row=6, column=1)
        tk.Label(self,text="Flush (ms):", font='Arial 10 bold', bg="white",width=23,anchor="e").grid(row=7, column=0)   
        tk.Entry(self,textvariable=self.flush_dur,width=17).grid(row=7, column=1)
        tk.Label(self,text="Reach Delay (ms):", font='Arial 10 bold', bg="white",width=23,anchor="e").grid(row=8, column=0)   
        tk.Entry(self,textvariable=self.reach_delay,width=17).grid(row=8, column=1)