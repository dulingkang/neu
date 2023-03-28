from lif import LIF
from snet import SNet
import time


class Net(SNet):
  def __init__(self) -> None:
    super().__init__()
    for _ in range(1000):
      LIF(4000)


net = Net()
t0 = time.time()
net(sim_t=2.0)
t1 = time.time()
print(t1 - t0)
