from ultralytics import YOLO
model = YOLO("yolov8n.pt")                    # ou chemin vers votre .pt
model.export(format="ncnn", half=True, dynamic=False)
print("→ Export NCNN généré dans yolov8n_ncnn_model/")
