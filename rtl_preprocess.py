#!/usr/bin/env python
# coding: utf-8
#

import argparse

parser = argparse.ArgumentParser()
# parser.add_argument('file', type=argparse.FileType('r'))
parser.add_argument('--file'    , help='file name')
parser.add_argument('--larktext', help='lark text')
args = parser.parse_args()
filename =  args.file
# print(filename)
with open(filename, "r") as file:
  filetext = file.read()

state = "NORMAL"
define_list = []
import re
for l in filetext.split("\n"):
  # line = line.split(" ")
  line = re.split(" +", l)
  line = [x for x in line if x]
  if  (line == []):
    l = ""
  elif(state == "NORMAL"):
    if(line[0]=="`define"):
      define_list.append(line)
      l = ""
    elif(line[0]=="`ifdef"):
      def_name = [x[1] for x in define_list]
      if line[1] in def_name:
        state = "IF_TRUE"
      else:
        state = "IF_FALSE"
      l = "// " + state +" " + str(def_name)
  elif(state == "IF_TRUE"):
    if(line[0]=="`else"):
      state = "EL_FALSE"
      l = ""
    elif(line[0]=="`endif"):
      l = ""
      state = "NORMAL"
  elif(state == "IF_FALSE"):
    l = ""
    if(line[0]=="`else"):
      state = "EL_TRUE"
      pass
    elif(line[0]=="`endif"):
      state = "NORMAL"
  elif(state == "EL_FALSE"):
    l = ""
    if(line[0]=="`endif"):
      state = "NORMAL"
  elif(state == "EL_TRUE"):
    if(line[0]=="`endif"):
      state = "NORMAL"
      l = ""
    
  print(l)

# print(define_list)
