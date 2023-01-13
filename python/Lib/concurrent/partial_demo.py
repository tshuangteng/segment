import requests
import urllib3
import concurrent.futures
from functools import partial

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

if __name__ == '__main__':
    """
    偏函数使用场景: 当要频繁调用某个函数时，其中某些参数是已知的固定值，多次调用这个函数.
    
    partial() 是被用作 “冻结” 某些函数的参数或者关键字参数，同时返回一个新的函数。
    
    真实场景: 
    url并发请求时,需要设定url,请求头,请求参数等.
    url并发请求时,要求每次传递的请求参数不同.

    解决方案就可以是: 使用偏函数封装 简单的请求函数,并固定该请求函数的url和请求头参数 新生成偏函数对象供后续使用. 
    
    如下示例
    def get_request(params, url, headers):
        try:
            res = requests.get(url=url, headers=headers, params=params)
            return res.json()
        except Exception as error:
            return None

    get_func = partial(get_request, url='https://fly.cainiao.com/chainTimeAnalysis/listChainTimeFinishRatio.json', headers=headers)

    params_list = []
    with concurrent.futures.ThreadPoolExecutor() as executor:
        for params, response_json in zip(params_list, executor.map(get_func, params_list, chunksize=8)):
            # sendDivisonCode = dict(params)['sendDivisionId']
            # receiveDivisonCode = dict(params)['receiveDivisionId']

            if not response_json:
                continue
            if response_json['data']:
                data = response_json['data']
            else:
                data = None
            # write_finish_ratio(data, stat_date, sendDivisonCode, receiveDivisonCode)
    """


    def demo(p1, p2, p3):
        res_str = p1 + p2 + p3 + '\n'
        return res_str


    p_demo = partial(demo, p1='hello', p2='world')

    res = p_demo(p3='!')
    res2 = p_demo(p3='.')
    res3 = p_demo(p3='...')
    print(res, res2, res3)
