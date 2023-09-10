class Solution {
    public int[] solution(int[] arr) {
        int[] answer = {};
        int length = arr.length;
        int temp;
        for (int i=0; i< length; i++)
        {
            if ((arr[i] >= 50) && (arr[i] % 2 ==0))
            {
                temp = arr[i]/2;
                arr[i] = temp;
            }
            else if((arr[i]<50) && (arr[i] %2 ==1))
            {
                temp = arr[i];
                arr[i] = temp *2;
            }
        }
        return arr;
    }
}