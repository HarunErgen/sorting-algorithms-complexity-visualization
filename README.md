# sort-algorithm-complexity-visualization
Time complexities of sorting algorithms are visualized via matplotlib.pyplot

Comparison sorts that are Quicksort, Merge sort and Heapsort; non-comparison sorts that are LSD Radix Sort and Counting Sort are tested based on the sizes of randomly shuffled arrays.

![Figure_2](https://user-images.githubusercontent.com/83069560/152866623-6e45372e-9a0b-4728-a8ba-b8de06fff281.png)

Among the comparison sorts, Quicksort was the fastest one on average. The reason of the faster sorting is that Quicksort doesn't do unnecessary element swaps compared to Merge sort and Heapsort. However, there remains the chance of worst-case performance which is *O(N<sup>2</sup>)* time. By randomly choosing the pivot, I tried to avoid worst cases of Quicksort. <br /> 
A comparison sort cannot perform better than *O(N logN)* on average.
|             | Best-case | Average-case | Worst-case |
| ------------- | ------------- | ------------- | ------------- |
| Quicksort  | *O(N logN)*  | *O(N logN)* | *O(N<sup>2</sup>)*|
| Merge sort  | *O(N logN)*  | *O(N logN)* | *O(N logN)* |
| Heapsort  | *O(N logN)*  | *O(N logN)*| *O(N logN)*|

Between LSD Radix Sort with Base 10 and Counting sort, Counting sort performed better on the arrays with bigger size. <br /> 
Non-comparison sorts are not limited to *Ω(N logN)*. In the table below, *r* is the range of numbers to be sorted, *k* is the size of the keys and *d* is the digit size.
|             | Best-case | Average-case | Worst-case |
| ------------- | ------------- | ------------- | ------------- |
| LSD Radix Sort  | *O(N)*  | *O(N ⋅ <sup>k</sup>&frasl;<sub>d</sub>)* | *O(N ⋅ <sup>k</sup>&frasl;<sub>d</sub>)*|
| Counting sort  | *O(N)*  | *O(N + r)* | *O(N + r)* |

*Zoom in on chart:*
![Figure_1](https://user-images.githubusercontent.com/83069560/152866876-c687f5a6-3d33-42d4-b033-d34e2225d202.png)
