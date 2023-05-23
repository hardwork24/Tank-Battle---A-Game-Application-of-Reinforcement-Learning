from tankbattle.env.sprites.wall import WallSprite
from tankbattle.env.constants import GlobalConstants
from tankbattle.env.manager import ResourceManager


class StageMap(object):
    def __init__(self, num_of_tiles, tile_size, current_path, sprites, walls, resources_manager):
        self.num_of_stages = 1
        self.num_of_tiles = num_of_tiles
        self.map = [None] * self.num_of_stages
        self.current_path = current_path
        self.sprites = sprites
        self.walls = walls
        self.tile_size = tile_size
        self.rc = resources_manager

        self.__build_map()

    def __build_map(self):


        self.map[0] = [[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
                       [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
                       [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
                       [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
                       [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
                       [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
                       [-1, -1,  0,  0,  0,  0,  2,  0,  0,  0,  0, -1, -1],
                       [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
                       [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
                       [-1, -1,  1, -1, -1, -1, -1, -1, -1, -1,  1, -1, -1],
                       [-1, -1, -1, -1, -1, 0 , 0 , 0 , -1, -1, -1, -1, -1],
                       [-1, -1, -1, -1, -1, 0 , -1, 0 , -1, -1, -1, -1, -1],
                       [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]]



    def load_map(self, stage):
        if stage >= self.num_of_stages:
            raise ValueError("Stage out of range !!!")


        # This is for static map
        for row in range(len(self.map[stage])):
            for col in range(len(self.map[stage][row])):
                if self.map[stage][row][col] == GlobalConstants.WALL_TILE:
                    wall_bg = self.rc.get_image(ResourceManager.SOFT_WALL)
                    wall = WallSprite(self.tile_size, col, row, wall_bg)
                    wall.type = GlobalConstants.SOFT_OBJECT
                    self.sprites.add(wall)
                    self.walls.add(wall)
                elif self.map[stage][row][col] == GlobalConstants.ROCK_TILE:
                    wall_bg = self.rc.get_image(ResourceManager.HARD_WALL)
                    wall = WallSprite(self.tile_size, col, row, wall_bg)
                    wall.type = GlobalConstants.HARD_OBJECT
                    self.sprites.add(wall)
                    self.walls.add(wall)
                elif self.map[stage][row][col] == GlobalConstants.SEA_TILE:
                    wall_bg = self.rc.get_image(ResourceManager.SEA_WALL)
                    wall = WallSprite(self.tile_size, col, row, wall_bg)
                    wall.type = GlobalConstants.TRANSPARENT_OBJECT
                    self.sprites.add(wall)
                    self.walls.add(wall)

    def number_of_stages(self):
        return self.num_of_stages