#!/usr/bin/env python3
import subprocess
import base64
import os
from subprocess import PIPE as spipe
import argparse
def _has_command(comm):
    if not type(comm) in (list,tuple):comm=(comm)
    try:
        subprocess.run(comm,stdout=spipe,stderr=spipe)
        return True
    except:return False
def has_tmux(path=None):return _has_command(("tmux","--help") if path is None else (path,"--help"))

def main():
    #to be continued
    aparser=argparse.ArgumentParser()
