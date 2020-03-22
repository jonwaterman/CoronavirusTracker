import requests
from datetime import datetime
from pytz import timezone
page = requests.get("https://ncov2019.live/data")
# f = open("corona_data.csv", "a+")

from bs4 import BeautifulSoup
soup = BeautifulSoup(page.content, "html.parser")

#   prints header information to console
print("\n\n")
print(datetime.now().astimezone(timezone("America/Chicago")))

#   prints header information to file
# f.write("\n\n")
# f.write(str(datetime.now().astimezone(timezone("America/Chicago"))))


table_data = soup.find_all("div", {"class" : "container--wrap col hide-mobile"})
for table in table_data:
    table_title = table.find("h2").text
    table_rows = table.find("tbody").find_all("tr")
    
    # prints information to console and file
    print("\n*****", table_title, "*****")
    print("REGION".ljust(35, " "), "CONFIRMED".ljust(8, " "), "DECEASED".ljust(8, " "), "RECOVERED".ljust(8, " "), "SERIOUS".ljust(8, " "), "INC_CONF".ljust(8, " "), "INC_DEAD".ljust(8, " "), sep="\t")

    # f.write("\n\n***** " + table_title + " *****")
    # f.write("\nREGION".ljust(35, " ") + "\t" + "CONFIRMED".ljust(5, " ") + "\t" + "DECEASED".ljust(5, " ") + "\t" + "RECOVERED".ljust(5, " ") + "\t" + "SERIOUS".ljust(5, " "))
    
    
    for region in table_rows:
        #try:
        print(region.find_all("td")[0].text.strip().ljust(35, "."), region.find_all("td")[1].text.strip().ljust(9, " "), region.find_all("td")[3].text.strip().ljust(9, " "), region.find_all("td")[5].text.strip().ljust(9, " "), region.find_all("td")[6].text.strip().ljust(9, " "), region.find_all("td")[2].text.strip().ljust(9, " "), region.find_all("td")[4].text.strip().ljust(9, " "), sep="\t")
        #f.write("\n" + region.find("td", {"class" : "text--gray"}).text.ljust(35, " ") + "\t" + region.find("td", {"class" : "text--green sorting_1"}).text.ljust(9, " ") + "\t" + region.find("td", {"class" : "text--red"}).text.ljust(9, " ") + "\t" + region.find("td", {"class" : "text--blue"}).text.ljust(9, " ") + "\t" + region.find("td", {"class" : "text--yellow"}).text.ljust(9, " "))
        # except AttributeError:
        #     print(region.find("td", {"class" : "text--gray"}).text.ljust(35, "."), region.find("td", {"class" : "text--green sorting_1"}).text.ljust(9, " "), region.find("td", {"class" : "text--red"}).text.ljust(9, " "), "N/A".ljust(9, " "), "N/A".ljust(9, " "), sep="\t")
        #     # f.write("\n" + region.find("td", {"class" : "text--gray"}).text.ljust(35, ".") + "\t" + region.find("td", {"class" : "text--green sorting_1"}).text.ljust(9, " ") + "\t" + region.find("td", {"class" : "text--red"}).text.ljust(9, " ") + "\t" + "N/A".ljust(9, " ") + "\t" + "N/A".ljust(9, " "))
# f.close()
# map color codes state by number of cases, not by per capita amount