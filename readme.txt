readme.txt updated by Matt Friend 19 November 2018.

The files in this directory generate a Sankey diagram using Google Vis:

- The data underlying the Sankey diagram are coded directly into file templates/sankey.html.
  Colours, line thickness, data label options etc. can also be amended in this file
  (see Google Vis for more details on how to do this).

- File "sankey.py" contains a minimal Flask application (written in Python 3.6.5, Anaconda distribution).
  When run this generates a local web page.

To copy the resulting Sankey diagram (e.g. to paste into a presentation), you need to copy and paste from the screen.
Unfortunately, Google Vis does not support automatic generation of .png files for Sankey diagrams.

To run "sankey.py", navigate to the correct directory and make sure you have the dependencies, including flask, installed
Then type the following at the command line:

    $ export FLASK_APP=sankey.py
    $ flask run


Notes:

1. The application is run locally - no data are sent to any external server.

2. For more details on Flask, see: http://flask.pocoo.org/docs/1.0/quickstart/

3. For more details on Google Vis, see: https://developers.google.com/chart/interactive/docs/gallery/sankey

4. As at November 2018, Google Vis notes that "The sankey chart may be undergoing substantial revisions in future Google Charts releases."
s