import re

addr_str = '广州市白云区石潭西路13号嘉发时尚中心C127－129档 ，33斤;江苏省无锡市新吴区塘南招商城A1一107号'
addr_str = '广州市白云区石潭西路13号嘉发时尚中心C127－129档 ，33斤；江苏省无锡市新吴区塘南招商城A1一107号'
re_res = re.match(r'(.*?)(;|；)(.*)', addr_str)

api_url = ''
api_name = re.match(r'(.*)/(\w+)\?', api_url).group(2)
