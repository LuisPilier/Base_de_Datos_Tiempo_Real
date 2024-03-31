-- Crear la base de datos
CREATE DATABASE sistema_tiempo_real;

-- Seleccionar la base de datos
\c sistema_tiempo_real


CREATE TABLE usuarios (
 id SERIAL PRIMARY KEY,
 nombre VARCHAR(255) NOT NULL,
 email VARCHAR(255) NOT NULL UNIQUE,
 contrasena VARCHAR(255) NOT NULL
);

CREATE TABLE productos (
 id SERIAL PRIMARY KEY,
 nombre VARCHAR(255) NOT NULL,
 descripcion TEXT,
 precio DECIMAL(10,2) NOT NULL,
 stock INTEGER NOT NULL
);

-- Crear índices
CREATE INDEX idx_usuarios_email ON usuarios (email);
CREATE INDEX idx_productos_nombre ON productos (nombre);

-- Optimizar la configuración
ALTER SYSTEM SET max_connections = 100;
ALTER SYSTEM SET shared_buffers = 128MB;
ALTER SYSTEM SET effective_cache_size = 2GB;

-- Ajustar parámetros de postgresql.conf según necesidades
define porque hiciste esta base de datos asi