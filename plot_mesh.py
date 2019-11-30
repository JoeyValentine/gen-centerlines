import pyvista as pv


def confirm():
    if len(plotter.picked_path.points) == 2:
        plotter.close()


if __name__ == '__main__':
    vti_file_name = 'level_sets.vti'

    data = pv.read(vti_file_name)
    vol = data.threshold_percent(30, invert=1)
    surf = vol.extract_geometry()
    smooth_surf = surf.smooth(n_iter=1000)

    plotter = pv.Plotter()
    plotter.add_mesh(smooth_surf, style='wireframe', color='black')
    plotter.add_key_event('a', confirm)
    plotter.enable_path_picking(color='red')

    plotter.show()

    points = plotter.picked_path.points
    print(points)
