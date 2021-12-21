## with `docker run` start container

### docker build .


### init base container

```
# nvidia-docker run -itd -e NVIDIA_VISIBLE_DEVICES=4,5 -v /home/tshuangteng/ocr:/usr/src/ocr -e PYTHONPATH="/usr/src/ocr" -e workspace="/usr/src/ocr" --name base_image --hostname base_image nvidia/cuda:10.2-devel-ubuntu18.04 /bin/bash
# docker commit base_image ocr/tshuangteng:v1
```

### create my image

```
nvidia-docker run -itd -e NVIDIA_VISIBLE_DEVICES=4,5 -p 6868:80 -v /home/tshuangteng/ocr:/usr/src/ocr -e PYTHONIOENCODING="utf-8" -e HOME="/usr/src/ocr" -e workspace="/usr/src/ocr" --name ocr --hostname ocr ocr/tshuangteng:v1 /bin/bash
```