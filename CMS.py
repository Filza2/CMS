import sqlite3,os,zipfile
from rich.console import Console;from rich.table import Table;from rich.columns import Columns;from rich.panel import Panel
from datetime import datetime
from time import sleep
console=Console()
conn=sqlite3.connect('customers.db');cursor=conn.cursor()#You can edit db name 

  
def header():
  os.system("cls" if os.name=='nt' else "clear");console.print(""" 
 ██████╗███╗   ███╗███████╗
██╔════╝████╗ ████║██╔════╝
██║     ██╔████╔██║███████╗
██║     ██║╚██╔╝██║╚════██║
╚██████╗██║ ╚═╝ ██║███████║
 ╚═════╝╚═╝     ╚═╝╚══════
 
  By @TweakPY - @vv1ck
 """,style='bold dark_magenta',justify='left')
  
  
def create_table():cursor.execute("CREATE TABLE IF NOT EXISTS customer (ID TEXT , Name TEXT , username TEXT , Phone_Number TEXT , Email TEXT , Address TEXT , Product_Name TEXT , Product_Price TEXT , Date_of_Purchase TEXT);")


def Add_customer():
  try:
    while 1!=0:
      Id_execute=cursor.execute("SELECT ID FROM customer").fetchall()
      if Id_execute==[]:
        ID=0
      else:
        for ID in Id_execute:
          ID=int(ID[0])
      customer_info=input('\n[+] Enter The user Data : ');header()#Name:username:Phone_Number:Email:Address:Product_Name:Product_Price:Date_Of_Purchase
      try:
        Name=customer_info.split(":")[0]
        if Name==' ' or Name=='':console.print("[[bold red]![/bold red]] [bold red]Error[/bold red], Invaild data, Customer must have a Name !!");exit()
      except IndexError:console.print("[[bold red]![/bold red]] [bold red]Error[/bold red], Invaild data, Customer must have a Name !!");exit()
      try:
        username=customer_info.split(":")[1]
        if username==' ' or username=='':console.print("[[bold red]![/bold red]] Error, Invaild data, Customer must have a username !!");exit()
      except IndexError:console.print("[[bold red]![/bold red]] [bold red]Error[/bold red], Invaild data, Customer must have a username !!");exit()
      try:PhoneNumber=customer_info.split(":")[2]
      except IndexError:console.print("[-] [bold gold3]Warning[/bold gold3], User does not have a phone number !");PhoneNumber=None
      try:Email=customer_info.split(":")[3]
      except IndexError:console.print("[-] [bold gold3]Warning[/bold gold3], User does not have a Email !");Email=None
      try:address=customer_info.split(":")[4]
      except IndexError:console.print("[-] [bold gold3]Warning[/bold gold3], User does not have a address !");address=None
      try:Product_Name=customer_info.split(":")[5]
      except IndexError:console.print("[[bold red]![/bold red]] [bold gold3]Warning[/bold gold3], User does not have a product name !!");Product_Name=None
      try:Product_Price=customer_info.split(":")[6]
      except IndexError:console.print("[-] [bold gold3]Warning[/bold gold3], User does not have a product price !");Product_Price=None
      try:Date_of_purchase=customer_info.split(":")[7]
      except IndexError:console.print("[-] [bold gold3]Warning[/bold gold3], User does not have a purchase date !");Date_of_purchase=None
      cursor.execute(f"insert into customer (ID,Name,username,Phone_Number,Email,Address,Product_Name,Product_Price,Date_of_Purchase) values ('{ID+1}','{Name}','{username}','{PhoneNumber}','{Email}','{address}','{Product_Name}','{Product_Price}','{Date_of_purchase}');")
      conn.commit()
      sleep(3);header();console.print(f'\n[+] The customer named {Name}, identified as ID {ID+1}, has been added [bold green]successfully[/bold green]\n')
  except Exception as e:header();console.print(f'\n[[bold red]![/bold red]] The customer with the name {Name} and ID {ID+1} has not been added. There was an [bold red]error[/bold red] during the process !\n')
  except KeyboardInterrupt:console.print('\n');exit()
  
