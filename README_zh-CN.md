# PaddleCompletion: 一个关于深度图补全的统一框架
</div>

<div align="center">

[English](README_模板.md)| [简体中文](README_zh-CN.md)

</div>
PaddleCompletion 是一款基于 PaddlePaddle 的深度补全工具箱，是 PaddleDepth项目的成员之一。
它具有可扩展性，容易上手的特点，此外它在相同的训练策略和环境下公平比较了双目立体匹配领域里面SOTA(state-of-the-art)的算法

## 基准测试和模型库

作为初始版本，PaddleCompletion目前支持以下算法。


1. [CFNet (CVPR2021)[1]](model_document/CFNet/README.md)
2. [FCFRNet (AAAI2021)](model_document/FCFRNet/README.md)

请点击上方的超链接查看每个算法的实现细节

## 安装

你可以通过如下命令下载PaddleStereo工具箱

<font color="red"> 


</font>

```
git clone https://github.com/imexb9584/Paddle_FCFRNet.git
pip install -r requirements.txt
```

## 数据集准备
你可以参照 [dataset_prepare](data_prepare/data_prepare.md) 来进行数据集的准备.

## 如何使用

### Training

1. 修改相应目录中的配置文件 ,必须确保yaml文件中的 ``evaluate`` 键匹配的值是 `None`.

2.Run the `Trainer.py` with specified config
```bash

python Trainer.py -c ./model_document/FCFRNet/FCFRNet.yaml
```


### Test
1.修改相应目录中的配置文件 ,必须确保yaml文件中的 ``evaluate`` 键能够匹配到权重文件地址的值.
2.如果您想尝试FCFRNet的运行，请先从 [this](https://aistudio.baidu.com/aistudio/datasetdetail/176607)下载权重文件
3以配置参数文件运行 `train.py` 文件
```bash

python train.py -c ./model_document/FCFRNet/FCFRNet.yaml
```



## 定制化算法

你可以按照如下步骤开发自己的算法:

1. 检查你的模型是否需要新的损失函数来进行训练，如果有把损失函数加入到 `loss_funcs`中
2. 检查你的模型是否需要模型来进行训练，如果有把模型加入到 `model`中
3. 加入你自己的配置文件（.sh or .yaml）

## 结果

我们在KITTI2015以及KITTI2012上评测了paddle Completion已经实现的算法. 

注意我们并没有通过额外的技巧来优化模型结果，因此你可以直接使用.sh的脚本文件来复现我们在表格中报告的精度

### Depth Completion

| Method  | RMSE    | MAE     | Photo | iRMSE | iMAE  | 
|---------|---------|---------|-------|-------|-------|
| FCFRNet | 784.224 | 222.639 | 0.000 | 2.370 | 1.014 |




## 贡献

PaddleCompletion工具箱目前还在积极维护与完善过程中。 我们非常欢迎外部开发者为PaddleCompletion提供新功能\模型。 如果您有这方面的意愿的话，请往我们的邮箱或者issue里面反馈
## 感谢
PaddleCompletion 是一款由来自不同高校和企业的研发人员共同参与贡献的开源项目。
我们感谢所有为项目提供算法复现和新功能支持的贡献者，以及提供宝贵反馈的用户。 
我们希望这个工具箱和基准测试可以为社区提供灵活的代码工具，供用户复现已有算法并开发自己的新模型，从而不断为开源社区提供贡献。

## 参考文献

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



## 联系方式


- [Wenxin Hou](https://houwenxin.github.io/): houwx001@gmail.com
- [Zhelun Shen](https://github.com/gallenszl): shenzhelun@pku.edu.cn
- [Bing Xiong](https://github.com/imexb9584): xb1personal0mailbox@gmail.com
