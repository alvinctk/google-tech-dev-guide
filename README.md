# Preparation for technical Interview

## Introduction 
Interview study to reinforces basic software engineering skills.

## Study Plan
- [Average googler four weeks study plan](https://www.linkedin.com/pulse/average-googler-four-weeks-study-plan-milad-naseri/?trk=v-feed)
- [Patterns For Coding Interview](./Plan/Patterns_For_Coding_Interview.md)
- [Patterns For Dynamic Programming](./Plan/Patterns_For_Dynamic_Programming.md)
- [Analysis for different sorting techniques](./Plan/Analysis_of_Sorting.md)

## Practice Your Code
- [Project Euler](https://projecteuler.net)
- [Topcoder](https://www.topcoder.com)
- [HackerRank](https://www.hackerrank.com)
- [LeetCode](https://leetcode.com)
- [Practice problems - Google Focus by Geeks for Geeks](https://practice.geeksforgeeks.org/explore/?company%5B%5D=Google&page=1&sortBy=accuracy)
- [Practice on a google doc](https://www.quora.com/What-are-some-tips-for-practicing-coding-on-Google-docs-for-a-phone-screen)

## General Interview Preparation 
- [Puzzles](https://www.geeksforgeeks.org/category/puzzles/)
- [Geeks for Geeks](https://www.geeksforgeeks.org)

## Style Guide
- [Google Style Guide](https://google.github.io/styleguide/)
- [Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)

## Tutorials
- [Hacker Earth Practice](https://www.hackerearth.com/practice/)
- [Python Quick Tutorials](https://www.techbeamers.com)
- [Hacker Earth - Bit Manipulation](https://www.hackerearth.com/practice/notes/bit-manipulation/)

## Interview Resources
- [Google Tech Dev Guide](https://techdevguide.withgoogle.com/)
- [Geeks for Geeks - Company preparation](https://www.geeksforgeeks.org/company-preparation/)
- [Geeks for Geeks - Google interview preparation](https://www.geeksforgeeks.org/google-interview-preparation/)
- [50 questions by Byte-Byte](https://www.byte-by-byte.com/wp-content/uploads/2019/01/50-Coding-Interview-Questions.pdf)
- [500 questions by techiedelight](https://www.techiedelight.com) or [via quora](https://techiedelight.quora.com/500-Data-Structures-and-Algorithms-interview-questions-and-their-solutions?share=1&utm_medium=email&utm_source=hackernewsletter&utm_term=code)
- [Top 10 algorithms in interview questions by Geeks for Geeks](https://www.geeksforgeeks.org/top-10-algorithms-in-interview-questions/) 
- [Big Oh Cheatsheet](http://bigocheatsheet.com)

## Lecture Videos 
- [MIT 6.006 Introduction to Algorithms, Fall 2011](https://www.youtube.com/playlist?list=PLUl4u3cNGP61Oq3tWYp6V_F-5jb5L2iHb)
    - To Do: watch the dynamic programming videos 


## Textbook Resources
- [Online text: Algorithms by Jeff Erickson](http://jeffe.cs.illinois.edu/teaching/algorithms/)
- [Online text: Introduction to Programming in Python](https://introcs.cs.princeton.edu/python/home/)
- [Online text: Algorithms, 4th Edition by Robert Sedgewick and Kevin Wayne](https://algs4.cs.princeton.edu/home/)
- Introduction to Algorithms, Third Edition by Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, Clifford Stein.
- The Algorithm Design Manual by Second Edition by Steven S. Skiena.
- Programming Pearls, Second Edition by Jon Bentley
- Data Structures and Algorithm Analysis in Java, Third Edition by Mark Allen Weiss.
- Data Structures and Algorithms with Python, Springer Press, by Kent D. Lee and Steve Hubbard
- Python Algorithms - Mastering Basic Algorithms in the Python Language, Second Edition by Magnus Lie Hetland
## Data structures

<details>
<summary> Binary Tree </summary>

- [Binary Tree](./Data_Structures/binary_tree.py)
- [AVL Tree notes](./Data_Structures/avl_tree.md)
- [AVL Tree code](./Data_Structures/avl_tree.py)

</details>

<details>
<summary>Stack</summary>

- [Linked listed implementation of FILO stack](./Data_Structures/stack_ll.py)
- [List (or array) implementation of FILO stack](./Data_Structures/stack_array.py)

</details>

<details>
<summary>Queue</summary>

- [Linked listed implementation of FIFO queue](./Data_Structures/queue_ll.py)
- [List (or array) implementation of FIFO queue](./Data_Structures/queue_array.py)

</details>

<details>
<summary>Heap</summary>

- Binary Heap
    - n = len(array)
    - last parent = ((n - 1) - 1)//2
    - parent index given i: parent = (i-1)//2
    - index of left child = 2 * parent + 1 
    - index of right child = 2 * parent + 2
    - where 0 <= i < n

```python3
from typing import List

def swap_min_value(array: List, parent, index):
    n = len(array)
    if index < n and array[parent] > array[index]:
        array[parent], array[index] = array[index], array[parent]
        
def min_heapify(array: List):
    
    n = len(array)
    last = n - 1

    # Last parent index
    parent = (last - 1) // 2

    while parent > 0:

        left, right = 2 * parent + 1, 2 * parent + 2
        
        swap_min_value(array, parent, left)
        swap_min_value(array, parent, right)
        
        parent -= 1
 ```

</details>



## Algorithms

### Mergesort
- [mergesort](./Sorting/mergesort/mergesort.py)


### Quicksort
- [pivot using midpoint value](./Sorting/quicksort/quicksort.py)

- [pivot using first value](./70_question/sorting/quick_sort.py)


### Heapsort 
- [Heapsort using binary heap](./70_question/sorting/heap_sort.py)

- To sort elements in ascending order:
	```
	start i = 0
	while i less than n-1
	    build max heap from i=0 to n-1-i
	    swap 0 and n-1-i element in order to put the max element at n-1-i index
	```

- To sort elements in descending order:
	```
	start i = 0
	while i less than n-1
	    build min heap from i=0 to n-1-i
	    swap 0 and n-1-i element in order to put the min element at n-1-i index
	```

## **Google Tech Dev Guide**
1. [Find the find longest word in dictionary that is a subsequence of a given string](./Foundations_of_Programming/1_find_longest_word_in_dictionary_that_is_a_subsequence_of_a_given_string)

2. [Find the max span of a given list](./Foundations_of_Programming/2_max_span/maxSpan.py)

3. [Remove all occurance of a pattern in a given string](./Foundations_of_Programming/3_without_string/withoutString.py)

4. [Sum numbers in a given string](./Foundations_of_Programming/4_sum_numbers/sumNumbers.py)

5. [Find a balance sum in an given list](./Foundations_of_Programming/5_can_balance/canBalance.py)

6. [Hangman game](./Foundations_of_Programming/6_hangman/hangman.py)

## LeetCode

### Sliding window
| Problem      | Difficulty     | Solution      | Test | Time Complexity | Space Complexity
| :---:        |     :---:      |  :---:        | :---:|  :---:          |  :---:
| [Maximum sliding window](./leetcode/max_sliding_window.py) |  || | 


## 70 Questions

### Array
| Problem      | Difficulty     | Solution      | Test | Time Complexity | Space Complexity
| :---:        |     :---:      |  :---:        | :---:|  :---:          |  :---:
| [Two number sums](./70_question/array/two_number_sum_problem.md) | Easy |[.py](./70_question/array/two_number_sum/two_number_sum.py) | |O(n)|O(n)| 
| [Three number sums](./70_question/array/three_number_sum_problem.md) | Medium| [.py](./70_question/array/three_number_sum/three_number_sum.py)||O(n^2)|O(n)|


### LinkedList
| Problem      | Difficulty     | Solution      | Test | Time Complexity | Space Complexity
| :---:        |     :---:      |  :---:        | :---:|  :---:          |  :---:
| Construction of a double linked list| Easy |[.py](./70_question/linked_list/double_linked_list.py) |||| 
| Remove Kth Node from End| Medium| [.py](./70_question/linked_list/delete_k_th_end_elements_from_linked_list.py)| |O(n)|O(1)|

### String
| Problem      | Difficulty     | Solution      | Test | Time Complexity | Space Complexity
| :---:        |     :---:      |  :---:        | :---:|  :---:          |  :---:
| Caesar Cipher| Easy |[.py](./70_question/string/caesar_cipher.py) |[.py](./70_question/string/caesar_cipher_test.py)|O(n)|O(1)| 
| Largest palindrome substring| Medium |[.py](./70_question/string/largest_palindrome_substring.py) |[.py](./70_question/string/largest_palindrome_substring_test.py)|O(n^2)|O(1)| 

### Searching
| Problem      | Difficulty     | Solution      | Test | Time Complexity | Space Complexity
| :---:        |     :---:      |  :---:        | :---:|  :---:          |  :---:
| Largest three numbers| Easy |[.py](./70_question/searching/largest_three_numbers.py) |[.py](./70_question/searching/largest_three_numbers_test.py)|O(n)|O(1)| 
| Binary search value| Easy | [.py](./70_question/searching/binary_search.py)| [.py](./70_question/searching/binary_search_test.py) |O(log n)|O(1)|

### Searching
| Problem      | Difficulty     | Solution      | Test | Time Complexity | Space Complexity
| :---:        |     :---:      |  :---:        | :---:|  :---:          |  :---:
| Bubble Sort| Easy |[.py](./70_question/sorting/bubble_sort.py) |[.py](./70_question/sorting/bubble_sort_test.py)|O(n^2)|O(1)| 
| Insertion Sort| Easy |[.py](./70_question/sorting/insertion_sort.py) |[.py](./70_question/sorting/insertion_sort_test.py)|O(n^2)|O(1)| 
| Selection Sort| Easy |[.py](./70_question/sorting/selection_sort.py) |[.py](./70_question/sorting/selection_sort_test.py)|O(n^2)|O(1)| 

## Hackerrank

[String validators](./hackerrank/string_validators.py)

## Stackoverflow and other articles

[Python: understanding slice notation](https://stackoverflow.com/questions/509211/understanding-slice-notation)

[Python: list vs tuple, when to use each](https://stackoverflow.com/questions/1708510/python-list-vs-tuple-when-to-use-each)

[Python: What is the difference between sorted(list) and list.sort()](https://stackoverflow.com/questions/22442378/what-is-the-difference-between-sortedlist-vs-list-sort)

[Python: max and min for integers](https://stackoverflow.com/questions/7604966/maximum-and-minimum-values-for-ints)

[Python: min(1, None)](https://stackoverflow.com/questions/6254871/python-minnone-x)

[Python: removing from a list](https://stackoverflow.com/questions/4426663/how-to-remove-the-first-item-from-a-list)

[Python: Deleting element from a dictionary](https://stackoverflow.com/questions/5844672/delete-an-element-from-a-dictionary)

[Python: Checking for integer overflow](https://stackoverflow.com/questions/45528637/checking-integer-overflow-in-python)

### Complexity

[Merge sort time and space complexity](https://stackoverflow.com/questions/10342890/merge-sort-time-and-space-complexity)


### LeetCode Articles

- [Leetcode optimize three sums](https://stackoverflow.com/questions/46410814/optimizing-solution-to-three-sum)
- [Implement stack using two queues](https://stackoverflow.com/questions/688276/implement-stack-using-two-queues)

### Deep copy vs shallow copy 

- [Geeks for geeks: copy - shallow vs deep](https://www.geeksforgeeks.org/copy-python-deep-copy-shallow-copy/)

### Typing Annotations
- [Python: Using Python's Type Annotations](https://dev.to/dstarner/using-pythons-type-annotations-4cfe)

- [Python Documentation: Typing](https://docs.python.org/3/library/typing.html)
