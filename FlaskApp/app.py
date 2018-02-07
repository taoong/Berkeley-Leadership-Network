from flask import Flask, render_template, request, json
import pandas as pd
import math
app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

@app.route("/people")
def people():
    return render_template('people.html')

@app.route("/companies")
def companies():
    return render_template('companies.html')

@app.route("/profile/<name>")
def profile(name):
    person = filteredVCdata[filteredVCdata['Full Name'].str.startswith(name.lower())]
    print(person)
    return render_template('linked_profile.html', name=person['Full Name'].iloc[0].title(),
                           job=person['Primary Job Title'].iloc[0].title(),
                           company=person['Primary Company'].iloc[0].title(),
                           location=person['Location'].iloc[0].title(),
                           sector=person['Investment interest/sector'].iloc[0].title(),
                           stage=person['Stage (Pre-Seed, Seed, Series A/B/C)'].iloc[0].title(),
                           bio=person['Bio'].iloc[0].title(),
                           picture=person['Row for Picture'].iloc[0].title())

# coding: utf-8

# In[1]:

import seaborn as sns
import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


from IPython.display import display, Latex, Markdown, HTML, Javascript

# In[90]:

rawvcData = pd.read_csv('blnData.csv')
rawvcData.head()

# In[ ]:




# In[91]:

rawvcData.columns

# In[92]:

filteredVCdata = rawvcData.loc[:, ["Full Name", "Primary Job Title", "Primary Company", "Location",
                                   "Investment interest/sector", "Stage (Pre-Seed, Seed, Series A/B/C)", "Bio", "Row for Picture"]]

# In[93]:

filteredVCdata.head()

# Angel/ partner/ founder
# location -- DONE
# Actively investing -- DONE
# Sector --- DONE

# In[ ]:




# In[94]:

for i in range(len(filteredVCdata.columns)):
    for x in filteredVCdata.columns:
        filteredVCdata[x] = filteredVCdata[x].str.lower()

# In[95]:

filteredVCdata.fillna('Null', inplace=True)


# In[96]:

#Returns if indicated investor contains the investment stage searched
def stageFilter(stageName):
    
    stageNameLowered = stageName.lower()
    return filteredVCdata[filteredVCdata["Stage (Pre-Seed, Seed, Series A/B/C)"].str.contains(stageNameLowered) == True]

# All results for the corresponding industry sector
def sectorFilter(sectorName):
    sectorNamelowered = sectorName.lower()
    return filteredVCdata[filteredVCdata["Sector "].str.contains(sectorNamelowered) == True]


# In[97]:

# sectorFilter("software")


# In[98]:

# Returns if the indicated investor is actively investing or not
def activeInvestor(firstName, lastName):
    nameNoSpace = filteredVCdata
    nameNoSpace["Full Name"] = nameNoSpace["Full Name"].str.replace(" ", "")
    fnLower = firstName.lower()
    lnLower = lastName.lower()
    fullName = fnLower + lnLower
    isolatedInvestor = nameNoSpace[nameNoSpace["Full Name"].str.contains(fullName) == True]

    return isolatedInvestor["Actively investing?"]


# In[99]:

# activeInvestor("benjamin", "ling")


# In[100]:

# Returns the location of the given investor
def locateInvestor(firstName, lastName):
    nameNoSpace = filteredVCdata
    nameNoSpace["Full Name"] = nameNoSpace["Full Name"].str.replace(" ", "")
    fnLower = firstName.lower()
    lnLower = lastName.lower()
    fullName = fnLower + lnLower
    isolatedInvestor = nameNoSpace[nameNoSpace["Full Name"].str.contains(fullName) == True]

    return isolatedInvestor["Location"]


# In[101]:

# locateInvestor("benjamin", "ling")


# In[114]:

# Returns those with the given job title
def roleFilter(jobTitle):
    nameNoSpace = filteredVCdata
    nameNoSpace["Primary Job Title"] = nameNoSpace["Primary Job Title"].str.replace(" ", "")
    jobTitleLower = jobTitle.lower()
    investorJob = nameNoSpace[nameNoSpace["Primary Job Title"].str.contains(jobTitleLower) == True]

    #     s1 = pd.merge(filteredVCdata, investorJob, how='inner', on=["Full Name"])
    #     s1.dropna(inplace = True)
    return investorJob


    # In[116]:

    # roleFilter("founder").head()


    # In[ ]:




    # In[ ]:

person = None

@app.route("/dataRequest", methods=['POST'])
def dataRequest():
    return json.dumps(filteredVCdata.to_dict('list'))


if __name__ == "__main__":
    app.run(port=9053, debug=True)

