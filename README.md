# Data Structures and Algorithms

This document provides a high-level overview of important data structures and algorithms, along with their definitions, common use cases, operations, and time complexities.

## 1. Arrays
**Definition**: An array is a fixed-size collection of elements stored in contiguous memory locations, allowing fast access to elements using an index.

### Sorting:
- **QuickSort**: Efficient sorting algorithm that uses divide-and-conquer. Average-case `O(n log n)`, Worst-case `O(n^2)` (when poorly pivoted).
- **MergeSort**: Stable sorting technique that divides the array and merges sorted subarrays. `O(n log n)`.

### Searching:
- **Binary Search**: Fast searching method that works on sorted arrays. `O(log n)`.

### Two Pointers:
- Optimized approach for array problems, using two pointers moving towards a condition. Often `O(n)`.

### Sliding Window:
- A technique for solving problems involving subarrays, maintaining a window and shifting it. Typically `O(n)`.

---

## 2. Linked Lists
**Definition**: A data structure consisting of nodes where each node points to the next node in sequence, allowing dynamic memory allocation.

### Traversal:
- Visiting each node in the list. `O(n)`.

### Insertion/Deletion:
- **At the beginning**: `O(1)` (constant time update).
- **At the end**: `O(n)` (without tail pointer, `O(1)` with tail pointer).
- **At a specific position**: `O(n)` (requires traversal).

### Reversal:
- Iterative: `O(n)`.
- Recursive: `O(n)` (plus `O(n)` stack space).

### Cycle Detection:
- **Floyd's Tortoise and Hare Algorithm**: Detects cycles using two pointers. `O(n)`.

---

## 3. Hash Tables (Hash Maps/Sets)
**Definition**: A data structure that maps keys to values using a hash function for fast retrieval.

### Key Operations:
- **Insertion/Deletion/Lookup**: Average `O(1)`, Worst-case `O(n)` (hash collisions).

### Collision Handling:
- **Chaining**: Stores multiple values in a single hash bucket. `O(1)` on average, `O(n)` worst-case.
- **Open Addressing**: Resolves collisions by probing for empty slots. `O(1)` on average, `O(n)` worst-case.

---

## 4. Trees (Binary Trees, Binary Search Trees, etc.)
**Definition**: A hierarchical data structure where nodes are connected in a parent-child relationship.

### Traversal:
- **Inorder, Preorder, Postorder**: Different ways to visit tree nodes. `O(n)`.

### Searching in BST:
- **Best/Average-case**: `O(log n)`.
- **Worst-case**: `O(n)` (unbalanced tree).

### Insertion/Deletion in BST:
- **Average-case**: `O(log n)`.
- **Worst-case**: `O(n)` (unbalanced BST).

---

## 5. Stacks
**Definition**: A Last In, First Out (LIFO) data structure where elements are added and removed from the top.

### Key Operations:
- **Push/Pop/Peek**: `O(1)`.

---

## 6. Queues
**Definition**: A First In, First Out (FIFO) data structure where elements are added at the rear and removed from the front.

### Key Operations:
- **Enqueue/Dequeue**: `O(1)`.

---

## 7. Heaps (Priority Queues)
**Definition**: A specialized tree-based structure used for priority-based operations.

### Key Operations:
- **Insertion**: `O(log n)`.
- **Deletion (Extract-Min/Max)**: `O(log n)`.
- **Building a Heap**: `O(n)`.

### Top K Elements:
- Using a heap: `O(n log k)`.

---

## 8. Graphs
**Definition**: A collection of nodes (vertices) connected by edges.

### Traversal:
- **Breadth-First Search (BFS)**: Visits nodes level by level. `O(V + E)`.
- **Depth-First Search (DFS)**: Explores as deep as possible before backtracking. `O(V + E)`.

### Shortest Path:
- **Dijkstra's Algorithm**: Finds shortest paths in weighted graphs. `O((V + E) log V)`.
- **Bellman-Ford Algorithm**: Handles negative weights. `O(VE)`.

### Cycle Detection:
- **DFS-based**: `O(V + E)`.
- **Union-Find**: `O(α(n))` (almost constant time).

---

## 9. Tries
**Definition**: A tree-like structure used for efficient storage and retrieval of strings.

### Key Operations:
- **Insertion/Searching**: `O(m)`, where `m` is the length of the key.

### Autocompletion:
- **Trie-based**: `O(m)`, where `m` is the prefix length.

---

## 10. Union-Find (Disjoint Set)
**Definition**: A data structure that tracks elements split into disjoint sets, often used in graphs.

### Key Operations:
- **Find/Union**: `O(α(n))`, nearly constant time with path compression.
- **Cycle Detection**: `O(α(n))`.

---

# General Algorithms/Techniques

## 1. Recursion
**Definition**: A technique where a function calls itself to solve subproblems.
- Example: Factorial `O(n)`, Fibonacci (naive `O(2^n)`, memoized `O(n)`).

## 2. Dynamic Programming (DP)
**Definition**: A technique to solve problems by breaking them into overlapping subproblems.
- **Top-down (Memoization)**: `O(n)`.
- **Bottom-up (Tabulation)**: `O(n)`.
- Example: Fibonacci `O(n)`, Knapsack `O(nW)`.

## 3. Greedy Algorithms
**Definition**: An approach where the locally optimal choice is made at each step.
- Example: Kruskal’s Algorithm (Minimum Spanning Tree): `O(E log E)`.
- Huffman Encoding: `O(n log n)`.

## 4. Backtracking
**Definition**: A trial-and-error method for exploring all possibilities and backtracking when necessary.
- Worst-case exponential `O(2^n)`.
- Example: N-Queens `O(N!)`, Sudoku Solver `O(9^n)`.

---

This document summarizes the key operations, definitions, use cases, and time complexities for various data structures and algorithms.

