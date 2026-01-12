import ast
from analyzer.syntax_checker import SyntaxChecker
from analyzer.logic_checker import LogicChecker
from analyzer.complexity_analyzer import ComplexityAnalyzer
from analyzer.suggestions import SuggestionEngine

def review_code(code):
    tree = ast.parse(code)

    syntax = SyntaxChecker()
    syntax.visit(tree)
    syntax.report_unused_variables()

    logic = LogicChecker()
    logic.visit(tree)

    complexity = ComplexityAnalyzer()
    complexity.visit(tree)

    suggestions = SuggestionEngine()

    print("\n🔍 PY CODE REVIEW REPORT\n")

    if syntax.issues:
        print("⚠️ Syntax & Usage Issues:")
        for issue in syntax.issues:
            print("-", issue)

    if logic.issues:
        print("\n⚠️ Logic Issues:")
        for issue in logic.issues:
            print("-", issue)

    print("\n⏱ Estimated Time Complexity:", complexity.estimate())

    print("\n💡 Suggestions:")
    for tip in suggestions.get_suggestions():
        print("-", tip)

if __name__ == "__main__":
    with open("samples/bad_code.py") as f:
        review_code(f.read())
