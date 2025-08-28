def reversePairs(nums):
    def merge_sort(low, high):
        if low >= high:
            return 0

        mid = (low + high) // 2

        count = 0
        count += merge_sort(low, mid)
        count += merge_sort(mid + 1, high)
        count += count_pairs(low, mid, high)
        merge(low,mid, high)
        return count
    
    def count_pairs(low, mid, high):
        count = 0
        j = mid + 1
        
        for i in range(low, mid + 1):
            while j <= high and nums[i] > 2 * nums[j]:
                j += 1
                
            count += (j -(mid + 1))
        return count
    
    def merge(low, mid, high):
        temp = []
        i, j = low, mid + 1
        
        while i <= mid and j <= high:
            if nums[i] <= nums[j]:
                temp.append(nums[i])
                i += 1
                
            else:
                temp.append(nums[j])
                j += 1
                
        while i <= mid:
            temp.append(nums[i])
            i += 1
            
        while j <= high:
            temp.append(nums[j])
            j += 1
            
        for k in range(len(temp)):
            nums[low + k] = temp[k]
            
    return merge_sort(0, len(nums) - 1)

if __name__ == "__main__":
    nums = [6, 4, 1, 2, 7]
    print(reversePairs(nums))