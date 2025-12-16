# Sorting Algorithms Performance Analysis

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Algorithms](https://img.shields.io/badge/Algorithms-Quick_Sort%20%7C%20Merge_Sort-orange.svg)]()

## Overview

Comprehensive performance analysis and comparison of **Quick Sort** and **Merge Sort** algorithms. This project evaluates execution time, memory usage, and comparison counts on datasets of varying sizes (10,000 and 100,000 elements) using both random and reversed data.

### Key Findings

- ⚡ **Quick Sort**: Faster on smaller datasets (10K elements) but inconsistent with large reversed arrays
- 📏 **Merge Sort**: More stable and predictable performance across all dataset sizes
- 💾 **Memory**: Quick Sort uses less memory (in-place sorting)
- 🔢 **Comparisons**: Merge Sort maintains consistent comparison counts

## Performance Results

### Array Size: 10,000 Elements

| Algorithm | Data Type | Execution Time | Comparisons | Memory Usage |
|-----------|-----------|---------------|-------------|-------------|
| **Quick Sort** | Random | 12.02 ms | 148,665 | 210.5 KB |
| **Merge Sort** | Random | 18.49 ms | 120,489 | 210.4 KB |
| **Quick Sort** | Reversed | 12.00 ms | 151,382 | 210.7 KB |
| **Merge Sort** | Reversed | 18.00 ms | 120,496 | 210.8 KB |

### Array Size: 100,000 Elements

| Algorithm | Data Type | Execution Time | Comparisons | Memory Usage |
|-----------|-----------|---------------|-------------|-------------|
| **Quick Sort** | Random | 167.04 ms | 1,912,188 | 212.6 KB |
| **Merge Sort** | Random | 249.65 ms | 1,536,060 | 214.6 KB |
| **Quick Sort** | Reversed | 161.12 ms | 2,073,779 | 216.1 KB |
| **Merge Sort** | Reversed | 268.87 ms | 1,535,923 | 218.9 KB |

## Algorithm Analysis

### Quick Sort

**Time Complexity:**
- Average Case: **O(n log n)**
- Best Case: **O(n log n)**  
- Worst Case: **O(n²)** (poor pivot selection)

**Space Complexity:** **O(log n)** (in-place sorting)

**Characteristics:**
- ✅ Faster for smaller datasets
- ✅ In-place sorting (low memory usage)
- ❌ Performance degrades with poor pivot selection
- ❌ Inconsistent on pre-sorted/reversed data

**When to Use:**
- Real-time systems requiring speed
- Memory-constrained environments
- Randomly distributed data

### Merge Sort

**Time Complexity:**
- All Cases: **O(n log n)** (guaranteed)

**Space Complexity:** **O(n)** (requires additional memory)

**Characteristics:**
- ✅ Consistent performance across all input types
- ✅ Predictable O(n log n) behavior
- ✅ Stable sorting algorithm
- ❌ Higher memory usage due to merging

**When to Use:**
- Large-scale data processing
- When stability is required
- Database management systems
- Big data analytics
- Cloud computing applications

## Methodology

### Test Setup

**Datasets:**
- Random Arrays: Integers ranging from 100,000 to 999,999
- Reversed Arrays: Sorted in descending order
- Sizes: 10,000 and 100,000 elements

**Metrics Measured:**
1. **Execution Time**: Time taken to sort (milliseconds)
2. **Memory Usage**: Memory consumption during sorting (KB)
3. **Comparisons**: Total number of element comparisons

**Tools Used:**
- Python 3.7+
- `time` module for execution timing
- `psutil` for memory profiling
- `matplotlib` for visualization

## Installation & Usage

### Prerequisites

```bash
python --version  # Python 3.7 or higher
```

### Install Dependencies

```bash
pip install matplotlib psutil
```

### Run Analysis

```bash
python sorting_algorithms_comparison.py
```

### Output

The script generates:
1. Console output with performance metrics
2. `sorting_results.png` - Visualization plots comparing:
   - Execution time
   - Number of comparisons
   - Memory usage

## Project Structure

```
Sorting-Algorithms-Analysis/
├── sorting_algorithms_comparison.py  # Main analysis script
├── README.md                         # Documentation
├── LICENSE                           # MIT License
└── .gitignore                        # Git ignore rules
```

## Analysis & Discussion

### Execution Time

**Quick Sort:**
- **Smaller datasets (10K)**: Quick Sort was faster (~12ms) due to in-place sorting eliminating merge overhead
- **Larger datasets (100K)**: Performance varied, especially with reversed data, due to pivot selection sensitivity

**Merge Sort:**
- Demonstrated consistent execution times across both dataset sizes
- Slightly slower for small arrays but maintained stability as size increased
- Reliable performance regardless of input data arrangement

### Memory Usage

**Quick Sort Advantage:**
- Minimal memory overhead due to in-place sorting
- Memory consumption remained relatively low even for large datasets
- No additional space needed for merging

**Merge Sort Consideration:**
- Required additional memory for temporary arrays during merging
- Memory usage increased significantly with dataset size
- Trade-off between memory and guaranteed performance

### Number of Comparisons

**Quick Sort:**
- Comparison count heavily influenced by data arrangement
- Efficient with random data (fewer comparisons)
- Poor performance with reversed data (more comparisons)
- Dependent on pivot selection quality

**Merge Sort:**
- Consistent comparison counts regardless of input
- Always divides array into halves and merges systematically
- Predictable behavior across all test scenarios
- Stable O(n log n) comparison complexity

## Real-World Implications

### Merge Sort Applications

✅ **Large-Scale Data Processing**: Predictable performance for big data
✅ **Database Management**: Reliable sorting for database operations
✅ **Cloud Computing**: Handles growing data volumes efficiently
✅ **External Sorting**: Works well with data that doesn't fit in memory

### Quick Sort Applications

✅ **Real-Time Systems**: Speed-critical applications
✅ **Memory-Constrained Devices**: Embedded systems, IoT devices
✅ **Random Data**: Performs excellently on unsorted data
⚠️ **Avoid**: Large pre-sorted or reversed datasets

## Conclusions

### Key Takeaways

1. **Merge Sort** is more reliable for large-scale data processing due to:
   - Consistent O(n log n) time complexity
   - Predictable performance across all input types
   - Stability in all scenarios

2. **Quick Sort** excels when:
   - Speed is critical for smaller datasets
   - Memory is limited
   - Data is randomly distributed

3. **Trade-offs**:
   - Quick Sort: Speed vs Consistency
   - Merge Sort: Memory vs Reliability

### Recommendations

- **For Production Systems**: Use **Merge Sort** for guaranteed performance
- **For Real-Time Apps**: Use **Quick Sort** with random data
- **For Large Datasets**: **Merge Sort** is the safer choice
- **For Memory-Constrained**: **Quick Sort** is more suitable

## Visualizations

The script generates three comparison plots:

1. **Execution Time**: Quick Sort vs Merge Sort across dataset sizes
2. **Comparisons**: Number of comparisons for both algorithms
3. **Memory Usage**: Memory consumption patterns

Each plot shows data for both random and reversed arrays, enabling comprehensive performance analysis.

## Code Features

- 📝 **Comprehensive Documentation**: Well-documented functions with docstrings
- 📊 **Performance Metrics**: Tracks time, memory, and comparisons
- 🔢 **Comparison Counting**: Accurate tracking of element comparisons
- 💾 **Memory Profiling**: Uses `psutil` for real-time memory monitoring
- 📈 **Visualization**: Matplotlib plots for result analysis

## References

1. Mania, P. (2023). *Python program for Merge Sort With code easy Explanation*.
2. GeeksforGeeks. (2014). *Python Program for QuickSort*.
3. Python speed testing - Time Difference - milliseconds. Stack Overflow.
4. psutil documentation. *psutil 7.0.0 documentation*.
5. Knuth, D.E. (1998). *The Art of Computer Programming: Sorting and Searching, Volume 3*. Addison-Wesley.
6. Khan Academy. (2018). *Big-O notation*.
7. StrataScratch. (2024). *A Complete Guide to Quick Sort Time Complexity*.

## Author

**Jasmeen** (Student ID: 21236862)  
Final Year Computer Science Student  
University of Central Lancashire

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

⭐ **Star this repository if you find it helpful for understanding sorting algorithms!**
