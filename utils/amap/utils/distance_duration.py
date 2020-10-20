import datetime

from common.logger import logger

log = logger(app_name='app', file_name=__name__)


def convert_number_to_meters(number):
    # if int(number) >= 1000:
    #     res = int(number) / 1000
    #     return f'{res}km'
    # else:
    #     return f'{number}m'
    res = int(number) / 1000
    return f'{res}km'


def convert_number_to_time(number):
    time_str = str(datetime.timedelta(seconds=int(number)))
    hours, minutes, seconds = time_str.split(':')
    # log.info(hours, minutes, seconds)
    if hours == '0':
        if minutes == '00':
            return f'{seconds}s'
        return f'{minutes}min{seconds}s'
    else:
        if 'days' in hours:
            hours_list = hours.split(' ')
            day_hours = int(hours_list[0]) * 24
            odd = int(hours_list[2])
            hours = day_hours + odd
        return f'{hours}h{minutes}min{seconds}s'


