# CFNet(CVPR 2021)
A paddle implementation of the paper CFNet: Cascade and Fused Cost Volume for Robust Stereo Matching, 
[\[CVPR 2021\]](https://openaccess.thecvf.com/content/CVPR2021/html/Shen_CFNet_Cascade_and_Fused_Cost_Volume_for_Robust_Stereo_Matching_CVPR_2021_paper.html)

<font color="red"> 大家根据自己复现的任务对应修改readme里面的abstract，training，evaluation代码以及模型文件（模型文件可以暂时空着）

注意一定要有可以直接复现出结果的.sh文件以及对应模型
</font>

## Abstract
Recently, the ever-increasing capacity of large-scale annotated datasets has led to profound progress in stereo matching. However, most of these successes are limited to a specific dataset and cannot generalize well to other datasets. The main difficulties lie in the large domain differences and unbalanced disparity distribution across a variety of datasets, which greatly limit the real-world applicability of current deep stereo matching models. In this paper, we propose CFNet, a Cascade and Fused cost volume based network to improve the robustness of the stereo matching network. First, we propose a fused cost volume representation to deal with the large domain difference. By fusing multiple low-resolution dense cost volumes to enlarge the receptive field, we can extract robust structural representations for initial disparity estimation. Second, we propose a cascade cost volume representation to alleviate the unbalanced disparity distribution. Specifically, we employ a variance-based uncertainty estimation to adaptively adjust the next stage disparity search space, in this way driving the network progressively prune out the space of unlikely correspondences. By iteratively narrowing down the disparity search space and improving the cost volume resolution, the disparity estimation is gradually refined in a coarse-tofine manner. When trained on the same training images and evaluated on KITTI, ETH3D, and Middlebury datasets with the fixed model parameters and hyperparameters, our proposed method achieves the state-of-the-art overall performance and obtains the 1st place on the stereo task of Robust Vision Challenge 2020.


## Training
**Scene Flow Datasets Pretraining**

run the script `./scripts/sceneflow.sh` to pre-train on Scene Flow datsets. Please update `DATAPATH` in the bash file as your training data path.

**Finetuning**

run the script `./scripts/robust.sh` to jointly finetune the pre-train model on four datasets,
i.e., KITTI 2015, KITTI2012, ETH3D, and Middlebury. Please update `DATAPATH` and `--loadckpt` as your training data path and pretrained SceneFlow checkpoint file.

## Evaluation
**Joint Generalization**

run the script `./scripts/eth3d_save.sh"`, `./scripts/mid_save.sh"` and `./scripts/kitti15_save.sh` to save png predictions on the test set of the ETH3D, Middlebury, and KITTI2015 datasets. Note that you may need to update the storage path of save_disp.py, i.e., `fn = os.path.join("/home3/raozhibo/jack/shenzhelun/cfnet/pre_picture/"`, fn.split('/')[-2]).

**Corss-domain Generalization**

run the script `./scripts/robust_test.sh"` to test the cross-domain generalizaiton of the model (Table.3 of the main paper). Please update `--loadckpt` as pretrained SceneFlow checkpoint file.

## Models

[Pretraining Model](https://drive.google.com/file/d/1gFNUc4cOCFXbGv6kkjjcPw2cJWmodypv/view?usp=sharing)
You can use this checkpoint to reproduce the result reported in Table.3 of the main paper

[Finetuneing Moel](https://drive.google.com/file/d/1H6L-lQjF4yOxq23wxs3HW40B-0mLxUiI/view?usp=sharing)
You can use this checkpoint to reproduce the result reported in the stereo task of Robust Vision Challenge 2020

## Citation
If you find this code useful in your research, please cite:
```
@InProceedings{Shen_2021_CVPR,
    author    = {Shen, Zhelun and Dai, Yuchao and Rao, Zhibo},
    title     = {CFNet: Cascade and Fused Cost Volume for Robust Stereo Matching},
    booktitle = {Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)},
    month     = {June},
    year      = {2021},
    pages     = {13906-13915}
}
```