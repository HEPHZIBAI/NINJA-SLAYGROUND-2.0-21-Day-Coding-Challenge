/*

Problem statement
You are given a number 'n'.



Return an integer that is the reverse of ‘n’.



Note:
Reverse of ‘n’ means an integer where, the most significant digit of ‘n’ is the least significant digit of the number, the second most significant digit of ‘n’ is the second least significant digit of the number and so on.


Example:
Input: 'n' = 123

Output: 321

Explanation:
Reverse of 'n' = 123 is 321.


Detailed explanation ( Input/output format, Notes, Images )
Sample Input 1:
34


Sample Output 1:
43


Explanation of sample output 1:
Reverse of ‘n’ = 34 is 43.


Sample Input 2:
121


Sample Output 2:
121


Expected Time Complexity:
Try to solve this in O(log(n)) 


Expected Space Complexity:
Try to solve this in O(1) 


Constraints:
0 <= ‘n’ <= 10^9

Time Limit: 1 sec

*/


public class Solution 
{
    public static int reverseNumber(int n) 
    {
        int s=0;
        while(n>0)
        {
            int r=n%10;
            s*=10;
            s+=r;
            n/=10;
        }
        return s;
    }
}