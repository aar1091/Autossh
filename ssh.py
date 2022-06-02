import paramiko,getpass,os

ssh = paramiko.SSHClient()
os.system("cls")
usuario = input("ingrese su nombre de usuario: ")

os.system("cls")
contrasena=getpass.getpass(prompt="Ingrese la contrasena: ", stream=None)
os.system("cls")
comando = input("Ingrese comando a ejecutar: ")
os.system("cls")
ip =[]
ser ="0"
while ser != "":
    ser = input("Ingrese la IP del servidor: ")
    ip.append(ser)
    os.system("cls")
ip.pop()
puerto = input("Puerto de conexion (Presione enter para usar el puerto 22 por defecto): ")
if puerto =="": puerto = 22
for ip_server in ip:
    print (f"aplicando '{comando}' al servidor: {ip_server}:{puerto}, Nombre de Usuario: {usuario} ")
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(ip_server,port=puerto,username=usuario,password=contrasena)
    entrada, salida, error = ssh.exec_command(comando)
    print("\r".join(salida.readlines()))
    print("\n")
    ssh.close()
print(f"Comando '{comando}' Aplicado con exito")