html_body = """
<html>
<head>
  <style>
    table {{
      border-collapse: collapse;
      width: 100%;
    }}
    th, td {{
      border: 1px solid #dddddd;
      text-align: left;
      padding: 8px;
    }}
    th {{
      background-color: #f2f2f2;
    }}
  </style>
</head>
<body>
  <h2>Trading Signal Report</h2>
  <table>
    <tr>
      <th>Instrument</th>
      <th>Status</th>
      <th>Indicators</th>
    </tr>
    {table_rows}
  </table>
  </body>
</html>"""