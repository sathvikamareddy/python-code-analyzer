import ast

class SyntaxChecker(ast.NodeVisitor):
    def __init__(self):
        self.issues = []
        self.assigned = set()
        self.used = set()

    def visit_Assign(self, node):
        for target in node.targets:
            if isinstance(target, ast.Name):
                self.assigned.add(target.id)
        self.generic_visit(node)

    def visit_Name(self, node):
        if isinstance(node.ctx, ast.Load):
            self.used.add(node.id)
        self.generic_visit(node)

    def report_unused_variables(self):
        for var in self.assigned:
            if var not in self.used:
                self.issues.append(
                    "Variable '{}' is assigned but never used.".format(var)
                )
