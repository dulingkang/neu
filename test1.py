import inspect
import re
import textwrap


class A:

  def __init__(self):
    pass

  def update(self):
    print(300)
    return 300

  def compile_func(self, func):
    func_source = inspect.getsource(func)
    func_source_dedented = textwrap.dedent(func_source)
    new_source = re.sub(r'300', '500', func_source_dedented)
    compiled_func = compile(new_source, '<string>', 'exec')
    exec(compiled_func, globals(), locals())
    return locals()[func.__name__]


a = A()
f = a.compile_func(a.update)
f(a)  # 需要传入实例对象
