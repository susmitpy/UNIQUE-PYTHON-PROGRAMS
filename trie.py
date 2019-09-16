#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 20:16:35 2019

@author: susmit
"""

class Node:
    def __init__(self,data,last_node=False):
        self.data = data
        self.last_node = last_node
        self.children = []
        
    def no_of_children(self):
        return len(self.children)
    

class Trie:
    def __init__(self):
        self.root = Node(1)
        self.no_of_last_nodes = 0
        
    def insert_word(self,word):
        pn = self.root # parent node
        l = len(word)
        
        for word_index, word_char in enumerate(word):
            char_in_tree = False
           # print("char to be inserted: ", word_char)
           # print("parent node data: ",pn.data)
            for child_node in pn.children:
              #  print("data of node beign checked: ", child_node.data)
                if child_node.data == word_char:
                    pn = child_node
                   # print("Changed parent node data: ",pn.data)
                    char_in_tree = True
                    break
            if char_in_tree:
                continue
            node = Node(word_char)
            if word_index == l-1:
               # print("Char is the last char in word")
                node.last_node = True
                self.no_of_last_nodes += 1
                pn.children.append(node)
               # print("data of children of parent node: ",[i.data for i in pn.children])
                break
           # print("Char is not the last char in word")
            pn.children.append(node)
           # print("data of children of parent node: ",[i.data for i in pn.children])
            pn = node
           # print("Changed parent node data: ",pn.data)
      #  print("Word inserted\n")
    def search_word(self,word):
        cn = self.root
        for c in word:
           # print(f"c: {c}")
            for child_node in cn.children:

# =============================================================================
#                 print(f"child node data: {child_node.data}")
#                 print(f"data of children of cn: {[i.data for i in cn.children]}")
# =============================================================================

                if child_node.data == c:
                    cn = child_node
                    break
        if cn == self.root:
            return False
        if cn.data[-1] == word[-1] and cn.last_node:
            return True
        return False
    
    def no_of_words(self):
        return self.no_of_last_nodes
    
words = ["amit","amount","amogh","car","cat","catwalk","carpenter","susmit"]
t = Trie()

for w in words:
    t.insert_word(w)
    
    
for w in words + ["carpen","amo","tommy"]:
    print(f"{w}: {t.search_word(w)}")

    