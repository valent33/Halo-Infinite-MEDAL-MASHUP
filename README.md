# Halo-Infinite-MEDAL-MASHUP
Source code for the extraction and processing of a player's medal in Halo Infinite


# Installation
See the Youtube tutorial for this project:
https://youtu.be/C3xE8eePcIE

Get your Autocode token:
https://docs.autocode.com/api-authentication-management/creating-and-managing-identity-tokens/

Install Gephi:
https://gephi.org/users/download/

Download the python file, insert your Autocode token and run the command
```
  python medal_mashup.py "yourgamertag" --save-images
```

Thereafter, it won't be necessary to use `--save-image`.

# Gephi
- Go to the Tools -> Plugins -> Available Plugins and install Image Preview. Install and restart Gephi.
- On startup, open graph file and select nodes table as the import style
- Press next -> finish -> ok
- Go to the Appearance -> Nodes -> Size tab and select ranking, choose weight. I recommend setting min to 10, max to 50 and changing the spline to a square root curve for the best results.
- (Optional) Go to the Appearance -> Nodes -> Color and select Partition, choose type. There you can color the medals by their types, that can be useful if you want to mix up the graph to disperse clusters manually.
- Go to Layout and select ForceAtlas 2. I recommend using 0.1 for scaling, 10 for gravity and Prevent Overlap on.
- Run the algorithm for a quick second
- (Optional) Right click on the largest nodes and settle them. That way, you can drag them to the center of the graph for a more impressive render. You can even keep ForceAtlas 2 running to see the effect live.
- Go to the Preview tab, set Nodes Opacity to 0, tick Render Nodes As Images, and set the path to the location where the images are downloaded. Nothing else matters.
- Press Refresh and you're done !

# Credits
Big shutout to HaloDotApi and all their devs, they do an incredible work and I could not have done it without them ! Go check them out :
https://twitter.com/HaloDotAPI

Follow me on Twitter:
https://twitter.com/Vayllle

