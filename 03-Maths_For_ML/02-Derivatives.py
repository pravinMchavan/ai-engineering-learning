"""
Derivatives from Scratch

This lesson teaches derivatives with:
1. Simple explanations
2. Text-based diagrams
3. A generated SVG graphic
"""

import math
from pathlib import Path


LESSON_DIR = Path(__file__).resolve().parent
SVG_PATH = LESSON_DIR / "02-Derivatives-diagrams.svg"


def section(title: str) -> None:
    print("\n" + "=" * 72)
    print(title)
    print("=" * 72)


def show_diagram(title: str, diagram: str) -> None:
    print(f"\n{title}")
    print(diagram)


def derivative_power_rule(n: int) -> str:
    """d/dx(x^n) = n*x^(n-1)"""
    if n == 1:
        return "1"
    elif n == 0:
        return "0"
    else:
        return f"{n}x^{n-1}"


def partial_derivative_x(expr: str) -> str:
    """Simple partial derivative examples"""
    if expr == "x^2 + y^3":
        return "2x"
    elif expr == "x*y + x^2":
        return "2x*y + 3"
    return "computed"


def gradient(expr: str) -> str:
    """Gradient vector"""
    if expr == "x^2 + y^2":
        return "(2x, 2y)"
    return "computed"


def chain_rule_example() -> str:
    """Example: d/dx((x^2 + 1)^3)"""
    return "3(x^2 + 1)^2 * 2x"


