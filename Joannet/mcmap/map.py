from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget

# Always start by initializing Qt (only once per application)
app = QApplication([])

# Define a window
window = QMainWindow()
window.setWindowTitle("Minecraft Map Viewer")

# Create a widget to hold the layout
layout_widget = QWidget()
window.setCentralWidget(layout_widget)

# Create a layout
layout = QGridLayout()
layout_widget.setLayout(layout)

# Show the window
window.show()

# Start the event loop
app.exec_()
