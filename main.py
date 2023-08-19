import instagrapi
import PIL
import os
import requests
import datetime
import pytz
import re
from PIL import Image, ImageDraw, ImageFont

neis_request_uid = "d3d340be73e647bba088ab388ff5f0cc"

weekdays = ["월요일","화요일","수요일","목요일","금요일","토요일","일요일"]

KST = pytz.timezone('Asia/Seoul')
r_time = datetime.datetime.now(KST)
r_year = r_time.year
r_month = r_time.month
r_day = r_time.day
r_sdt = r_time.weekday()

text = "칼슘찹쌀현미밥 돈육김치찌개59.10.13. 순대채소볶음5.6.10.13. 크림소스떡볶음 1.25.6.13. 진미채볶음4.5.6.13.17. 깍두기9.13. 티라미수케이크 125.6.13."
"""
def getl():
  get_neis = requests.get(
      f"https://open.neis.go.kr/hub/schoolInfo?Type=json&SCHUL_NM=판곡고등학교&KEY={neis_request_uid}"
  ).json()
  school_uid = get_neis["schoolInfo"][1]["row"][0]["SD_SCHUL_CODE"]
  edu_code = get_neis["schoolInfo"][1]["row"][0]["ATPT_OFCDC_SC_CODE"]
  school_uname = get_neis["schoolInfo"][1]["row"][0]["SCHUL_NM"]
  #get lunch list
  a_date = None
  r_year = 0
  r_month = 0
  r_day = 0
  KST = pytz.timezone('Asia/Seoul')
  r_time = datetime.datetime.now(KST)
  r_year = r_time.year
  if r_time.month <= 9:
    r_month = "0" + str(r_time.month)
  else:
    r_month = r_time.month
  r_day = r_time.day
  r_int = f"{r_year}{r_month}{r_day}"
  a_date = r_int
  print(
      f"https://open.neis.go.kr/hub/mealServiceDietInfo?Type=json&KEY={neis_request_uid}&ATPT_OFCDC_SC_CODE={edu_code}&SD_SCHUL_CODE={school_uid}&MLSV_YMD={a_date}"
  )
  get_lunch = requests.get(
      f"https://open.neis.go.kr/hub/mealServiceDietInfo?Type=json&KEY={neis_request_uid}&ATPT_OFCDC_SC_CODE={edu_code}&SD_SCHUL_CODE={school_uid}&MLSV_YMD={a_date}"
  ).json()
  print(get_lunch)
  lunch_list = get_lunch["mealServiceDietInfo"][1]["row"][0]["DDISH_NM"]
  lunch_text = lunch_list.replace("<br/>", "\n")
  return lunch_text
text = getl()

#나이스 4세대 업그레이드로 인해 급식 정보가 6월 16일 이후로 올라오지 않음(조만간 해소될것 같음)
"""
refine_t = re.sub("[0-9]", "", text)
refine_t = refine_t.replace(".", "")
menu_list = refine_t.split(" ")

wid, hei = (1080, 1350)
basic_image = Image.open("basic.jpg")
BMfont = ImageFont.truetype("BMJUA.ttf", 100)
mefont = ImageFont.truetype("BMJUA.ttf", 90)
fw, fh = BMfont.getsize(f"{r_month}월 {r_day}일 {weekdays[r_sdt]} 급식")
drawImage = ImageDraw.Draw(basic_image)
drawImage.text((int(wid / 2) - fw / 2, 150),
               f"{r_month}월 {r_day}일 {weekdays[r_sdt]} 급식",
               fill="white",
               font=BMfont,
               align="center")
start_num = 400
menu_list = [menu for menu in menu_list if menu != ""]
for menu in menu_list:
  fw2, fh2 = mefont.getsize(menu)
  drawImage.text((int(wid / 2) - fw2 / 2, start_num),
                 menu,
                 fill="white",
                 font=mefont,
                 align="center")
  start_num += 100
drawImage.rectangle([(180,340),(900,start_num+60)],outline="white",width=5)
basic_image.save("test.jpg")
"""
client = instagrapi.Client()
client.login("hcm_0920","hcm0920*")
client.photo_upload("test.jpg",f"판곡고등학교 {r_year}년 {r_month}월 {r_day}일 {weekdays[r_sdt]} 급식")
"""
