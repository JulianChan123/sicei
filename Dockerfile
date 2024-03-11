# Usa la imagen base de Python 3.9
FROM python:3.9

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia el archivo de requisitos (requirements.txt) al contenedor en /app
COPY requirements.txt .

# Instala las dependencias del proyecto
RUN pip install --no-cache-dir -r requirements.txt

# Copia el código de la aplicación al contenedor en /app
COPY . .

# Expone el puerto 8000 en el contenedor
EXPOSE 8000

# Comando para ejecutar la aplicación usando Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]