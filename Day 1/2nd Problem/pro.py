# l1 = [3,4,2,1,3,3]
# l2 = [4,3,5,3,9,3]
# res = []
# for i in range(len(l1)):
#     res.append(l1[i] * (l2.count(l1[i])))
# print(sum(res))


def read_input_file(input_file):
    l1, l2 = [], []
    with open(input_file, "r") as file:
        for line in file:
            nums = list(map (int, line.strip().split()))
            l1.append(nums[0])
            l2.append(nums[1])
        return l1, l2
    
def fun(l1,l2):
    ans = []
    for i in range(len(l1)):
        ans.append(l1[i] * (l2.count(l1[i])))
    return sum(ans)

def write_output_file(result, output_file):
    with open(output_file, "w") as file:
        file.write(f"output: {result}")

input_file = "input.txt"
output_file = "output.txt"

l1,l2 = read_input_file(input_file)

result = fun(l1, l2)

write_output_file( result, output_file)
