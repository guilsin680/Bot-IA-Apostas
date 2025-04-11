import os
import requests

def enviar_telegram(mensagem):
    bot_token = os.getenv("TELEGRAM_BOT_TOKEN")
    chat_id = os.getenv("TELEGRAM_CHAT_ID")

    if bot_token and chat_id:
        url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
        payload = {"chat_id": chat_id, "text": mensagem}
        requests.post(url, data=payload)
    else:
        print("❌ Variáveis de ambiente do Telegram não configuradas.")
date,home_team,away_team,home_goals,away_goals,result
2024-04-01,Barcelona,Real Madrid,2,1,Home
2024-04-02,Liverpool,Man City,1,3,Away
2024-04-03,Bayern Munich,Dortmund,2,2,Draw
2024-04-04,PSG,Marseille,3,0,Home
2024-04-05,Juventus,Milan,1,1,Draw
2024-04-06,Arsenal,Chelsea,2,2,Draw
2024-04-07,Roma,Napoli,1,2,Away
2024-04-08,Atletico Madrid,Sevilla,3,1,Home
