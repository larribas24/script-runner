#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script runner
=============
Main executable file. Launchs multithreading processes 
taken from a txt file. Place this file in the same directory.
@Luis Arribas - DXC.technology

"""

import subprocess
import threading

 
class MyThread(threading.Thread):
    def __init__(self, threadID, path):
        threading.Thread.__init__(self)
        self.path = path
        self.threadID = threadID

    def run(self):
        print("Starting " + self.path)
        subprocess.run(["python", self.path])

def prepare_tasks(tasks_path):
    tasks = []
    file_object = open(tasks_path, "r")
    lines = file_object.readlines()
    
    for line in lines:
        line = line.strip()
        tasks.append(line)
        
    return tasks    

def run():
    for t in range(len(tasks)):
        threads.append(MyThread(t, tasks[t]))
     
    for t in range(len(tasks)):
        threads[t].start()
        
    for t in range(len(tasks)):
        threads[t].join()
        print(f"Stopping {threads[t].path}..." )
    
    
    print("Exiting Main Thread. No startup Python scripts running")

if __name__ == '__main__':

    tasks_path = './run_on_start.txt'
    tasks = prepare_tasks(tasks_path)
    threads = []
    run()