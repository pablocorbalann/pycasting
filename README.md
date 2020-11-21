<p align="center"><img src="images/logo.png" width="75px" alt="..."></p>
<h1 align="center">2D Raycasting</h1>
<h3 align="center"> Implementation of a 2D raycasting algorithm using Pygame</h3>
<p align="center"><img alt="Hex.pm" src="https://img.shields.io/hexpm/l/plug?color=yellow&label=LICENSE&style=for-the-badge"></p>

---

### Using the app
If you want to use the web in your computer, you should follow this steps.
##### Prequisites
* Python (v3.7+) installed.
* Git installed and configured
* pip (v3) instaled
##### Steps
###### Clone the repository in your local machine
```shell
git clone https://github.com/PabloCorbCon/2d-raycast.git
```
###### Move inside the repository
```shell
cd 2d-raycast
```
###### Install all the packages needed
```shell
pip install -r requirements.txt
```
###### Start the Pygame app
```
python app.py
```
###### If you have multiple Python instalations use Python 3(+7)
```
python3 app.py
```

---

### Configuration
All the **configuration** of the application has been **externalized** to the code itself so that you can modify it to your liking in the simplest way possible.

You can see the default configuration in the `CONFIG.json` file.

You can modify this configuration to your liking, for example to change the width of the tiles or the color of the walls.

#### Adding walls
You can also add walls to the game. Just go to the `/walls/walls` configuration file section and you will see a list of values with this syntax.
```
[
  [[a1, b1], [c1, d1]],
  [[a2, b2], [c2, d2]],
  ...
  [[aN, bN], [cN, dN]]
]
```
These lists represent Cartesian coordinates, in a plane a segment has a start point and an end point. **This two points can be seen as** `a & b`where `a = {x1, y1}` and `b = {x2, y2}`. **So the wall segments are determined in the form of**:
```
[
  [[x1, y1], [x2, y2]]
]
```
<p align="center"><img src="images/cartesian-plane.gif" alt="..."></p>
