import os
import wandb

from utils import *
from dataset import CrearDataset, LoadTestDataset, LoadForPrediction 
#from train import ModelGeneration, TrainModel
from predict import SavePredictions_new, LoadModel
# from predict_sint import SavePredictions_new, LoadModel
#from evaluation import ShowPredictions, ShowTable, ConfusionMatrix

if __name__ == "__main__":
    EXPERIMENT = 'final_unet_model'
    
    cfg = LoadParams('experiments/'+ EXPERIMENT + '.json')
    os.environ["CUDA_VISIBLE_DEVICES"]=cfg["CUDA_VISIBLE_DEVICES"]
  #  os.environ["WANDB_API_KEY"] = '665e68bb4dd1224ff5144638d4a66a290f925520'
  #  wandb.login()
   
    model = LoadModel(cfg)

    Images = LoadForPrediction(cfg, path='/home/ALBA/unet/smoke_dataset/goproNoIrShabeni1', ext='*.JPG')

    save_path = "/home/ALBA/unet/predictions_ronan/"
    SavePredictions_new(model, Images, cfg, save_path)

    