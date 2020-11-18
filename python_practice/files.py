#File Handling
#
# f=open('dummy_file.py','r')
#
# print(f.read())
# print(f.read(4))
# f.write()
# print(f.readline())
# print(f.readlines())
#
# w,r,a
# t,b

#
# with open('dummy_file.py','r') as f:
#     print(f.read())
# 
# with open('dummy_file.py','a') as g:
#     print(g.write('atlanta'))

with open('dummy_file.py') as w:
    print(w.read())
