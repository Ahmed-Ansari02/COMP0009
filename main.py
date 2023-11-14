# Propositional logic

proposition_letters = {"p", "q", "r", "s"}
operations = {"1": "IMPLICATION", "2": "OR", "3": "AND"}


class Formula:
    def __init__(self, left=None, right=None, op=None, symbol=None):
        self.symbol = symbol
        self.left = left
        self.right = right
        self.op = op

    def __str__(self):
        return f"Formula(Symbol: {self.symbol} Left: {self.left} Operation: {self.op} Right: {self.right})"


def check_formula(formula):
    stack = []
    for char in formula:
        if char == "(":
            stack.append(char)
        elif char == ")":
            if len(stack) == 0:
                return False
            stack.pop()
    return len(stack) == 0


def parse_tree(formula):
    print(formula)
    if len(formula) == 1 and formula in proposition_letters:
        return Formula(symbol=formula)
    elif formula and formula[0] == "(":
        if not check_formula(formula):
            raise Exception("Invalid formula")
        for i in range(len(formula)):
            if formula[i] == ")" and check_formula(formula[1:i]):
                if i == len(formula) - 1:
                    return parse_tree(formula[1:-1])
                else:
                    left = parse_tree(formula[1:i])
                    op = operations[formula[i + 1]]
                    right = parse_tree(formula[i + 2 :])
                    return Formula(left, right, op=op)
    for char in formula:
        if char in operations:
            op = operations[char]
            left = parse_tree(formula[: formula.index(char)])
            right = parse_tree(formula[formula.index(char) + 1 :])
            return Formula(left, right, op)


def clean_formula(formula):
    formula = formula.replace("=>", "1")
    formula = formula.replace("\/", "2")
    formula = formula.replace("/\ ", "3")
    formula = formula.replace(" ", "")
    return formula


formula = input("Enter a formula: ")
formula = clean_formula(formula)

print(formula)
print(parse_tree(formula))
