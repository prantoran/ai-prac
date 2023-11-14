conda create --name tf python=3.9
conda activate tf
conda install -c conda-forge cudatoolkit=11.8.0
pip install nvidia-cudnn-cu11==8.6.0.163
pip install --upgrade pip
pip install tensorflow==2.13.*