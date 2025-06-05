# Gerar a versão em HTML com DataTables (paginada e interativa)
html_interativo = """
<!DOCTYPE html>
<html lang="pt">
<head>
    <meta charset="UTF-8">
    <title>Vocabulário Irregular ES-PT</title>
    <link rel="stylesheet" type="text/css"
          href="https://cdn.datatables.net/1.13.4/css/jquery.dataTables.min.css">
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <script type="text/javascript"
            src="https://cdn.datatables.net/1.13.4/js/jquery.dataTables.min.js"></script>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 2em;
        }
        table {
            width: 100%;
        }
    </style>
</head>
<body>
    <h1>Vocabulário Irregular Espanhol-Português</h1>
    <p>Lista de palavras cuja tradução não é dedutível por regras sistemáticas.</p>
    <table id="vocabulario" class="display">
        <thead>
            <tr>
                <th>Espanhol</th>
                <th>Português</th>
            </tr>
        </thead>
        <tbody>
"""

# Adicionar dados à tabela
for _, row in df_irregulares_22.iterrows():
    html_interativo += f"<tr><td>{row['es']}</td><td>{row['pt']}</td></tr>\n"

# Finalizar HTML
html_interativo += """
        </tbody>
    </table>
    <script>
        $(document).ready(function() {
            $('#vocabulario').DataTable({
                "pageLength": 25,
                "language": {
                    "url": "//cdn.datatables.net/plug-ins/1.13.4/i18n/pt-BR.json"
                }
            });
        });
    </script>
</body>
</html>
"""

# Salvar arquivo HTML
html_table_path = "/mnt/data/vocabulario_es_pt_interativo.html"
with open(html_table_path, "w", encoding="utf-8") as f:
    f.write(html_interativo)

html_table_path
