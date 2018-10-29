# Difficult destinations in Colombia - How easy is to fly to some towns in Colombia?

![alt text](https://github.com/cjcarvajal/difficult-destinations-colombia/blob/master/img1.png)

There is an official airline in Colombia called [Satena](https://www.satena.com/), its run under the Defense Ministry command, its mission is to provide air services such as passsenger flights or mail to some remote regions in the country, regions where the poverty, violence conflicts or lack of infrastructure forbid other comercial airlines to offer the same service. So Satena accomplish a social goal, integrating this remote locations into the economic and politic development of the country.

In this visualization, I analyze the routes provide by Satena, and identify some possible improvements in their service.

## Dataset

The data was taken from an official goverment page [Datos Abiertos](https://www.datos.gov.co/Seguridad-y-Defensa/RUTAS-COMERCIALES-SATENA/4hnp-vug9).

## The Technology Used

I wrote a python script to preprocess the data, the script is in this repository as [preprocess.py](https://github.com/cjcarvajal/difficult-destinations-colombia/blob/master/preprocess.py), it just reads a stored version from the original dataset and builds a json structure defining nodes and links.

To run this project just download the [index.html](https://github.com/cjcarvajal/difficult-destinations-colombia/blob/master/index.html) and the [satena.jpg](https://github.com/cjcarvajal/difficult-destinations-colombia/blob/master/satena.jpg) files and save them in the same folder, then open the index.html in your browser. Although not necessary, you could install a local http server on your machine, and serve the index html file from there, the easiest way (I think) is using the [SimpleHTTPServer](https://docs.python.org/2/library/simplehttpserver.html) Python utility, just be sure to have Python installed in your machine, go to the folder where you download the index.html and run:

```
python -m SimpleHTTPServer 8080
```

Open your browser and type http://localhost:8080/ and voila!

You may want to learn this technologies which were used to build the visualization.

* [Javascript](https://www.w3schools.com/js/)
* [D3 version 5](https://d3js.org/)
* [css](https://www.w3schools.com/Css/)
* [html](https://www.w3schools.com/html/)
* [python](https://www.python.org/)

I have used most of the Mike Bostock code for making the network view, check the original version [here](https://beta.observablehq.com/@mbostock/d3-force-directed-graph). 

## Live Project

I have published my project in githubpages, so you can check it right [here](https://cjcarvajal.github.io/flight-analysis/).

### License

This project has MIT license which can be consulted in the LICENSE of this repository.