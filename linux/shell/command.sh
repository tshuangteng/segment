
#kill -9 `pgrep -f './tb_scan'`

#xargs（英文全拼： eXtended ARGuments）在xargs指令中，{} 是代指管道前面指令的输出，但是对于xargs指令来说，是一个一个的输入，不是整体输入
#在find指令输出时，在结尾加上 -print0 那么就会变成参数之间使用 0 分割, 避免因为默认分割符是空格和换行，一个带有空格的文件名就会变成多个文件被处理

#移动当前目录下 非marked_ship_202203*的其他文件 到上级目录bak
# find . ! -name . ! -name "marked_ship_202203*" | xargs -i cp -r {} ../bak/

#使用find命令在当前目录下, 不包含子目录中查找文件
# find ./ -maxdepth 1 -name '*.csv'

#除了某个文件, 删除其他
# rm `ls | grep -v "^abc$"`
# find ./ -type f \! -name "abc" -exec rm -rf {}\;
# ls | grep -v abc | xargs -i rm -rf {}
