# Ley de Hooke con Manim Community

## Modalidad elegida
Ruta 12: **Manim**, trabajo individual. El proyecto es una mini pieza animada sobre la **Ley de Hooke**, un concepto físico que explica la fuerza restauradora de un resorte cuando se deforma.

## Qué implementé
La animación está organizada en una portada, tres escenas principales y un cierre:

1. **Deformación y fuerza restauradora:** se muestra la masa en equilibrio, una fuerza externa que estira el resorte y la fuerza del resorte dirigida de regreso al equilibrio.
2. **Oscilación:** la masa se desplaza a ambos lados del equilibrio mientras aparecen las expresiones del movimiento armónico.
3. **Energía:** dos barras dinámicas representan el intercambio entre energía potencial elástica y energía cinética.

## Recursos de Manim utilizados
Utilicé `Text` y `MathTex` para textos y ecuaciones; `Line`, `DashedLine`, `Arrow`, `Rectangle` y `RoundedRectangle` para la construcción visual; `FadeIn`, `FadeOut`, `Write`, `Create` y `GrowArrow` para apariciones y escrituras; `VGroup` para agrupar objetos; y `ValueTracker`, `.animate` y `always_redraw` para actualizar el movimiento y las barras de energía.

## Adaptación propia
La adaptación propia consistió en conectar en una sola explicación visual tres ideas: la deformación del resorte, la oscilación de la masa y el intercambio de energía. Además, incorporé barras dinámicas para comunicar cuándo aumenta la energía potencial y cuándo aumenta la energía cinética.

## Documentación seguida
Consulté la documentación oficial de **Manim Community**, especialmente la instalación, el inicio rápido y los ejemplos:

- https://docs.manim.community/en/stable/
- https://docs.manim.community/en/stable/tutorials/quickstart.html
- https://docs.manim.community/en/stable/examples.html

## Qué aprendí y qué dificultad tuve
Aprendí a organizar una animación por escenas, construir objetos gráficos a partir de coordenadas y usar `ValueTracker` junto con `always_redraw` para producir cambios visibles. La principal dificultad técnica fue configurar el entorno en Windows para que `MathTex` funcionara correctamente, ya que fue necesario instalar MiKTeX y trabajar dentro del entorno virtual donde estaba instalado Manim.

## Ejecución rápida
La instalación detallada está en `INSTALACION_Y_EJECUCION.md`. Con el entorno activado:

```powershell
python -m manim -pql ley_de_hooke_comentado_final.py LeyDeHooke
```

Para renderizar la versión final en alta calidad:

```powershell
python -m manim -pqh ley_de_hooke_comentado_final.py LeyDeHooke
```

## Video explicativo

Video de sustentación del proyecto: [Cómo animar la Ley de Hooke con Python y Manim](https://youtu.be/ZpiE-PVUHy0)
