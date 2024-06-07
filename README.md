# Cloudrunner

Currently served at: http://193.196.37.183:8080

Computes deterministic samples on request.

Repos:

- https://github.com/KIT-ISAS/Cloudrunner
- https://github.com/KIT-ISAS/IsasJuliaApi
- https://github.com/KIT-ISAS/web-app


## Available Methods & Syntax

### Addition (for demonstration)

Usage:

- http://193.196.37.183:8080/?M=add&a=1&b=2
- http://193.196.37.183:8080/?M=add&a=2.5&b=1.4


### 2D High-Quality Gaussian LCD Samples

![plot](media/glcdhq.png)

Usage ( **SLOW** | Requests take a few seconds! ):

- <http://193.196.37.183:8080/?M=sample_LCD_Gauss_2D&C=[1,0;0,.25]&L=5>
- <http://193.196.37.183:8080/?M=sample_LCD_Gauss_2D&C=[1,0;0,.1]&L=10>

Advantages:

- The most homogeneous Gaussian samples currently known.

Disadvantages:

- Computation takes long
- New computation for every i) Gaussian aspect ratio and ii) number of samples

Sources:

- Code: https://github.com/KIT-ISAS/GLCD-HQ
- Publications: https://isas.iar.kit.edu/Publications.php  {CDC09_HanebeckHuber, ACC13_Gilitschenski}



## TODO
- Standard Normal Gaussian LCD Samples
- Sample Reduction



