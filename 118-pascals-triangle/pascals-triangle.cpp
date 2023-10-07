class Solution {
public:

// SOLUTION NO 1

//  vector<vector<int>> ans;
//          vector<int> pre;
//          vector<int> curr;

//          for(int i = 0; i< N; i++){
//              for(int j = 0; j< i+1; j++){
//                 //Check for first and last element for a row
//                 if(j == 0 || j == i){
//                     curr.push_back(1);
//                 }
//                 //creating the next row using previous maintained row
//                 else{
//                     curr.push_back(pre[j-1]+ pre[j]);
//                 }
                 
//              }
//              ans.push_back(curr);
//              pre = curr;
//              curr.clear();
//          }

//          return ans;

// ********************************************************

// SOLUITON 2
  //Generating a single row by using that row number
   vector<int> rowGenrater(int row){
       long long ans = 1;
       vector<int> rowVec;
       rowVec.push_back(1);

       for(int i = 1; i< row; i++){
           ans = ans * (row - i);
           ans = ans/i;
           rowVec.push_back(ans);
       }
       return rowVec;

   }
   //Genrating whole resultant vector by calling rowGenrater for each row
    vector<vector<int>> generate(int numRows) {
        vector<vector<int>> ans;
          for(int i = 1; i<= numRows; i++){
              ans.push_back(rowGenrater(i));
          }

          return ans;
    }
};