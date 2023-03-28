from jax.tree_util import register_pytree_node
import jax.numpy as jnp
from neuron import Neuron


class LIF(Neuron):

  def __init__(self, size, V_th=20.0, v_init=-55.0, V_rest=-60.0, R=1.0, tau=20.0, I_e=0.0) -> None:
    super(LIF, self).__init__()
    self.size = size
    self.v_init = v_init
    self.v = self.set_value('v', jnp.ones(size) * self.v_init)
    self.spike = self.set_value('spike', jnp.zeros(size, dtype=bool))
    self.V_th = V_th
    self.V_rest = V_rest
    self.R = R
    self.tau = tau
    self.I_e = 0

  def update(self):
    import jax.numpy as jnp
    from share_manager import ShareManager

    def step(v, I, V_rest, R, tau):
      # TODO(@hj): Now, dt is currently set to a fixed value of 0.1 for just-in-time compilation, but will be changed to a variable later
      dt = 0.1
      # TODO(@hj): By default, the first argument is a variable that will change if there is a better alternative
      val = v

      a = (-v + V_rest + R * I) / tau
      b = -0.5
      exp_b = (jnp.exp(b * dt) - 1) / (dt * b)
      return val + dt * exp_b * a

    v = step(self.v, self.I_e, self.V_rest, self.R, self.tau)
    self.spike = v >= self.V_th
    self.v = v


def node_maker(node):
  return ((node.size, node.V_th, node.v_init, node.V_rest, node.R, node.tau, node.I_e), ())


register_pytree_node(LIF, node_maker, lambda _, xs: LIF(*xs))
