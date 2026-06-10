# Automação de Inicialização do Windows

Script em Python para automatizar tarefas iniciais no Windows, abrindo sites e aplicativos automaticamente após o login do usuário.

## Funcionalidades

- Aguarda alguns segundos para o Windows terminar de carregar;
- Abre links configurados no navegador padrão;
- Abre o WhatsApp Desktop;
- Pode ser colocado na pasta de inicialização do Windows.

## Tecnologias utilizadas

- Python
- webbrowser
- subprocess
- time

## Como funciona

O script possui uma lista de links configuráveis:

```python
LINKS = [
    "https://www.google.com",
    "https://your-email-provider.com"
]
```

Ao executar o arquivo, ele aguarda o tempo definido em `STARTUP_DELAY`, abre os links no navegador padrão e depois tenta abrir o WhatsApp Desktop.

## Como executar

No terminal, execute:

```bash
python startup_automation.py
```

## Como iniciar junto com o Windows

1. Pressione `Win + R`;
2. Digite:

```text
shell:startup
```

3. Pressione Enter;
4. Coloque um atalho do arquivo `startup_automation.py` dentro da pasta aberta.

Assim, o script será executado automaticamente quando o Windows iniciar.

## Segurança

Não coloque senhas, links internos de empresas ou dados pessoais em repositórios públicos.

## Autor

Lucas Bonatto
