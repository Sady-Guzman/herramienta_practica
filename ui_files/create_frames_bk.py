
from PySide6.QtWidgets import QFrame, QLabel, QLineEdit

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        # Your existing setup code...

        # Connect the button to the method
        self.btn_acpt_cant.clicked.connect(self.generate_frames)
        
        # Keep track of the last Y position for the frames
        self.last_frame_y = 270  # This is where t_frame3 ends

    def generate_frames(self):
        # Get the number of frames to generate from the spinbox
        num_frames = self.spin_cant.value()
        
        # Loop to create the frames
        for i in range(num_frames):
            self.create_frame(i + 4)  # Start from t_frame4, t_frame5, etc.

    def create_frame(self, frame_num):
        # Create a new frame below the last one
        new_frame = QFrame(self.Dialog)
        new_frame.setObjectName(f"t_frame{frame_num}")
        new_frame.setGeometry(QRect(20, self.last_frame_y + 50, 591, 41))
        new_frame.setFrameShape(QFrame.Shape.StyledPanel)
        new_frame.setFrameShadow(QFrame.Shadow.Raised)

        # Add the components inside the frame (just like in t_frame1)
        label_name = QLabel(f"T{frame_num}", new_frame)
        label_name.setGeometry(QRect(0, 10, 31, 16))
        
        input_op = QLineEdit(new_frame)
        input_op.setObjectName(f"t{frame_num}_op")
        input_op.setGeometry(QRect(530, 10, 51, 21))

        input_bs = QLineEdit(new_frame)
        input_bs.setObjectName(f"t{frame_num}_bs")
        input_bs.setGeometry(QRect(110, 10, 51, 21))

        input_a = QLineEdit(new_frame)
        input_a.setObjectName(f"t{frame_num}_a")
        input_a.setGeometry(QRect(320, 10, 51, 21))

        input_cg = QLineEdit(new_frame)
        input_cg.setObjectName(f"t{frame_num}_cg")
        input_cg.setGeometry(QRect(390, 10, 51, 21))

        input_h = QLineEdit(new_frame)
        input_h.setObjectName(f"t{frame_num}_h")
        input_h.setGeometry(QRect(180, 10, 51, 21))

        input_bi = QLineEdit(new_frame)
        input_bi.setObjectName(f"t{frame_num}_bi")
        input_bi.setGeometry(QRect(40, 10, 51, 21))

        input_i = QLineEdit(new_frame)
        input_i.setObjectName(f"t{frame_num}_i")
        input_i.setGeometry(QRect(460, 10, 51, 21))

        input_d = QLineEdit(new_frame)
        input_d.setObjectName(f"t{frame_num}_d")
        input_d.setGeometry(QRect(250, 10, 51, 21))

        # Update the last frame's Y-position
        self.last_frame_y += 50  # Increase by the height of the frame (41px) + some spacing


''' version 2 de create_frame()'''


def create_frame(self, frame_num):
    # Create a new frame below the last one
    new_frame = QFrame(self.Dialog)
    new_frame.setObjectName(f"t_frame{frame_num}")
    new_frame.setGeometry(QRect(20, self.last_frame_y + 50, 591, 41))
    new_frame.setFrameShape(QFrame.Shape.StyledPanel)
    new_frame.setFrameShadow(QFrame.Shadow.Raised)

    # Add components to the frame
    label_name = QLabel(f"T{frame_num}", new_frame)
    label_name.setGeometry(QRect(0, 10, 31, 16))

    input_op = QLineEdit(new_frame)
    input_op.setObjectName(f"t{frame_num}_op")
    input_op.setGeometry(QRect(530, 10, 51, 21))

    input_bs = QLineEdit(new_frame)
    input_bs.setObjectName(f"t{frame_num}_bs")
    input_bs.setGeometry(QRect(110, 10, 51, 21))

    input_a = QLineEdit(new_frame)
    input_a.setObjectName(f"t{frame_num}_a")
    input_a.setGeometry(QRect(320, 10, 51, 21))

    input_cg = QLineEdit(new_frame)
    input_cg.setObjectName(f"t{frame_num}_cg")
    input_cg.setGeometry(QRect(390, 10, 51, 21))

    input_h = QLineEdit(new_frame)
    input_h.setObjectName(f"t{frame_num}_h")
    input_h.setGeometry(QRect(180, 10, 51, 21))

    # Update the last frame's Y position
    self.last_frame_y = new_frame.geometry().bottom()


''' ----------------------------------------------------   '''

# Should look like this:
def create_frame(self, frame_id):
    new_frame = QFrame(self.Dialog)
    new_frame.setObjectName(f"t_frame{frame_id}")
    # Set layout and components inside the frame
    layout = QVBoxLayout(new_frame)
    label = QLabel(f"New Frame {frame_id}", new_frame)
    layout.addWidget(label)
    new_frame.setLayout(layout)
    
    # Show the frame (if it's not automatically visible)
    new_frame.show()

