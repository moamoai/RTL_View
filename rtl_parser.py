#!/usr/bin/env python
# coding: utf-8
#

from lark import Lark
import argparse

parser = argparse.ArgumentParser()
# parser.add_argument('file', type=argparse.FileType('r'))
parser.add_argument('--file'    , help='file name')
parser.add_argument('--larktext', help='lark text')
args = parser.parse_args()
filename =  args.file

larktext =  args.larktext
with open(filename, "r") as file:
  filetext = file.read()
with open(larktext, "r") as file:
  larktext = file.read()

l = Lark(larktext)

#print( l.parse("Hello, World!") )
tree = l.parse(filetext)
print(tree.pretty())


from lark import Transformer
input_list  = []
output_list = []

class MyTransformer(Transformer):
    def start(self, tmp):
      pass
    def input(self, tmp):
      input_list.append(tmp)
    def output(self, tmp):
      output_list.append(tmp)
#      print(tmp)
#        return k, v

MyTransformer().transform(tree)

print(input_list)
print(output_list)

# class TreeToJson(Transformer):
#     def string(self, (s,)):
#         return s[1:-1]
#     def number(self, (n,)):
#         return float(n)
# 
#     list = list
#     pair = tuple
#     dict = dict
# 
#     null = lambda self, _: None
#     true = lambda self, _: True
#     false = lambda self, _: False
