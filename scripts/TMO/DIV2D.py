import typing
import numpy as np
import pyqtgraph as pg
import ami.graph_nodes as gn
from amitypes import Array1d, Array2d
from ami.flowchart.library.common import CtrlNode
from ami.flowchart.library.DisplayWidgets import Histogram2DWidget
from pyqtgraph import QtCore



class DIV2DProc(object):

    def __init__(self,args):
    
        self.args = args


    def __call__(self, arr1,arr2):  
            

        return arr1/arr2 


class DIV2D(CtrlNode):

    """
    numpy.array2d division
    """

    nodeName = "DIV2D"



                  # entry point must be called func
    

    def __init__(self, name):
        super().__init__(name, terminals={'arr1': {'io': 'in', 'ttype': Array2d},
                                          'arr2': {'io': 'in', 'ttype': Array2d},
                                          'out': {'io': 'out', 'ttype': Array2d}})

    def to_operation(self, inputs, conditions={}):
        outputs = self.output_vars()

        node = gn.Map(name=self.name()+"_operation",
                      condition_needs=conditions,
                      inputs=inputs, outputs=outputs, parent=self.name(),
                      func=DIV2DProc(self.values))
        return node                
