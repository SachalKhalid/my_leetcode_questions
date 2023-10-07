class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int minVal = INT_MAX;
        int maxStockPrice = 0;

        for(int i = 0; i< prices.size(); i++){

            minVal = min(minVal, prices[i]);
            maxStockPrice = max(maxStockPrice, prices[i] - minVal); 
        }
        return maxStockPrice;
    }
};