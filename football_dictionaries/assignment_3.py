def players_by_country_and_position(squads_list):
    squad = players_as_dictionaries(squads_list)
    by_country = {}
    
    for player in squad:
        country = player['country']
        position = player['position']
        by_country.setdefaul(country,{})
        by_country.setdefault(position,[])
        by_country[country][position].append(player)
    return by_country
