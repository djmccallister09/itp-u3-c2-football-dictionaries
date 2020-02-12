def players_as_dictionaries(squads_list):
    new_list = []  #establish new list to append dictionary items to
    for i in squads_list: #assigns key and value to dictionary from orig list
        new_dict = {}
        new_dict['number'] = i[0]
        new_dict['position'] = i[1]
        new_dict['name'] = i[2]
        new_dict['date_of_birth'] = i[3]
        new_dict['caps'] = i[4]
        new_dict['club'] = i[5]
        new_dict['country'] = i[6]
        new_dict['club_country'] = i[7]
        new_dict['year'] = i[8]
        new_list.append(new_dict)
    return new_list
