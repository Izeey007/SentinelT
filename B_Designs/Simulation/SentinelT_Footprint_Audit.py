import bpy
from mathutils import Vector

MAX_X_MM = 500.0
MAX_Y_MM = 500.0
scene = bpy.context.scene


def get_scene_bounds():
    points = []
    depsgraph = bpy.context.evaluated_depsgraph_get()

    for obj in scene.objects:
        if obj.type != 'MESH' or obj.hide_get():
            continue
        evaluated = obj.evaluated_get(depsgraph)
        for corner in evaluated.bound_box:
            points.append(evaluated.matrix_world @ Vector(corner))

    if not points:
        return None

    min_x = min(p.x for p in points)
    max_x = max(p.x for p in points)
    min_y = min(p.y for p in points)
    max_y = max(p.y for p in points)
    min_z = min(p.z for p in points)
    max_z = max(p.z for p in points)

    return {
        'x_mm': (max_x - min_x) * 1000.0,
        'y_mm': (max_y - min_y) * 1000.0,
        'z_mm': (max_z - min_z) * 1000.0,
    }


original_frame = scene.frame_current
results = []
failed = []

for frame in range(scene.frame_start, scene.frame_end + 1):
    scene.frame_set(frame)
    bpy.context.view_layer.update()
    bounds = get_scene_bounds()
    if bounds is None:
        continue

    passed = bounds['x_mm'] <= MAX_X_MM and bounds['y_mm'] <= MAX_Y_MM
    results.append((frame, bounds['x_mm'], bounds['y_mm'], bounds['z_mm'], passed))
    if not passed:
        failed.append(results[-1])

scene.frame_set(original_frame)

if not results:
    raise RuntimeError('No visible mesh geometry found.')

max_x = max(results, key=lambda r: r[1])
max_y = max(results, key=lambda r: r[2])
max_z = max(results, key=lambda r: r[3])

print('SENTINELT FOOTPRINT AUDIT')
print(f'Maximum X: {max_x[1]:.2f} mm (frame {max_x[0]})')
print(f'Maximum Y: {max_y[2]:.2f} mm (frame {max_y[0]})')
print(f'Maximum Z: {max_z[3]:.2f} mm (frame {max_z[0]})')
print(f'Frames checked: {len(results)}')
print(f'Failed frames: {len(failed)}')
print('STATUS:', 'PASS' if not failed else 'FAIL')