def Edit_customer():
  try:
    try:
      Id_execute=cursor.execute("SELECT ID FROM customer").fetchall()
    except IndexError:console.print("[[bold red]![/bold red]] [bold red]Error[/bold red], No Customers Detected on The Database !!");exit()
    customer_id=input('\n[+] Enter The user id : ');header()
    if customer_id in str(Id_execute):
      customer_info=input('[+] Enter The New user Data : ');header()#Name:username:Phone_Number:Email:Address:Product_Name:Product_Price:Date_Of_Purchase
      try:
        Name=customer_info.split(":")[0]
        if Name==' ' or Name=='':console.print("[[bold red]![/bold red]] [bold red]Error[/bold red], Invaild data, Customer must have a Name !!");exit()
      except IndexError:console.print("[[bold red]![/bold red]] [bold red]Error[/bold red], Invaild data, Customer must have a Name !!");exit()
      try:
        username=customer_info.split(":")[1]
        if username==' ' or username=='':console.print("[[bold red]![/bold red]] [bold red]Error[/bold red], Invaild data, Customer must have a username !!");exit()
      except IndexError:console.print("[[bold red]![/bold red]] [bold red]Error[/bold red], Invaild data, Customer must have a username !!");exit()
      try:PhoneNumber=customer_info.split(":")[2]
      except IndexError:console.print("[-] [bold gold3]Warning[/bold gold3], User does not have a phone number !");PhoneNumber=None
      try:Email=customer_info.split(":")[3]
      except IndexError:console.print("[-] [bold gold3]Warning[/bold gold3], User does not have a Email !");Email=None
      try:address=customer_info.split(":")[4]
      except IndexError:console.print("[-] [bold gold3]Warning[/bold gold3], User does not have a address !");address=None
      try:Product_Name=customer_info.split(":")[5]
      except IndexError:console.print("[[bold red]![/bold red]] [bold gold3]Warning[/bold gold3], User does not have a product name !!");Product_Name=None
      try:Product_Price=customer_info.split(":")[6]
      except IndexError:console.print("[-] [bold gold3]Warning[/bold gold3], User does not have a product price !");Product_Price=None
      try:Date_of_purchase=customer_info.split(":")[7]
      except IndexError:console.print("[-] [bold gold3]Warning[/bold gold3], User does not have a purchase date !");Date_of_purchase=None
      cursor.execute(f"UPDATE customer  SET  Name='{Name}' , username='{username}' , Phone_Number='{PhoneNumber}' , Email='{Email}' , Address='{address}' , Product_Name='{Product_Name}' , Product_Price='{Product_Price}' , Date_of_Purchase='{Date_of_purchase}'  WHERE ID='{customer_id}';")
      conn.commit()
      sleep(3);header();console.print(f'\n[+] The customer identified as ID {customer_id}, has been updated [bold green]successfully[/bold green]\n')
    else:header();console.print('\n[[bold red]![/bold red]] [bold red]Error[/bold red], Customer Not Found on The Database !\n');exit()
  except Exception as e:header();console.print(f'\n[[bold red]![/bold red]] [bold red]Error[/bold red], There was an error during the process !\n');exit()

def Delete_customer():
  try:
    try:
      Id_execute=cursor.execute("SELECT ID FROM customer").fetchall()
    except IndexError:console.print("[[bold red]![/bold red]] [bold red]Error[/bold red], No Customers Detected on The Database !!");exit()
    customer_id=input('\n[+] Enter The user id : ');header()
    if customer_id in str(Id_execute):
      deleted_customer=cursor.execute(f'SELECT Name,id FROM customer where id={customer_id};').fetchall()
      for deleted_customer_name,deleted_customer_id in deleted_customer:continue
      cursor.execute(f'DELETE FROM customer WHERE id={customer_id};')
      conn.commit()
      sleep(1);header();console.print(f'\n[+] The customer named {deleted_customer_name}, identified as ID {deleted_customer_id}, has been [bold green]successfully[/bold green] deleted\n')
    else:header();console.print('\n[[bold red]![/bold red]] [bold red]Error[/bold red], Customer Not Found on The Database !\n');exit()
  except Exception as e:header();console.print(f'\n[[bold red]![/bold red]] [bold red]Error[/bold red], There was an error during the process !\n');exit()

