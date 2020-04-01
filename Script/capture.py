import xlrd
from netmiko import Netmiko

def function_capture(data_path):

    book = xlrd.open_workbook(data_path)
    first_sheet = book.sheet_by_index(0)
    cell = first_sheet.cell(0,0)

    for i in range(first_sheet.nrows):
        my_device = {
            "host": first_sheet.row_values(i)[0],
            "username": first_sheet.row_values(i)[1],
            "password": first_sheet.row_values(i)[2],
            "device_type": first_sheet.row_values(i)[3],
        }

        print('Device Executed')
        print(my_device["host"])

        try:
            net_connect = Netmiko(**my_device)
            output = net_connect.send_command("show run")
            print(output)
            write=open(first_sheet.row_values(i)[0]+'.txt','w')
            write.write(output)
            net_connect.disconnect()
        except:
            pass




