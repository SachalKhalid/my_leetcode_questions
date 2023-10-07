class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        int n = matrix.size(); //row    
        int m = matrix[0].size();//col
 
        int col0 = 1;
        //Intializing the refrenced col and row within matrix with 0
        for(int i = 0; i< n; i++){
            for(int j = 0; j< m; j++){

                if(matrix[i][j] == 0){

                    matrix[i][0] = 0;

                    if(j != 0){
                        matrix[0][j] = 0;
                    }
                    else{
                        col0 = 0;
                    }
                }
            }
        }
        
        //Intializing the remaingin matrix without first row and col with 0s accroding to refrenced row and col

        for(int i = 1; i< n; i++){
            for(int j = 1; j< m; j++){

                if(matrix[i][j] != 0){

                    if(matrix[0][j] == 0 || matrix[i][0] == 0){
                        matrix[i][j] = 0;
                    }
                }

            }
        }

    //step 3: Finally mark the 1st col & then 1st row:
    if (matrix[0][0] == 0) {
        for (int j = 0; j < m; j++) {
            matrix[0][j] = 0;
        }
    }
    
    if (col0 == 0) {
        for (int i = 0; i < n; i++) {
            matrix[i][0] = 0;
        }
    }

    }
};