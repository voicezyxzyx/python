# def greet_user(user_name):
#     for name in user_name:
#         sendmsg="hello "+name+'!'
#         print(sendmsg)
# greet_user(user_name=['zyx','zzz','zz'])

# unprited_paper=['iphone case','robet pendant','doc']
# complted_paper=[]
# while unprited_paper:
#     current_paper=unprited_paper.pop()
#     print("printing model......"+current_paper)
#     complted_paper.append(current_paper)
# for complted in complted_paper:
#     print(complted)


#magic=["zzz","zyx","zxc"]
# def show_magic():
#     for name in magic:
#         print(magic)
# show_magic()

magic = ["zzz", "zyx", "zxc"]
new_magic=[]
def make_great(magic,new_magic):
    while magic:
        current_magic=magic.pop()
        current_magic="the great "+current_magic
        new_magic.append(current_magic)
def show_magic(new_magic):
    for magician in new_magic:
        print(magician)
make_great(magic,new_magic)
show_magic(new_magic)
