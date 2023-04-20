# Install torch & torchvision

```bash
sudo apt-get install libjpeg-dev zlib1g-dev libpython3-dev libavcodec-dev libavformat-dev libswscale-dev
```

# installing CUDA-enabled torch

```
//1.10
gdown "https://drive.google.com/file/d/1TqC6_2cwqiYacjoLhLgrZoap6-sVL2sd/view?usp=sharing" --fuzzy
python3 -m pip install ./torch-1.10.0a0+git36449ea-cp36-cp36m-linux_aarch64.whl

//1.7.0
wget https://nvidia.box.com/shared/static/cs3xn3td6sfgtene6jdvsxlr366m2dhq.whl
python3 -m pip install ./*.whl
```

```bash
wget https://github.com/pytorch/vision/archive/refs/tags/v0.8.0.zip // OR https://github.com/pytorch/vision/archive/refs/tags/v0.11.0.zip
unzip v*zip -d torchvision
cd torchvision/*/
export BUILD_VERSION=0.x.0  #将x改成自己的版本 
pip3 install 'pillow<7'
sudo python3 setup.py install  // --user
```

```bash
sudo apt install python3-seaborn /xxx 
```

```bash
python3 ./detect.py --source 0 --device 0 --weight yolov7-tiny.pt
```

