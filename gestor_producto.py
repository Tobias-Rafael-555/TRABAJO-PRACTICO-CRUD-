import psycopg2

class gestorproducto:
    def __init__(self, dataname, user, password, host, port ):
        self.conexion = psycopg2.connect(
        dbname = dataname, 
        user = user,
        password = password,
        host = host,
        port = port
        )
        print("Conexion existosa")
        self.cursor = self.conexion.cursor()
        print("Conexión exitosa a la base de datos")
    
    #El metodo insertar se encarga de insertar un nurvo dato o conjunto de datos en una tabla     
    def insertar_producto(self, nombre, precio, stock):
        
        try:
            self.cursor.execute(
                 
                 "INSERT INTO productos(nombre, precio, stock) VALUES(%s, %s, %s)", (nombre, precio, stock)
                 
                )
            
        except Exception as e:
            
            print('Error al insertar el dato', e)
        self.conexion.commit()
        print("Se inserto correctamente")
    #El metodo listar se encarga de mostrar los datos contenidos en la tabla productos  
    def listar(self):
        
        self.cursor.execute(
            "SELECT * FROM productos;"
        )
        filas = self.cursor.fetchall()
        
        if not filas:
            
            print("No hay registros para mostrar")
            
            return
        
        print(f"{'ID':<4} {'Nombre':<20} {'Precio':<25} {'Stock':<20}")
        
        for f in filas:
            
            print(f"{f[0]:<4} {f[1]:<20} {f[2]:<25} {f[3]:<20}")
    
    #Este metodo se encarga de modificar un registro 
    def modificar(self, id_producto, stock):
        
        self.cursor.execute("UPDATE productos SET stock = %s WHERE id_producto = %s", (stock, id_producto))
        
        
        if self.cursor.rowcount > 0:
            
            self.conexion.commit()
            
            print(f"Se modifico correctamente")
      
        else:
            
            print("No se pudo modicar. Verifica si se ingreso el ID correcto. ")
    
    # Este metodo se encarga de borrar un registro 
    def borrar(self, id_producto):
        
        try:
            self.cursor.execute(" DELETE FROM productos WHERE id_producto=%s", (id_producto,))
            
        except psycopg2.Error as e:
            
            self.conexion.rollback()
            
            print("No se puede eliminar el dato")
            
        self.conexion.commit()
           
        print("El registro se elimino correctamente.")
    
    # Este metodo se encarga de cerrar la conexion
    def cerrar(self):
        
        self.cursor.close()
        
        self.conexion.close()
        
        print("Conexion cerrada exitosamente..")
    
    # Este metodo se encarga de mostrar el menu de opciones 
def mostrar_menú():
    print("\n===== GESTION DE PRODUCTO =====")
    print("1. Agregar producto")
    print("2. Listar productos")
    print("3. Modificar stock de un producto")
    print("4. Borrar producto")
    print("5. Cerrar conexion :(")
    print("===============================")
 
def main():
    gestor = gestorproducto(
            dataname = 'comercio', 
            user = 'postgres',
            password = '*****',
            host = 'localhost',
            port = 5432
            )
    
    while True:
        
        mostrar_menú()
        
        opc = int(input("Seleccione una opcion del menu: "))
        
        if opc == 1:
            
            nombre = input("Ingrese el nombre del producto: ")
            
            precio = int(input("Ingrese el precio del producto:"))
            
            stock = int(input("Ingrese el stock: "))
            
            gestor.insertar_producto(nombre, precio, stock)
            
        elif opc == 2:
            
            gestor.listar()
            
        elif opc == 3:
            
            id_producto = int(input("Ingrese el ID del producto a modificar: "))
             
            stock = int(input("Ingrese el nuevo valor del stock: "))
            
            gestor.modificar(id_producto, stock)
            
        elif opc == 4:
            
            id_producto = int(input("Ingrese el ID del producto a borrar: "))
            
            gestor.borrar(id_producto)
            
        elif opc == 5:
            
            gestor.cerrar()
            
        else:
            
            print("Opcion invalida. Ingrese una opcion del menu. ")
            
if __name__ == "__main__":
    
    main()