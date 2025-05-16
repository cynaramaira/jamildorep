import os

pasta_posts = "_posts"
for nome in os.listdir(pasta_posts):
    if len(nome) > 100:  # Ajuste o limite se necessário
        novo_nome = nome[:90] + ".md"  # Encurta mantendo a data
        os.rename(os.path.join(pasta_posts, nome), os.path.join(pasta_posts, novo_nome))
        print(f"Renomeado: {nome} -> {novo_nome}")