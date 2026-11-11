import sqlite3
import os

class InventarioBD:
    def __init__(self, nombre_carpeta, nombre_db):
        # 1. Configuración de rutas dinámicas al inicializar el objeto
        self.carpeta = os.path.join(os.getcwd(), nombre_carpeta)
        os.makedirs(self.carpeta, exist_ok=True)
        self.ruta_db = os.path.join(self.carpeta, nombre_db)
        
        # 2. Conexión y cursor internos
        self.conexion = sqlite3.connect(self.ruta_db)
        self.cursor = self.conexion.cursor()
        
        # 3. Inicializar la tabla automáticamente
        self._crear_tabla()

    def _crear_tabla(self):
        self.cursor.execute("DROP TABLE IF EXISTS herramientas")
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS herramientas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT,
                categoria TEXT,
                cantidad INTEGER,
                en_stock BOOLEAN
            )
        ''')
        self.conexion.commit()

    def insertar(self, nombre, categoria, cantidad, en_stock):
        self.cursor.execute('''
            INSERT INTO herramientas (nombre, categoria, cantidad, en_stock)
            VALUES (?, ?, ?, ?)
        ''', (nombre, categoria, cantidad, en_stock))
        self.conexion.commit()

    def listar(self):
        self.cursor.execute('SELECT * FROM herramientas')
        resultados = self.cursor.fetchall()
        print("\n--- Estado Actual de la Base de Datos ---")
        for fila in resultados:
            print(fila)

    def actualizar_cantidad(self, nombre, nueva_cantidad):
        self.cursor.execute('''
            UPDATE herramientas
            SET cantidad = ?
            WHERE nombre = ?
        ''', (nueva_cantidad, nombre))
        self.conexion.commit()

    def eliminar(self, nombre):
        self.cursor.execute('''
            DELETE FROM herramientas
            WHERE nombre = ?
        ''', (nombre,))
        self.conexion.commit()

    def cerrar(self):
        self.conexion.close()


# --- USO DEL OBJETO ---
if __name__ == "__main__":
    # Instanciamos la clase (crea la carpeta, la base y la tabla sola)
    mi_inventario = InventarioBD("electricista_poo", "taller.db")

    # Insertamos datos usando los métodos del objeto
    mi_inventario.insertar('Alicates', 'Herramienta', 5, 1)
    mi_inventario.insertar('Multímetro', 'Medición', 3, 1)
    mi_inventario.insertar('Destornillador', 'Herramienta', 10, 1)

    # Listamos el estado inicial
    mi_inventario.listar()

    # Actualizamos un registro
    mi_inventario.actualizar_cantidad('Alicates', 8)

    # Borramos un registro
    mi_inventario.eliminar('Destornillador')

    # Listamos el estado final
    mi_inventario.listar()

    # Cerramos la conexión prolijamente
    mi_inventario.cerrar()
