import itertools
import re

# Logical implies
def implies(p, q):
    return (not p) or q

# Convert symbols to Python format
def convert_symbols(expr):
    expr = expr.replace('^', ' and ')
    expr = expr.replace('v', ' or ')
    expr = expr.replace('!', ' not ')

    # Handle implication (->)
    # This pattern looks for basic variables or groups inside parentheses
    pattern = r'(\w+|\([^()]*\))\s*->\s*(\w+|\([^()]*\))'
    while re.search(pattern, expr):
        expr = re.sub(pattern, r'implies(\1, \2)', expr)
    
    return expr

# Extract variables
def get_variables(expr):
    tokens = re.findall(r'\b[A-Za-z]+\b', expr)
    keywords = {"and", "or", "not", "implies"}
    return sorted(set(t for t in tokens if t.lower() not in keywords))

# Extract sub-expressions (simple)
def get_subexpressions(expr):
    subs = set()
    # Find things inside ()
    subs.update(re.findall(r'\([^()]+\)', expr))
    # Find things with NOT
    subs.update(re.findall(r'not\s+\w+', expr))
    return list(subs)

# Evaluate expression
def evaluate(expr, values):
    local_dict = dict(values)
    local_dict["implies"] = implies
    return eval(expr, {}, local_dict)

# Convert back to logical symbols
def pretty(e):
    return (e.replace('and', '^')
             .replace('or', 'v')
             .replace('not', '!')
             .replace('implies', '->'))

# Main function
def truth_table():
    user_expr = input("Enter expression using ^ v ! -> :\n ")
    expr = convert_symbols(user_expr)

    variables = get_variables(expr)
    sub_exprs = get_subexpressions(expr)
    all_exprs = sub_exprs + [expr]

    headers = variables + [pretty(e) for e in all_exprs]
    col_width = max(len(h) for h in headers) + 2

    print("\nTruth Table:\n")

    # Header
    for h in headers:
        print(h.center(col_width), end="|")
    print()

    print("-" * (col_width * len(headers)))

    # Rows
    for combo in itertools.product([False, True], repeat=len(variables)):
        values = dict(zip(variables, combo))

        # Variable values
        for v in variables:
            val = 'T' if values[v] else 'F'
            print(val.center(col_width), end="|")

        # Expression values
        try:
            for e in all_exprs:
                result = evaluate(e, values)
                val = 'T' if result else 'F'
                print(val.center(col_width), end="|")
        except Exception as err:
            print(f"\nError: {err}")
            return
        
        print()

# Run program
if __name__ == "__main__":
    truth_table()