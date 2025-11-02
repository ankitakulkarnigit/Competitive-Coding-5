# // Time Complexity : O(n)
# // Space Complexity : O(h)
# // Did this code successfully run on Leetcode : Yes
# // Any problem you faced while coding this : No


# // Your code here along with comments explaining your approach

# Used DFS with level tracking to solve this:

# Traverse the tree recursively, passing the current level (1-indexed) down the call stack
# For each node:
# If it's the first node in its level (level > len(res)), add its value to the result
# Otherwise, update the existing level's max value with max(res[level-1], root.val)
# Time Complexity: O(N) — visit every node once
# Space Complexity: O(H) — recursion stack depth (H = tree height)
# 💡 Key insight: The result list's length tracks how many levels you've seen so far, letting you know when you've reached a new level.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        self.res = []
        self.helper(root, 1)
        return self.res

    def helper(self, root, level):
        if root is None:
            return

        if level > len(self.res):
            self.res.append(root.val)
        
        else:
            temp = max(self.res[level-1], root.val)
            self.res[level-1] = temp

        level += 1
        self.helper(root.left,level)
        self.helper(root.right,level)
        