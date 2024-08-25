import click
import mysql.connector

def parse_userdata(passwd_path):
    passwd = open(passwd_path, "r")
    users_list= []

    for line in passwd:
        splited_line = line.split(":")
        temp_vaules_=(splited_line[2],splited_line[0],splited_line[5],splited_line[6].strip())
        users_list.append(temp_vaules_)
    passwd.close()
    return users_list

def insert_into_DB(users_list,db,u,p):
    
    mydb = mysql.connector.connect(
        host=db,
        user=u,
        password=p,
        database="Users"
        )
    mycursor = mydb.cursor()

    for user in users_list:
        sql = "INSERT INTO User_Details (id, Username, Home_Directory, Login_Shell) VALUES (%s, %s, %s, %s)"
        mycursor.execute(sql,user)
        mydb.commit()
    print ("Data instered into DB sucessfully")

@click.command()
@click.option('--db', required=True ,help='Database IP Address or Hostname')
@click.option('--u', required=True ,help='Database username')
@click.option('--p', prompt=True, hide_input=True , help="Database password of the user" )
@click.option('--passwd_path', prompt=True, required=True , help="path of the passwd file" )

def cli(passwd_path,db,u,p):
    insert_into_DB ( parse_userdata(passwd_path),db,u,p)

if __name__ == "__main__":
    cli ()
    