def Show_One_customer():
    try:
      try:
        Id_execute=cursor.execute("SELECT ID FROM customer").fetchall()
      except IndexError:console.print("[[bold red]![/bold red]] [bold red]Error[/bold red], No Customers Detected on The Database !!");exit()
      customer_id=input('\n[+] Enter The user id : ');header()
      if customer_id in str(Id_execute):
        customer_view=cursor.execute(f'SELECT ID,Name,username,Phone_Number,Email,Address,Product_Name,Product_Price,Date_of_Purchase FROM customer where id={customer_id};').fetchall()
        for ID,Name,username,Phone_Number,Email,Address,Product_Name,Product_Price,Date_of_Purchase in customer_view:continue
        sleep(1);header();console.print(f'\ncustomer {Name} :coffee: ! \n',style='bold red1');cur=[Panel(f"[bold dim]ID: {ID}[/bold dim]\n[bold green]Name: {Name}[/bold green]\n[bold dark_green]username: {username}[/bold dark_green]\n[bold blue]Phone Number: {Phone_Number}[/bold blue]\n[bold navy_blue]Email: {Email}[/bold navy_blue]\n[bold grey19]Address: {Address}[/bold grey19]\n[bold purple4]Product Name: {Product_Name}[/bold purple4]\n[bold purple3]Product Price: {Product_Price}[/bold purple3]\n[bold blue_violet]Date of Purchase: {Date_of_Purchase}[/bold blue_violet]",expand=True)]
        console.print(Columns(cur));console.print('\n')
      else:header();console.print('\n[[bold red]![/bold red]] [bold red]Error[/bold red], Customer Not Found on The Database !\n');exit()
    except Exception as e:header();console.print(f'\n[[bold red]![/bold red]] [bold red]Error[/bold red], There was an error during the process !\n');exit()
    
def Show_All_customers():
  try:
      customer_view=cursor.execute(f'SELECT ID,Name,username,Phone_Number,Email,Address,Product_Name,Product_Price,Date_of_Purchase FROM customer;').fetchall()
      header()
      console.print("\n[bold magenta] Customers List [/bold magenta] 💻 !\n")
      table=Table(show_header=True, header_style="bold grey3")
      table.add_column("ID", style="bold dim",width=10)
      table.add_column("Name",style="bold green",min_width=20)
      table.add_column("username",style="bold dark_green",min_width=20)
      table.add_column("Phone Number",style="bold blue",min_width=20)
      table.add_column("Email", style="bold navy_blue",width=28)
      table.add_column("Address",style="bold grey19",min_width=25)
      table.add_column("Product Name",style="bold purple4",min_width=20)
      table.add_column("Product Price",style="bold purple3",min_width=20)
      table.add_column("Purchase Date", style="bold blue_violet",width=20)
      for ID,Name,username,Phone_Number,Email,Address,Product_Name,Product_Price,Date_of_Purchase in customer_view:
        table.add_row(ID,Name,username,Phone_Number,Email,Address,Product_Name,Product_Price,Date_of_Purchase)
      sleep(1);console.print(table);console.print('\n')
  except Exception as e:header();console.print(f'\n[[bold red]![/bold red]] [bold red]Error[/bold red], There was an error during the process !\n');exit()
    
def backup():
  try:
    console.print(f'\n[+] creating a copy from customers.db now ...\n')
    now=datetime.now();data_time=str(now.strftime("%d_%m_%y_%I_%M"))
    with zipfile.ZipFile(f'customers_backup_{data_time}.zip','w') as file:
      file.write('customers.db')
    sleep(1);header();console.print(f'\n[+] Backup has been created [bold green]successfully[/bold green] for customers_{data_time}\n');exit()
  except Exception as e:header();console.print(f'\n[[bold red]![/bold red]] [bold red]Error[/bold red], There was an error during the process !\n',e);exit()
  
  
def CMS_Core():
  console.print('''
{
  "1":"Add Customer"
  "2":"Edit Customer",
  "3":"Delete Customer",
  "4":"View Customer",
  "5":"View all Customers",
  "6":"Create Backup file",
  "7":"View DataBase Report", 
}''')
  i=int(input("\n- Enter the service number : "))
  if i==1:Add_customer()
  elif i==2:Edit_customer()
  elif i==3:Delete_customer()
  elif i==4:Show_One_customer()
  elif i==5:Show_All_customers()
  elif i==6:backup()
  elif i==7:
    try:os.system('python DBView.py')
    except KeyboardInterrupt:exit('\n')
    except:console.print("\n[bold red]- Error, DataBase Report is in a External File Named 'DBView.py' run it [bold red]\n");exit()
  else:exit()
header();create_table();CMS_Core()