# Restaurante App - Semana 16
 
## Autor
 
**Hugo Carlin Castillo Calva**
Carrera: Tecnologías de la Información
 
---
 
## Descripción
 
Restaurante App es una aplicación desarrollada en Python utilizando Tkinter que permite gestionar usuarios, productos y ventas mediante una arquitectura modular organizada en modelos, servicios y vistas.
 
La evolución correspondiente a la Semana 15 incorpora una nueva sección de Ventas, manteniendo las funcionalidades desarrolladas en semanas anteriores y evidenciando el uso de eventos, callbacks y persistencia de datos mediante archivos JSON.
 
---
 
## Objetivo de la Semana 16
 
Implementar una sección de Ventas que permita relacionar usuarios y productos mediante una operación sencilla gestionada desde la interfaz gráfica.
 
La solución incorpora:
 
- Eventos mediante botones.
- Uso de `command=`.
- Callbacks.
- Persistencia en JSON.
- Actualización dinámica de la interfaz.
- Uso de recursos visuales desde la carpeta `assets`.
 
---
 
## Funcionalidades del sistema
 
### Inicio de sesión
 
- Validación de credenciales.
- Acceso al sistema mediante RestauranteServicio.
 
### Usuarios
 
- Consulta de usuarios registrados.
- Visualización mediante Treeview.
 
### Productos
 
- Registro de productos.
- Actualización de productos.
- Eliminación de productos.
- Consulta de productos registrados.
- Persistencia en `productos.json`.
 
### Ventas
 
- Selección de usuario mediante Combobox.
- Selección de producto mediante Combobox.
- Registro de ventas mediante botón.
- Persistencia en `ventas.json`.
- Visualización de ventas registradas mediante Treeview.
- Actualización automática de la información después del registro.
 
---
 
## Modelo Venta
 
La clase Venta representa una relación sencilla entre:
 
- Usuario
- Producto
- Fecha
 
Campos utilizados:
 
- identificador
- usuario_id
- producto_codigo
- fecha
 
---
 
## Persistencia de datos
 
La aplicación utiliza archivos JSON para almacenar la información.
 
```text
datos/
├── usuarios.json
├── productos.json
└── ventas.json
```
 
---
 
## Uso de eventos y callbacks
 
El registro de ventas evidencia el uso de eventos estudiados durante la Semana 15.
 
```text
Usuario
↓
Botón "Registrar venta"
↓
command=
↓
Callback
↓
RestauranteServicio
↓
Persistencia en ventas.json
↓
Actualización de Treeview
↓
Respuesta visual
```
 
---
 
## Recursos visuales
 
La aplicación utiliza la carpeta `assets` para almacenar:
 
- Logo del sistema.
- Iconos de navegación.
- Iconos de acciones.
 
```text
assets/
└── icons/
├── logo.png
├── home.png
├── users.png
├── productos.png
├── sales.png
├── add.png
├── search.png
├── delete.png
```
 
---
 
## Estructura del proyecto
 
```text
restaurante_app/
├── datos/
│ ├── productos.json
│ ├── usuarios.json
│ └── ventas.json
│
├── modelos/
│ ├── producto.py
│ ├── usuario.py
│ └── venta.py
│
├── servicios/
│ ├── archivo_servicio.py
│ └── restaurante_servicio.py
│
├── ui/
│ ├── login_view.py
│ └── main_view.py
│
├── assets/
│ └── icons/
│
└── main.py
```
 
---
 
## Tecnologías utilizadas
 
- Python
- Tkinter
- ttk
- JSON
- Pillow (PIL)
 
---
 
## Ejecución del proyecto
 
1. Abrir una terminal en la carpeta del proyecto.
2. Ejecutar:
 
```bash
python main.py
```
 
3. Iniciar sesión.
4. Navegar por Usuarios, Productos y Ventas.
 
---
 
## Evolución realizada en la Semana 15
 
- Incorporación de la sección Ventas.
- Creación del modelo Venta.
- Persistencia mediante `ventas.json`.
- Implementación de callbacks mediante `command=`.
- Actualización dinámica de Treeview.
- Integración de logo e iconos mediante la carpeta `assets`.
- Conservación de las funcionalidades desarrolladas en semanas anteriores.
 
---