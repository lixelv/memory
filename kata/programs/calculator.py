import re

def find_deepest_expr(expr):
    stack = []
    max_depth = 0
    deepest_expr = ""

    for i, char in enumerate(expr):
        if char == "(":
            stack.append(i)
        elif char == ")":
            if stack:
                start = stack.pop()
                depth = len(stack)

                if depth > max_depth:
                    max_depth = depth
                    deepest_expr = expr[start:i+1]

    while deepest_expr.startswith("(") and deepest_expr.endswith(")"):
        deepest_expr = deepest_expr[1:-1]

    if deepest_expr and not (deepest_expr.startswith("(") and deepest_expr.endswith(")")):
        deepest_expr = "(" + deepest_expr + ")"

    return deepest_expr if deepest_expr else expr

def solve_expression(expr):
    result = re.findall(r'(?:(?<=[\+\-\*\/\^])|^)(-?\d*\.?\d+(?:e\-?\d+)?)|([\+\-\*\/\^])', expr.replace("(", ""))
    result = [float(i) if i not in "-+/*^" else i for j in result for i in j if i]
    while len(result) > 1:
        i = 1
        while i < len(result):
            if result[i] == "^":
                result[i-1:i+2] = [result[i-1] ** result[i+1]]
                i -= 2
            i += 2
        while i < len(result):
            if result[i] in "*/":
                result[i-1:i+2] = [result[i-1] * result[i+1]] if result[i] == "*" else [result[i-1] / result[i+1]]
                i -= 2
            i += 2
            
        i = 1
        while i < len(result):
            if result[i] in "+-":
                result[i-1:i+2] = [result[i-1] + result[i+1]] if result[i] == "+" else [result[i-1] - result[i+1]]
                i -= 2
            i += 2
    return result[0]
        
def calc(expr):
    expr = expr.replace(" ", "").replace("**", "^")
    expr = "(" + expr + ")"
    while "(" in expr:
        expr = expr.replace('--', '+').replace('+-', '-').replace('*+', '*').replace('/+', '/').replace("(+", "(")
        deepest_expr = find_deepest_expr(expr)
        result = solve_expression(deepest_expr)
        expr = expr.replace(deepest_expr, str(result))
    return float(solve_expression(expr)) if float(expr) % 1 != 0 else int(solve_expression(expr.replace('.0', '')))

if __name__ == "__main__":
    print(calc(input()))