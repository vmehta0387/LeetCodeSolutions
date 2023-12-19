# You are given two non-empty linked lists representing two non-negative integers. 
# The digits are stored in reverse order, and each of their nodes contains a single digit. 
# Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

def addTwoNumbers(l1, l2):
    
    l1_rev = reversed(l1)
    l2_rev = reversed(l2)
    sum = int("".join(map(str, l1_rev))) + int("".join(map(str, l2_rev)))
    result = list(map(int,str(sum)))
    result.reverse()
    return result


l1 = [2,4,3] 
l2 = [5,6,4]
res = addTwoNumbers(l1, l2)
print(res)