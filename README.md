## PURPOSE

Compute average salary in accordance to [LA R.S. 11:2031](http://www.legis.la.gov/legis/Law.aspx?d=74999)

----

## NOTES

* note that each of our members gets paid from both the parish and the state (two separate direct deposits)
  * we must first sum the parish + state = total monthly salary, before executing rolling_60 average test
  * note that we must apply a salary cap test, as outlined in the statute above. 
  * you will see that I started to define a function that i could call with .apply....but I am not sure that I can use my function and the pd.rolling(60).mean() function also. What would be your suggestion to implement the capping test?

* export_format files 1- 8 = test case info to use. this is a direct output from our software (written in APL+WIN)
  * i formatted the output such that the column headers are now in row 1, for pandas df to work right
  * note - two have quarterly postings for parish, not monthly. CANNOT split quarters

* export_key = identification info and what avg salary expected result should be. all expected results were calculated by our actuary, all example files are members who have already retired and files are finalized

* export_noformat and export_noformat2 = examples of what the output looks like straight from our software. 
  * note the column headers are not in row 1
  * note there is residual info at the end of the file after the salary postings
  * MY QUESTION: is there a way to code this such that a user does not have to delete appropriate rows before importing to our program?
    * meaning: can you create a pandas dataframe from the middle of a file, or must the column headers always be in row 1?

*samp_avg_salary = this is an alternative excel calculator I created to determine the high 60 months range prior to learning python. This particular file is using salary info for test case csv 'excel_format' 
  * this is to be used as an expanded example of what the python program should accomplish and how it should work
  * this test case implements a salary cap (see statute linked above for capping rules)