def build_svg() -> None:
    width = 980
    height = 760

    # Panel positions
    panels = [
        (40, 40, 430, 280, "1. Function and Derivative"),
        (510, 40, 430, 280, "2. Partial Derivatives"),
        (40, 380, 430, 280, "3. Gradient"),
        (510, 380, 430, 280, "4. Chain Rule"),
    ]

    def draw_function(panel_x: int, panel_y: int) -> str:
        """Draw f(x) = x^2 and tangent at x=2"""
        svg = ""
        # Axes
        svg += f'<line x1="{panel_x + 40}" y1="{panel_y + 230}" x2="{panel_x + 380}" y2="{panel_y + 230}" stroke="#444" stroke-width="2" />'
        svg += f'<line x1="{panel_x + 40}" y1="{panel_y + 230}" x2="{panel_x + 40}" y2="{panel_y + 30}" stroke="#444" stroke-width="2" />'
        svg += f'<text x="{panel_x + 385}" y="{panel_y + 236}" font-size="14" fill="#333">x</text>'
        svg += f'<text x="{panel_x + 32}" y="{panel_y + 26}" font-size="14" fill="#333">f(x)</text>'

        # Function curve (approximate parabola)
        path = "M"
        for i in range(0, 11):
            x = panel_x + 40 + i * 30
            y_val = i**2 * 2  # scaled
            y = panel_y + 230 - y_val
            path += f"{x},{y} "
            if i < 10:
                path += "L"
        svg += f'<path d="{path}" stroke="#d1495b" stroke-width="3" fill="none" />'

        # Tangent at x=2 (slope = 4)
        x_tangent = panel_x + 40 + 2 * 30
        y_tangent = panel_y + 230 - 8
        svg += f'<line x1="{x_tangent - 40}" y1="{y_tangent + 80}" x2="{x_tangent + 40}" y2="{y_tangent - 80}" stroke="#00798c" stroke-width="2" />'
        svg += f'<text x="{x_tangent + 10}" y="{y_tangent - 10}" font-size="12" fill="#00798c">tangent, slope=4</text>'

        return svg

    def draw_partials(panel_x: int, panel_y: int) -> str:
        """3D surface representation"""
        svg = ""
        # Simple grid
        for i in range(5):
            x = panel_x + 60 + i * 60
            svg += f'<line x1="{x}" y1="{panel_y + 50}" x2="{x + 30}" y2="{panel_y + 200}" stroke="#ccc" stroke-width="1" />'
            y = panel_y + 80 + i * 30
            svg += f'<line x1="{panel_x + 60}" y1="{y}" x2="{panel_x + 360}" y2="{y - 15}" stroke="#ccc" stroke-width="1" />'

        # Partial arrows
        svg += f'<line x1="{panel_x + 200}" y1="{panel_y + 150}" x2="{panel_x + 240}" y2="{panel_y + 130}" stroke="#edae49" stroke-width="3" marker-end="url(#arrowhead)" />'
        svg += f'<text x="{panel_x + 250}" y="{panel_y + 125}" font-size="12" fill="#edae49">&#2202;f/&#2202;x</text>'
        svg += f'<line x1="{panel_x + 200}" y1="{panel_y + 150}" x2="{panel_x + 180}" y2="{panel_y + 110}" stroke="#00798c" stroke-width="3" marker-end="url(#arrowhead)" />'
        svg += f'<text x="{panel_x + 140}" y="{panel_y + 105}" font-size="12" fill="#00798c">&#2202;f/&#2202;y</text>'

        return svg

    def draw_gradient(panel_x: int, panel_y: int) -> str:
        """Gradient vectors on a surface"""
        svg = ""
        # Contour lines
        for r in range(1, 4):
            cx = panel_x + 210
            cy = panel_y + 150
            svg += f'<circle cx="{cx}" cy="{cy}" r="{r * 40}" stroke="#d5d0c2" stroke-width="2" fill="none" />'

        # Gradient arrows pointing outward
        for angle in [0, 45, 90, 135, 180, 225, 270, 315]:
            rad = math.radians(angle)
            start_x = panel_x + 210 + 30 * math.cos(rad)
            start_y = panel_y + 150 + 30 * math.sin(rad)
            end_x = panel_x + 210 + 50 * math.cos(rad)
            end_y = panel_y + 150 + 50 * math.sin(rad)
            svg += f'<line x1="{start_x}" y1="{start_y}" x2="{end_x}" y2="{end_y}" stroke="#d1495b" stroke-width="2" marker-end="url(#arrowhead)" />'

        svg += f'<text x="{panel_x + 220}" y="{panel_y + 220}" font-size="12" fill="#d1495b">&#8711;f direction</text>'
        return svg

    def draw_chain(panel_x: int, panel_y: int) -> str:
        """Chain rule diagram"""
        svg = ""
        # Boxes
        svg += f'<rect x="{panel_x + 100}" y="{panel_y + 100}" width="80" height="40" rx="8" fill="#fffdf8" stroke="#d5d0c2" />'
        svg += f'<text x="{panel_x + 120}" y="{panel_y + 125}" font-size="14" fill="#333">x</text>'

        svg += f'<rect x="{panel_x + 220}" y="{panel_y + 100}" width="80" height="40" rx="8" fill="#fffdf8" stroke="#d5d0c2" />'
        svg += f'<text x="{panel_x + 240}" y="{panel_y + 125}" font-size="14" fill="#333">u = g(x)</text>'

        svg += f'<rect x="{panel_x + 340}" y="{panel_y + 100}" width="80" height="40" rx="8" fill="#fffdf8" stroke="#d5d0c2" />'
        svg += f'<text x="{panel_x + 360}" y="{panel_y + 125}" font-size="14" fill="#333">y = f(u)</text>'

        # Arrows
        svg += f'<line x1="{panel_x + 180}" y1="{panel_y + 120}" x2="{panel_x + 220}" y2="{panel_y + 120}" stroke="#444" stroke-width="2" marker-end="url(#arrowhead)" />'
        svg += f'<line x1="{panel_x + 300}" y1="{panel_y + 120}" x2="{panel_x + 340}" y2="{panel_y + 120}" stroke="#444" stroke-width="2" marker-end="url(#arrowhead)" />'

        # Derivative labels
        svg += f'<text x="{panel_x + 190}" y="{panel_y + 95}" font-size="12" fill="#00798c">du/dx</text>'
        svg += f'<text x="{panel_x + 310}" y="{panel_y + 95}" font-size="12" fill="#edae49">dy/du</text>'

        return svg

    svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">
    <defs>
        <marker id="arrowhead" markerWidth="10" markerHeight="10" refX="7" refY="3" orient="auto">
            <polygon points="0 0, 8 3, 0 6" fill="#222" />
        </marker>
    </defs>
    <rect width="100%" height="100%" fill="#f8f6ef" />
    <text x="40" y="24" font-size="26" font-family="Segoe UI, Arial, sans-serif" fill="#1c355e">Derivatives from Scratch</text>
    """

    for px, py, pw, ph, title in panels:
        svg_content += f'<rect x="{px}" y="{py}" width="{pw}" height="{ph}" rx="18" fill="#fffdf8" stroke="#d5d0c2" />'
        svg_content += f'<text x="{px + 18}" y="{py + 28}" font-size="18" fill="#222">{title}</text>'

    svg_content += draw_function(40, 40)
    svg_content += draw_partials(510, 40)
    svg_content += draw_gradient(40, 380)
    svg_content += draw_chain(510, 380)

    svg_content += "</svg>"

    with open(SVG_PATH, "w") as f:
        f.write(svg_content)

    print(f"SVG saved to {SVG_PATH}")


if __name__ == "__main__":
    section("DERIVATIVES FROM SCRATCH")

    print("1. WHAT IS A DERIVATIVE?")
    print("A derivative measures the rate of change of a function.")
    print("Example: f(x) = x^2, f'(x) = 2x")

    show_diagram("Text diagram", """
f(x) = x^2

      ^
      |
  9   * (3,9)
      |  \\
      |   \\
      |    \\
------O------* tangent at x=3
      |
      v
""")

    print("\n2. POWER RULE")
    for n in [0, 1, 2, 3]:
        print(f"d/dx(x^{n}) = {derivative_power_rule(n)}")

    print("\n3. PARTIAL DERIVATIVES")
    print("For f(x,y) = x^2 + y^3")
    print(f"∂f/∂x = {partial_derivative_x('x^2 + y^3')}")
    print("∂f/∂y = 3y^2")

    print("\n4. GRADIENT")
    print(f"∇f for f(x,y) = x^2 + y^2: {gradient('x^2 + y^2')}")

    print("\n5. CHAIN RULE")
    print(f"d/dx((x^2 + 1)^3) = {chain_rule_example()}")

    print("\n6. BUILDING DIAGRAMS")
    build_svg()