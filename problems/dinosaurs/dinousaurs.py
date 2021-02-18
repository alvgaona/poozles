# https://gist.github.com/alvgaona/b6ad35add72b8e6d8c095f4c1cb07f4e


from dinosaur import Dinosaur


def gather_dinosaurs(lines1, lines2):
    dino_dict = {}

    for line in lines1:
        line = line.replace('\n', '').split(',')
        dinosaur = line[0]
        dino_dict[dinosaur] = {}
        dino_dict[dinosaur]['stride_length'] = line[1]
        dino_dict[dinosaur]['stance'] = line[2]

    for line in lines2:
        line = line.replace('\n', '').split(',')
        dinosaur = line[0]

        if dino_dict.get(dinosaur) is None:
            dino_dict[dinosaur] = {}

        dino_dict[dinosaur]['leg_length'] = line[1]
        dino_dict[dinosaur]['diet'] = line[2]

    return dino_dict


def create_sorted_dinosaurs(dino_dict: dict) -> list:
    dinosaurs = []
    for k, v in dino_dict.items():
        leg_length = v.get('leg_length')
        stride_length = v.get('stride_length')

        if leg_length is not None:
            leg_length = float(leg_length)

        if stride_length is not None:
            stride_length = float(stride_length)

        dinosaurs.append(Dinosaur(k, leg_length, stride_length, v.get('stance'), v.get('diet')))

    return sorted(dinosaurs, key=lambda x: x.speed(), reverse=True)
