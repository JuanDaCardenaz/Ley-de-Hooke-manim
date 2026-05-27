from manim import *
import numpy as np

config.background_color = "#07111F"                              # Fondo oscuro para destacar figuras y fórmulas.
BLANCO, GRIS, CIAN = "#F5F7FF", "#AAB6CC", "#43D9FF"             # Colores de títulos, apoyo visual y resorte.
AZUL, AMARILLO, NARANJA = "#4F8CFF", "#FFD166", "#FF9F43"       # Colores de masa, ecuaciones y fuerza externa.
ROJO, VERDE, PANEL = "#EA1538", "#67E8A6", "#101D31"            # Colores de fuerza restauradora, energía y relleno.


class LeyDeHooke(Scene):                                          # Scene es la clase base de una animación en Manim.
    def construct(self):                                          # Organiza el orden completo del video.
        self.portada()
        self.deformacion()
        self.oscilacion()
        self.energia()
        self.cierre()

    def limpiar(self):                                            # Limpia la pantalla entre partes de la explicación.
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.6)  # FadeOut: desaparecer suavemente; run_time: duración.

    def titulo(self, n, texto):                                  # Formato reutilizable para titular las tres escenas.
        a = Text(f"ESCENA {n} / 3", font_size=18, color=CIAN, weight=BOLD)  # font_size: tamaño; BOLD: negrita.
        b = Text(texto, font_size=29, color=BLANCO, weight=BOLD)
        g = VGroup(a, b).arrange(DOWN, aligned_edge=LEFT, buff=0.08).to_corner(UL, buff=0.35)  # VGroup agrupa; buff separa; LEFT alinea.
        l = Line(b.get_left(), b.get_right(), color=CIAN, stroke_width=2).next_to(b, DOWN, buff=0.08)  # stroke_width: grosor del trazo.
        return VGroup(g, l)

    def pared(self, x=-5.1, y=-0.35):                            # Dibuja el soporte fijo al que está unido el resorte.
        base = Line([x, y - 0.75, 0], [x, y + 0.75, 0], color=GRIS, stroke_width=5)
        rayas = VGroup(*[                                         # Seis rayas diagonales para identificar visualmente la pared.
            Line([x, yy, 0], [x - 0.25, yy - 0.20, 0], color=GRIS, stroke_width=2)
            for yy in np.linspace(y - 0.62, y + 0.70, 6)         # np.linspace reparte seis alturas uniformemente.
        ])
        return VGroup(base, rayas)

    def resorte(self, centro, y=-0.35, pared=-5.08):             # Construye el resorte según la posición horizontal de la masa.
        fin = centro - 0.48                                      # Punto aproximado donde el resorte toca el borde izquierdo de la masa.
        pts = [[pared, y, 0], [pared + 0.18, y, 0]]              # Primer tramo horizontal que sale de la pared.
        largo = fin - pared - 0.36                               # Espacio disponible para distribuir el zigzag central.
        for i in range(9):                                       # Genera nueve puntos intermedios del resorte.
            px = pared + 0.18 + largo * (i + 1) / 10             # Reparte los puntos horizontalmente a lo largo del resorte.
            py = y + (0.19 if i % 2 == 0 else -0.19)             # Alterna arriba y abajo para formar el zigzag.
            pts.append([px, py, 0])                              # Agrega cada punto calculado a la trayectoria.
        pts += [[fin - 0.18, y, 0], [fin, y, 0]]                 # Último tramo horizontal que conecta con la masa.
        return VMobject(color=CIAN, stroke_width=4).set_points_as_corners(pts)  # VMobject une los puntos con segmentos visibles.

    def masa(self, x, y=-0.35):                                 # Crea el bloque que representa la masa del sistema.
        caja = RoundedRectangle(                                 # RoundedRectangle: rectángulo con esquinas redondeadas.
            width=0.95, height=0.72, corner_radius=0.10, color=AZUL,  # width/ancho; height/alto; corner_radius/redondeo.
            fill_color=PANEL, fill_opacity=1, stroke_width=3     # fill_color/relleno; fill_opacity/opacidad; stroke_width/borde.
        ).move_to([x, y, 0])                                    # move_to coloca la caja en la coordenada indicada.
        return VGroup(caja, Dot([x, y, 0], radius=0.065, color=CIAN))  # Dot: punto central decorativo de la masa.

    def montaje(self, x, y=-0.35):                              # Une resorte y masa para que funcionen como un mismo montaje.
        return VGroup(
            always_redraw(lambda: self.resorte(x.get_value(), y)),    # always_redraw redibuja el resorte cuando cambia x.
            always_redraw(lambda: self.masa(x.get_value(), y))        # La masa se actualiza con la misma posición.
        )

    def portada(self):                                           # Presentación inicial del tema y de la ecuación principal.
        a = Text("Ley de Hooke", font_size=62, color=BLANCO, weight=BOLD).shift(0.65 * UP)  # shift: desplazar hacia arriba.
        b = Text("De la deformación a la oscilación", font_size=29, color=GRIS).next_to(a, DOWN)  # next_to: colocar debajo.
        f = MathTex(r"\vec{F}_s=-k\vec{x}", font_size=58, color=AMARILLO).next_to(b, DOWN, buff=0.42)  # MathTex escribe fórmulas.
        self.play(FadeIn(a, shift=0.18 * UP), FadeIn(b), run_time=1.3)  # FadeIn: aparecer suavemente.
        self.play(Write(f), run_time=1.2)                        # Write: escribir la fórmula de forma progresiva.
        self.wait(3.0)                                          # Mantiene la portada visible para poder leerla.
        self.limpiar()

    def deformacion(self):                                      # ESCENA 1: muestra la deformación y la fuerza restauradora.
        x = ValueTracker(-2.6)                                  # ValueTracker guarda la posición inicial: equilibrio.
        t = self.titulo(1, "Deformación y fuerza restauradora")
        eq = DashedLine([-2.6, -1.1, 0], [-2.6, 0.32, 0], color=GRIS)  # DashedLine: línea punteada de equilibrio.
        leq = Text("equilibrio", font_size=18, color=GRIS).next_to(eq, DOWN, buff=0.08)
        ext = Arrow([-1.6, -0.35, 0], [-0.35, -0.35, 0], color=NARANJA, buff=0)  # Flecha naranja: fuerza externa hacia la derecha.
        res = Arrow([-0.75, -0.35, 0], [-2.0, -0.35, 0], color=ROJO, buff=0)     # Flecha roja: fuerza del resorte hacia el equilibrio.
        lext = MathTex(r"\vec{F}_{ext}", color=NARANJA).next_to(ext, UP)
        lres = MathTex(r"\vec{F}_s", color=ROJO).next_to(res, DOWN)
        f = MathTex(r"\vec{F}_s=-k\vec{x}", font_size=46, color=AMARILLO).shift(1.55 * UP)
        frase = Text("El resorte siempre empuja hacia el equilibrio.", font_size=24, color=GRIS).to_edge(DOWN)
        self.play(FadeIn(t), FadeIn(self.pared()), Create(eq), FadeIn(leq), FadeIn(self.montaje(x)), run_time=1.2)  # Create dibuja la referencia.
        self.play(GrowArrow(ext), FadeIn(lext), x.animate.set_value(-0.75), run_time=3.3)  # GrowArrow crea la flecha y .animate estira el resorte.
        self.play(FadeOut(ext), FadeOut(lext), GrowArrow(res), FadeIn(lres), Write(f), run_time=1.5)  # FadeOut retira la fuerza externa.
        self.play(FadeIn(frase), run_time=0.7)
        self.wait(3.0)
        self.limpiar()

    def oscilacion(self):                                       # ESCENA 2: representa el movimiento repetido alrededor del equilibrio.
        x = ValueTracker(-0.75)                                 # Empieza desde el extremo derecho, con el resorte estirado.
        t = self.titulo(2, "Al soltarlo, aparece la oscilación")
        eq = DashedLine([-2.6, -1.1, 0], [-2.6, 0.32, 0], color=GRIS)
        f = MathTex(
            r"x(t)=A\cos(\omega t)", r"\qquad \omega=\sqrt{\frac{k}{m}}",  # Fórmulas que explican el movimiento armónico.
            font_size=39, color=AMARILLO
        ).shift(1.55 * UP)
        frase = Text("La posición se repite alrededor del equilibrio.", font_size=24, color=GRIS).to_edge(DOWN)
        self.play(FadeIn(t), FadeIn(self.pared()), Create(eq), FadeIn(self.montaje(x)), Write(f), run_time=1.6)
        for destino in [-4.45, -0.75, -4.45, -0.75, -2.60]:    # Posiciones elegidas para mostrar la oscilación visual.
            tiempo = 1.9 if destino != -2.60 else 1.1           # El último movimiento termina más rápido en equilibrio.
            self.play(x.animate.set_value(destino), run_time=tiempo, rate_func=smooth)  # smooth suaviza cada recorrido.
        self.play(FadeIn(frase), run_time=0.7)
        self.wait(2.5)
        self.limpiar()

    def energia(self):                                          # ESCENA 3: muestra el intercambio entre energía potencial y cinética.
        x = ValueTracker(-0.75)                                 # La masa comienza en un extremo: alta energía potencial.
        A = 1.85                                                # Amplitud: distancia máxima respecto al equilibrio.
        t = self.titulo(3, "La energía cambia de forma")
        eq = DashedLine([-2.6, -1.42, 0], [-2.6, -0.05, 0], color=GRIS)
        f = MathTex(r"E=K+U_e", r"\qquad U_e=\frac{1}{2}kx^2", font_size=38, color=AMARILLO).shift(1.45 * UP)
        bu = RoundedRectangle(width=0.45, height=2.1, corner_radius=0.05, color=ROJO).move_to([3.3, -0.30, 0])   # Marco para U_e.
        bk = RoundedRectangle(width=0.45, height=2.1, corner_radius=0.05, color=VERDE).move_to([4.6, -0.30, 0])  # Marco para K.

        def altura_u():                                        # Calcula qué tan alta debe verse la barra roja.
            return max(0.03, 1.98 * ((x.get_value() + 2.6) / A) ** 2)  # La energía potencial aumenta en ambos extremos.

        ru = always_redraw(lambda: Rectangle(                   # Relleno rojo: energía potencial elástica U_e.
            width=0.32, height=altura_u(), fill_color=ROJO, fill_opacity=0.9, stroke_width=0
        ).next_to(bu.get_bottom(), UP, buff=0.06))
        rk = always_redraw(lambda: Rectangle(                   # Relleno verde: energía cinética K, complementaria a U_e.
            width=0.32, height=2.01 - altura_u(), fill_color=VERDE, fill_opacity=0.9, stroke_width=0
        ).next_to(bk.get_bottom(), UP, buff=0.06))
        labels = VGroup(MathTex(r"U_e", color=ROJO).next_to(bu, DOWN), MathTex(r"K", color=VERDE).next_to(bk, DOWN))
        frase = Text("La energía total se conserva.", font_size=25, color=GRIS).to_edge(DOWN)
        self.play(FadeIn(t), FadeIn(self.pared(y=-0.72)), Create(eq), FadeIn(self.montaje(x, y=-0.72)), Write(f), run_time=1.5)
        self.play(Create(bu), Create(bk), FadeIn(ru), FadeIn(rk), FadeIn(labels), run_time=1.1)  # Aparecen los indicadores de energía.
        for destino in [-4.45, -0.75, -4.45, -2.60]:           # Mientras la masa se mueve, las barras se actualizan.
            tiempo = 2.2 if destino != -2.60 else 1.2
            self.play(x.animate.set_value(destino), run_time=tiempo, rate_func=smooth)
        self.play(FadeIn(frase), run_time=0.7)
        self.wait(3.0)
        self.limpiar()

    def cierre(self):                                           # Pantalla final: resume la idea central de la animación.
        a = Text("Ley de Hooke", font_size=54, color=BLANCO, weight=BOLD).shift(0.7 * UP)
        f = MathTex(r"\vec{F}_s=-k\vec{x}", font_size=60, color=AMARILLO).next_to(a, DOWN)
        b = Text("Una fuerza restauradora produce oscilación.", font_size=27, color=GRIS).next_to(f, DOWN)
        self.play(FadeIn(a), Write(f), run_time=1.3)
        self.play(FadeIn(b), run_time=0.8)
        self.wait(3.0)
