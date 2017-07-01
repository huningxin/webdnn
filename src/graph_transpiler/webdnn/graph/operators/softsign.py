from typing import Optional

from webdnn.graph.operator import Operator
from webdnn.graph.operators.attributes.elementwise import Elementwise
from webdnn.graph.operators.attributes.inplace import Inplace
from webdnn.graph.variable import Variable


class Softsign(Operator):
    """Softsign activation

    https://www.tensorflow.org/api_docs/python/tf/nn/softsign
    x / (abs(x) + 1)

    Args:
        name (str): Operator name.

    """

    def __init__(self, name: Optional[str]):
        super().__init__(name)
        self.attributes = {Elementwise(self),
                           Inplace(self, "x", "y")}

    def __call__(self, x: Variable):
        """
        Args:
            x (:class:`~webdnn.graph.variable.Variable`): Input

        Returns:
            tuple of :class:`~webdnn.graph.variable.Variable`: Output
        """
        y = Variable(x.shape, x.order)
        self.append_input("x", x)
        self.append_output("y", y)
        return y,
