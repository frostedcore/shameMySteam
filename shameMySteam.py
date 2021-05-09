from steam.steamid import SteamID
import urllib3
import json
import random
api='8F8613847230EEB3619FC6C78968A9CD'

sickBurns=[
    'If I was your father I wouldn\'t come back after getting cigarrettes either because ',
    'If you were missing, I would probably look for you only out of social obligation because ',
    'I hope your crops fail and wish you starvation because ',
    'If you were on fire, and I had a glass of water, I would drink it because '
]


def main():
    zero = 0
    undothehundo = 0
    print("Welcome to Shame My Steam.\nPrepare for cronic depression.\n")

    SURL = input("Please enter your Steam profile URL:")
    SID = SteamID.from_url(SURL)

    http = urllib3.PoolManager()
    r = http.request('GET', f'http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={api}&steamid={SID}&format=json&include_appinfo=1')
    games = json.loads(r.data)['response']['games']

    for game in games:
        if game['playtime_forever'] == 0:
            print(random.choice(sickBurns) + f"you haven\'t even played {game['name']}!!!")
            zero += 1
        elif game['playtime_forever'] < 100:
            print(random.choice(sickBurns) + f"you\'ve only played {game['playtime_forever']} hours of {game['name']}")
            undothehundo += 1

    print(
        f'\n\nYou haven\'t played {zero} games in your Steam Library'
        f'\nYou have played {undothehundo} for less than a hundred hours',
        f'\n\nThat\'s a total of {zero + undothehundo} peice of shit points!'
    )

if __name__ == "__main__":
    main()