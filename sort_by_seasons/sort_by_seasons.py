def sort_by_seasons(items: list):
    def order_by_seasons(item:dict):
        for k,v in item.items():
            if k=="seasons":
                seasons_num=v
        return seasons_num
    return sorted(items,key=order_by_seasons)

if __name__=="__main__":
    shows = [{ "name": "Dexter", "rating" : 8.6, "seasons":9 }, { "name": "Friends", "rating" : 8.9, "seasons":10 },  { "name": "Simpsons", "rating" : 8.7, "seasons":32 }  ]

    for show in sort_by_seasons(shows):
        print(f"{show['name']} {show['seasons']} seasons")