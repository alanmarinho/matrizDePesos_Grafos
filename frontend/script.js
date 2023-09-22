document.addEventListener('DOMContentLoaded', function () {
  function solicitarDados(nomeArquivo) {
    return fetch(`/api/matriz?arquivo=${nomeArquivo}`)
    .then(response => response.json())
    .then(data => {
      return data.matriz_ponderada;
    })
    .catch(error => {
      console.error('Erro ao solicitar dados:', error);
      throw error;
    });
  }

  function criarTabela(matriz) {
    let tabela = document.getElementById('table');
    tabela.innerHTML = '';

    let table = document.createElement('table');
    let thead = document.createElement('thead');
    let tbody = document.createElement('tbody');
    table.appendChild(thead);
    table.appendChild(tbody);

    let row = document.createElement('tr');
    for (let i = 0; i <= matriz.length; i++) {
      if (i == 0) {
        let data = document.createElement('th');
        data.innerHTML = ' ';
        row.appendChild(data);
      } else {
        let data = document.createElement('th');
        data.innerHTML = i;
        row.appendChild(data);
      }

    }
    thead.appendChild(row);

    for (let i = 0; i < matriz.length; i++) {
      let row = document.createElement('tr');
      let rowNum = i + 1;
      let data = document.createElement('td');
      data.innerHTML = rowNum;
      row.appendChild(data);

      for (let j = 0; j < matriz[i].length; j++) {
        let data = document.createElement('td');
        data.innerHTML = matriz[i][j];
        row.appendChild(data);
      }
      tbody.appendChild(row);
    }

    tabela.appendChild(table);
  }

  document.getElementById('submit').addEventListener('click', function(event) {
    event.preventDefault();
    const dropdown = document.getElementById('dropdown');
    const nomeArquivo = dropdown.value;
    solicitarDados(nomeArquivo).then(criarTabela);
  });
 
});