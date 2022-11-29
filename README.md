# PaddleCompletion: A Unified Framework for Depth Completion
</div>

<div align="center">

[English](README_模板.md)| [简体中文](README_zh-CN.md)

</div>
A lightweight, easy-to-extend, easy-to-learn, high-performance, and for-fair-comparison toolkit based 
on PaddlePaddle for Depth Completion. It is a part of the Paddledepth project.


## Implemented Algorithms

As initial version, we support the following algoirthms. We are working on more algorithms. Of course, you are welcome to add your algorithms here.

1. [CFNet (CVPR2021)[1]](CFNet/README.md)
2. [FCFRNet (AAAI2021)](model_document/FCFRNet/README.md)

Please click the hyperlink of each algorithm for more detailed explanation.

## Installation

You can either git clone this whole repo by:

```
git clone https://github.com/imexb9584/Paddle_FCFRNet.git
cd Paddle-completion
pip install -r requirements.txt
```

## Dataset 
see guidance in [dataset_prepare](data_prepare/data_prepare.md) for dataset preparation.

## Usage

### Training

1. Modify the configuration file in the corresponding directories,must confirm ``evaluate`` get `None`.

2.Run the `train.py` with specified config
```bash

python Trainer.py -c ./model_document/FCFRNet/FCFRNet.yaml
```


### Test
1. Modify the configuration file in the corresponding directories,must confirm ``evaluate`` get the path of weight value.
2. If you want to try run fcfrnet,please download weight from [this](https://aistudio.baidu.com/aistudio/datasetdetail/176607)
3. Run the `train.py` with specified config
```bash

python train.py -c ./model_document/FCFRNet/FCFRNet.yaml
```


## Customization

It is easy to design your own method following the 3 steps:

1. Check whether your method requires new loss functions, if so, add your loss in the `loss_funcs`
2. Check and write your own model's to `model`
3. Write your own config file (.yaml) in model_doucument file



## Results

We present results of our implementations on  benchmarks: KITTI2015. 
We did not perform careful parameter tuning and simply used the default config files. 
You can easily reproduce our results using provided shell scripts!


### Paddle Completion TestData On KITTI2015

| Method  | RMSE    | MAE     | Photo | iRMSE | iMAE  | RMSE1   | RMSE2   |
|---------|---------|---------|-------|-------|-------|---------|---------|
| FCFRNet | 784.224 | 222.639 | 0.000 | 2.370 | 1.014 | 784.224 | 784.224 |




## Contribution

The toolkit is under active development and contributions are welcome! 
Feel free to submit issues or emails to ask questions or contribute your code. 
If you would like to implement new features, please submit a issue or emails to discuss with us first.

## Acknowledgement
PaddleDepth is an open source project that is contributed by researchers and engineers 
from various colleges and companies. 
We appreciate all the contributors who implement their methods or add new features, 
as well as users who give valuable feedbacks. 
We wish that the toolbox and benchmark could serve the growing research community by 
providing a flexible toolkit to reimplement existing methods and develop their new algorithms.

## References

[1] Liu, L., Song, X., Lyu, X., Diao, J., Wang, M., Liu, Y., & Zhang, L. (2021). FCFR-Net: Feature Fusion based Coarse-to-Fine Residual Learning for Depth Completion. Proceedings of the AAAI Conference on Artificial Intelligence, 35(3), 2136-2144. https://doi.org/10.1609/aaai.v35i3.16311


[comment]: <> (## Citation)

[comment]: <> (If you think this toolkit or the results are helpful to you and your research, please cite us!)

[comment]: <> (```)

[comment]: <> (@Misc{deepda,)

[comment]: <> (howpublished = {\url{https://github.com/jindongwang/transferlearning/tree/master/code/DeepDA}},   )

[comment]: <> (title = {DeepDA: Deep Domain Adaptation Toolkit},  )

[comment]: <> (author = {Wang, Jindong and Hou, Wenxin})

[comment]: <> (}  )

[comment]: <> (```)



## Contact

- [Wenxin Hou](https://houwenxin.github.io/): houwx001@gmail.com
- [Zhelun Shen](https://github.com/gallenszl): shenzhelun@pku.edu.cn
- [Bing Xiong](https://github.com/imexb9584): bingxiong9527@siat.edu.cn