"""
Vectors from Scratch

This lesson teaches vectors with:
1. Simple explanations
2. Text-based diagrams
3. A generated SVG graphic
"""

from pathlib import Path


LESSON_DIR = Path(__file__).resolve().parent
SVG_PATH = LESSON_DIR / "01-Vector-diagrams.svg"


def section(title: str) -> None:
    print("\n" + "=" * 72)
    print(title)
    print("=" * 72)


def show_diagram(title: str, diagram: str) -> None:
    print(f"\n{title}")
    print(diagram)


def vector_add(a: list[int], b: list[int]) -> list[int]:
    return [x + y for x, y in zip(a, b)]


def vector_subtract(a: list[int], b: list[int]) -> list[int]:
    return [x - y for x, y in zip(a, b)]


def scalar_multiply(k: int, v: list[int]) -> list[int]:
    return [k * value for value in v]


def dot_product(a: list[int], b: list[int]) -> int:
    return sum(x * y for x, y in zip(a, b))


def build_svg() -> None:
    width = 980
    height = 760
    panel_w = 430
    panel_h = 280
    left_x = 40
    right_x = 510
    top_y = 40
    bottom_y = 380

    def axes(panel_x: int, panel_y: int) -> str:
        return f"""
        <line x1="{panel_x + 40}" y1="{panel_y + 230}" x2="{panel_x + 380}" y2="{panel_y + 230}" stroke="#444" stroke-width="2" />
        <line x1="{panel_x + 40}" y1="{panel_y + 230}" x2="{panel_x + 40}" y2="{panel_y + 30}" stroke="#444" stroke-width="2" />
        <text x="{panel_x + 385}" y="{panel_y + 236}" font-size="14" fill="#333">x</text>
        <text x="{panel_x + 32}" y="{panel_y + 26}" font-size="14" fill="#333">y</text>
        <circle cx="{panel_x + 40}" cy="{panel_y + 230}" r="3" fill="#333" />
        <text x="{panel_x + 12}" y="{panel_y + 248}" font-size="12" fill="#333">O</text>
        """

    def arrow(panel_x: int, panel_y: int, x: int, y: int, color: str, label: str) -> str:
        origin_x = panel_x + 40
        origin_y = panel_y + 230
        end_x = origin_x + x * 40
        end_y = origin_y - y * 40
        return f"""
        <line x1="{origin_x}" y1="{origin_y}" x2="{end_x}" y2="{end_y}" stroke="{color}" stroke-width="4" marker-end="url(#arrowhead)" />
        <text x="{end_x + 8}" y="{end_y - 8}" font-size="14" fill="{color}">{label}</text>
        """

    def shifted_arrow(start_x: int, start_y: int, dx: int, dy: int, color: str, label: str) -> str:
        end_x = start_x + dx * 40
        end_y = start_y - dy * 40
        return f"""
        <line x1="{start_x}" y1="{start_y}" x2="{end_x}" y2="{end_y}" stroke="{color}" stroke-width="4" marker-end="url(#arrowhead)" stroke-dasharray="8 6" />
        <text x="{end_x + 8}" y="{end_y - 8}" font-size="14" fill="{color}">{label}</text>
        """

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">
    <defs>
        <marker id="arrowhead" markerWidth="10" markerHeight="10" refX="7" refY="3" orient="auto">
            <polygon points="0 0, 8 3, 0 6" fill="#222" />
        </marker>
    </defs>
    <rect width="100%" height="100%" fill="#f8f6ef" />
    <text x="40" y="24" font-size="26" font-family="Segoe UI, Arial, sans-serif" fill="#1c355e">Vectors from Scratch</text>

    <rect x="{left_x}" y="{top_y}" width="{panel_w}" height="{panel_h}" rx="18" fill="#fffdf8" stroke="#d5d0c2" />
    <text x="{left_x + 18}" y="{top_y + 28}" font-size="18" fill="#222">1. A vector on a 2D plane</text>
    {axes(left_x, top_y)}
    {arrow(left_x, top_y, 2, 3, "#d1495b", "v = [2, 3]")}

    <rect x="{right_x}" y="{top_y}" width="{panel_w}" height="{panel_h}" rx="18" fill="#fffdf8" stroke="#d5d0c2" />
    <text x="{right_x + 18}" y="{top_y + 28}" font-size="18" fill="#222">2. Vector addition</text>
    {axes(right_x, top_y)}
    {arrow(right_x, top_y, 2, 3, "#00798c", "v1 = [2, 3]")}
    {arrow(right_x, top_y, 4, 1, "#edae49", "v2 = [4, 1]")}
    {shifted_arrow(right_x + 40 + 2 * 40, top_y + 230 - 3 * 40, 4, 1, "#edae49", "move v2 here")}
    {arrow(right_x, top_y, 6, 4, "#2a9d8f", "v1 + v2 = [6, 4]")}

    <rect x="{left_x}" y="{bottom_y}" width="{panel_w}" height="{panel_h}" rx="18" fill="#fffdf8" stroke="#d5d0c2" />
    <text x="{left_x + 18}" y="{bottom_y + 28}" font-size="18" fill="#222">3. Scalar multiplication</text>
    {axes(left_x, bottom_y)}
    {arrow(left_x, bottom_y, 2, 3, "#3d5a80", "v = [2, 3]")}
    {arrow(left_x, bottom_y, 4, 6, "#ee6c4d", "2v = [4, 6]")}

    <rect x="{right_x}" y="{bottom_y}" width="{panel_w}" height="{panel_h}" rx="18" fill="#fffdf8" stroke="#d5d0c2" />
    <text x="{right_x + 18}" y="{bottom_y + 28}" font-size="18" fill="#222">4. Dot product idea</text>
    <text x="{right_x + 18}" y="{bottom_y + 62}" font-size="16" fill="#222">v1 = [2, 3]</text>
    <text x="{right_x + 18}" y="{bottom_y + 92}" font-size="16" fill="#222">v2 = [4, 1]</text>
    <text x="{right_x + 18}" y="{bottom_y + 132}" font-size="18" fill="#b23a48">v1 . v2 = (2 x 4) + (3 x 1) = 11</text>
    <text x="{right_x + 18}" y="{bottom_y + 174}" font-size="16" fill="#222">Multiply matching values, then add.</text>
    <text x="{right_x + 18}" y="{bottom_y + 204}" font-size="16" fill="#222">A larger dot product often means stronger alignment.</text>
    <text x="{right_x + 18}" y="{bottom_y + 244}" font-size="14" fill="#666">File generated by 01-Vector.py</text>
    </svg>"""

    SVG_PATH.write_text(svg, encoding="utf-8")


v1 = [2, 3]
v2 = [4, 1]
vector_addition = vector_add(v1, v2)
vector_subtraction = vector_subtract(v1, v2)
scaled_vector = scalar_multiply(2, v1)
dot_value = dot_product(v1, v2)


section("1. What is a vector?")
print("A vector is an ordered collection of numbers.")
print("In machine learning, it often represents one data point or one set of weights.")
print(f"Example: v1 = {v1}")
show_diagram(
    "Text diagram:",
    """
          y
          ^
          |
      3   |        * (2, 3)
          |      /
          |    /
          |  /
          |/
    -------O--------------------> x

    O = origin = (0, 0)
    v1 = [2, 3]
    """.strip("\n"),
)


section("2. Types of vectors")
print("Vectors can be classified in different ways.")
print("These are the most common beginner-level types of vectors.")
show_diagram(
    "Text diagram:",
    """
    Zero vector       = [0, 0]
    Unit vector       = length 1
    Row vector        = [1, 2, 3]
    Column vector     = [[1], [2], [3]]
    Equal vectors     = same values and same direction
    Negative vectors  = opposite direction
    """.strip("\n"),
)
print("1. Zero vector: all values are 0. Example: [0, 0]")
print("2. Unit vector: vector with length 1. Example: [1, 0]")
print("3. Row vector: written in one row. Example: [1, 2, 3]")
print("4. Column vector: written in one column. Example: [[1], [2], [3]]")
print("5. Equal vectors: same magnitude and same direction")
print("6. Negative vectors: same magnitude but opposite direction")


section("3. Row vector, column vector, and matrix")
print("A row vector is written horizontally.")
print("A column vector is written vertically.")
print("A matrix is a rectangular table of numbers made of rows and columns.")
show_diagram(
    "Text diagram:",
    """
    Row vector:
    [1  2  3]

    Column vector:
    [1]
    [2]
    [3]

    Matrix:
    [1  2  3]
    [4  5  6]
    """.strip("\n"),
)
print("Row vector example: [1, 2, 3]")
print("It has 1 row and 3 columns.")
print("Column vector example:")
print("[[1], [2], [3]]")
print("It has 3 rows and 1 column.")
print("Matrix example:")
print("[[1, 2, 3], [4, 5, 6]]")
print("It has 2 rows and 3 columns.")
print("A vector is a special case of a matrix.")
print("Row vector = 1 x n matrix")
print("Column vector = n x 1 matrix")


section("4. Span of vectors")
print("Span means all possible vectors we can make using scalar multiplication and addition.")
print("If we combine vectors in different amounts, the full set of results is called the span.")
show_diagram(
    "Text diagram:",
    """
    Let:
    v1 = [1, 0]
    v2 = [0, 1]

    Any vector in the span looks like:
    a*v1 + b*v2

    = a*[1, 0] + b*[0, 1]
    = [a, b]

    So these two vectors can reach the whole 2D plane.
    """.strip("\n"),
)
print("Example 1:")
print("If v1 = [1, 0] and v2 = [0, 1], their span covers the full 2D plane.")
print("Because we can make [a, b] for any numbers a and b.")
print("Example 2:")
print("If v1 = [1, 0] only, its span is just a line on the x-axis.")
print("So span can be a point, a line, a plane, or even higher-dimensional space.")


section("5. Dimension of a vector")
print("Dimension means how many values are inside the vector.")
print("[5] has dimension 1")
print("[2, 3] has dimension 2")
print("[2, 3, 4] has dimension 3")
show_diagram(
    "Text diagram:",
    """
    [5]           -> 1D
    [2, 3]        -> 2D
    [2, 3, 4]     -> 3D
    [1, 5, 9, 2]  -> 4D
    """.strip("\n"),
)


section("6. Vector addition")
print(f"v1 = {v1}")
print(f"v2 = {v2}")
print(f"v1 + v2 = {vector_addition}")
print("Addition means add matching positions.")
show_diagram(
    "Text diagram:",
    """
    v1 = [2, 3]
    v2 = [4, 1]

    [2, 3]
    [4, 1]
    ------
    [6, 4]

    Geometric idea:
    Move v2 to the tip of v1.
    The final arrow from origin is v1 + v2.
    """.strip("\n"),
)


section("7. Vector subtraction")
print(f"v1 - v2 = {vector_subtraction}")
print("Subtraction also happens position by position.")
show_diagram(
    "Text diagram:",
    """
    v1 = [2, 3]
    v2 = [4, 1]

    [2, 3]
    [4, 1]
    ------
    [-2, 2]

    Subtraction tells us how to move from v2 to v1.
    """.strip("\n"),
)


section("8. Scalar multiplication")
print(f"2 * {v1} = {scaled_vector}")
print("A scalar is a single number.")
print("Scalar multiplication stretches or shrinks the vector.")
show_diagram(
    "Text diagram:",
    """
    v  = [2, 3]
    2v = [4, 6]

    Same direction, bigger length

          *
         /
        /      2v
       /
      *   v
     /
    O---------------------------->
    """.strip("\n"),
)


section("9. Dot product")
print(f"v1 . v2 = {dot_value}")
print("Formula: (2 x 4) + (3 x 1) = 11")
print("Dot product is useful for measuring similarity and making predictions.")
show_diagram(
    "Text diagram:",
    """
    v1 = [2, 3]
    v2 = [4, 1]

    Dot product:
    (2 x 4) + (3 x 1)
    = 8 + 3
    = 11
    """.strip("\n"),
)


section("10. Why vectors matter in machine learning")
print("Vectors are everywhere in machine learning.")
print("A row in a dataset can be a vector.")
print("Weights in a model can be a vector.")
print("Predictions often involve vector operations.")
show_diagram(
    "Text diagram:",
    """
    One student record:
    [age, study_hours, attendance]
    [19, 6, 92]

    One model weight vector:
    [0.5, 1.2, 0.8]

    Prediction idea:
    input . weights
    """.strip("\n"),
)


section("11. Practice questions")
print("1. Which type of vector is [0, 0, 0]?")
print("2. Write [1, 2, 3] as a row vector.")
print("3. Write [1, 2, 3] as a column vector.")
print("4. What is the span of [1, 0]?")
print("5. What is the span of [1, 0] and [0, 1]?")


section("12. Diagram file")
build_svg()
print(f"Graphical diagram saved to: {SVG_PATH}")
print("Open the SVG file in a browser to view the visual explanation.")


section("13. Final idea")
print("Think of a vector as a container of numbers.")
print("Those numbers can describe position, features, or model weights.")
print("If you understand row vectors, column vectors, matrices, span,")
print("and basic operations, you have a strong foundation.")
