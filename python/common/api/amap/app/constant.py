from pathlib import Path

from utils.amap import api_usability

root_path = Path.cwd().parent

# KEY = [
#     '6c3a24427483a8af82c31598f7d3dc5a', '9f35b81d2117a69c708bf4f690097ad7',
#     '0c46912df8675d59284baac6dee65ec1', '48417b0f71adc0b69e149cf8cb078f51',
#     'dff1295876b077359f35f2ec50e63230', '1e8de942760283f914bd8cccef81deea', '9f1041efdf308ed684039bf2833b8c23',
#     'e896bc786912ce5f57187ecd65526685', 'a1616c46d97c4161fdf506b9f1c43163', ]

KEY = ['9e2f140fabbaddae90b2b893f6af5f77', '1d2d30dda78963b7bd9e24427579176f', 'cd944ffd37222f5e4cd6c6c826130fa7',
       '329d40f01f1f1d69c87264bec55fbf09', '13c672873efeaeb7d81a4edf9e56055a', '4aecebe00bafef1a4fcd16d467698605',
       '242b4f35aa2d63387560eb5efade62be', '01c698912ad0e117090a3054ffb46d14', '5a4e5c697901454e0827ce0f8610d1c6']

DISTANCE_API = 'https://restapi.amap.com/v3/distance?'

BICYCLING_API = 'https://restapi.amap.com/v4/direction/bicycling?'

DRIVING_API = 'https://restapi.amap.com/v3/direction/driving?'

WALKING_API = 'https://restapi.amap.com/v3/direction/walking?'

REGEO_API = 'https://restapi.amap.com/v3/geocode/regeo?'

EXCEL_FILE = Path(root_path, '_file/ranging.xlsx')

NEW_EXCEL_FILE = Path(root_path, '_file/new_lon_lat.xlsx')

TMP_TXT_FILE = Path(root_path, '_file/tmp.txt')

TXT_FILE = Path(root_path, '_file/res.txt')

# for key in KEY:
#     api_usability(key=key)
