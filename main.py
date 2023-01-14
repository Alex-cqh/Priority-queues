# Linked List Node
import random
import time

import matplotlib.pyplot as plt


class Node:
    def __init__(self, key=None, next=None):
        self.key = key
        self.next = next


# Transition Node
class TransNode:
    def __init__(self, key=None, index=None):
        self.key = key
        self.index = index


# Binary Tree Node
class BinaryTreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def get_parent(i):
    if i == 0:
        return None
    else:
        return (i - 1) // 2


def get_left_child(i):
    return 2 * i + 1


def get_right_child(i):
    return 2 * i + 2


# Linked List to Binary Tree
class Conversion:
    # storing head of linked list and root for the Binary Tree
    def __init__(self, key):
        self.head = None
        self.root = None

    def push(self, new_key):
        new_node = Node(new_key, None)
        new_node.next = self.head
        self.head = new_node

    def convertListToTree(self):
        # storing the parent nodes
        q = []
        # Linked List is None
        if self.head is None:
            self.root = None
            return
        self.root = BinaryTreeNode(self.head.key)
        q.append(self.root)
        self.head = self.head.next
        while self.head:
            parent = q.pop(0)
            left_child = None
            right_child = None
            left_child = BinaryTreeNode(self.head.key)
            q.append(left_child)
            self.head = self.head.next
            if self.head:
                right_child = BinaryTreeNode(self.head.key)
                q.append(right_child)
                self.head = self.head.next
            parent.left = left_child
            parent.right = right_child

    def inorderTraversal(self, root):
        if root:
            self.inorderTraversal(root.left)
            print(root.key, end=" ")
            self.inorderTraversal(root.right)


class MinPriorityQueue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = -1

    def insert(self, key):
        # create new_node
        new_node = Node(key, None)
        # MinPriorityQueue is None
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.size = self.size + 1
            return
        # MinPriorityQueue is not None
        self.tail.next = new_node
        self.tail = new_node
        self.size = self.size + 1
        cur = TransNode(key, self.size)
        while cur.index > 0:
            parent_index = (cur.index - 1) // 2
            List_index = 0
            Parent_Node = self.head
            # Find Parent Node
            while List_index < parent_index:
                Parent_Node = Parent_Node.next
                List_index += 1
            # Compartor
            if new_node.key < Parent_Node.key:
                new_node.key, Parent_Node.key = Parent_Node.key, new_node.key
            new_node = Parent_Node
            cur.key = Parent_Node.key
            cur.index = parent_index

    def delMin(self):
        # MinPriorityQueue is None
        if self.head is None:
            return None
        # MinPriorityQueue is not None
        min_key = self.head.key
        self.head.key = self.tail.key
        self.size = self.size - 1
        cur = self.head
        first_child = self.head
        tail=self.head
        child_index = 0
        queue_index = 0
        tail_index=0
        while tail_index<self.size:
            tail=tail.next
            tail_index=tail_index+1
        self.tail=tail
        self.tail.next=None
        # child node exist
        while 2 * child_index + 1 <= self.size:
            while queue_index < 2 * child_index + 1:
                queue_index = queue_index + 1
                first_child = first_child.next
            # two child
            if 2 * child_index + 2 <= self.size:
                if first_child.key < first_child.next.key:
                    min_child = first_child
                    child_index = 2 * child_index + 1
                else:
                    min_child = first_child.next
                    child_index = 2 * child_index + 2
            else:
                # one child
                min_child = first_child
                child_index = 2 * child_index + 1
            if cur.key > min_child.key:
                cur.key, min_child.key = min_child.key, cur.key
                cur = min_child
                first_child = min_child
            else:
                break
        return min_key


if __name__ == "__main__":
    MinQueue = MinPriorityQueue()
    # Time consuming
    insert_time = []
    delete_time = []
    # test numbers
    test_num = 100
    for i in range(test_num):
        # insert
        start = time.time()
        for i in range(1, 100):
            MinQueue.insert(random.randint(1, 100))
        end = time.time()
        insert_time.append(end - start)
        # delMin
        start = time.time()
        delete_ele=MinQueue.delMin()
        end = time.time()
        delete_time.append(end - start)

    # draw
    plt.plot(range(test_num), insert_time, label="insert")
    plt.plot(range(test_num), delete_time, label="delete")
    plt.xlabel("test times")
    plt.ylabel("time/s")
    plt.legend()
    plt.show()
