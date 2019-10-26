import pyvista as pv
import sys

from PyQt5 import Qt


class MainWindow(Qt.QMainWindow):

    def __init__(self, vti_file_name: str, parent=None):
        Qt.QMainWindow.__init__(self, parent)

        self.vti_file_name = vti_file_name

        # create the frame
        self.frame = Qt.QFrame()
        vlayout = Qt.QVBoxLayout()

        # add the pyvista interactor object
        self.vtk_widget = pv.QtInteractor(self.frame)
        vlayout.addWidget(self.vtk_widget)

        self.frame.setLayout(vlayout)
        self.setCentralWidget(self.frame)

        # simple menu to demo functions
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu('File')
        exitButton = Qt.QAction('Exit', self)
        exitButton.setShortcut('Ctrl+Q')
        exitButton.triggered.connect(self.close)
        fileMenu.addAction(exitButton)

        # allow adding a sphere
        meshMenu = mainMenu.addMenu('Mesh')
        self.add_sphere_action = Qt.QAction('Add Sphere', self)
        self.add_sphere_action.triggered.connect(self.add_sphere)
        meshMenu.addAction(self.add_sphere_action)

    def add_sphere(self) -> None:
        """ add a sphere to the pyqt frame """
        data = pv.read(self.vti_file_name)
        vol = data.threshold_percent(30, invert=1)
        surf = vol.extract_geometry()
        smooth_surf = surf.smooth(n_iter=1000)
        self.vtk_widget.add_mesh(smooth_surf)
        self.vtk_widget.reset_camera()


if __name__ == '__main__':
    app = Qt.QApplication(sys.argv)
    window = MainWindow('level_sets.vti')
    window.show()
    sys.exit(app.exec_())
