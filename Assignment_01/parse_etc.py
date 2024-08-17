passwd = open("passwd", "r")
users= {}

for line in passwd:
    splited_line = line.split(":")
    username=splited_line[0]
    user_data=[splited_line[5],splited_line[2]]
    users.update({username:user_data})

print(users)
passwd.close()