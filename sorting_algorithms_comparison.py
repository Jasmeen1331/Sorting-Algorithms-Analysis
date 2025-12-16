#!/usr/bin/env python3
"""
Sorting Algorithms Performance Analysis
Comparison of Quick Sort vs Merge Sort

Author: Jasmeen (21236862)
Purpose: Analyze and compare performance metrics of sorting algorithms
Metrics: Execution time, memory usage, number of comparisons
Datasets: Random and reversed arrays of sizes 10,000 and 100,000
"""

import random
import time
import matplotlib.pyplot as plt
import psutil
import sys
import os


# ============================================
# QUICK SORT IMPLEMENTATION
# ============================================

def quick_sort(array, low, high):
    """
    Recursive Quick Sort algorithm with comparison counting.
    
    Time Complexity:
        - Average: O(n log n)
        - Worst: O(n²) (when poorly chosen pivots)
    
    Args:
        array: List to be sorted
        low: Starting index
        high: Ending index
        
    Returns:
        Number of comparisons made
    """
    comparisons = 0
    if low < high:
        pi, comparisons = partition(array, low, high)
        left_comparisons = quick_sort(array, low, pi - 1)
        right_comparisons = quick_sort(array, pi + 1, high)
        return comparisons + left_comparisons + right_comparisons
    return comparisons


def partition(array, low, high):
    """
    Partition function for Quick Sort.
    Chooses rightmost element as pivot.
    
    Args:
        array: List to partition
        low: Starting index
        high: Ending index
        
    Returns:
        Tuple of (pivot_position, comparisons)
    """
    pivot = array[high]  # Rightmost element as pivot
    i = low - 1
    comparisons = 0
    
    for j in range(low, high):
        comparisons += 1
        if array[j] < pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    
    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1, comparisons


# ============================================
# MERGE SORT IMPLEMENTATION  
# ============================================

def merge_sort(arr):
    """
    Recursive Merge Sort algorithm.
    
    Time Complexity: O(n log n) in all cases
    Space Complexity: O(n)
    
    Args:
        arr: List to be sorted
        
    Returns:
        Tuple of (sorted_array, comparisons)
    """
    if len(arr) <= 1:
        return arr, 0
    
    mid = len(arr) // 2
    left_half, left_comparisons = merge_sort(arr[:mid])
    right_half, right_comparisons = merge_sort(arr[mid:])
    merged, merge_comparison = merge(left_half, right_half)
    
    total_comparisons = left_comparisons + right_comparisons + merge_comparison
    return merged, total_comparisons


def merge(left, right):
    """
    Merge two sorted arrays.
    
    Args:
        left: First sorted array
        right: Second sorted array
        
    Returns:
        Tuple of (merged_array, comparisons)
    """
    result = []
    i = j = 0
    comparisons = 0
    
    while i < len(left) and j < len(right):
        comparisons += 1
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result, comparisons


# ============================================
# UTILITY FUNCTIONS
# ============================================

def get_memory_usage():
    """
    Get current memory usage in KB.
    
    Returns:
        Memory usage in kilobytes
    """
    process = psutil.Process(os.getpid())
    memory_info = process.memory_info()
    return memory_info.rss / 1024  # Convert to KB


# ============================================
# MAIN PERFORMANCE ANALYSIS
# ============================================

def main():
    """
    Main function to run sorting algorithm comparison.
    Tests both algorithms on random and reversed arrays.
    """
    # Initialize result storage
    results = []
    
    # Arrays for plotting
    quick_sort_times_random = []
    merge_sort_times_random = []
    quick_sort_memory_random = []
    merge_sort_memory_random = []
    merge_sort_comparisons_random = []
    quick_sort_comparisons_random = []
    
    quick_sort_times_reversed = []
    merge_sort_times_reversed = []
    quick_sort_memory_reversed = []
    merge_sort_memory_reversed = []
    merge_sort_comparisons_reversed = []
    quick_sort_comparisons_reversed = []
    
    sizes = [10000, 100000]  # Array sizes for testing
    
    for size in sizes:
        print(f"\nTesting with array size: {size}")
        
        # Generate random array
        array = random.sample(range(100000, 999999), size)
        
        # Test on random array
        quick_sort_array_random = array.copy()
        merge_sort_array_random = array.copy()
        
        # Quick Sort on random array
        start_time = time.time()
        quick_comparisons_random = quick_sort(quick_sort_array_random, 0, 
                                             len(quick_sort_array_random) - 1)
        quick_sort_time_random = (time.time() - start_time) * 1000
        memory_quick_sort_random = get_memory_usage()
        
        # Merge Sort on random array
        start_time = time.time()
        merged_array_random, merged_comparisons_random = merge_sort(merge_sort_array_random)
        merge_sort_time_random = (time.time() - start_time) * 1000
        memory_merge_random = get_memory_usage()
        
        # Store results
        quick_sort_times_random.append(quick_sort_time_random)
        merge_sort_times_random.append(merge_sort_time_random)
        quick_sort_memory_random.append(memory_quick_sort_random)
        merge_sort_memory_random.append(memory_merge_random)
        quick_sort_comparisons_random.append(quick_comparisons_random)
        merge_sort_comparisons_random.append(merged_comparisons_random)
        
        # Test on reversed array
        reversed_array = array[::-1]
        quick_sort_array_reversed = reversed_array.copy()
        merge_sort_array_reversed = reversed_array.copy()
        
        # Quick Sort on reversed array
        start_time = time.time()
        quick_comparisons_reversed = quick_sort(quick_sort_array_reversed, 0, 
                                               len(quick_sort_array_reversed) - 1)
        quick_sort_time_reversed = (time.time() - start_time) * 1000
        memory_quick_sort_reversed = get_memory_usage()
        
        # Merge Sort on reversed array
        start_time = time.time()
        merged_array_reversed, merged_comparisons_reversed = merge_sort(merge_sort_array_reversed)
        merge_sort_time_reversed = (time.time() - start_time) * 1000
        memory_merge_reversed = get_memory_usage()
        
        # Store results
        quick_sort_times_reversed.append(quick_sort_time_reversed)
        merge_sort_times_reversed.append(merge_sort_time_reversed)
        quick_sort_memory_reversed.append(memory_quick_sort_reversed)
        merge_sort_memory_reversed.append(memory_merge_reversed)
        quick_sort_comparisons_reversed.append(quick_comparisons_reversed)
        merge_sort_comparisons_reversed.append(merged_comparisons_reversed)
        
        print(f"Quick Sort (Random): {quick_sort_time_random:.2f}ms, "
              f"{quick_comparisons_random} comparisons")
        print(f"Merge Sort (Random): {merge_sort_time_random:.2f}ms, "
              f"{merged_comparisons_random} comparisons")
    
    # Generate visualizations
    create_visualizations(sizes, quick_sort_times_random, merge_sort_times_random,
                         quick_sort_times_reversed, merge_sort_times_reversed,
                         quick_sort_comparisons_random, merge_sort_comparisons_random,
                         quick_sort_comparisons_reversed, merge_sort_comparisons_reversed,
                         quick_sort_memory_random, merge_sort_memory_random,
                         quick_sort_memory_reversed, merge_sort_memory_reversed)
    
    print("\n✓ Analysis complete! Check sorting_results.png for visualizations.")


