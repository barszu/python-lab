def find_polygon(polygons, mouse_pos):
    for p in polygons:
        x, y = mouse_pos
        if p.mask.get_at((x, y)):
            return p
    return None

