# Bot Discord para Render (Worker)

## Passos para rodar

1. Coloque `main.py` e `requirements.txt` no repositório GitHub.
2. Crie um **Worker** no Render, conectando este repositório.
3. Configure:
   - **Runtime:** Python 3.11
   - **Start Command:** python main.py
4. Adicione variáveis de ambiente:
   - TOKEN → token do bot
   - GUILD_ID → ID do servidor
   - CHANNEL_ID → ID do canal
   - ROLE_ID → ID do cargo [FALA BAIXO NENGUE]
5. Faça deploy e o bot rodará 24/7.
6. Teste no Discord com `!teste Mensagem de Teste`.
