__author__ = 'gkannappan'


import pandas

#fw = open('/Users/gkannappan/Desktop/In24Hrs/root/Classified_Final.txt', 'w+')
#f1 = open('/Users/gkannappan/Desktop/In24Hrs/root/File_with_Lat_Long.txt')
ReviewText = pandas.read_csv("/Users/gkannappan/Documents/Intuit/Analytics Playground/Text Classification/AUTUMN/AMZN_Disc_DF2.txt", delimiter= '|', index_col=False, header=0, usecols=[0, 1, 2, 3, 4]);
rev_text = ReviewText['ReviewText'].tolist()

Import_Message = ['import']
Negative_Import = ['problem', "couldn't", "forgot", "issue", "didn't", "did not", "doesn't", "does not" ,"unsuccessful", "buggy", "crashed", "inaccessible", "unhappy", "fails", "fail", "can not"]
Positive_Import = ["easily", "easy", "fairly", "accurate", "can be"]
Partial_Import = ["enter", "manually", "missing", "not complete", "incomplete", "partial", "improper"]

Download_Message = ["download"]
Negative_Download = ["hours to", "difficult", "not", "worthless", "junk", "horrible", "took hours", "hours", "disappoint", "awful", "error", "problem", "uninstalled", "unable", "repair", "inconvenient"]
Positive_Download = ["easy", "flawlessly", "automatic", "easily", "satisfied"]

Install_Message = ["install"]
Negative_Install = ["problem", "won't", "unable", "defective", "issues", "hard", "failed", "discrepancy"]
Positive_Install = ["easy", "no problem", "simple", "straightforward", "perfectly", "no issues", "no glitches", "easier", "seamless", "quickly", "fine"]

Price_Message = ["price", "cost", "fee", "charge"]
Negative_Price = ["additional $", "wasted money", "additional", "greedy", "deceptive", "excessively", "over", "high", "over priced", "outrageous", "come down a bit", "overpriced", "steep", "different", "simplified", "increas", "raised", "not worth", "hidden", "difficult to justify", "extra", "expensive", "another", "$", "went up", "not fair", "rip off", "didnt save", "do not like", "include free", "very pricey", "more", "include", "charged", "too much", "ripoff", "rip"]
Positive_Price = ["excellent value", "fantastic", "lower", "excellent", "decent", "comparable", "worth every penny", "fairly", "competitively", "reasonable", "worth", "good", "great", "no cost", "best", "happy", "awesome", "nice", "comfortable", "easier", "better", "drop", "free of charge"]


for l in rev_text:
    if any(w in l for w in Import_Message) and any(w in l for w in Negative_Import):
        print 'Import-Negative'
    elif any(w in l for w in Import_Message) and any(w in l for w in Positive_Import):
        print 'Import-Positive'
    elif any(w in l for w in Import_Message) and any(w in l for w in Partial_Import):
        print 'Import-Partial'
    elif any(w in l for w in Download_Message) and any(w in l for w in Negative_Download):
        print 'Download-Negative'
    elif any(w in l for w in Download_Message) and any(w in l for w in Positive_Download):
        print 'Download-Positive'
    elif any(w in l for w in Install_Message) and any(w in l for w in Negative_Install):
        print 'Install-Negative'
    elif any(w in l for w in Install_Message) and any(w in l for w in Positive_Install):
        print 'Install-Positive'
    elif any(w in l for w in Price_Message) and any(w in l for w in Negative_Price):
        print 'Price-Negative'
    elif any(w in l for w in Price_Message) and any(w in l for w in Positive_Price):
        print 'Price-Positive'
    else:
        print 'Other-Message'

