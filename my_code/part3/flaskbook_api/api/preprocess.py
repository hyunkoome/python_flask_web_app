# 학습 완료 모델에 입렵하기 쉽게 데이터를 정돈하는 전처리

import torchvision


def image_to_tensor(image):
    """이미지 데이터를 텐서형의 수치 데이터로 변환"""
    image_tensor = torchvision.transforms.functional.to_tensor(image)
    return image_tensor
