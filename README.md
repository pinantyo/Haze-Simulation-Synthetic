# Haze Synthetic Generator
Modified haze simulation using _Atmospheric Scattering Model_ (ASM)
<p align="center" width="100%">
  $I(x) = J(x).t(x) + A(1 - t(x))$
</p>

<p align="center" width="100%">
  $t(x) = e^{\lambda d(x)}$
</p>


<div align="center" width="100%">
    <img width="99%" src="https://github.com/pinantyo/Haze-Simulation-Synthetic/blob/main/data/Process.png">
    <p>Process flow on haze generator</p>
</div>

## Input
- Cirrus band obtained from Landsat <a href="https://code.earthengine.google.com">Google Earth Engine Code</a>

<p align="center" width="100%">
    <img width="20%" src="https://github.com/pinantyo/Haze-Simulation-Synthetic/blob/main/data/cirrus/cirrus1.png">
    <img width="20%" src="https://github.com/pinantyo/Haze-Simulation-Synthetic/blob/main/data/cirrus/cirrus2.png"> 
    <img width="20%" src="https://github.com/pinantyo/Haze-Simulation-Synthetic/blob/main/data/cirrus/cirrus3.png"> 
    <img width="20%" src="https://github.com/pinantyo/Haze-Simulation-Synthetic/blob/main/data/cirrus/cirrus4.png"> 
</p>

- Data Land-Use Segmentation <a href="https://x-ytong.github.io/project/GID.html">GID-5</a> | <a href="https://sites.google.com/view/zhouwx/dataset#h.p_hQS2jYeaFpV0">WHDLD</a> | <a href="https://landcover.ai.linuxpolska.com/">Landcover.ai</a> | <a href="https://www.kaggle.com/datasets/balraj98/deepglobe-land-cover-classification-dataset">Deep Globe Landcover Segmentation</a>

## Output
<p align="center" width="100%">
    <img width="40%" src="https://github.com/pinantyo/Haze-Simulation-Synthetic/blob/main/data/hazy/Pairs1.png">
    <img width="40%" src="https://github.com/pinantyo/Haze-Simulation-Synthetic/blob/main/data/hazy/Pairs2.png">
</p>

## Reference
<p>Song, Yuda and He, Zhuqing and Qian, Hui and Du, Xin. 2023. Vision Transformers for Single Image Dehazing. IEEE Transactions on Image Processing. https://github.com/zhuqinghe/RS-Haze</p>
