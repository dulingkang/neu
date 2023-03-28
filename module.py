from name import Name
from typing import Callable
import inspect
import re
import textwrap


class Module(object):

  def __init__(self) -> None:
    from share_manager import ShareManager
    self.name = Name.get_name(self.__class__.__name__)
    ShareManager.dic[self.name] = {}
    ShareManager.modules.append(self)

  def set_value(self, name, value):
    from share_manager import ShareManager

    ShareManager.dic[self.name][name] = value
    return value

  def get_value(self, name):
    from share_manager import ShareManager

    return ShareManager.dic[self.name].get(name, None)

  def __hash__(self) -> int:
    return hash((self.name))

  def __eq__(self, __value: object) -> bool:
    return (isinstance(__value, Module)) and (self.name == __value.name)

  def compile_func(self, func: Callable) -> Callable:
    from share_manager import ShareManager

    func_source = inspect.getsource(func)
    func_source = textwrap.dedent(func_source)

    attr_names = re.findall(r'self\.(\w+)\s=', func_source)
    for attr_name in attr_names:
      if attr_name not in ShareManager.dic[self.name]:
        raise ValueError(f"Attribute '{attr_name}' not found in ShareManager.dic[{self.name}]")
    new_source = re.sub(r'self\.(\w+)\s=', lambda match: f"ShareManager.dic[self.name]['{match.group(1)}'] =",
                        func_source)
    compiled_func = compile(new_source, '<string>', 'exec')
    exec(compiled_func, globals(), locals())
    return locals()[func.__name__]
