# 🧰 StockWise API

API REST para la **gestión de inventario** desarrollada con **Django 5.2.7** y **Django REST Framework 3.15.2**.  
Permite administrar **productos** y **categorías**, realizar búsquedas, y obtener información detallada con relaciones entre entidades.

---

## 🚀 Tecnologías utilizadas

- **Python 3.13.3**
- **Django 5.2.7**
- **Django REST Framework 3.15.2**
- **django-filter**

---

## ⚙️ Instrucciones para ejecutar el proyecto

1. Clonar el repositorio o crear la carpeta del proyecto:
   ```bash
   cd C:\Django\stockwise_api
   ```

2. Activar el entorno virtual:
   ```bash
   env\Scripts\activate
   ```

3. Ejecutar el servidor:
   ```bash
   python manage.py runserver
   ```

4. Abrir en el navegador:  
   👉 [http://127.0.0.1:8000/api/](http://127.0.0.1:8000/api/)

---

## 📦 Endpoints disponibles

Todos los endpoints funcionan desde **http://127.0.0.1:8000/api/**  
Las pruebas se pueden realizar directamente en el navegador (sin Postman).

---

### 🧩 CATEGORÍAS

#### 🔹 Listar categorías  
**GET:**  
👉 [http://127.0.0.1:8000/api/categories/](http://127.0.0.1:8000/api/categories/)

#### 🔹 Crear categoría  
**POST:**  
👉 [http://127.0.0.1:8000/api/categories/](http://127.0.0.1:8000/api/categories/)  
**JSON ejemplo:**
```json
{
  "name": "Electrónicos",
  "description": "Dispositivos electrónicos"
}
```

#### 🔹 Editar categoría  
**PATCH:**  
👉 [http://127.0.0.1:8000/api/categories/1/](http://127.0.0.1:8000/api/categories/1/)  
**JSON ejemplo:**
```json
{
  "description": "Categoría actualizada"
}
```

#### 🔹 Eliminar categoría  
**DELETE:**  
👉 [http://127.0.0.1:8000/api/categories/1/](http://127.0.0.1:8000/api/categories/1/)

---

### 📦 PRODUCTOS

#### 🔹 Listar productos  
**GET:**  
👉 [http://127.0.0.1:8000/api/products/](http://127.0.0.1:8000/api/products/)

#### 🔹 Crear producto  
**POST:**  
👉 [http://127.0.0.1:8000/api/products/](http://127.0.0.1:8000/api/products/)  
**JSON ejemplo:**
```json
{
  "name": "Laptop HP",
  "quantity": 10,
  "price": 2500.50,
  "description": "Laptop potente con procesador Intel i7",
  "category": 1
}
```

#### 🔹 Editar producto  
**PATCH:**  
👉 [http://127.0.0.1:8000/api/products/1/](http://127.0.0.1:8000/api/products/1/)  
**JSON ejemplo:**
```json
{
  "price": 2700
}
```

#### 🔹 Eliminar producto  
**DELETE:**  
👉 [http://127.0.0.1:8000/api/products/1/](http://127.0.0.1:8000/api/products/1/)

#### 🔹 Buscar producto  
**GET:**  
👉 [http://127.0.0.1:8000/api/products/?search=laptop](http://127.0.0.1:8000/api/products/?search=laptop)

---

### 🌟Producto con detalle de categoría

#### 🔹 Ver productos con categoría anidada  
**GET:**  
👉 [http://127.0.0.1:8000/api/products/?detailed](http://127.0.0.1:8000/api/products/?detailed)

**Ejemplo de respuesta:**
```json
{
  "id": 1,
  "name": "Laptop HP",
  "quantity": 10,
  "price": "2500.50",
  "description": "Laptop potente con procesador Intel i7",
  "category": {
    "id": 1,
    "name": "Electrónicos",
    "description": "Dispositivos electrónicos",
    "created_at": "2025-10-15T20:00:00Z",
    "updated_at": "2025-10-15T20:00:00Z"
  }
}
```

---

## 🧪 Datos de ejemplo (ya cargados en pruebas)
- **Categorías:**
  - Electrónicos
  - Hogar
  - Oficina 
- **Productos:**
  - Laptop HP  
  - Aspiradora Philips 
  - Silla Ergonómica
 

## ✅ Verificación rápida

| Acción | Método | URL | Resultado esperado |
|--------|--------|-----|--------------------|
| Listar categorías | GET | `/api/categories/` | Lista de categorías |
| Crear categoría | POST | `/api/categories/` | Nueva categoría creada |
| Listar productos | GET | `/api/products/` | Lista de productos |
| Buscar producto | GET | `/api/products/?search=laptop` | Producto filtrado |
| Ver detalle completo (punto extra) | GET | `/api/products/?detailed` | Producto con categoría anidada |
