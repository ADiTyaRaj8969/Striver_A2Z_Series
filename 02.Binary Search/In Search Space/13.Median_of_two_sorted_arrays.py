# QUESTION:
# CODE:
# TODO: Extract test cases from the examples above
# Call your function: findMedianSortedArrays()
# Print result:
# cout << "Result: " << result << endl;

def findMedianSortedArrays(& nums1, & nums2): if (nums1).__len__() > nums2).__len__()) return findMedianSortedArrays(nums2, nums1) opt_cnt = (nums1).__len__() + nums2).__len__() + 1) / 2 low = 0, high = nums1).__len__() while (low <= high) cut1 = low + (high - low) / 2 cut2 = opt_cnt - cut1 int l1, l2, r1, r2 (cut1 - 1 < 0) ? l1 = INT_MIN : l1 = nums1[cut1 - 1] (cut2 - 1 < 0) ? l2 = INT_MIN : l2 = nums2[cut2 - 1] (cut1 >= nums1).__len__()) ? r1 = INT_MAX : r1 = nums1[cut1] (cut2 >= nums2).__len__()) ? r2 = INT_MAX : r2 = nums2[cut2] if (l1 <= r2 and l2 <= r1) if ((nums1).__len__() + nums2).__len__()) % 2 == 0) return (max(l1, l2) + min(r1, r2)) / 2.0 return max(l1, l2) else if (l1 > r2) high = cut1 - 1 else low = cut1 + 1 return 0.0

# TIME COMPLEXITY = O(N^2)
# SPACE COMPLEXITY = O(1)
```
