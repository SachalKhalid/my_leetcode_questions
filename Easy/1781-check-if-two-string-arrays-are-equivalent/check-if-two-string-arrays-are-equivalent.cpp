class Solution {
public:
    bool arrayStringsAreEqual(vector<string>& word1, vector<string>& word2) {
        string a = "";
        string b = "";
        for (const auto& str : word1) {
            a += str;
        }
         for (const auto& str : word2) {
            b += str;
        }
        if (a==b) return true;
        else return false;
    }
};