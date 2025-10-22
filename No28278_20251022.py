import sys

num_list = []
output = []

def push(num):
    num_list.append(num)
    
def pop():
    if num_list:
        output.append(str(num_list.pop()))
    else:
        output.append("-1")
        
def count_num():
    output.append(str(len(num_list))) 
    
def check_list():
    if num_list:
        output.append("0")
    else:
        output.append("1")
        
def check_last_num():
    if num_list:
        output.append(str(num_list[-1]))
    else:
        output.append("-1")

input = sys.stdin.readline
num_order = int(input())

for _ in range(num_order):
    order = input().split()
    cmd = order[0]
    if cmd == '1':
        num = int(order[1])
        push(num)
    elif cmd == '2':
        pop()
    elif cmd == '3':
        count_num()
    elif cmd == '4':
        check_list()
    elif cmd == '5':
        check_last_num()
        
print("\n".join(output))