def move_to_pos(x, y):
    current_x = get_pos_x()
    current_y = get_pos_y()

    if current_x < x:
        for _ in range(x - current_x):
            move(East)

    if current_y < y:
        for _ in range(y - current_y):
            move(North)

        if current_x > x:
            val = x - current_x
            val = val - val - val
            for _ in range(val):
                move(West)

        if current_y > y:
            val = y - current_y
            val = val - val - val
            for _ in range(val):
                move(South)


move_to_pos(0, 0)


def odd(a):
    if a % 2 == 0:
        return False
    else:
        return True


def even(a):
    if a % 2 == 0:
        return True
    else:
        return False


def tplace():
    if odd(get_pos_x()) == False and odd(get_pos_y()) == False:
        return True
    elif odd(get_pos_x()) == True and odd(get_pos_y()) == True:
        return True


while True:
    for i in range(get_world_size()):
        if get_pos_y() == 0:
            plant(Entities.grass)
            if can_harvest():
                harvest()

        else:
            if tplace() == True:
                if get_ground_type() == Grounds.Soil:
                    pass
                else:
                    till()

                plant(Entities.Tree)

                if get_water() < 0.5:
                    use_item(Items.Water_Tank)

            else:
                if (
                    get_ground_type() == Grounds.soil
                    and get_entity_type() == Entities.Carrots
                    and can_harvest() == True
                ):
                    harvest()
                    trade(Items.Carrot_Seed)
                    plant(Entities.Carrots)
                elif get_ground_type() != Grounds.Soil:
                    till()
                    trade(Items.Carrot_Seed)
                    plant(Entities.Carrots)
                elif get_ground_type() == Grounds.Soil and get_entity_type() != Entities.Carrots:
                    trade(Items.Carrot_Seed)
                    plant(Entities.Carrots)
        move(East)
        if can_harvest():
            harvest()
    move(North)