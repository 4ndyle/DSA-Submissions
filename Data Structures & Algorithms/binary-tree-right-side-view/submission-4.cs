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
    public List<int> RightSideView(TreeNode root) {
        if (root == null)
        {
            return new List<int>();
        }

        // bfs 
        Queue<TreeNode> queue = new Queue<TreeNode>();
        queue.Enqueue(root);

        List<int> results = new List<int>();

        // while there are still nodes to be proessed
        while (queue.Count > 0)
        {
            // get the node in the current level and add the rightmost node to the results 
            int currLevelLength = queue.Count;
            List<TreeNode> currLevelNodes = new List<TreeNode>();

            for (int i = 0; i < currLevelLength; i++)
            {
                TreeNode currNode = queue.Dequeue();
                currLevelNodes.Add(currNode);

                if (currNode.left != null) { queue.Enqueue(currNode.left); }
                if (currNode.right != null) { queue.Enqueue(currNode.right); }
            }

            results.Add(currLevelNodes[currLevelNodes.Count - 1].val);
        }

        return results;
    }
}
