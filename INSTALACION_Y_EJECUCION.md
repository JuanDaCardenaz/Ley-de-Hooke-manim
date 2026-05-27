# Instalación y ejecución del proyecto en Windows

Este archivo explica solamente lo necesario para abrir y ejecutar la animación entregada.

## 1. Programas necesarios

El proyecto fue desarrollado y probado con:

- **Python 3.13.13**.
- **Manim Community v0.20.1**.
- **MiKTeX** para procesar las fórmulas creadas con `MathTex`.

El código utiliza `from manim import *`, por lo que debe ejecutarse con **Manim Community**.

## 2. Instalar Python

1. Descargar Python 3.13 para Windows desde la página oficial: https://www.python.org/downloads/windows/
2. Durante la instalación, marcar **Add python.exe to PATH**.
3. Terminar la instalación.
4. Abrir una terminal nueva y comprobar la versión:

```powershell
python --version
```

En el equipo donde se creó el proyecto, el resultado fue:

```text
Python 3.13.13
```

## 3. Instalar MiKTeX

El código contiene fórmulas creadas con `MathTex`, por ejemplo `\vec{F}_s=-k\vec{x}`. Para convertir esas fórmulas en elementos visibles de la animación, en Windows se instaló **MiKTeX**.

1. Descargar el instalador básico de MiKTeX desde: https://miktex.org/download
2. Ejecutar el instalador y completar la instalación.
3. Abrir **MiKTeX Console**.
4. Revisar si hay actualizaciones e instalarlas.
5. Permitir que MiKTeX instale paquetes faltantes cuando los solicite.

La primera ejecución con fórmulas puede tardar más porque MiKTeX puede necesitar descargar paquetes adicionales.

Para comprobar que LaTeX quedó disponible:

```powershell
latex --version
```

## 4. Abrir la carpeta del proyecto

Descargar este repositorio y guardarlo en una carpeta. Su contenido principal debe verse así:

```text
ley_de_hooke_manim/
├── ley_de_hooke_comentado_final.py
├── README.md
├── requirements.txt
├── INSTALACION_Y_EJECUCION.md
└── video/
    └── ENLACE_O_ARCHIVO_DEL_VIDEO.txt
```

Abrir una terminal dentro de la carpeta. Ejemplo si se guardó en Descargas:

```powershell
cd "C:\Users\USUARIO\Downloads\ley_de_hooke_manim"
```

Cambiar `USUARIO` por el nombre real del usuario de Windows.

## 5. Crear y activar el entorno virtual

El entorno virtual permite instalar las dependencias solamente para este proyecto.

Crear el entorno:

```powershell
python -m venv .venv
```

Activarlo en PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Cuando esté activo, normalmente aparecerá `(.venv)` al inicio de la línea de la terminal.

Si PowerShell no permite activarlo, se puede abrir **Símbolo del sistema (cmd)** en la misma carpeta y ejecutar:

```bat
.venv\Scripts\activate.bat
```

## 6. Instalar Manim y las dependencias

Con el entorno virtual activo, ejecutar:

```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Comprobar que Manim quedó instalado:

```powershell
python -m manim --version
```

La versión utilizada en este proyecto es:

```text
Manim Community v0.20.1
```

## 7. Ejecutar la animación

Para una prueba rápida en calidad baja:

```powershell
python -m manim -pql ley_de_hooke_comentado_final.py LeyDeHooke
```

Para renderizar la versión final en alta calidad:

```powershell
python -m manim -pqh ley_de_hooke_comentado_final.py LeyDeHooke
```

### Significado del comando

- `python -m manim`: ejecuta Manim desde el Python del entorno virtual.
- `-p`: abre el video cuando finaliza el renderizado.
- `-ql`: calidad baja para pruebas rápidas.
- `-qh`: calidad alta para la entrega final.
- `ley_de_hooke_comentado_final.py`: archivo que contiene la animación comentada.
- `LeyDeHooke`: clase principal que Manim debe renderizar.

Manim crea automáticamente la carpeta `media/`, donde guarda los videos renderizados.

## 8. Problemas comunes

### Aparece un error relacionado con `MathTex` o LaTeX

Abrir **MiKTeX Console**, instalar actualizaciones pendientes y volver a ejecutar la animación con conexión a Internet para que MiKTeX instale los paquetes que falten.

### La terminal no encuentra Manim

Verificar que el entorno virtual esté activo y repetir:

```powershell
python -m pip install -r requirements.txt
```

### El archivo se abre con Python, pero no se genera el video

El archivo debe renderizarse con Manim, no con el botón normal de ejecución de Python:

```powershell
python -m manim -pql ley_de_hooke_comentado_final.py LeyDeHooke
```