def create_visualizations(sizes, *args):
    """
    Create performance comparison plots.
    """
    (quick_times_rand, merge_times_rand, quick_times_rev, merge_times_rev,
     quick_comp_rand, merge_comp_rand, quick_comp_rev, merge_comp_rev,
     quick_mem_rand, merge_mem_rand, quick_mem_rev, merge_mem_rev) = args
    
    plt.figure(figsize=(15, 5), facecolor='lightgray')
    
    # Execution Time Plot
    plt.subplot(1, 3, 1)
    plt.plot(sizes, quick_times_rand, marker='o', linestyle='--', 
             label='Quick Sort (Random)', color='red')
    plt.plot(sizes, merge_times_rand, marker='s', linestyle='--', 
             label='Merge Sort (Random)', color='black')
    plt.plot(sizes, quick_times_rev, marker='o', linestyle='--', 
             label='Quick Sort (Reversed)', color='blue')
    plt.plot(sizes, merge_times_rev, marker='s', linestyle='--', 
             label='Merge Sort (Reversed)', color='green')
    plt.ylabel('Execution Time (ms)')
    plt.xlabel('Array Size')
    plt.title('Execution Time Comparison')
    plt.xticks(sizes)
    plt.legend()
    plt.grid(True)
    
    # Comparisons Plot
    plt.subplot(1, 3, 2)
    plt.plot(sizes, quick_comp_rand, marker='o', linestyle='--', 
             label='Quick Sort (Random)', color='red')
    plt.plot(sizes, merge_comp_rand, marker='s', linestyle='--', 
             label='Merge Sort (Random)', color='black')
    plt.plot(sizes, quick_comp_rev, marker='o', linestyle='--', 
             label='Quick Sort (Reversed)', color='blue')
    plt.plot(sizes, merge_comp_rev, marker='s', linestyle='--', 
             label='Merge Sort (Reversed)', color='green')
    plt.ylabel('Number of Comparisons')
    plt.xlabel('Array Size')
    plt.title('Comparisons Comparison')
    plt.xticks(sizes)
    plt.legend()
    plt.grid(True)
    
    # Memory Usage Plot
    plt.subplot(1, 3, 3)
    plt.plot(sizes, quick_mem_rand, marker='o', linestyle='--', 
             label='Quick Sort (Random)', color='red')
    plt.plot(sizes, merge_mem_rand, marker='s', linestyle='--', 
             label='Merge Sort (Random)', color='black')
    plt.plot(sizes, quick_mem_rev, marker='o', linestyle='--', 
             label='Quick Sort (Reversed)', color='blue')
    plt.plot(sizes, merge_mem_rev, marker='s', linestyle='--', 
             label='Merge Sort (Reversed)', color='green')
    plt.ylabel('Memory Usage (KB)')
    plt.xlabel('Array Size')
    plt.title('Memory Usage Comparison')
    plt.xticks(sizes)
    plt.legend()
    plt.grid(True)
    
    plt.tight_layout()
    plt.savefig('sorting_results.png', dpi=300, bbox_inches='tight')
    print("\n✓ Visualization saved as 'sorting_results.png'")


if __name__ == "__main__":
    print("="*60)
    print("   SORTING ALGORITHMS PERFORMANCE ANALYSIS")
    print("   Quick Sort vs Merge Sort Comparison")
    print("="*60)
    main()
