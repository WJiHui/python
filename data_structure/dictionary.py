
def init_dict_fromkeys():
    a = dict.fromkeys(["k1", "k2", "k3"], [])
    print(a)  # {'k1': [], 'k2': [], 'k3': []}

    a["k1"].append(12)
    print(a)  # {'k1': [12], 'k2': [12], 'k3': [12]}  所有的values都是一样的

    a["k2"].append(34)
    print(a)  # {'k1': [12, 34], 'k2': [12, 34], 'k3': [12, 34]}

    a["k3"] = 56
    print(a)  # {'k1': [12, 34], 'k2': [12, 34], 'k3': 56}


if __name__ == '__main__':
    init_dict_fromkeys()
