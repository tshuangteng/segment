import pg8000
import re

###################
# example code
###################

conf = {
    'user': 'gpadmin',
    'host': '10.131.51.17',
    'port': 5432,
    'database': 'suanfa'
}


def get_areacode(cur, bm):
    """
    :param cur:
    :param bm: int
    :return: str like int
    """
    sql = f"select shi from gs where bm ='{bm}';"
    cur.execute(sql)
    areacode_tuple = cur.fetchall()
    areacode_ = str(areacode_tuple[0][0]).strip(' ')
    try:
        areacode = re.match(r'.*?(\d+).*', areacode_).group(1)
    except Exception as error:
        print(f'--- areacode_tuple: {areacode_tuple} ---> {error} ---')
        areacode = 'none'
    return areacode


def get_result(cur, areacode):
    """
    :param cur:
    :param areacode:
    :return: ['(京)市辖区', '110000', '110100']
    """
    sql = f"select cityname,provinceid,country_city_code from city where areacode='{areacode}';"
    cur.execute(sql)
    result_tuple = cur.fetchall()
    result_list = result_tuple[0]
    return result_list


if __name__ == '__main__':
    con = pg8000.connect(**conf)
    cur = con.cursor()

    areacode = ''
    try:
        res = get_result(cur, areacode)
    except Exception as e:
        print(f'--- {areacode} :ERROR ---> {e} ---')

    cur.close()
    con.close()
