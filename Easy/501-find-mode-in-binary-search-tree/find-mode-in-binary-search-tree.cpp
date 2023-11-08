/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    unordered_map<int, int> freq;
    void inorder(TreeNode* root){
        if (root == NULL){
            return;
        }
        inorder(root->left);
        ++freq[root->val];
        inorder(root->right);

    }
    vector<int> findMode(TreeNode* root) {
        vector<int> ans;
        inorder(root);
        int maxVal = 0;
        for(auto& p: freq){
           maxVal = max(maxVal, p.second);
        }

       for(auto& p:freq){
           if (p.second == maxVal){
             ans.push_back(p.first);
           }
       }

       return ans;
    }

};