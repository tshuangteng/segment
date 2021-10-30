#/bin/bash

# [root@sf105170 ~]# echo `date +%Y%m%d -d "1 day ago"`
# 20211018



# 原始文件/shel/csv_import_real.sh   10.181.86.12
# new file

#!/bin/bash
# 20211020 update by 98092616

real_csv_path=/addr7/full_piece/real
simulation_csv_path=/addr7/full_piece/simulation

yesterday=$(date "+%Y%m%d" -d "1 day ago")

for file_path in $real_csv_path $simulation_csv_path;do
    for single_file in `ls $file_path/$yesterday/*00.csv`;do
      if [ $file_path = $real_csv_path ];then
        psql -d  develop   -h  localhost   -U gpadmin  -p 5432  -c "\copy addr_real from $single_file with csv header";
      fi

      if [ $file_path = $simulation_csv_path ]; then
        psql -d  develop   -h  localhost   -U gpadmin  -p 5432  -c "\copy addr_simulation from $single_file with csv header";
      fi

      if [ $? -ne 0 ];then
        echo "error: import $single_file"
      fi
    done
done



