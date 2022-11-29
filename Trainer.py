from train import FCFRNet_train
from utils.config import  get_config
import argparse
import os

parser = argparse.ArgumentParser(description='Sparse-to-Dense train')
parser.add_argument('-c',
                    '--config',
                    type=str,
                    help="the path of config yaml"

)

args = parser.parse_args()
configs=get_config(args.config)
assert  configs.train_mode in ["dense", "sparse", "photo", "sparse+photo", "dense+photo"],"train mode only can be \"dense\", \"sparse\", \"photo\", \"sparse+photo\", \"dense+photo\""
assert  configs.val in ["select", "full"],"val mode only can be \"select\", \"full\""
assert  configs.dataset["input_mode"] in ['d', 'rgb', 'rgbd', 'g', 'gd'],"input mode only can be \'d\', \'rgb\', \'rgbd\', \'g\', \'gd\'"

if __name__ == '__main__':
    if configs.model_name == "fcfrnet":
        FCFRNet_train(configs)

