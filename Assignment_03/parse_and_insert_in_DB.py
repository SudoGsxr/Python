import mysql.connector

mydb = mysql.connector.connect(
  host="10.200.14.212",
  user="ypython",
  password="ypython",
  database="Users"
)

mycursor = mydb.cursor()
filename = "passwd"

def parse_userdata(filename):
    passwd = open(filename, "r")
    users_list= []

    for line in passwd:
        splited_line = line.split(":")
        temp_vaules_=(splited_line[2],splited_line[0],splited_line[5],splited_line[6].strip())
        users_list.append(temp_vaules_)
    passwd.close()
    return users_list
    

def insert_into_DB(users_list):
        for user in users_list:
            sql = "INSERT INTO User_Details (id, Username, Home_Directory, Login_Shell) VALUES (%s, %s, %s, %s)"
            mycursor.execute(sql,user)
            mydb.commit()
        print ("Data instered into DB sucessfully")
        
if __name__ == "__main__":
    insert_into_DB(parse_userdata(filename))
