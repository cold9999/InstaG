import bs4, requests, lxml

def get_lun(year,mon,day):
  if mon < 10:
    mon = f"0{mon}"
  if day < 10:
    day = f"0{day}"
  data_html = requests.get(f"https://pangok.hs.kr/?_page=64&_action=view&_view=view&yy={year}&mm={mon}&dd={day}").text
  #text = driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/div/div[2]/div/div[3]/div/div/div/div[3]/div[2]/div[3]/dl/dd").text
  return text
print(get_lun(2023,8,18))