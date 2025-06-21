# file: code_checker.py

import ast

def check_python_code(code):
    try:
        tree = ast.parse(code)
        function_names = [node.name for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)]
        return {"status": "success", "functions": function_names}
    except SyntaxError as e:
        return {"status": "error", "message": str(e)}
