# AVL-Trees

Compare the performance of an unbalanced Binary Search Tree vs. a self-balancing AVL Tree</font>

Use the `BinarySearchTree`, `TreeNode`, `AVLTree`, and `AVLTreeNode` classes as found in our [class notebook on this topic](http://www.pas.rochester.edu/~rsarkis/csc162/_static/notebooks/14-Binary%20Search%20Trees/Binary%20Search%20and%20AVL%20Trees.ipynb).

The worst-case performance of both those structures is listed below.

| operation | Binary Search Tree |    AVL Tree__  |
| --------- | ------------------ | -------------- | 
| put 	    | $O(n)$             | $O(log_2 n)$   |
| get 	    | $O(n)$             | $O(log_2 n)$   |
| in 	    | $O(n)$             | $O(log_2 n)$   |
| del 	    | $O(n)$             | $O(log_2 n)$   |


**Your task:** Do your best to test the run time complexity of these operations on these two types of trees. This means:

   * Concoting some set of data to input into the trees (perhaps my previous word examples)
   
   * Using timer objects
   
   * Plots
