def find_min(V):
    # All denominations of Indian Currency
    deno = [1, 2, 5, 10, 20, 50, 100, 500, 1000]
    n = len(deno)
    
    # Initialize Result
    ans = []
    
    # Traverse through all denominations
    i = n - 1
    while i >= 0:
        # Find denominations
        while V >= deno[i]:
            V -= deno[i]
            ans.append(deno[i])
        i -= 1
    
    # Print result
    print("Following is the minimal number of change for", n, ":", end=" ")
    for i in range(len(ans)):
        print(ans[i], end=" ")

# Driver Code
if __name__ == '__main__':
    amount = int(input("Enter the amount: "))
    find_min(amount)
