class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        // To track the smaller array 
        int[] A = nums1;
        int[] B = nums2;
        int total = A.length + B.length;
        int half = (total+1) / 2; // +1 to round up

        if(B.length < A.length) {
            int[] temp = A;
            A = B;
            B = temp;
        }

        int left = 0;
        int right = A.length;

        while(left <= right) {
            int i = (left + right) / 2; // A
            int j = half - i; // B
            // This is the pointers to the LEFT SIDE of the partition
            // 
            int Aleft = i > 0 ? A[i-1] : Integer.MIN_VALUE; // Edge cases included
            int Aright = i < A.length ? A[i] : Integer.MAX_VALUE;

            int Bleft = j > 0 ? B[j-1] : Integer.MIN_VALUE;
            int Bright = j < B.length ? B[j] : Integer.MAX_VALUE;

            if(Aleft <= Bright && Bleft <= Aright) {
                // Odd Case then Even case
                if(total % 2 != 0) return Math.max(Aleft, Bleft); 
                else return (Math.max(Aleft,Bleft) + Math.min(Aright, Bright)) / 2.0;
            }
            else if(Aleft > Bright) right = i - 1;
            else left = i + 1;
        }

        return -1; // If out of bounds. 

    }
}

// A = 1234
// B = 12345678

// total = 4+8 = 12
// half = 12/2 = 6
// left = 0
// right = 4
// i = (4+0)/2 = 2 median for A 
// j = 6-2 = 4 median for B

// Aleft = A[2-1 = 1] = 2
// Aright = A[2] = 3
// Bleft = B[4-1 = 3] = 4
// Bright = B[4] = 5

// fail case cause Bleft !<= Aright
// will shift left by +1, as it voids Aright to be part of the "smaller" partition
// so redoes the loop

// i = (5+0)/2 = 2
// j = 6-1 = 5
// // would do it again as i and j will just be the same values
// i = (6+0)/2 = 3
// j = 6-3 = 3

// Aleft = A[3-1 = 2] = 3
// Aright = A[3] = 4
// Bleft = B[3-1 = 2] = 3
// Bright = B[3] = 4

// Aleft == Bright, and Bleft == Aright
// because our total is 12, even, will do:
// (Math.max(3,3) + Math.min(4, 4)) / 2.0 = (7) / 2.0 = 3.5 returns 3.5
