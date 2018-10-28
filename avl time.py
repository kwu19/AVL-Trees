#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 17:37:47 2018

@author: kefei
"""

class AVLTreeNode(TreeNode):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.balance_factor = 0 # For AVL Tree

class AVLTree(BinarySearchTree):
    def __init__(self):
        super().__init__() 
    
    def put(self, key, val):
        if self.root:
            self.__put(key, val, self.root)
        else:
            self.root = AVLTreeNode(key, val)
            
        self.size += 1
        
    def __put(self, key, val, current_node):
        if key < current_node.key:
            if current_node.has_left_child():
                self.__put(key,val,current_node.left_child)
            else:
                current_node.left_child = AVLTreeNode(key,val,parent=current_node)
                self.update_balance(current_node.left_child)
        else:
            if current_node.has_right_child():
                self.__put(key,val,current_node.right_child)
            else:
                current_node.right_child = AVLTreeNode(key,val,parent=current_node)
                self.update_balance(current_node.right_child)                

    def update_balance(self, node):
        if node.balance_factor > 1 or node.balance_factor < -1:
            self.rebalance(node)
            return
        
        if node.parent != None:
            if node.is_left_child():
                node.parent.balance_factor += 1
            elif node.is_right_child():
                node.parent.balance_factor -= 1

            if node.parent.balance_factor != 0:
                self.update_balance(node.parent)

    def rebalance(self, node):
        if node.balance_factor < 0:
            if node.right_child.balance_factor > 0:
                # Do an LR Rotation
                self.rotate_right(node.right_child)
                self.rotate_left(node)
            else:
                # single left
                self.rotate_left(node)
        elif node.balance_factor > 0:
            if node.left_child.balance_factor < 0:
                # Do an RL Rotation
                self.rotate_left(node.left_child)
                self.rotate_right(node)
            else:
                # single right
                self.rotate_right(node)

    def rotate_left(self,rot_root):
        new_root = rot_root.right_child
        rot_root.right_child = new_root.left_child
        
        if new_root.left_child != None:
            new_root.left_child.parent = rot_root
            
        new_root.parent = rot_root.parent
        
        if rot_root.is_root():
            self.root = new_root
        else:
            if rot_root.is_left_child():
                rot_root.parent.left_child = new_root
            else:
                rot_root.parent.right_child = new_root

        new_root.left_child = rot_root
        rot_root.parent = new_root
        rot_root.balance_factor = rot_root.balance_factor + 1 - min(new_root.balance_factor, 0)
        new_root.balance_factor = new_root.balance_factor + 1 + max(rot_root.balance_factor, 0)


    def rotate_right(self,rot_root):
        new_root = rot_root.left_child
        rot_root.left_child = new_root.right_child
        if new_root.right_child != None:
            new_root.right_child.parent = rot_root
        new_root.parent = rot_root.parent
        if rot_root.is_root():
            self.root = new_root
        else:
            if rot_root.is_right_child():
                rot_root.parent.right_child = new_root
            else:
                rot_root.parent.left_child = new_root
        new_root.right_child = rot_root
        rot_root.parent = new_root
        rot_root.balance_factor = rot_root.balance_factor - 1 - max(new_root.balance_factor, 0)
        new_root.balance_factor = new_root.balance_factor - 1 + min(rot_root.balance_factor, 0)
        
# avl tree time
import matplotlib.pyplot as plt
import requests
import random
import timeit
import time

req = requests.get("http://t2.hhg.to/ospd.txt")
words = req.text.split("\n")
words_tree_avl = []
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
    words_tree = AVLTree()
    
    start = time.time()
    for i, word in enumerate(lst):
        #t_put = timeit.Timer("words_tree.put(key, val)", globals = {"words_tree": words_tree, "key":word, "val":i})
        #tmp_put = t_put.timeit(1)
        #total_put += tmp_put
        words_tree.put(word, i)
    end = time.time()
    
    total_put = end - start
    total_time_put.append(total_put)
    words_tree_avl.append(words_tree)

for tree in words_tree_avl:
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