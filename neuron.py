from module import Module
from typing import Any


class Neuron(Module):
  def __init__(self) -> None:
    super().__init__()

  def __call__(self, *args: Any, **kwds: Any) -> Any:
    compiled_method = self.compile_func(self.update)
    compiled_method(self)

  def update(self):
    pass
