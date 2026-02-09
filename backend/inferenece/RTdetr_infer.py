# from multiprocessing import freeze_support
# import os
# os.environ['PYTORCH_ALLOC_CONF'] = 'expandable_segments:True'
# import torch

# def main():
#     from ultralytics import RTDETR

#     print("Clearing CUDA cache before training...\n")
#     torch.cuda.empty_cache()
#     model = RTDETR("/mnt/local/rishinew/REAL_PEST_DETETCTION/runs/detect/train2/weights/best.pt")

#     results = model("/mnt/local/rishinew/REAL_PEST_DETETCTION/test_files/Rootworm", save=True, device="cpu", conf=0.4, name="tets/Rootworm", verbose=True)
    
#     print("\nClearing CUDA cache after training...\n")
#     torch.cuda.empty_cache()

# if __name__ == '__main__':
#     freeze_support()
    
    
from ultralytics import RTDETR

model = RTDETR("models/best.pt")

results = model(r"test_files\snail", save=True, device="cuda", conf=0.4, name="result", verbose=True)