#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 17:36:37 2018

@author: kefei
"""

class TreeNode:
    def __init__(self, key, val, left=None, right=None, parent=None):
        self.key = key
        self.payload = val
        self.left_child = left
        self.right_child = right
        self.parent = parent
        
    def has_left_child(self):
        return self.left_child
    
    def has_right_child(self):
        return self.right_child
    
    def is_left_child(self):
        return self.parent and self.parent.left_child == self
    
    def is_right_child(self):
        return self.parent and self.parent.right_child == self

    def is_root(self):
        return not self.parent
    
    def is_leaf(self):
        return not (self.right_child or self.left_child)
    
    def has_any_children(self):
        return self.right_child or self.left_child
    
    def has_both_children(self):
        return self.right_child and self.left_child
        
    def replace_node_data(self, key, value, lc, rc):
        self.key = key
        self.payload = value
        self.left_child = lc
        self.right_child = rc
        
        if self.has_left_child():
            self.left_child.parent = self
            
        if self.has_right_child():
            self.right_child.parent = self
            
    def __iter__(self):
        # inorder traversal of (sub-)tree
        # left children, root (self), right children
        if self:
            if self.has_left_child():
                for elem in self.left_child:
                    yield elem
                    
            yield self.key
            
            if self.has_right_child():
                for elem in self.right_child:
                    yield elem
                    
    def splice_out(self):
        if self.is_leaf():
            if self.is_left_child():
                self.parent.left_child = None
            else:
                self.parent_right_child = None
        elif self.has_any_children():
            
            if self.has_left_child():
                if self.is_left_child():
                    self.parent.left_child = self.left_child
                else:
                    self.parent_right_child = self.left_child
                    
                self.left_child.parent = self.parent
            else:
                if self.is_left_child():
                    self.parent.left_child = self.right_child
                else:
                    self.parent.right_child = self.right_child
                    
                self.right_child.parent = self.parent
                
                
    def find_successor(self):
        succ = None
        if self.has_right_child():
            succ = self.right_child.find_min()
        else:
            if self.parent:
                if self.is_left_child():
                    succ = self.parent
                else:
                    self.parent.right_child = None
                    succ = self.parent.find_successor()
                    self.parent.right_child = self
                    
        return succ
    
    def find_min(self):
        current = self
        
        while current.has_left_child():
            current = current.left_child
            
        return current
    
class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0
        
    def length(self):
        return self.size
    
    def __len__(self):
        return self.length()
    
    def __iter__(self):
        return self.root.__iter__()
    
    def put(self, key, val):
        if self.root:
            self.__put(key, val, self.root)
        else:
            self.root = TreeNode(key, val)
            
        self.size += 1
        
    def __put(self, key, val, current_node):
        #print("Called from BinarySearchTree class")
        if key < current_node.key:        
            if current_node.has_left_child():
                self.__put(key, val, current_node.left_child)
            else:
                current_node.left_child = TreeNode(key, val, parent=current_node)  # base case 
        else: # key is >= than current_node.key
            if current_node.has_right_child():
                self.__put(key, val, current_node.right_child)
            else:
                current_node.right_child = TreeNode(key, val, parent=current_node)  # base case
                
    def __setitem__(self, k, v):
        self.put(k, v)
        
    def get(self, key):
        if self.root:
            res = self.__get(key, self.root)
            if res:
                return res.payload
            else:
                return None
        else:
            return None
        
    def __get(self, key, current_node):
        if not current_node:
            return None
        elif current_node.key == key:
            return current_node
        elif key < current_node.key:
            return self.__get(key, current_node.left_child)
        else:
            return self.__get(key, current_node.right_child)
        
    def __getitem__(self, key):
        return self.get(key)
    
    
    def __contains__(self, key):
        if self.__get(key, self.root):
            return True
        else:
            return False
        
        #return bool(self.__get(key, self.root))
        #return True if self.__get(key, self.root) else False
        
    def delete(self, key):
        if self.size > 1:
            node_to_remove = self.__get(key, self.root)
            if node_to_remove:
                self.remove(node_to_remove)  # TODO: 'remove' needs to be defined!
                self.size -= 1
            else:
                raise KeyError('Key not in tree')
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size -=1
        else:
            raise KeyError('Key not in tree')
            
    def __delitem__(self, key):
        self.delete(key)
        
    def splice_out(self):
        if self.is_leaf():
            if self.is_left_child():
                self.parent.left_child = None
            else:
                self.parent_right_child = None
        elif self.has_any_children():
            
            if self.has_left_child():
                if self.is_left_child():
                    self.parent.left_child = self.left_child
                else:
                    self.parent_right_child = self.left_child
                    
                self.left_child.parent = self.parent
            else:
                if self.is_left_child():
                    self.parent.left_child = self.right_child
                else:
                    self.parent.right_child = self.right_child
                    
                self.right_child.parent = self.parent
                
                
    def find_successor(self):
        succ = None
        if self.has_right_child():
            succ = self.right_child.find_min()
        else:
            if self.parent:
                if self.is_left_child():
                    succ = self.parent
                else:
                    self.parent.right_child = None
                    succ = self.parent.find_successor()
                    self.parent.right_child = self
                    
        return succ
    
    def find_min(self):
        current = self
        
        while current.has_left_child():
            current = current.left_child
            
        return current
    
    
    def remove(self, current_node):
        if current_node.is_leaf():  # leaf
            if current_node == current_node.parent.left_child:
                current_node.parent.left_child = None
            else:
                current_node.parent.right_child = None
        elif current_node.has_both_children():  # interior
            succ = current_node.find_successor()
            succ.splice_out()
            current_node.key = succ.key
            current_node.payload = succ.payload

        else:  # this node has one child
            if current_node.has_left_child():
                if current_node.is_left_child():
                    current_node.left_child.parent = current_node.parent
                    current_node.parent.left_child = current_node.left_child
                elif current_node.is_right_child():
                    current_node.left_child.parent = current_node.parent
                    current_node.parent.right_child = current_node.left_child
                else:
                    current_node.replace_node_data(current_node.left_child.key,
                                                   current_node.left_child.payload,
                                                   current_node.left_child.left_child,
                                                   current_node.left_child.right_child)
            else:
                if current_node.is_left_child():
                    current_node.right_child.parent = current_node.parent
                    current_node.parent.left_child = current_node.right_child
                elif current_node.is_right_child():
                    current_node.right_child.parent = current_node.parent
                    current_node.parent.right_child = current_node.right_child
                else:
                    current_node.replace_node_data(current_node.right_child.key,
                                                   current_node.right_child.payload,
                                                   current_node.right_child.left_child,
                                                   current_node.right_child.right_child)
                    
# binary search tree time
import matplotlib.pyplot as plt
import requests
import random
import timeit
import time

req = requests.get("http://t2.hhg.to/ospd.txt")
words = req.text.split("\n")
words_tree_bin = []
total_time_put = []
total_time_get = []
total_time_in = []
total_time_del = []
    
words_list_1 = random.sample(words, 6000) + ['eye']
words_list_2 = random.sample(words, 8000) + ['eye']
words_list_3 = random.sample(words, 10000) + ['eye']
words_list_4 = random.sample(words, 12000) + ['eye']
words_list_5 = random.sample(words, 14000) + ['eye']
words_list_6 = random.sample(words, 16000) + ['eye']
words_list_7 = random.sample(words, 18000) + ['eye']
words_list_8 = random.sample(words, 20000) + ['eye']
words_list_9 = random.sample(words, 22000) + ['eye']
words_list_10 = random.sample(words, 24000) + ['eye']
words_list_11 = random.sample(words, 26000) + ['eye']
words_list_12 = random.sample(words, 28000) + ['eye']


words_list = [words_list_1, words_list_2, words_list_3, words_list_4, words_list_5,
             words_list_6, words_list_7, words_list_8, words_list_9, words_list_10,
             words_list_11, words_list_12]

for lst in words_list:
    words_tree = BinarySearchTree()
    
    start = time.time()
    for i, word in enumerate(lst):
        #t_put = timeit.Timer("words_tree.put(key, val)", globals = {"words_tree": words_tree, "key":word, "val":i})
        #tmp_put = t_put.timeit(1)
        #total_put += tmp_put
        words_tree.put(word, i)
    end = time.time()
    
    total_put = end - start
    total_time_put.append(total_put)
    words_tree_bin.append(words_tree)

for tree in words_tree_bin:
    words_tree = tree
    t_get = timeit.Timer("words_tree.get(key)", globals = {"words_tree": words_tree, "key": 'eye'})  
    #words_tree = tree
    #start = time.time()
    #words_tree.get('eye')
    #end = time.time()
    #total_get = end-start
    total_get = t_get.timeit(1)
    total_time_get.append(total_get)
    
    words_tree = tree
    t_in = timeit.Timer("key in words_tree", globals = {"words_tree": words_tree, "key": 'eye'})
    total_in = t_in.timeit(1)
    #words_tree = tree
    #start = time.time()
    #'eye' in words_tree
    #end = time.time()
    #total_in = end-start
    total_time_in.append(total_in)
    
    words_tree = tree
    t_del = timeit.Timer("del words_tree[key]", globals = {"words_tree": words_tree, "key": 'eye'})
    total_del = t_in.timeit(1)
    #words_tree = tree
    #start = time.time()
    #del words_tree['eye']
    #end = time.time()
    #total_del = end-start
    total_time_del.append(total_del)
    
print(total_time_put)
print(total_time_get)
print(total_time_in)   
print(total_time_del)

sizes = [len(lst) for lst in words_list]

fig, ax = plt.subplots()
plt.ylabel("Running Time (ms)")
plt.xlabel("Input Size ($N$)")
plt.plot(sizes, total_time_put, 'x', label='put')
plt.plot(sizes, total_time_get, 'D', label='get')
plt.plot(sizes, total_time_in, '-', label='in')
plt.plot(sizes, total_time_del, '.', label='del', color='y')

legend = plt.legend(loc='center right', fontsize='small')
plt.show()