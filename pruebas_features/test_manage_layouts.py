''' ejemplo generado por gpt para manejo de elementos dinamicos'''

from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit
)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dynamic Layouts with Uniform LineEdits")

        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)

        # Dictionary to track layouts and their line edits
        self.vertical_layouts = {}  # {layout_key: {index: QLineEdit}}

        # Button to add new layouts
        self.add_layout_button = QPushButton("Add Vertical Layout")
        self.add_layout_button.clicked.connect(self.add_vertical_layout)
        self.main_layout.addWidget(self.add_layout_button)

        # Button to add a new LineEdit to all layouts
        self.add_line_edit_button = QPushButton("Add LineEdit to All Layouts")
        self.add_line_edit_button.clicked.connect(self.add_line_edit_to_all_layouts)
        self.main_layout.addWidget(self.add_line_edit_button)

        # Button to read all LineEdits
        self.read_all_button = QPushButton("Read All LineEdits")
        self.read_all_button.clicked.connect(self.read_all_line_edits)
        self.main_layout.addWidget(self.read_all_button)

    def add_vertical_layout(self):
        """Create and add a new vertical layout."""
        # Generate a unique key for the new layout
        layout_key = f"Layout_{len(self.vertical_layouts) + 1}"

        # Create a new vertical layout and widget container
        new_layout = QVBoxLayout()
        layout_container = QWidget()
        layout_container.setLayout(new_layout)
        self.main_layout.addWidget(layout_container)

        # Add an empty dictionary to track LineEdits in this layout
        self.vertical_layouts[layout_key] = {"layout": new_layout, "line_edits": {}}

        # Ensure all layouts have the same number of LineEdits
        current_line_edit_count = len(next(iter(self.vertical_layouts.values()))["line_edits"]) if self.vertical_layouts else 0
        for i in range(current_line_edit_count):
            self.add_line_edit_to_specific_layout(layout_key, i + 1)

        print(f"Added {layout_key}")

    def add_line_edit_to_all_layouts(self):
        """Add a new LineEdit to all existing layouts."""
        if not self.vertical_layouts:
            print("No layouts available to add a LineEdit.")
            return

        # Determine the index for the new LineEdit
        new_line_edit_index = len(next(iter(self.vertical_layouts.values()))["line_edits"]) + 1

        # Add a LineEdit to each layout
        for layout_key in self.vertical_layouts.keys():
            self.add_line_edit_to_specific_layout(layout_key, new_line_edit_index)

    def add_line_edit_to_specific_layout(self, layout_key, line_edit_index):
        """Add a LineEdit to a specific layout."""
        layout_data = self.vertical_layouts[layout_key]

        # Create a new LineEdit
        line_edit = QLineEdit()
        line_edit.setPlaceholderText(f"{layout_key} LineEdit {line_edit_index}")

        # Add the LineEdit to the layout and track it
        layout_data["layout"].addWidget(line_edit)
        layout_data["line_edits"][line_edit_index] = line_edit
        print(f"Added LineEdit {line_edit_index} to {layout_key}")

    def read_all_line_edits(self):
        """Read and print the values of all LineEdits in all layouts."""
        for layout_key, layout_data in self.vertical_layouts.items():
            print(f"--- {layout_key} ---")
            for index, line_edit in layout_data["line_edits"].items():
                print(f"  LineEdit {index}: {line_edit.text()}")

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()