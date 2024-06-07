import numpy as np
from algorithm import *

class SyntheticData:
    def __init__(self, num_people, num_ads, num_billboards, matrix_size, categories, colors):
        if num_ads > num_billboards:
            raise ValueError("Number of ads should be less than number of billboards")
        self.num_people = num_people
        self.num_ads = num_ads
        self.num_billboards = num_billboards
        self.matrix_size = matrix_size
        self.categories = categories
        self.colors = colors

        self.matrix = np.zeros((self.matrix_size, self.matrix_size))

        # self.billboards = self.generate_billboards_bias()
        self.billboards = self.generate_billboards_data()
        
        self.people = self.generate_people_data()
        # self.people = self.generate_people_bias()
        
        self.ads = self.generate_ads_bias()
        # self.ads = self.generate_ads_data()

        # algorithm1(self.people, self.billboards, self.ads)
        algorithm2(self.people, self.billboards, self.ads)

    def generate_people_bias(self):
        np.random.seed(0)
        cluster = self.num_people // 4
        categories = [self.categories[0]] * cluster + [self.categories[1]] * cluster + [self.categories[2]] * cluster + [self.categories[3]] * cluster
        x = np.concatenate((np.random.randint(0, self.matrix_size / 2, cluster), np.random.randint(self.matrix_size / 2, self.matrix_size, cluster), np.random.randint(0, self.matrix_size / 2, cluster), np.random.randint(self.matrix_size / 2, self.matrix_size, cluster)))
        y = np.concatenate((np.random.randint(0, self.matrix_size / 2, cluster * 2), np.random.randint(self.matrix_size / 2, self.matrix_size, cluster * 2)))

        data = {
            'person_id': np.arange(self.num_people),
            'x': x,
            'y': y,
            'category': categories
        }

        for i in range(cluster):
            new_x = data['x'][i]
            new_y = data['y'][i]
            while self.matrix[new_x][new_y] > 0:
                new_x = np.random.randint(0, self.matrix_size / 2)
                new_y = np.random.randint(0, self.matrix_size / 2)
            data['x'][i] = new_x
            data['y'][i] = new_y
            self.matrix[new_x][new_y] = 1

        for i in range(cluster, 2 * cluster):
            new_x = data['x'][i]
            new_y = data['y'][i]
            while self.matrix[new_x][new_y] > 0:
                new_x = np.random.randint(self.matrix_size / 2, self.matrix_size)
                new_y = np.random.randint(0, self.matrix_size / 2)
            data['x'][i] = new_x
            data['y'][i] = new_y
            self.matrix[new_x][new_y] = 1

        for i in range(2 * cluster, 3 * cluster):
            new_x = data['x'][i]
            new_y = data['y'][i]
            while self.matrix[new_x][new_y] > 0:
                new_x = np.random.randint(0, self.matrix_size / 2)
                new_y = np.random.randint(self.matrix_size / 2, self.matrix_size)
            data['x'][i] = new_x
            data['y'][i] = new_y
            self.matrix[new_x][new_y] = 1

        for i in range(3 * cluster, self.num_people):
            new_x = data['x'][i]
            new_y = data['y'][i]
            while self.matrix[new_x][new_y] > 0:
                new_x = np.random.randint(self.matrix_size / 2, self.matrix_size)
                new_y = np.random.randint(self.matrix_size / 2, self.matrix_size)
            data['x'][i] = new_x
            data['y'][i] = new_y
            self.matrix[new_x][new_y] = 1

        return [[i, x, y, inte] for i, x, y, inte in zip(data['person_id'], data['x'], data['y'], data['category'])]

    def generate_people_data(self):
        np.random.seed(0)
        data = {
            'person_id': np.arange(self.num_people),
            'x': np.random.randint(0, self.matrix_size, self.num_people),
            'y': np.random.randint(0, self.matrix_size, self.num_people),
            'category': np.random.choice(self.categories, self.num_people)
        }

        for i in range(self.num_people):
            new_x = data['x'][i]
            new_y = data['y'][i]
            while self.matrix[new_x][new_y] > 0:
                new_x = np.random.randint(0, self.matrix_size)
                new_y = np.random.randint(0, self.matrix_size)

            data['x'][i] = new_x
            data['y'][i] = new_y

            self.matrix[new_x][new_y] = 1

        return [[i, x, y, inte] for i, x, y, inte in zip(data['person_id'], data['x'], data['y'], data['category'])]

    def generate_ads_bias(self):
        ads_per_category = self.num_ads // len(self.categories)
        
        ads_distribution = []
        for i in range(len(self.categories)):
            ads_distribution += [self.categories[i]] * ads_per_category

        data = {
            'ads_id': np.arange(self.num_ads),
            'category': ads_distribution
        }

        return [[i, cat] for i, cat in zip(data['ads_id'], data['category'])]

    def generate_ads_data(self):
        np.random.seed(1)
        data = {
            'ads_id': np.arange(self.num_ads),
            'category': np.random.choice(self.categories, self.num_ads),
        }
        return [[i, cat] for i, cat in zip(data['ads_id'], data['category'])]

    def generate_billboards_bias(self):
        
        data = {
            'billboard_id': np.arange(self.num_billboards),
            'x': [self.matrix_size // 4, self.matrix_size // 4, self.matrix_size * 3 // 4, self.matrix_size * 3 // 4],
            'y': [self.matrix_size // 4, self.matrix_size * 3 // 4, self.matrix_size // 4, self.matrix_size * 3 // 4],
            'ads_id': [-1, -1, -1, -1]
        }

        for i in range(4):
            self.matrix[data['x'][i]][data['y'][i]] = 2

        return [[i, x, y, aid] for i, x, y, aid in zip(data['billboard_id'], data['x'], data['y'], data['ads_id'])]

    def generate_billboards_data(self):
        np.random.seed(2)
        data = {
            'billboard_id': np.arange(self.num_billboards),
            'x': np.random.randint(0, self.matrix_size, self.num_billboards),
            'y': np.random.randint(0, self.matrix_size, self.num_billboards),
            'ads_id': np.full(self.num_billboards, -1)
        }

        for i in range(self.num_billboards):
            self.matrix[data['x'][i]][data['y'][i]] = 2

        return [[i, x, y, aid] for i, x, y, aid in zip(data['billboard_id'], data['x'], data['y'], data['ads_id'])]
    
    def draw_people(self, display):
        for i in range(self.num_people):
            display.draw_circle(self.people[i][1], self.people[i][2], self.colors[self.people[i][3]])
        
    def draw_billboards(self, display):
        for i in range(self.num_billboards):
            color = (0,0,0) if self.billboards[i][3] == -1 else self.colors[self.ads[self.billboards[i][3]][1]]
            display.draw_rect(self.billboards[i][1], self.billboards[i][2], color)

    def update_person(self, p_id, dire):
        new_x = self.people[p_id][1] + dire[0]
        new_y = self.people[p_id][2] + dire[1]
        if new_x < 0 or new_x >= self.matrix_size:
            return
        if new_y < 0 or new_y >= self.matrix_size:
            return
        if self.matrix[new_x][new_y] > 0:
            return
        
        self.matrix[self.people[p_id][1]][self.people[p_id][2]] = 0
        self.people[p_id][1] = new_x
        self.people[p_id][2] = new_y
        self.matrix[new_x][new_y] = 1

if __name__ == "__main__":
    data = SyntheticData(5, 5, 5, 20, ['technology', 'fashion', 'food'], {'technology': (155, 0, 0), 'fashion': (0, 155, 0), 'food': (0, 0, 155)})
    for i in data.people:
        print(i)
    
    print()
    for i in data.billboards:
        print(i)