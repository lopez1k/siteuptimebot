import requests
import re
from aiogram import Bot
from utils.database import DataBase as db

async def check(bot):
    conn, cur = db.connection()
    users = db.check_site()
    results = []  # Список для збереження результатів
    for user in users:
        cur.execute("SELECT pause FROM users WHERE uid = ?", (user[0],))
        pause = cur.fetchone()
        if pause[0] == 0:
            cur.execute("SELECT website FROM sites WHERE uid=?", (user[0],))
            websites = cur.fetchall()
            cur.execute("SELECT silent FROM users WHERE uid = ?", (user[0],))
            silent = cur.fetchone()
            for url in websites:
                try:
                    response = requests.get(url[0], timeout=10)  # Таймаут 10 секунд
                    if response.status_code == 200:
                        html = response.text
                        with open("a", "a", encoding="utf-8") as file:
                            file.write(f"{html}\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                        if re.search(r'wp-content', html, re.IGNORECASE):
                            print(f"✅ {url[0]} Сайт безпечний.")
                            results.append(f"✅ <code>{url[0]}</code>: <b>Сайт безпечний.</b>")

                    else:
                        print(f"⚠️ {url[0]}: Сайт недоступний. Статус код: {response.status_code}")
                        results.append(f"⚠️ {url[0]} Сайт недоступний. Статус код: {response.status_code}")
                except requests.RequestException as e:
                    print(f"⚠️ {url[0]}: Помилка запиту - {str(e)}")
                    results.append(f"⚠️ <code>{url[0]}</code>: <b>Помилка запиту</b>")
            text = f"\n"
            for r in results:
                text += f"{r}\n\n" 
            results.clear() 
            if silent[0] == 0:
                await bot.send_message(chat_id=user[0], text=text, disable_web_page_preview=True)
            elif silent[0] == 1:
                await bot.send_message(chat_id = user[0], text = text, disable_web_page_preview = True, disable_notification=True)
        


async def check_site(url):
    results = []
    try:
        response = requests.get(url, timeout=10) 
        if response.status_code == 200:
            html = response.text
            if re.search(r'wp-content', html, re.IGNORECASE):
                print(f"✅ {url} Сайт безпечний.")
                results.append(f"✅ <code>{url}</code>: <b>Сайт безпечний.</b>")

            else:
                print(f"⚠️ {url}: Сайт недоступний. Статус код: {response.status_code}")
                results.append(f"⚠️ {url} Сайт недоступний. Статус код: {response.status_code}")
        else:
                print(f"⚠️ {url}: Сайт недоступний. Статус код: {response.status_code}")
                results.append(f"⚠️ {url} Сайт недоступний. Статус код: {response.status_code}")
                               
    except requests.RequestException as e:
        print(f"⚠️ {url}: Помилка запиту - {str(e)}")
        results.append(f"⚠️ <code>{url}</code>: <b>Помилка! Можливо, ви не вірно ввели URL адресу.</b>")
    text = f"\n"
    for r in results:
        text += f"{r}\n\n" 
    results.clear() 
    return text
            
        
