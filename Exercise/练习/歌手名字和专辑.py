def make_album(singer_name,cd_name):
    Info={singer_name+''+cd_name}
    return Info
while True:
    print("请输入歌手的名字：")
    print("enter 'quit' at any time to quit")
    singer_name=input("歌手名字为：")
    if singer_name == 'quit':
        break
    cd_name=input("专辑的名字为：")
    if cd_name == 'quit':
        break
make_album(singer_name,cd_name)
print("歌手的名字和专辑为："+make_album)


