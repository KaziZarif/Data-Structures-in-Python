# Data Structures in Python

This repository contains implementations of fundamental data structures in Python. Each folder corresponds to a self-contained module focused on a particular data structure.

## Project Structure

### Doubly Linked List
- Implementation of a **doubly linked list**, supporting insertion, deletion, and traversal in both directions.
- Includes node class with `prev` and `next` pointers.

### Singly Linked List
- Implementation of a **singly linked list** with basic list operations.
- Designed to be generic and supports common use cases like push, pop, and search.

### Priority Queue (Heap-based)
- Implements a **min-heap** based priority queue.
- Maintains the heap property using `up_heap` and `down_heap` operations.
- Efficient insert and extract-min in logarithmic time.

### Priority Queue (List-based)
- Implements a **list-based** min priority queue.
- Simpler structure
- Insertions are `O(1)` and removals (min extraction) are `O(n)`.

### Undirected Graph (Edge List)
- Implements an **undirected graph** using the **edge list** representation.
- Maintains a sequence of vertices and a sequence of edges.
- Each edge stores references to the two vertices it connects.
- Supports operations like:
  - Insert/remove vertex
  - Insert/remove edge
  - Query for opposite vertex

