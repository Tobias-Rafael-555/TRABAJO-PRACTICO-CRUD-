import psycopg2

class gestor_pedido:
    
    def __init__(self, dataname, user, password, host, port):
        
        self.conexion = psycopg2.connect(
            dbname = dataname,
            user = user,
            password = password,
            host = host,
            port = port
            
            )
        print("Conexion establecida")
        
        self.cursor = self.conexion.cursor()
        
        print("Conexion exitosa a la base de datos..")
        
    def insertar(self, id_cliente, id_producto, cantidad):
        
        try:
            self.cursor.execute(
                "INSERT INTO pedidos (id_cliente, id_producto, cantidad) VALUES (%s, %s, %s)",
                (id_cliente, id_producto, cantidad)
            )
            
            self.conexion.commit()
            
            print("El pedido se registró de forma exitosa..")
            
        except psycopg2.Error as e:
            
            self.conexion.rollback()
            
            print(f"No se pudo registrar el pedido: {e}")
            
    def listar(self):
        
        self.cursor.execute(" SELECT * FROM pedidos; ")
        
        registro = self.cursor.fetchall()
        
        if registro:
            
            
            print(f"{'ID_Pedido':<12}{'ID_Cliente':<12}{'ID_Producto':<14}{'Cantidad':<10}{'Fecha'}")
            
            for f in registro:
                
                print(f"{f[0]:<12}{f[1]:<12}{f[2]:<14}{f[3]:<10}{f[4]}")
                
        else:
            
            print("No hay regitros para mostrar ")
            
    def modificar(self, id, cantidad):
        
        self.cursor.execute(" UPDATE pedidos SET cantidad=%s WHERE id_pedido=%s", (cantidad, id))
        
        if self.cursor.rowcount > 0:
            
            self.conexion.commit()
            
            print("Se modifico correctamente")
            
        else:
            
            self.conexion.rollback()
            
            print(" No se pudo modificar." )
            
    def borrar(self, id):
        
        try:
            
            self.cursor.execute("DELETE FROM pedidos WHERE id_pedido=%s", (id,))
            
            self.conexion.commit()
            
            print("El registro se elimno de forma exitosa ")
        except psycopg2.Error as e:
            
            self.conexion.rollback()
            
            print("No se puede eliminar el registro")
            
    
    def cerrar(self):
        
        self.cursor.close()
                
        self.conexion.close()
                
        print("Conexion cerrada exitosamente..")
        
def mostrar_menú():
    print("\n===== GESTION DE PRODUCTO =====")
    print("1. Agregar pedido ")
    print("2. Listar pedidos ")
    print("3. Modificar cantidad del pedido ")
    print("4. Borrar pedido ")
    print("5. Cerrar conexion :(")
    print("===============================")
 
def main():
    gestor = gestor_pedido(
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
            
            id_cliente = int(input("Ingrese el identificador de cliente: "))
            
            id_producto = int(input("Ingrese el identificador del producto: "))
            
            cantidad = int(input("Ingrese la cantidad:"))
            
            gestor.insertar(id_cliente, id_producto, cantidad)
        
        elif opc == 2:
            
            gestor.listar()
            
        elif opc == 3:
            
            gestor.listar()
            
            id = int(input("Ingrese el identificador del pedido que desea modificar: "))
            
            cantidad = int(input("Ingrese la cantidad que desea registrar: "))
            
            gestor.modificar(id, cantidad)
            
            print("Registros actualizados")
            
            gestor.listar()
            
        elif opc == 4:
            
            id = int(input("Ingrese el identifcador del pedido que desea eliminar: "))
            
            gestor.borrar(id)
            
            print("Registros actualizados")
                        
            gestor.listar()
                        
            
        elif opc == 5:
            
            gestor.cerrar()
            
        else:
            
            print("Ingrese una opcion valida")
            
if __name__ == "__main__":
    
    main()
                
            