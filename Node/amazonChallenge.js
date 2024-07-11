function groupStringsByCharacters(arr) {
    const map = new Map();
  
    arr.forEach(str => {
      // Ordena os caracteres da string para criar uma chave única para o mapa
      const sortedStr = str.split('').sort().join('');
      
      // Se a chave já existe no mapa, adiciona a string ao array correspondente
      if (map.has(sortedStr)) {
        map.get(sortedStr).push(str);
      } else {
        // Caso contrário, cria um novo array para essa chave
        map.set(sortedStr, [str]);
      }
    });
  
    // Retorna os valores do mapa como um array de arrays
    return Array.from(map.values());
  }
  
  // Exemplo de uso
  const input = ["124", "412", "425", "241", "524", "324", "2141"];
  const result = groupStringsByCharacters(input);
  console.log(result); // [["124", "241", "412"], ["425","524"],["324"],["2141"]]
  