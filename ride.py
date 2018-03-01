class Ride:
    def __init__(self, start_pos, end_pos, earliest_step, latest_step, r_id):
        self.start_pos = start_pos
        self.end_pos = end_pos
        self.earliest_step = earliest_step
        self.latest_step = latest_step
        self.id = r_id

    def distance(self):
        return abs(self.end_pos[0] - self.start_pos[0]) + abs(self.end_pos[1] - self.start_pos[1])
