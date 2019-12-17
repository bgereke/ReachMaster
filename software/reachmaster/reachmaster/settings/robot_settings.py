from .. import config
import Tkinter as tk 
import tkFileDialog
import tkMessageBox
import numpy as np
import os

class RobotSettings(tk.Toplevel):

    def __init__(self, parent):
        #create window
        tk.Toplevel.__init__(self, parent)
        self.transient(parent) 
        self.grab_set()
        self.title('Robot Settings')   
        self.configure(bg='white')
        self.protocol('WM_DELETE_WINDOW', self.on_quit)
        #initialize tk variables from config
        self.cfg = config.json_load_byteified(open('./temp/tmp_config.txt'))
        self.alpha = tk.StringVar()
        self.alpha.set(str(self.cfg['RobotSettings']['alpha']))
        self.tol = tk.StringVar()
        self.tol.set(str(self.cfg['RobotSettings']['tol']))
        self.period = tk.StringVar()
        self.period.set(str(self.cfg['RobotSettings']['period']))
        self.off_dur = tk.StringVar()
        self.off_dur.set(str(self.cfg['RobotSettings']['off_dur']))
        self.num_tol = tk.StringVar()
        self.num_tol.set(str(self.cfg['RobotSettings']['num_tol']))
        self.x_push_wt = tk.StringVar()
        self.x_push_wt.set(str(self.cfg['RobotSettings']['x_push_wt']))
        self.x_pull_wt = tk.StringVar()
        self.x_pull_wt.set(str(self.cfg['RobotSettings']['x_pull_wt']))
        self.y_push_wt = tk.StringVar()
        self.y_push_wt.set(str(self.cfg['RobotSettings']['y_push_wt']))
        self.y_pull_wt = tk.StringVar()
        self.y_pull_wt.set(str(self.cfg['RobotSettings']['y_pull_wt']))
        self.z_push_wt = tk.StringVar()
        self.z_push_wt.set(str(self.cfg['RobotSettings']['z_push_wt']))
        self.z_pull_wt = tk.StringVar()
        self.z_pull_wt.set(str(self.cfg['RobotSettings']['z_pull_wt']))
        self.rew_zone_x = tk.StringVar()
        self.rew_zone_x.set(str(self.cfg['RobotSettings']['rew_zone_x']))
        self.rew_zone_y_min = tk.StringVar()
        self.rew_zone_y_min.set(str(self.cfg['RobotSettings']['rew_zone_y_min']))
        self.rew_zone_y_max = tk.StringVar()
        self.rew_zone_y_max.set(str(self.cfg['RobotSettings']['rew_zone_y_max']))
        self.rew_zone_z_min = tk.StringVar()
        self.rew_zone_z_min.set(str(self.cfg['RobotSettings']['rew_zone_z_min']))
        self.rew_zone_z_max = tk.StringVar()
        self.rew_zone_z_max.set(str(self.cfg['RobotSettings']['rew_zone_z_max']))
        self.calibration_file = tk.StringVar()
        self.calibration_file.set(str(self.cfg['RobotSettings']['calibration_file']))
        self.command_file = tk.StringVar()
        self.command_file.set(str(self.cfg['RobotSettings']['command_file']))
        self.command_source = tk.StringVar()
        self.command_source.set(self.cfg['RobotSettings']['command_source'])
        self.ygimbal_to_joint = tk.StringVar()
        self.ygimbal_to_joint.set(str(self.cfg['RobotSettings']['ygimbal_to_joint']))
        self.zgimbal_to_joint = tk.StringVar()
        self.zgimbal_to_joint.set(str(self.cfg['RobotSettings']['zgimbal_to_joint']))
        self.xgimbal_xoffset = tk.StringVar()
        self.xgimbal_xoffset.set(str(self.cfg['RobotSettings']['xgimbal_xoffset']))
        self.ygimbal_yoffset = tk.StringVar()
        self.ygimbal_yoffset.set(str(self.cfg['RobotSettings']['ygimbal_yoffset']))
        self.zgimbal_zoffset = tk.StringVar()
        self.zgimbal_zoffset.set(str(self.cfg['RobotSettings']['zgimbal_zoffset']))
        self.x_origin = tk.StringVar()
        self.x_origin.set(str(self.cfg['RobotSettings']['x_origin']))
        self.y_origin = tk.StringVar()
        self.y_origin.set(str(self.cfg['RobotSettings']['y_origin']))
        self.z_origin = tk.StringVar()
        self.z_origin.set(str(self.cfg['RobotSettings']['z_origin']))
        self.reach_dist_min = tk.StringVar()
        self.reach_dist_min.set(str(self.cfg['RobotSettings']['reach_dist_min']))
        self.reach_dist_max = tk.StringVar()
        self.reach_dist_max.set(str(self.cfg['RobotSettings']['reach_dist_max']))
        self.reach_angle_max = tk.StringVar()
        self.reach_angle_max.set(str(self.cfg['RobotSettings']['reach_angle_max']))
        #configure window
        self.configure_window()

    def on_quit(self):          
        self.cfg['RobotSettings']['alpha'] = float(self.alpha.get())
        self.cfg['RobotSettings']['tol'] = float(self.tol.get())
        self.cfg['RobotSettings']['period'] = float(self.period.get())
        self.cfg['RobotSettings']['off_dur'] = int(self.off_dur.get()) 
        self.cfg['RobotSettings']['num_tol'] = int(self.num_tol.get())
        self.cfg['RobotSettings']['x_push_wt'] = float(self.x_push_wt.get())
        self.cfg['RobotSettings']['x_pull_wt'] = float(self.x_pull_wt.get())
        self.cfg['RobotSettings']['y_push_wt'] = float(self.y_push_wt.get())
        self.cfg['RobotSettings']['y_pull_wt'] = float(self.y_pull_wt.get())
        self.cfg['RobotSettings']['z_push_wt'] = float(self.z_push_wt.get())
        self.cfg['RobotSettings']['z_pull_wt'] = float(self.z_pull_wt.get())
        self.cfg['RobotSettings']['rew_zone_x'] = int(self.rew_zone_x.get())
        self.cfg['RobotSettings']['rew_zone_y_min'] = int(self.rew_zone_y_min.get())
        self.cfg['RobotSettings']['rew_zone_y_max'] = int(self.rew_zone_y_max.get())
        self.cfg['RobotSettings']['rew_zone_z_min'] = int(self.rew_zone_z_min.get())
        self.cfg['RobotSettings']['rew_zone_z_max'] = int(self.rew_zone_z_max.get())
        self.cfg['RobotSettings']['calibration_file'] = self.calibration_file.get()
        self.cfg['RobotSettings']['command_file'] = self.command_file.get()
        self.cfg['RobotSettings']['command_source'] = self.command_source.get()        
        self.cfg['RobotSettings']['ygimbal_to_joint'] = int(self.ygimbal_to_joint.get())
        self.cfg['RobotSettings']['zgimbal_to_joint'] = int(self.zgimbal_to_joint.get())
        self.cfg['RobotSettings']['xgimbal_xoffset'] = int(self.xgimbal_xoffset.get())
        self.cfg['RobotSettings']['ygimbal_yoffset'] = int(self.ygimbal_yoffset.get())
        self.cfg['RobotSettings']['zgimbal_zoffset'] = int(self.zgimbal_zoffset.get())
        self.cfg['RobotSettings']['x_origin'] = int(self.x_origin.get())
        self.cfg['RobotSettings']['y_origin'] = int(self.y_origin.get())
        self.cfg['RobotSettings']['z_origin'] = int(self.z_origin.get())
        self.cfg['RobotSettings']['reach_dist_min'] = int(self.reach_dist_min.get())
        self.cfg['RobotSettings']['reach_dist_max'] = int(self.reach_dist_max.get())
        self.cfg['RobotSettings']['reach_angle_max'] = float(self.reach_angle_max.get())        
        config.save_tmp(self.cfg)
        self.destroy()

    def configure_window(self):
        tk.Label(self,text='Position Smoothing:', font='Arial 10 bold', bg='white',width=26,anchor='e').grid(row=1, column=0)   
        tk.Entry(self,textvariable=self.alpha,width=17).grid(row=1, column=1)
        tk.Label(self,text='Valve Period (usec):', font='Arial 10 bold', bg='white',width=26,anchor='e').grid(row=2, column=0)   
        tk.Entry(self,textvariable=self.period,width=17).grid(row=2, column=1)
        tk.Label(self,text='Off Duration (msec):', font='Arial 10 bold', bg='white',width=26,anchor='e').grid(row=3, column=0)   
        tk.Entry(self,textvariable=self.off_dur,width=17).grid(row=3, column=1)
        tk.Label(self,text='Converge Tolerance (bits):', font='Arial 10 bold', bg='white',width=26,anchor='e').grid(row=4, column=0)   
        tk.Entry(self,textvariable=self.tol,width=17).grid(row=4, column=1)
        tk.Label(self,text='# w/in Tolerance:', font='Arial 10 bold', bg='white',width=26,anchor='e').grid(row=5, column=0)   
        tk.Entry(self,textvariable=self.num_tol,width=17).grid(row=5, column=1)
        tk.Label(self,text='X Push Weight:', font='Arial 10 bold', bg='white',width=26,anchor='e').grid(row=6, column=0)   
        tk.Entry(self,textvariable=self.x_push_wt,width=17).grid(row=6, column=1)
        tk.Label(self,text='X Pull Weight:', font='Arial 10 bold', bg='white',width=26,anchor='e').grid(row=7, column=0)   
        tk.Entry(self,textvariable=self.x_pull_wt,width=17).grid(row=7, column=1)
        tk.Label(self,text='Y Push Weight:', font='Arial 10 bold', bg='white',width=26,anchor='e').grid(row=8, column=0)   
        tk.Entry(self,textvariable=self.y_push_wt,width=17).grid(row=8, column=1)
        tk.Label(self,text='Y Pull Weight:', font='Arial 10 bold', bg='white',width=26,anchor='e').grid(row=9, column=0)   
        tk.Entry(self,textvariable=self.y_pull_wt,width=17).grid(row=9, column=1)
        tk.Label(self,text='Z Push Weight:', font='Arial 10 bold', bg='white',width=26,anchor='e').grid(row=10, column=0)   
        tk.Entry(self,textvariable=self.z_push_wt,width=17).grid(row=10, column=1)
        tk.Label(self,text='Z Pull Weight:', font='Arial 10 bold', bg='white',width=26,anchor='e').grid(row=11, column=0)   
        tk.Entry(self,textvariable=self.z_pull_wt,width=17).grid(row=11, column=1)
        tk.Label(self,text='Reward Zone X Min (bits):', font='Arial 10 bold', bg='white',width=26,anchor='e').grid(row=12, column=0)   
        tk.Entry(self,textvariable=self.rew_zone_x,width=17).grid(row=12, column=1)
        tk.Label(self,text='Reward Zone Y Min (bits):', font='Arial 10 bold', bg='white',width=26,anchor='e').grid(row=13, column=0)   
        tk.Entry(self,textvariable=self.rew_zone_y_min,width=17).grid(row=13, column=1)
        tk.Label(self,text='Reward Zone Y Max (bits):', font='Arial 10 bold', bg='white',width=26,anchor='e').grid(row=14, column=0)   
        tk.Entry(self,textvariable=self.rew_zone_y_max,width=17).grid(row=14, column=1)
        tk.Label(self,text='Reward Zone Z Min (bits):', font='Arial 10 bold', bg='white',width=26,anchor='e').grid(row=15, column=0)   
        tk.Entry(self,textvariable=self.rew_zone_z_min,width=17).grid(row=15, column=1)
        tk.Label(self,text='Reward Zone Z Max (bits):', font='Arial 10 bold', bg='white',width=26,anchor='e').grid(row=16, column=0)   
        tk.Entry(self,textvariable=self.rew_zone_z_max,width=17).grid(row=16, column=1)
        tk.Button(self,text='Run Calibration',font='Arial 10 bold',width=14,command=self.run_calibration_callback).grid(row=1, column=5)
        tk.Label(self,text='Calibration File:', font='Arial 10 bold', bg='white',width=26,anchor='e').grid(row=2, column=4)
        tk.Label(self,textvariable=self.calibration_file, bg='white').grid(row=2, column=5)
        tk.Button(self,text='Browse', font='Arial 10 bold',width=14, command=self.calibration_browse_callback).grid(row=2, column=6)
        tk.Label(self,text='Command File:', font='Arial 10 bold', bg='white',width=26,anchor='e').grid(row=3, column=4)
        tk.Label(self,textvariable=self.command_file, bg='white').grid(row=3, column=5)
        tk.Button(self,text='Browse', font='Arial 10 bold',width=14, command=self.command_browse_callback).grid(row=3, column=6)
        tk.Label(self,text='Command Type:', font='Arial 10 bold', bg='white',width=26,anchor='e').grid(row=4, column=4)
        self.command_type_menu = tk.OptionMenu(self,self.command_source,
            'read_from_file',
            'sample_from_file',
            'parametric_sample'            
            )
        self.command_type_menu.configure(width=26)
        self.command_type_menu.grid(row=4, column=5)
        tk.Label(self,text='Min Reach Distance (mm):', font='Arial 10 bold', bg='white',width=26,anchor='e').grid(row=5, column=4)   
        tk.Entry(self,textvariable=self.reach_dist_min,width=17).grid(row=5, column=5)
        tk.Label(self,text='Max Reach Distance (mm):', font='Arial 10 bold', bg='white',width=26,anchor='e').grid(row=6, column=4)   
        tk.Entry(self,textvariable=self.reach_dist_max,width=17).grid(row=6, column=5)
        tk.Label(self,text='Max Reach Angle (rad):', font='Arial 10 bold', bg='white',width=26,anchor='e').grid(row=7, column=4)   
        tk.Entry(self,textvariable=self.reach_angle_max,width=17).grid(row=7, column=5)
        tk.Label(self,text='Y Gimbal to Joint (mm):', font='Arial 10 bold', bg='white',width=26,anchor='e').grid(row=8, column=4)   
        tk.Entry(self,textvariable=self.ygimbal_to_joint,width=17).grid(row=8, column=5)
        tk.Label(self,text='Z Gimbal to Joint (mm):', font='Arial 10 bold', bg='white',width=26,anchor='e').grid(row=9, column=4)   
        tk.Entry(self,textvariable=self.zgimbal_to_joint,width=17).grid(row=9, column=5)
        tk.Label(self,text='X Gimbal X Offset (mm):', font='Arial 10 bold', bg='white',width=26,anchor='e').grid(row=10, column=4)   
        tk.Entry(self,textvariable=self.xgimbal_xoffset,width=17).grid(row=10, column=5)
        tk.Label(self,text='Y Gimbal Y Offset (mm):', font='Arial 10 bold', bg='white',width=26,anchor='e').grid(row=11, column=4)   
        tk.Entry(self,textvariable=self.ygimbal_yoffset,width=17).grid(row=11, column=5)
        tk.Label(self,text='Z Gimbal Z Offset (mm):', font='Arial 10 bold', bg='white',width=26,anchor='e').grid(row=12, column=4)   
        tk.Entry(self,textvariable=self.zgimbal_zoffset,width=17).grid(row=12, column=5)
        tk.Label(self,text='X Origin (bits):', font='Arial 10 bold', bg='white',width=26,anchor='e').grid(row=13, column=4)   
        tk.Entry(self,textvariable=self.x_origin,width=17).grid(row=13, column=5)
        tk.Label(self,text='Y Origin (bits):', font='Arial 10 bold', bg='white',width=26,anchor='e').grid(row=14, column=4)   
        tk.Entry(self,textvariable=self.y_origin,width=17).grid(row=14, column=5)
        tk.Label(self,text='Z Origin (bits):', font='Arial 10 bold', bg='white',width=26,anchor='e').grid(row=15, column=4)   
        tk.Entry(self,textvariable=self.z_origin,width=17).grid(row=15, column=5)

    def run_calibration_callback(self):
        print('not implemented')

    def calibration_browse_callback(self):
        self.calibration_file.set(tkFileDialog.askopenfilename())
        self.cfg['RobotSettings']['calibration_file'] = self.calibration_file.get()                  

    def command_browse_callback(self):
        self.command_file.set(tkFileDialog.askopenfilename())
        self.cfg['RobotSettings']['command_file'] = self.command_file.get()