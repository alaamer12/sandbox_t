import sys

def sandbox_code(code):
    # Define a dictionary for the locals() namespace
    local_vars = {}
    # Define a dictionary for the globals() namespace
    global_vars = {}
    # Set some restricted built-in functions and modules
    restricted_builtins = {
        '__import__': None,
        'input': None,
        'open': None,
        'exec': None,
        'eval': None,
        'compile': None,
        'dir': None,
        'globals': None,
        'locals': None,
        'vars': None,
        'sys': None,
    }
    # Create a custom print function
    def custom_print(*args, **kwargs):
        print(*args, **kwargs)
    restricted_builtins['print'] = custom_print
    # Execute the code in a restricted environment
    try:
        exec(code, {'__builtins__': restricted_builtins}, local_vars)
    except Exception as e:
        print("Error:", e)
    # Return the local variables after execution
    return local_vars

# Example usage
code = """
a = 1
b = 2
print("Sum:", a + b)
print("System path:", sys.path)
"""

sandboxed_vars = sandbox_code(code)
print("Sandboxed vars:", sandboxed_vars)
