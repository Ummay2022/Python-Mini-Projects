class Forecast:
    def __init__(self, rainfall, descriptors):
        self.rainfall = rainfall
        self.descriptors = descriptors
       
    def dataPreparation(self):
        for j in range(len(self.rainfall[0])):
            for i in range(len(self.rainfall)):
                if self.rainfall[i][j] < 0:
                    if self.descriptors[j] == "sunny":
                        self.rainfall[i][j] = 0
                    elif self.descriptors[j] == "thunderstorm":
                            self.rainfall[i][j] = abs(self.rainfall[i][j])
                    elif self.descriptors[j] == "rainy":
                            #Array to store positive values
                            positive_values = [] 
                            for k in range(len(self.rainfall)):
                                if k != i and self.rainfall[k][j] >= 0:
                                    positive_values.append(self.rainfall[k][j])
                                    if len(positive_values) > 0:
                                        self.rainfall[i][j] = sum(positive_values) // len(positive_values)
                                    elif (len(positive_values) == 0):
                                        self.rainfall[i][j] = 0
                   
                   
    
    def totalRainfall(self):
        total = 0
        for i in range(len(self.rainfall)):
            for j in range(len(self.rainfall[i])):
                if self.rainfall[i][j] >= 0:
                    total += max(0, self.rainfall[i][j])
        return total

    def trend(self, n):
        total_precipitation = 0
        for i in range(len(self.rainfall)):
            for j in range(len(self.rainfall[i])):
                if j >= len(self.rainfall[i]) - n:
                    total_precipitation += self.rainfall[i][j]
        avg_precipitation = total_precipitation // (len(self.rainfall) * n)
        if avg_precipitation < 50:
            return "sunny"
        elif avg_precipitation >= 50 and avg_precipitation != 75:
            return "rainy"
        else:
            return "thunderstorm"
