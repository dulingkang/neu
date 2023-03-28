from module import Module
from neuron import Neuron
import jax


class SNet(Module):

  def __init__(self, dt=0.1) -> None:
    super().__init__()
    self.dt = dt

  def __call__(self, *args, **kwargs):
    from share_manager import ShareManager
    sim_t = kwargs.get('sim_t', 1.0)

    neurons = [m for m in ShareManager.modules if isinstance(m, Neuron)]

    jax.jit(_step(neurons, 0.1))


def _step(neurons, dt):

  def update_neuron(neuron):
    return neuron()

  jax.lax.scan(update_neuron, None, neurons)
