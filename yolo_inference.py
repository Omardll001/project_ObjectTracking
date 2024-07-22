from ultralytics import YOLO

model = YOLO("models/best.pt")  # load a pretrained model

result = model.predict('input_videos/madrid vs city.mp4', save=True)  # predict on an image

print(result[0])

print('--------------------------------')

for box in result[0].boxes:
    print(box)
    
    