/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int val=0, TreeNode left=null, TreeNode right=null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */



public class Solution {
    int kthSmallestValue = -1;
    int currentPosition = 0;

    public int KthSmallest(TreeNode root, int k) {
        dfsHelper(root, k);
        return kthSmallestValue;
    }

    // in order traversal 
    public void dfsHelper(TreeNode root, int k) {
        // base case 
        if (root == null || kthSmallestValue != -1) {
            return;
        }

        // process the left subtree
        dfsHelper(root.left, k);

        // process the current node 
        currentPosition += 1; 

        if (currentPosition == k) {
            kthSmallestValue = root.val;
            return;
        }

        // process the right subtrree
        dfsHelper(root.right, k);
    }
}
