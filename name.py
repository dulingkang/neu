# Copyright (c) 2023 CNAEIT
#
# Licensed under the Apache License, Version 2.0 (the 'License');
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an 'AS IS' BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


class Name(object):
  """
  A class that generates unique names based on a given string.

  This class keeps track of how many times a given string has been used as a name,
  and appends an increasing number to it every time it is requested again.

  Parameters
  ----------
  n : str
    The base string to generate names from.
  """
  names = {}

  @classmethod
  def get_name(cls, n: str):
    """
    Returns a unique name based on the given string.

    Parameters
    ----------
    n : str
      The base string to generate names from.

    Returns
    -------
    str
      A unique name that consists of the base string and an increasing number.
    """
    count = cls.names.get(n, -1)
    cls.names[n] = count + 1
    return n + str(count + 1)