#iterates the content of the Verbatim (rev_text) using a for loop
'''
    #print any(l in k for l in One_Run) #This ll return True or False based on the keywords' presence in Verbatim
    #if any(l in k for l in Run_One) and not any(l in k for l in Extras_NoBall) and not any(l in k for l in Extras_Bye) and not any(l in k for l in Extras_LegBye):
    if any(l in k2 for l in BBMP_Road_Damage):
        print >> fw,"{}|BBMP|Road|Damage|{}|{}|{}".format(k0, k3, k7, k8)
    elif any(l in k2 for l in BBMP_Road_Pothole):
        print >> fw,"{}|BBMP|Road|Pothole|{}|{}|{}".format(k0, k3, k7, k8)
    elif any(l in k2 for l in BBMP_Road_Encroachment):
        print >> fw,"{}|BBMP|Road|Encroachment|{}|{}|{}".format(k0, k3, k7, k8)
    elif any(l in k2 for l in BBMP_Road_RoadMaintenance):
        print >> fw,"{}|BBMP|Road|Maintenance|{}|{}|{}".format(k0, k3, k7, k8)
    elif any(l in k2 for l in BBMP_Animals_StrayAnimals):
        print >> fw,"{}|BBMP|Animals|StrayAnimal|{}|{}|{}".format(k0, k3, k7, k8)
    elif any(l in k2 for l in BBMP_Cleanliness_Garbage):
        print >> fw,"{}|BBMP|Cleanliness|Garbage|{}|{}|{}".format(k0, k3, k7, k8)
    elif any(l in k2 for l in BTP_Traffic_TrafficJam):
        print >> fw,"{}|BTP|Traffic|TrafficJam|{}|{}|{}".format(k0, k3, k7, k8)
    elif any(l in k2 for l in BTP_Violation_Traffic):
        print >> fw,"{}|BTP|Violation|Traffic|{}|{}|{}".format(k0, k3, k7, k8)
    elif any(l in k2 for l in BTP_Violation_Parking):
        print >> fw,"{}|BTP|Violation|Parking|{}|{}|{}".format(k0, k3, k7, k8)
    elif any(l in k2 for l in BESCOM_Electricity_PowerOutage):
        print >> fw,"{}|BESCOM|Electricity|PowerOutage|{}|{}|{}".format(k0, k3, k7, k8)
    elif any(l in k2 for l in BESCOM_Infrastructure_Maintenance):
        print >> fw,"{}|BESCOM|Infrastructure|Maintenance|{}|{}|{}".format(k0, k3, k7, k8)
    elif any(l in k2 for l in BESCOM_Lights_Streelight):
        print >> fw,"{}|BESCOM|Lights|Streelight|{}|{}|{}".format(k0, k3, k7, k8)
    elif any(l in k2 for l in BMTC_Experience_RudeBehavior):
        print >> fw,"{}|BMTC|Experience|RudeBehavior|{}|{}|{}".format(k0, k3, k7, k8)
    elif any(l in k2 for l in BMTC_Infrastructure_BusShelter):
        print >> fw,"{}|BMTC|Infrastructure|BusShelter|{}|{}|{}".format(k0, k3, k7, k8)
    elif any(l in k2 for l in BMTC_Buses_MoreBuses):
        print >> fw,"{}|BMTC|Buses|MoreBuses|{}|{}|{}".format(k0, k3, k7, k8)
    elif any(l in k2 for l in BMTC_Others_Other):
        print >> fw,"{}|BMTC|Others|Other|{}|{}|{}".format(k0, k3, k7, k8)
    elif any(l in k2 for l in BWSSB_Water_Problem):
        print >> fw,"{}|BWSSB|Water|Problem|{}|{}|{}".format(k0, k3, k7, k8)
    elif any(l in k2 for l in BWSSB_Sewage_Problem):
        print >> fw,"{}|BWSSB|Sewage|Problem|{}|{}|{}".format(k0, k3, k7, k8)
    elif any(l in k2 for l in KSPCB_Pollution_Air):
        print >> fw,"{}|KSPCB|Pollution|Air|{}|{}|{}".format(k0, k3, k7, k8)
    elif any(l in k2 for l in KSPCB_Pollution_Noise):
        print >> fw,"{}|KSPCB|Pollution|Water|{}|{}|{}".format(k0, k3, k7, k8)
    else:
        print >> fw,"{}|Other|Other|Other|{}|{}|{}".format(k0, k3, k7, k8)
'''

'''
    if any(l in k2 for l in BBMP_Road_Damage):
        print >> fw,"{}|BBMP|Road|Damage|{}|{}|{}".format(k0, k3, k7, k8)
    elif any(l in k2 for l in BBMP_Road_Pothole):
        print >> fw,"{}|BBMP|Road|Pothole|{}|{}|{}".format(k0, k3, k7, k8)
    elif any(l in k2 for l in BBMP_Road_Encroachment):
        print >> fw,"{}|BBMP|Road|Encroachment|{}|{}|{}".format(k0, k3, k7, k8)
    elif any(l in k2 for l in BBMP_Road_RoadMaintenance):
        print >> fw,"{}|BBMP|Road|Maintenance|{}|{}|{}".format(k0, k3, k7, k8)
    elif any(l in k2 for l in BBMP_Animals_StrayAnimals):
        print >> fw,"{}|BBMP|Animals|StrayAnimal|{}|{}|{}".format(k0, k3, k7, k8)
    elif any(l in k2 for l in BBMP_Cleanliness_Garbage):
        print >> fw,"{}|BBMP|Cleanliness|Garbage|{}|{}|{}".format(k0, k3, k7, k8)
    elif any(l in k2 for l in BTP_Traffic_TrafficJam):
        print >> fw,"{}|BTP|Traffic|TrafficJam|{}|{}|{}".format(k0, k3, k7, k8)
    elif any(l in k2 for l in BTP_Violation_Traffic):
        print >> fw,"{}|BTP|Violation|Traffic|{}|{}|{}".format(k0, k3, k7, k8)
    elif any(l in k2 for l in BTP_Violation_Parking):
        print >> fw,"{}|BTP|Violation|Parking|{}|{}|{}".format(k0, k3, k7, k8)
    elif any(l in k2 for l in BESCOM_Electricity_PowerOutage):
        print >> fw,"{}|BESCOM|Electricity|PowerOutage|{}|{}|{}".format(k0, k3, k7, k8)
    elif any(l in k2 for l in BESCOM_Infrastructure_Maintenance):
        print >> fw,"{}|BESCOM|Infrastructure|Maintenance|{}|{}|{}".format(k0, k3, k7, k8)
    elif any(l in k2 for l in BESCOM_Lights_Streelight):
        print >> fw,"{}|BESCOM|Lights|Streelight|{}|{}|{}".format(k0, k3, k7, k8)
    elif any(l in k2 for l in BMTC_Experience_RudeBehavior):
        print >> fw,"{}|BMTC|Experience|RudeBehavior|{}|{}|{}".format(k0, k3, k7, k8)
    elif any(l in k2 for l in BMTC_Infrastructure_BusShelter):
        print >> fw,"{}|BMTC|Infrastructure|BusShelter|{}|{}|{}".format(k0, k3, k7, k8)
    elif any(l in k2 for l in BMTC_Buses_MoreBuses):
        print >> fw,"{}|BMTC|Buses|MoreBuses|{}|{}|{}".format(k0, k3, k7, k8)
    elif any(l in k2 for l in BMTC_Others_Other):
        print >> fw,"{}|BMTC|Others|Other|{}|{}|{}".format(k0, k3, k7, k8)
    else:
        print >> fw,"{}|Other|Other|Other|{}|{}|{}".format(k0, k3, k7, k8)
'''


