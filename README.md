# Data Structures and Algorithms

This document provides a high-level overview of important data structures and algorithms, along with their common use cases and operations.

## 1. Arrays
### Sorting:
- **QuickSort**: Efficient average-case time complexity `O(nlog n)`.
- **MergeSort**: Stable sort, useful when order matters `O(nlog n)`.

### Searching:
- **Binary Search**: Fast search in sorted arrays `O(log n)`.

### Two Pointers:
- In-place manipulation, often for sorted arrays (e.g., removing duplicates).

### Sliding Window:
- Useful for subarray problems, finding maximum/minimum within a window.

---

## 2. Linked Lists
### Traversal:
- Iterate through the list and understand the node structure.

### Insertion/Deletion:
- At the beginning, end, or at a specific position.

### Reversal:
- In-place reversal using recursive and iterative approaches.

### Cycle Detection:
- **Floyd's Tortoise and Hare algorithm**.

---

## 3. Hash Tables (Hash Maps/Sets)
### Key Operations:
- **Insertion/Deletion/Lookup**: Understand the basic operations.
- **Collision Handling**: Learn about methods like chaining and open addressing.
- **Hash Functions**: Know how hash functions work.

---

## 4. Trees (Binary Trees, Binary Search Trees, etc.)
### Traversal:
- **Inorder, Preorder, Postorder** (both recursive and iterative).

### Searching:
- **BST Search**: Find a node with a given value efficiently.

---

## 5. Stacks
### Key Operations:
- **Push/Pop/Peek**: Understand basic operations.

---

## 6. Queues
### Key Operations:
- **Enqueue/Dequeue**: Understand how queues work.

---

## 7. Heaps (Priority Queues)
### Key Operations:
- **Insertion/Deletion**: Understand how to insert and remove elements.
- **Building a Heap**: Learn heap construction.

### Top K Elements:
- Use heaps to find the `k` largest/smallest elements.

---

## 8. Graphs
### Traversal:
- **Breadth-First Search (BFS)**
- **Depth-First Search (DFS)**

### Shortest Path:
- **Dijkstra's Algorithm**: Find the shortest path in weighted graphs.

### Cycle Detection:
- Use **DFS** to detect cycles.

---

## 9. Tries
### Key Operations:
- **Insertion/Searching**: For words/prefixes in a dictionary.

### Autocompletion:
- Use a trie to implement word suggestions.

---

## 10. Union-Find (Disjoint Set)
### Key Operations:
- **Find/Union**: Efficiently manage connected components.
- **Cycle Detection**: Detect cycles in undirected graphs using Union-Find.

---

# General Algorithms/Techniques

## 1. Recursion
- Define problems in terms of themselves.
- Example problems: Factorial calculation, tree traversals, depth-first search.

## 2. Dynamic Programming (DP)
- Break problems into overlapping subproblems and store results to avoid recomputation.
- Example problems: Fibonacci sequence, Knapsack problem, Longest Common Subsequence.

## 3. Greedy Algorithms
- Make locally optimal choices in the hope of finding a global optimum.
- Example implementation: Kruskal's algorithm for minimum spanning trees.

## 4. Backtracking
- Incrementally build solutions, exploring all possible paths, and backtrack when necessary.
- Example problems: Sudoku solver, N-Queens problem, generating permutations.
