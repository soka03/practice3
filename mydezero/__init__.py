if '__file__' in globals():
    import os, sys
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))




is_simple_core = False  # True

if is_simple_core:
    from mydezero.core_simple import Variable
    from mydezero.core_simple import Function
    from mydezero.core_simple import using_config
    from mydezero.core_simple import no_grad
    from mydezero.core_simple import as_array
    from mydezero.core_simple import as_variable
    from mydezero.core_simple import setup_variable
else:
    from mydezero.core import Variable
    from mydezero.core import Function
    from mydezero.core import using_config
    from mydezero.core import no_grad
    from mydezero.core import as_array
    from mydezero.core import as_variable
    from mydezero.core import setup_variable
    
setup_variable()