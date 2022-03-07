from .events import GeneralQueueHandler
from .wavefronts import W
from .spirals import NodeRegion
from .spiraltree import SpiralTree

import numpy as np
from matplotlib import pyplot as plt
from core.treebuilder.local_utils import tdraw

def buildTree(root=(0, 0), leaves=None, b=1.9):
    
    stacked = np.column_stack(leaves)
    
    extent = [(stacked[0].min(), stacked[1].min()), (stacked[0].max(), stacked[1].max())] # (lowerleft), (upperright)

    never_activated = [NodeRegion(b=b, root=root, leaf=leaf) for leaf in leaves]
    
    queue = GeneralQueueHandler(never_activated) # assign NodeRegions for leaves as terminal events
    w = W()
    T = SpiralTree()
    for event in queue:
        event(w, T, queue, extent=extent)
        # queue.delete(event)
        print(len(queue))
        # tdraw(list(T.nodes)[1:])
        # plt.show()
        # if len(queue) == 13:
        #     break
    return T


if __name__ == "__main__":
    leaves = [ (17, -4), (20, 7), (-10, 15), (-5, 20), (-8, -20), (20, 0), (5, 10), (22, 4), (-30, 5), (-35, -6)]
    buildTree(leaves=leaves)

