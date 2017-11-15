Making FiveThirtyEight (FTE) Graphs with Python
-----------------------

Data visualization.

Using *matplotlib* and *pandas* to replicate the core parts of any FiveThirtyEight (FTE) visualization.
Technical description of FTE style can be found [here](https://github.com/matplotlib/matplotlib/blob/38be7aeaaac3691560aeadafe46722dda427ef47/lib/matplotlib/mpl-data/stylelib/fivethirtyeight.mplstyle) and some characteristics' discussion can be found [here](https://dataorigami.net/blogs/napkin-folding/17543615-replicating-538s-plot-styles-in-matplotlib)

Example of [FTE graphs](https://fivethirtyeight.com/features/the-52-best-and-weirdest-charts-we-made-in-2016/)


* bachelor_degree_female_USA_1970to2011:

    This describes the percentage of Bachelors conferred to women in the US from 1970 to 2011.
    Dataset has been compiled by [Randal Olson](http://www.randalolson.com/2014/06/14/percentage-of-bachelors-degrees-conferred-to-women-by-major-1970-2012/)


* UK_crime_data_2010_2016:

    This describes the occurrence of reported crime to Metropolitan Police (UK)from December 2010 to December 2016.
    Data is provided by  [Data.Police.UK](https://data.police.uk/data/)


Installation
----------------------

### Download the data
* Clone this repo to your computer.
* Get into the folder using `cd making-FTP-Graphs`.
* Run `mkdir data`.
* Run `mkdir plots`.
* Switch into the `data` directory using `cd data`.
* Download the data files into the `data` directory.
* Switch back into the `making-FTP-Graphs` directory using `cd ..`

bachelor_degree_female_USA_1970to2011
----------------------
* [data file](http://www.randalolson.com/wp-content/uploads/percent-bachelors-degrees-women-usa.csv)
* Run:
    * `python female_bachelor_degree`
    (make sure the directory is `bachelor_degree_female_USA_1970to2011`)


UK_crime_data_2010_2016
----------------------
* Jupyter notebook


To do
----------------------
* Automatically add label to lines