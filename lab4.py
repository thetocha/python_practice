def str_raise(string):
    x = string.split()
    raise_flag = True
    for world in x:
        for i in range(len(world) - 1):
            if world[i] >= world[i + 1]:
                raise_flag = False
        if raise_flag:
            return world
        raise_flag = True
    return None


if __name__ == "__main__":
    print(str_raise("aaaa  zxy   aec edf "))
