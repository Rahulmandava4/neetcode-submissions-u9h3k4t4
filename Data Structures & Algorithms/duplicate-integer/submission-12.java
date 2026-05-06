class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashSet<Integer> map = new HashSet<>();
        for (int i=0;i< nums.length; i++){
            map.add(nums[i]);

        }
        if (nums.length != map.size()){
            return true;

        }else{
            return false;
        }


    }
}