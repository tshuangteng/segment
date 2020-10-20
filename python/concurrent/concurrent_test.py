import concurrent.futures
import requests

with concurrent.futures.ThreadPoolExecutor() as executor:
    future_to_url = {executor.submit(requests.post, url, data=json.dumps({'mailNoes': [waybill_no], 'appKey': '100030'}), verify=False): waybill_number for waybill_number in waybill_number_list}
    finish = 1
    for future in concurrent.futures.as_completed(future_to_url):
        waybill_number = future_to_url[future]
        try:
            response_content = future.result().json()
            finish += 1
        except Exception as error:
            logger.info(f'{error}')
            logger.info(f'get {waybill_number} no data!')
            # break
            continue

# 和偏函数的使用

get_func = partial(get_request, url=URL)

with concurrent.futures.ThreadPoolExecutor() as executor:
    for waybill_no, res_json in zip(waybill_no_list, executor.map(get_func, waybill_no_list, chunksize=400)):
        if not res_json:
            continue
        else:
            # 写入地址信息
            pass
