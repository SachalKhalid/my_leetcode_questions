class Solution {
public:
    void sortColors(vector<int>& nums) {
        int a=0;
        int b=0;
        int c=0;
        for(int i=0;i<nums.size();i++)
        {
            if(nums[i] == 0){
                a+=1;
            }
            else if(nums[i] == 1){
                b+=1;
            }
            else if(nums[i] == 2){
                c+=1;
            }
        }

        for(int i= 0; i< a; i++){
            nums[i] = 0;
        }
        for(int i = a; i<b+a; i++){
            nums[i] = 1;
        }
        for(int i = b+a; i<nums.size(); i++){
            nums[i] = 2;
        }
    }
};