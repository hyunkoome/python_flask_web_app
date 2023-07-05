import torch
# import torchvision
from torchvision.models.detection import maskrcnn_resnet50_fpn, MaskRCNN_ResNet50_FPN_Weights

if __name__ == "__main__":
    # weights=MaskRCNN_ResNet50_FPN_Weights.DEFAULT
    # weights=MaskRCNN_ResNet50_FPN_Weights.COCO_V1
    model = maskrcnn_resnet50_fpn(weights=MaskRCNN_ResNet50_FPN_Weights.COCO_V1)
    torch.save(model, 'flaskbook_api/model.pt')

