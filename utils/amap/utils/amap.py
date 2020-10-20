import json
import re
from requests import request

from common.logger import logger
from utils.distance_duration import convert_number_to_meters as cm
from utils.distance_duration import convert_number_to_time as ct

log = logger(app_name='app', file_name=__name__)


def api_usability(key):
    test_origin = '102.576109,26.600000'
    test_destination = '102.577385,26.620000'
    api_url = f'https://restapi.amap.com/v4/direction/bicycling?key={key}&origin={test_origin}&destination={test_destination}'

    data = request(method='get',
                   url=api_url)
    response = data.content.decode(encoding='utf8')

    if json.loads(response)['errmsg'] != 'OK':
        log.info(json.loads(response)['errmsg'])
        return None
    else:
        log.info(json.loads(response)['errmsg'])
        return True


def get_request_api(key, origin, destination, api_url):
    api_name = re.match(r'(.*)/(\w+)\?', api_url).group(2)
    log.info(f'{api_name}--> origin:{origin}, destination:{destination}')
    if api_name == 'walking' or api_name == 'driving':
        if api_name == 'walking':
            api_url = f'{api_url}key={key}&origin={origin}&destination={destination}'
        else:
            api_url = f'{api_url}key={key}&origin={origin}&destination={destination}&extensions=base'
        response = request(method='get',
                           url=api_url, verify=False).content.decode(encoding='utf8')
        json_date = json.loads(response)
        if json_date['status'] != '1':
            error_info = json_date['info']
            log.info(api_name + ':' + error_info)
            # if error_info == 'DAILY_QUERY_OVER_LIMIT':
            #     pass
            return 0, 0
        else:
            data_distance = json_date['route']['paths'][0]['distance']
            data_duration = json_date['route']['paths'][0]['duration']
            return cm(data_distance), ct(data_duration)

    elif api_name == 'bicycling':
        api_url = f'{api_url}key={key}&origin={origin}&destination={destination}&type=0'
        response = request(method='get',
                           url=api_url, verify=False).content.decode(encoding='utf8')
        json_date = json.loads(response)
        if json_date['errmsg'] != 'OK':
            log.info(api_name + ':' + json_date['errdetail'])
            return 0, 0
        else:
            data_distance = json_date['data']['paths'][0]['distance']
            data_duration = json_date['data']['paths'][0]['duration']
            return cm(data_distance), ct(data_duration)

    elif api_name == 'distance':
        api_url = f'{api_url}key={key}&origins={origin}&destination={destination}&type=0'
        response = request(method='get',
                           url=api_url, verify=False).content.decode(encoding='utf8')
        json_date = json.loads(response)
        if json_date['status'] != '1':
            log.info(api_name + ':' + json_date['info'])
            return 0, 0
        else:
            data_distance = json_date['results'][0]['distance']
            data_duration = json_date['results'][0]['duration']
            return cm(data_distance), ct(data_duration)


def lonlat_to_location(url, key, lonlat):
    api_url = f'{url}key={key}&location={lonlat}'
    response = request(method='get',
                       url=api_url, verify=False).content.decode(encoding='utf8')
    json_date = json.loads(response)
    if json_date['status'] != '1':
        error_info = json_date['info']
        log.info(error_info)
        return 0, 0
    else:
        location = json_date['regeocode']['formatted_address']
        if location:
            return location
        else:
            return '0'


def lat_lon_decimal(address):
    address_list = address.split(',')
    if not address_list:
        a_list = address.split(".")
        address_list = ['.'.join(a_list[:2]), '.'.join(a_list[2:])]
    try:
        lat, lon = float(address_list[0]), float(address_list[1])
    except Exception:
        return 0, 0
    return f'{round(lat, 6)},{round(lon, 6)}'


if __name__ == '__main__':
    pass
