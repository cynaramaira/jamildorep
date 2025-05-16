import json
import os
import re

# Carregar o arquivo JSON corretamente
with open('C:/Users/User/Documents/acervo/meu-site/data/json_2000.json', 'r', encoding='utf-8') as file:
    noticias = json.load(file)["rows"]

# Criar a pasta _posts se não existir
os.makedirs("_posts", exist_ok=True)

# Função para remover tags HTML do conteúdo (mantendo acentos e caracteres especiais)
def remover_html(texto):
    return re.sub(r'<.*?>', '', texto)

# Função para limpar caracteres proibidos apenas no nome do arquivo
def limpar_nome_arquivo(titulo):
    titulo_limpo = re.sub(r'[\/:*?"<>|]', '-', titulo.replace(' ', '-').lower())
    titulo_limpo = titulo_limpo.replace("\t", "").replace("\n", "").strip()  # Remove caracteres invisíveis
    return titulo_limpo

# Criar um post para cada notícia
for noticia in noticias:
    try:
        # Extrair apenas a data sem o horário
        data_formatada = noticia["data_publicacao"].split(" ")[0]

        # Gerar nome do arquivo limpo (com substituições seguras)
        nome_arquivo = f"_posts/{data_formatada}-{limpar_nome_arquivo(noticia['titulo'])}.md"

        # Verificar se o arquivo já existe
        if os.path.exists(nome_arquivo):
            print(f"⚠ Post já existe, pulando: {nome_arquivo}")
            continue  # Pula a criação deste arquivo

        # Criar e escrever o conteúdo do post (preservando caracteres especiais)
        with open(nome_arquivo, 'w', encoding='utf-8') as f:
            f.write(f"---\nlayout: post\ntitle: \"{noticia['titulo']}\"\ndate: {data_formatada}\ntags: {noticia['materia_tags']}\nauthor: {noticia['autor']}\n---\n")
            f.write(remover_html(noticia['conteudo']))  # Mantém caracteres especiais no texto

        print(f"✔ Post criado: {nome_arquivo}")

    except KeyError as e:
        print(f"❌ Erro ao processar notícia: Campo ausente - {e}")

print("✅ Todos os posts foram gerados com sucesso!")