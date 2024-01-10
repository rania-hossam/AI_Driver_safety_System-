import torch
import cv2
from ultralytics import YOLO



class Road_instances_segmentation:
    def __init__(self, model_name):
        self.model = self.load_model(model_name)
        self.classes = self.model.names
        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'
        print('Using Device:', self.device)
    
    def get_video_capture(self):
        return cv2.VideoCapture(0)
    
    def load_model(self, model_name):
        model = YOLO(model_name)
        return model
    
    def score_frame(self, frame):
        self.model.to(self.device)
        frame = [frame]
        results = self.model(frame)
        box, labels,= results[0].boxes.xyxy.cpu(), results[0].boxes.cls.cpu()
        return labels , box
    
    def class_to_label(self, x):
        return self.classes[int(x)]
    
    def plot_boxes(self, results, frame):
        labels , box = results
        n = len(labels)
        x_shape, y_shape = frame.shape[1], frame.shape[0]
        for i in range(n):
            row = box[i]
            if row[3] >= 0.2:
                x1, y1, x2, y2 = map(int, row[:4])
                bgr = (0, 255, 255)
                cv2.rectangle(frame, (x1, y1), (x2, y2), bgr, 2)
                cv2.putText(frame, self.class_to_label(labels[i]), (x1, y1-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, bgr, 2)
        return frame
    

    def __call__(self):
        cap = self.get_video_capture()
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            results = self.score_frame(frame)
            frame2 = self.plot_boxes(results, frame)
            try:
                labels, cords = results
                n = len(labels)
                x_shape, y_shape = frame.shape[1], frame.shape[0]
            except Exception as e:
                print("ERROR: " + str(e))

            cv2.imshow("frame", frame2)
            if cv2.waitKey(5) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()

detector = Road_instances_segmentation(model_name= 'Road_instances_segmentation.pt')
detector()