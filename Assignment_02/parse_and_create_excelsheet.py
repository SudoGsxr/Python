import xlsxwriter

filename = "passwd"

def parse_userdata(filename):
    passwd = open(filename, "r")
    users= {}

    for line in passwd:
        splited_line = line.split(":")
        username=splited_line[0]
        user_data=[splited_line[5],splited_line[2],splited_line[6].strip()]
        users.update({username:user_data})
    passwd.close()
    return users

def create_excelsheet (users):
    workbook = xlsxwriter.Workbook('Users.xlsx')
    worksheet = workbook.add_worksheet()
    header_row_format = workbook.add_format({'bold': True})
    worksheet.set_column(2, 3, 15)

    excel_headers=["Id", "Username", "Home Directory", "Login Shell"]
    for _ in range(4):
        #I’d, username, home directory, login shell 
        worksheet.write (0,_,excel_headers[_],header_row_format)
    row =1
    col =0
    for key,value in users.items():
        for _ in range (4):
            worksheet.write (row,col,value[1])
            worksheet.write (row,col+1,key)
            worksheet.write (row,col+2,value[0])
            worksheet.write (row,col+3,value[2])
        row +=1
    
    workbook.close()

if __name__ == "__main__":
    create_excelsheet( parse_userdata(filename))


