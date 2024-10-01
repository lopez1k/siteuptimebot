import requests
import re
from aiogram import Bot
from utils.database import DataBase as db

async def check(bot):
    conn, cur = db.connection()
    users = db.check_site()
    results = [] 
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    } # Список для збереження результатів
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
                    response = requests.get(url[0], timeout=10, headers=headers)  # Таймаут 10 секунд
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
            try:
                if silent[0] == 0:
                    await bot.send_message(chat_id=user[0], text=text, disable_web_page_preview=True)
                elif silent[0] == 1:
                    await bot.send_message(chat_id = user[0], text = text, disable_web_page_preview = True, disable_notification=True)
            except:
                pass


async def check_site(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    results = []
    try:
        response = requests.get(url, timeout=10, headers=headers) 
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
            
        


async def check_site_file(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    results = []
    try:
        response = requests.get(url, timeout=10, headers=headers) 
        if response.status_code == 200:
            html = response.text
            if re.search(r'wp-content', html, re.IGNORECASE):
                print(f"✅ {url} Сайт безпечний.")
                results.append(f"✅Сайт безпечний")

            else:
                print(f"⚠️ {url}: Сайт недоступний. Статус код: {response.status_code}")
                results.append(f"⚠️ Сайт недоступний. Статус код: {response.status_code}")
        else:
                print(f"⚠️ {url}: Сайт недоступний. Статус код: {response.status_code}")
                results.append(f"⚠️ Сайт недоступний. Статус код: {response.status_code}")
                               
    except requests.RequestException as e:
        print(f"⚠️ {url}: Помилка запиту - {str(e)}")
        results.append(f"⚠️Помилка! Можливо, ви не вірно ввели URL адресу")
    text = f"\n"
    for r in results:
        text += f"{r}\n\n" 
    results.clear() 
    return text
            
        
