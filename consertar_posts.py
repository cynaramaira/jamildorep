import os
import re

# Pasta onde estão os posts
pasta_posts = "_posts"

# Função para corrigir o front matter YAML
def corrigir_front_matter(arquivo):
    with open(arquivo, 'r', encoding='utf-8') as f:
        conteudo = f.read()

    # Verifica se o YAML do início está correto
    if not conteudo.startswith("---"):
        print(f"🚨 Corrigindo front matter em: {arquivo}")
        
        # Adiciona o front matter correto
        titulo = os.path.basename(arquivo).split("-", 3)[-1].replace(".md", "").replace("-", " ").title()
        novo_yaml = f"---\nlayout: post\ntitle: \"{titulo}\"\ndate: {arquivo.split('/')[-1][:10]}\n---\n"
        conteudo = novo_yaml + conteudo
    
    # Salvar correção
    with open(arquivo, 'w', encoding='utf-8') as f:
        f.write(conteudo)

# Percorrer todos os arquivos Markdown
for nome_arquivo in os.listdir(pasta_posts):
    caminho_arquivo = os.path.join(pasta_posts, nome_arquivo)

    if caminho_arquivo.endswith(".md"):
        corrigir_front_matter(caminho_arquivo)

print("✅ Todos os posts foram verificados e corrigidos!")