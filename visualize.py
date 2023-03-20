import copy
import sys
from PyQt5.QtWidgets import *

from ui.window import Window


def preprocess_data(data_dict):
    """
    Preprocess 3d data
    Transformation between unreal coordination (example data) and qt coordination
    y_qt = -y_unreal
    """
    data_dict = copy.deepcopy(data_dict)

    for k, v in data_dict.items():
        if k in ['gt3d', 'pred3d', 'camera', 'map_center']:
            data_dict[k][..., 1] *= -1
    return data_dict


if __name__ == '__main__':


    meta_info = {
        'skeleton': [[10, 8], [8, 6], [11, 9], [9, 7], [6, 7], [0, 6], [1, 7], [0, 1], [0, 2],
        [1, 3], [2, 4], [3, 5],[0, 12], [1, 13], [12, 13]],
        'preprocess_func': preprocess_data,
        # RGB
        'camera_colors': [[255, 0, 0], [0, 255, 0], [0, 0, 255], [255, 0, 255], [0, 255, 255], [255, 255, 0],],
        'human_colors': [[126, 12, 250], [1, 17, 250], [12, 153, 250], [250, 249, 25], [250, 158, 25],
                       [12, 250, 226], [0, 250, 82], [81, 250, 12], [250, 96, 25], [250, 25, 230]],
        'symbols': ['t', 'o', '+', 's', 'p', 'h', 'star', 'd', 't1', 't2', 't3'],
    }

    app = QApplication(sys.argv)
    win = Window(meta_info)
    win.show()
    sys.exit(app.exec())  # block
