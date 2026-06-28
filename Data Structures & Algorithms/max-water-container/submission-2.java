class Solution {
    public int maxArea(int[] heights) {
        int left = 0;
        int right = heights.length-1;
        int max_area = 0;
        while (left < right){
            int length = right - left;
            int width = Math.min(heights[right], heights[left]);
            int area = length * width;
            max_area = Math.max(max_area, area);
            if (heights[left] < heights[right]){
                left++;
            }else{
                right--;
            }
        }
        return max_area;

    }
}
