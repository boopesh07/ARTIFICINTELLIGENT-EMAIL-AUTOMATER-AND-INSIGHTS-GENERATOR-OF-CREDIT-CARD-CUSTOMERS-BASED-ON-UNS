import yagmail
import csv

#receiver = "s.boopesh@gmail.com"
body = "<html><h1>Hello there from Key Bank USA </h1><br><h2> Test mail from Boopesh AI Advertiser </h2> </html>"
filename = "cluster 1.csv"

yag = yagmail.SMTP(user='artificial.bank.advertiser@gmail.com',password="Thalaboo@007")
with open("cluster 1.csv") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for name, email in reader:
            yag.send(to=email,subject="Yagmail test with attachment",contents=body, attachments=filename)
"""For the manager mail which should attach all the cluster files
   make a list of files """         



