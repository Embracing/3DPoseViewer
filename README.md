# 3DPoseViewer

<div align="left">

  <a>![Python 3.9+](https://img.shields.io/badge/Python-3.9%2B-brightgreen.svg)</a>
  <a href="https://github.com/metaopt/torchopt/blob/HEAD/LICENSE">![License](https://img.shields.io/github/license/metaopt/torchopt?label=license&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCIgd2lkdGg9IjI0IiBoZWlnaHQ9IjI0IiBmaWxsPSIjZmZmZmZmIj48cGF0aCBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik0xMi43NSAyLjc1YS43NS43NSAwIDAwLTEuNSAwVjQuNUg5LjI3NmExLjc1IDEuNzUgMCAwMC0uOTg1LjMwM0w2LjU5NiA1Ljk1N0EuMjUuMjUgMCAwMTYuNDU1IDZIMi4zNTNhLjc1Ljc1IDAgMTAwIDEuNUgzLjkzTC41NjMgMTUuMThhLjc2Mi43NjIgMCAwMC4yMS44OGMuMDguMDY0LjE2MS4xMjUuMzA5LjIyMS4xODYuMTIxLjQ1Mi4yNzguNzkyLjQzMy42OC4zMTEgMS42NjIuNjIgMi44NzYuNjJhNi45MTkgNi45MTkgMCAwMDIuODc2LS42MmMuMzQtLjE1NS42MDYtLjMxMi43OTItLjQzMy4xNS0uMDk3LjIzLS4xNTguMzEtLjIyM2EuNzUuNzUgMCAwMC4yMDktLjg3OEw1LjU2OSA3LjVoLjg4NmMuMzUxIDAgLjY5NC0uMTA2Ljk4NC0uMzAzbDEuNjk2LTEuMTU0QS4yNS4yNSAwIDAxOS4yNzUgNmgxLjk3NXYxNC41SDYuNzYzYS43NS43NSAwIDAwMCAxLjVoMTAuNDc0YS43NS43NSAwIDAwMC0xLjVIMTIuNzVWNmgxLjk3NGMuMDUgMCAuMS4wMTUuMTQuMDQzbDEuNjk3IDEuMTU0Yy4yOS4xOTcuNjMzLjMwMy45ODQuMzAzaC44ODZsLTMuMzY4IDcuNjhhLjc1Ljc1IDAgMDAuMjMuODk2Yy4wMTIuMDA5IDAgMCAuMDAyIDBhMy4xNTQgMy4xNTQgMCAwMC4zMS4yMDZjLjE4NS4xMTIuNDUuMjU2Ljc5LjRhNy4zNDMgNy4zNDMgMCAwMDIuODU1LjU2OCA3LjM0MyA3LjM0MyAwIDAwMi44NTYtLjU2OWMuMzM4LS4xNDMuNjA0LS4yODcuNzktLjM5OWEzLjUgMy41IDAgMDAuMzEtLjIwNi43NS43NSAwIDAwLjIzLS44OTZMMjAuMDcgNy41aDEuNTc4YS43NS43NSAwIDAwMC0xLjVoLTQuMTAyYS4yNS4yNSAwIDAxLS4xNC0uMDQzbC0xLjY5Ny0xLjE1NGExLjc1IDEuNzUgMCAwMC0uOTg0LS4zMDNIMTIuNzVWMi43NXpNMi4xOTMgMTUuMTk4YTUuNDE4IDUuNDE4IDAgMDAyLjU1Ny42MzUgNS40MTggNS40MTggMCAwMDIuNTU3LS42MzVMNC43NSA5LjM2OGwtMi41NTcgNS44M3ptMTQuNTEtLjAyNGMuMDgyLjA0LjE3NC4wODMuMjc1LjEyNi41My4yMjMgMS4zMDUuNDUgMi4yNzIuNDVhNS44NDYgNS44NDYgMCAwMDIuNTQ3LS41NzZMMTkuMjUgOS4zNjdsLTIuNTQ3IDUuODA3eiI+PC9wYXRoPjwvc3ZnPgo=)</a>

</div>

A python viewer for visualizing 3D human poses and facilitating debugging of pose related tasks. This code supplements the following paper:
> [Proactive Multi-Camera Collaboration for 3D Human Pose Estimation (ICLR 2023)](https://openreview.net/pdf?id=CPIy9TWFYBG)

<p align="center">
  <img style='width : 90%' src="./docs/demo.gif" />
</p>

## Features

* Support multi-human and multi-camera.
* Written in python, easy to use and hack.
* Based on Qt, easy to add various interactive widgets.

## Install

Requirements:

* python >= 3.9
* numpy
* [pyqtgraph](https://github.com/pyqtgraph/pyqtgraph)
  * PyQt5
  * pyopengl
  * cupy (optional)
* pyav
* pims

```shell
pip install -r requirements.txt
```

## Quickstart

1. Save your 3d pose data as a numpy data file ```.npz```.
2. Save 2D images captured from different views as seperate video files ```.mp4```.
3. Open them with the visualizer.

```python
python -m visualize  # open the example data under /examples/seq1
```

## Feed Your Own Data

<details>

<summary>3D data (.npz file)</summary>

* `gt3d`: GT 3d human pose sequence. Numpy array of shape `[t, max_Ngt, j, 3]`. `t`: frame id. `max_Ngt`: max number of gt humans across the whole sequence. Fill zeros for missing humans and joints. `[j, 3]`: 3D location of j joints.

* `pred3d`: Predicted 3d human pose sequence. Numpy array of shape `[t, max_Npred, j, 3]`. max_Npred: max number of pred humans. Fill zeros for missing humans and joints.

* `camera (optional)`: camera location sequence. Numpy array of shape `[t, max_c, 5, 3]`. `max_c`: max number of cameras in a frame. More detailes can be found [here](docs/Camera.md).

* `map_center (optional)`: center of map, used to offset the ground plane. Default to `[0, 0, 0]`.

</details>

<details>

<summary>2D view (optional)</summary>

* Video files, `.mp4, .mov, .avi`, the same length as 3D data.

</details>

## Citation

If you find this viewer helpful, please cite:

```bibtex
@inproceedings{ciproactive,
  title={Proactive Multi-Camera Collaboration for 3D Human Pose Estimation},
  author={Ci, Hai and Liu, Mickel and Pan, Xuehai and Zhong, Fangwei and Wang, Yizhou},
  booktitle={International Conference on Learning Representations},
  year={2023}
}
```

## License

Apache License, Version 2.0.
