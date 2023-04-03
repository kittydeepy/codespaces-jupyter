** Sorting **
## Uses
   - Database search
   - normal search

## Classifications:
	- By Number of Comparisons
		- Best case O(nlogn)
        - Worst case O(n^2)
    - Number of Swaps
        - Called inversions
    - Memory Usage
        - Auxilary space O(1) or O(nlogn)
    - Recursion
        - quick sort
    - Non Recusrsive
        - selectio, bubble, insertion
    - Both Recursion and Non-Recurion
        - merge sort
    - Stability
        - after the sorting if the indexs remain the same it is stable
        - Merge sort good for stability
    - Adaptability
        -   Quick sort, as the input is presorted the time complexity change
    - Sorting Type:
        - Internal Memory sort: very fast access (in-memory sort)
        - External sort: Use external memory like hard disk
    - Non Camprison (Linear)
        - Bucket, Radix, Counting

            Insertion Sort 	    Selection Sort 	    Merge Sort 	    Quick Sort 	    Bubble Sort 	    Insertion Sort
Best Case       Ω(n) 	         Ω(n2)  	        Ω(nlog(n)) 	    Ω(nlog(n)) 	    Ω(n^2)               Ω(n)
Average Case 	θ(n2) 	         θ(n2)              θ(nlog(n)) 	    θ(nlog(n)) 	    θ(n2) 	             θ(n2)
Worst Case 	    O(n2) 	         O(n2) 	            O(nlog(n))      O(nlog(n)) 	    O(n2) 	        	 O(n2)
