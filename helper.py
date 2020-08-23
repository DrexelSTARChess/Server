color_to_player_num = {"white": 1, "black": 2}
player_num_to_color = {1: "white", 2: "black"}


def get_other_player_num(player_number):
    if player_number == 1:
        return 2
    else:
        return 1
