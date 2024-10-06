# f=open('text.txt','w')
# f.writelines('This is a new text to teach the python for beginners')
# f.close()


# f=open('text.txt','r')
# file=f.readline()
# print(file)
# f.close()


# with open('sumit.txt','w',encoding='utf-8') as file:
file=open('lal.txt','w')

file.write('sumit\n')
file.write('30\n')
file.write('chim tabaak tam tam\n')
file.write('sumit randi pel ke bhaga\n')
file.write('wet pussy\n')
file.write('12\n')
file.write('15\n')

f=open('lal.txt','rt')

for i in f:
    if i.strip:
        num=int(i)
        if(num%2==0):
            even=open('even.txt','a')
            even.write(str(num))
            even.write("\n")
        else:
            odd=open("odd.txt",'a')
            odd.write(str(num))
            odd.write("\n")
f.close()




