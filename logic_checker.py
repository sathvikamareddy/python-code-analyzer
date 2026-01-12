import ast

class LogicChecker(ast.NodeVisitor):
    def __init__(self):
        self.issues = []

    def visit_For(self, node):
        if isinstance(node.iter, ast.Call):
            if hasattr(node.iter.func, "id") and node.iter.func.id == "range":
                self.issues.append(
                    "Avoid using range(len()). Use direct iteration instead."
                )
        self.generic_visit(node)
