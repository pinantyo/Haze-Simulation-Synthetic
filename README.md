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
- Cirrus band obtained from Landsat  ![Google Earth Engine Code](https://code.earthengine.google.com)

<p align="center" width="100%">
    <img width="20%" src="https://github.com/pinantyo/Haze-Simulation-Synthetic/blob/main/data/cirrus/cirrus1.png">
    <img width="20%" src="https://github.com/pinantyo/Haze-Simulation-Synthetic/blob/main/data/cirrus/cirrus2.png"> 
    <img width="20%" src="https://github.com/pinantyo/Haze-Simulation-Synthetic/blob/main/data/cirrus/cirrus3.png"> 
    <img width="20%" src="https://github.com/pinantyo/Haze-Simulation-Synthetic/blob/main/data/cirrus/cirrus4.png"> 
</p>

- Data Land-Use Segmentation ![GID-5](https://x-ytong.github.io/project/GID.html) | ![WHDLD](https://sites.google.com/view/zhouwx/dataset#h.p_hQS2jYeaFpV0) | ![Landcover.ai](https://landcover.ai.linuxpolska.com/) | ![Deep Globe Landcover Segmentation](https://www.kaggle.com/datasets/balraj98/deepglobe-land-cover-classification-dataset)

## Output
<p align="center" width="100%">
    <img width="40%" src="https://github.com/pinantyo/Haze-Simulation-Synthetic/blob/main/data/hazy/Pairs1.png">
    <img width="40%" src="https://github.com/pinantyo/Haze-Simulation-Synthetic/blob/main/data/hazy/Pairs2.png">
</p>
