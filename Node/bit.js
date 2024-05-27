// Função para imprimir a representação binária de um número
function toBinaryString(num) {
    return num.toString(2).padStart(8, '0'); // 8 bits para facilitar a visualização
}

// Exemplo de operações de manipulação de bits
let a = 5; // Representação binária: 00000101
let b = 3; // Representação binária: 00000011

// Operação AND
let resultAND = a & b; // 00000101 & 00000011 = 00000001 (1 em decimal)
console.log(`AND: ${toBinaryString(a)} & ${toBinaryString(b)} = ${toBinaryString(resultAND)} (${resultAND})`);

// Operação OR
let resultOR = a | b; // 00000101 | 00000011 = 00000111 (7 em decimal)
console.log(`OR:  ${toBinaryString(a)} | ${toBinaryString(b)} = ${toBinaryString(resultOR)} (${resultOR})`);

// Operação XOR
let resultXOR = a ^ b; // 00000101 ^ 00000011 = 00000110 (6 em decimal)
console.log(`XOR: ${toBinaryString(a)} ^ ${toBinaryString(b)} = ${toBinaryString(resultXOR)} (${resultXOR})`);

// Operação Shift Left (deslocamento para a esquerda)
let resultShiftLeft = a << 1; // 00000101 << 1 = 00001010 (10 em decimal)
console.log(`Shift Left: ${toBinaryString(a)} << 1 = ${toBinaryString(resultShiftLeft)} (${resultShiftLeft})`);

// Operação Shift Right (deslocamento para a direita)
let resultShiftRight = a >> 1; // 00000101 >> 1 = 00000010 (2 em decimal)
console.log(`Shift Right: ${toBinaryString(a)} >> 1 = ${toBinaryString(resultShiftRight)} (${resultShiftRight})`);
