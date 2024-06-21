# 1. Two Sum

## Definition
You need to discover is there a two elements in array, that summary gives us target?

### Example 1:

- **Input:** `nums = [2,7,11,15], target = 9`
- **Output:** `[0,1]`
- **Explanation:** `Because nums[0] + nums[1] == 9, we return [0, 1].`
### Example 2:

- **Input:** ``nums = [3,2,4], target = 6``
- **Output:** `[1,2]`
### Example 3:

- **Input:** `nums = [3,3], target = 6`
- **Output:** `[0,1]`

## Solution
I've solved this task by deleting every 0-index element, and finding in least array (target - 0-index element)

### Code
```py
class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        while nums:
            current_element = nums.pop(0)
            i += 1

            sub_target = target - current_element

            if sub_target in nums:
                return [i - 1, nums.index(sub_target) + i]
```

# 2. Add Two Numbers

## Definition
You given 2 not sorted linked lists with integers inside, you need to add both of them to each other into third linked list.

### Example 1:

- **Input:** l1 = `[2,4,3], l2 = [5,6,4]`

- **Output:** `[7,0,8]`

- **Explanation:** `342 + 465 = 807.`

### Example 2:

- **Input:** `l1 = [0], l2 = [0]`

- **Output:** `[0]`

### Example 3:

- **Input:** `l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]`

- **Output:** `[8,9,9,9,0,0,0,1]`

## Solution
I was iteration throw both of lists, if sum of their numbers larger then 9 I sets variable `shift = 1`, else `shift = 0`, and after shift adds to the next element.

### Code
```py
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode, shift=None) -> ListNode:
        result = ListNode()

        current = l1.val + l2.val + (shift or 0)
        if current > 9:
            shift = 1
        else:
            shift = 0

        result.val = current % 10
        if l1.next and l2.next:
            result.next = self.addTwoNumbers(l1.next, l2.next, shift=shift)
        elif l1.next or l2.next:
            result.next = self.addTwoNumbers(
                l1.next if l1.next else l2.next, ListNode(0), shift=shift
            )
        elif shift:
            result.next = ListNode(1)

        return result
```

# 3. Longest Substring Without Repeating Characters

## Definition
Given a string `s`, find the length of the longest 
substring without repeating characters.

### Example 1:

- Input: `s = "abcabcbb"`
- Output: `3`
- Explanation: `The answer is "abc", with the length of 3.`
### Example 2:

- Input: `s = "bbbbb"`
- Output: `1`
- Explanation: `The answer is "b", with the length of 1.`
### Example 3:

- Input: `s = "pwwkew"`
- Output: `3`
- Explanation: `The answer is "wke", with the length of 3.`

## Solution
I'we solved it in time `O(n^2)` in worst case, average `O(n log n)`, 1-st things 1-st making list from string by `.split("")`. After poping 0-index element into `el` also making set `cache`, and iterating throw lasted array, if we saw item, then iterating, breaking also comparing maximal_len with len that we got now.

### Code
```py
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maximal = 0
        l = len(s)
        
        for c in range(len(s)):
            cache = set()
            i = c
            while True:
                el = s[i]
                if el in cache:
                    maximal = max(maximal, len(cache))
                    break
                else:
                    cache.add(el)
                    i += 1
                    if i == l:
                        maximal = max(maximal, len(cache))
                        break
        
        return maximal
```

# 1052. Grumpy Bookstore Owner

## Definition
There is a bookstore owner that has a store open for `n` minutes. Every minute, some number of customers enter the store. You are given an integer array customers of length `n` where `customers[i]` is the number of the customer that enters the store at the start of the `ith` minute and all those customers leave after the end of that minute.

On some minutes, the bookstore owner is grumpy. You are given a binary array `grumpy` where `grumpy[i]` is 1 if the bookstore owner is grumpy during the `ith` minute, and is 0 otherwise.

When the bookstore owner is grumpy, the customers of that minute are not satisfied, otherwise, they are satisfied.

The bookstore owner knows a secret technique to keep themselves not grumpy for minutes consecutive minutes, but can only use it once.

Return the maximum number of customers that can be satisfied throughout the day.

### Examples:

### Example 1:

- Input: `customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], minutes = 3`
- Output: `16`
- Explanation: `The bookstore owner keeps themselves not grumpy for the last 3 minutes. The maximum number of customers that can be satisfied = 1 + 1 + 1 + 1 + 7 + 5 = 16.`
### Example 2:

- Input: `customers = [1], grumpy = [0], minutes = 1`
- Output: `1`

## Solution
I've got and filtered the customers list by grump, iterated throw filtered list, 've got the max profit, and added it to sum of not grump time customers.

### Code
```py
class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        result = sum([customers[i] for i in range(len(customers)) if not grumpy[i]])
        combined = [(customers[i], i) for i in range(len(customers)) if grumpy[i]]
        maximal = 0

        for i in range(len(combined)):
            el, c_i = combined[i]
            sub_maximal = el

            j = i + 1
            while j < len(combined) and combined[j][1] - c_i < minutes:
                sub_maximal += combined[j][0]
                j += 1
            
            maximal = max(maximal, sub_maximal)
        
        return result + maximal
```

# Number. Template

## Definition
what?

### Examples:

- **Input:** l1 = `[2,4,3], l2 = [5,6,4]`

- **Output:** `[7,0,8]`

- **Explanation:** `342 + 465 = 807.`

## Solution
How you've solved it?

### Code
Your code.