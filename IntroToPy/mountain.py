import ast

class Mountain:
    def __init__(self, name, height, country,cod):
        self.name = name
        self.height = height
        self.country = country
        self.cod = cod

    def __str__(self):
        return f"{self.name} ({self.height} m) in {self.country}"

    def __repr__(self):
        return f"Mountain(name={self.name}, height={self.height}, country={self.country})"

def load_mountain(mountains_file):
    mountain_data = {}
    mountain_height={}
    count = 0
    with open(mountains_file, "r", encoding="utf-8") as data_file:
        for line in data_file:
            parts = line.strip().split('\t') 
            mountain1 = Mountain(
                name=parts[0],
                height=parts[1] if parts[1] != 'NULL' else None,
                country=parts[2],
                cod=parts[3]
            )
            if mountain1.height is None:
                count+=1
            mountain_data[mountain1.cod] = mountain1
            mountain_height[mountain1.height]=mountain1
            sorted_randoms = sorted(mountain_height.keys())
    return mountain_data, len(mountain_data.keys()),count,sorted_randoms

if __name__ == "__main__":
    mountain_data, long,count,sorted_randoms = load_mountain("IntroToPy/mountains_db.tsv")
    print(f"Loaded {long} unique country generated in a sequence.") 
    print(f"Number of mountains with no height: {count}")
    print(f"Min random: {sorted_randoms[0]}; Max random: {sorted_randoms[-1]}")
