class ZeroSums:
    def threesum(self,nums_list):
        final_arr = []
        nums_list.sort() 
        n = len(nums_list) #length of list
        found = False

        for i in range(0, n - 1):

            # setting the lower and upper bound for indexing
            l = i + 1
            u = n - 1
            while l < u:
                if (nums_list[i] + nums_list[l] + nums_list[u] == 0):
                    final_arr.append([nums_list[i],nums_list[l],nums_list[u]])
                    l += 1
                    u -= 1
                    found = True    
                # increament lower bound by 1 if sum < 0.    
                elif (nums_list[i] + nums_list[l] + nums_list[u] < 0):
                    l += 1

                # decrement upper bound by 1 if sum < 0.    
                else:
                    u -= 1

        if found:
            return final_arr
        else:
            return "Three elements with sum zero not found!"    



sum1 = ZeroSums()

input_arr = [-25, -10, -7, -3, 2, 4, 8, 10]
print(f'The sample input array: {input_arr}\n')

output_arr = sum1.threesum(input_arr)
print(f'The final output array with having their sums equal to zero: {output_arr}')

