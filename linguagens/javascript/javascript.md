# Apostila: Curso Introdutório de JavaScript

> Esta apostila faz parte do projeto **DevKickStart** e tem como objetivo ensinar os conceitos básicos da linguagem JavaScript para iniciantes. Aqui você encontrará teoria detalhada, exemplos comentados, práticas e exercícios que te ajudarão a iniciar sua jornada na programação web.

---

## Índice

- [Apostila: Curso Introdutório de JavaScript](#apostila-curso-introdutório-de-javascript)
  - [Índice](#índice)
  - [1. Introdução ao JavaScript](#1-introdução-ao-javascript)
  - [2. Instalação e ambiente de desenvolvimento](#2-instalação-e-ambiente-de-desenvolvimento)
    - [Testando no navegador](#testando-no-navegador)
    - [Instalando o Node.js](#instalando-o-nodejs)
    - [IDEs recomendadas](#ides-recomendadas)
  - [3. Primeiros passos com JavaScript](#3-primeiros-passos-com-javascript)
    - [Seu primeiro programa](#seu-primeiro-programa)
    - [Comentários](#comentários)
  - [4. Tipos de dados](#4-tipos-de-dados)
  - [5. Variáveis e operadores](#5-variáveis-e-operadores)
    - [Declaração de variáveis](#declaração-de-variáveis)
    - [Operadores](#operadores)
  - [6. Estruturas condicionais](#6-estruturas-condicionais)
  - [7. Estruturas de repetição](#7-estruturas-de-repetição)
    - [For](#for)
    - [While](#while)
    - [For...of](#forof)
  - [8. Funções](#8-funções)
    - [Função tradicional](#função-tradicional)
    - [Função com parâmetros e retorno](#função-com-parâmetros-e-retorno)
    - [Arrow Function](#arrow-function)
  - [9. Arrays e objetos](#9-arrays-e-objetos)
    - [Arrays](#arrays)
    - [Objetos](#objetos)
  - [10. Boas práticas e dicas](#10-boas-práticas-e-dicas)
  - [11. Exercícios propostos](#11-exercícios-propostos)
  - [12. Fontes recomendadas](#12-fontes-recomendadas)
    - [Créditos](#créditos)

---

## 1. Introdução ao JavaScript

O **JavaScript** é uma linguagem de programação **interpretada** e **dinamicamente tipada**, criada em **1995** por **Brendan Eich**.  
Ela é a **linguagem padrão da Web**, sendo executada diretamente nos navegadores, e também utilizada no **back-end** com o **Node.js**.

Hoje, o JavaScript é uma das linguagens mais populares do mundo, usada para:

- **Desenvolvimento Web** (Front-end e Back-end)
- **Aplicações Mobile** (React Native, Ionic)
- **Aplicações Desktop** (Electron, Tauri)
- **Automação e scripts**
- **Jogos e WebApps interativos**

Sua principal característica é a **flexibilidade**: o mesmo código pode rodar no navegador ou em um servidor.

---

## 2. Instalação e ambiente de desenvolvimento

### Testando no navegador

Você pode usar o **console** do navegador para executar código JS:

1. Abra o **Google Chrome** ou **Firefox**
2. Pressione `F12` → vá em **Console**
3. Digite:
   ```js
   console.log("Olá, mundo!");
   ```

### Instalando o Node.js

Para rodar JS fora do navegador:

1. Acesse [nodejs.org](https://nodejs.org)
2. Baixe a versão LTS (recomendada)
3. Após instalar, teste no terminal:
   ```bash
   node -v
   ```
   Se aparecer algo como `v20.10.0`, deu certo ✅

### IDEs recomendadas

- **VS Code** → Leve e com suporte a extensões JS  
- **WebStorm** → Completa, da JetBrains  
- **StackBlitz** ou **CodePen** → Ideias rápidas online  

---

## 3. Primeiros passos com JavaScript

### Seu primeiro programa

```js
console.log("Olá, mundo!");
```

> `console.log()` é usado para exibir mensagens no console (semelhante ao `print()` do Python).

### Comentários

```js
// Comentário de uma linha

/*
Comentário
de múltiplas linhas
*/
```

---

## 4. Tipos de dados

JavaScript possui **tipagem dinâmica**, ou seja, o tipo é definido automaticamente quando o valor é atribuído.

Tipos primitivos principais:

- **String** → textos  
- **Number** → números inteiros ou decimais  
- **Boolean** → verdadeiro ou falso  
- **Undefined** → variável declarada sem valor  
- **Null** → ausência de valor  
- **Object** → coleções de dados  
- **Array** → listas ordenadas  

Exemplo:

```js
let nome = "João";       // String
let idade = 25;          // Number
let ativo = true;        // Boolean
let lista = [1, 2, 3];   // Array
let pessoa = { nome: "Ana", idade: 30 }; // Objeto
```

Conversões:

```js
Number("10");    // string -> number
String(20);      // number -> string
Boolean(0);      // false
Boolean(1);      // true
```

---

## 5. Variáveis e operadores

### Declaração de variáveis

- `var` → escopo global (evite)
- `let` → escopo de bloco
- `const` → valor constante

```js
let nome = "Lucas";
const PI = 3.14;
```

### Operadores

1. **Aritméticos**  
   `+`, `-`, `*`, `/`, `%`, `**`
   ```js
   let soma = 10 + 5; // 15
   ```

2. **Comparação**  
   `==`, `===`, `!=`, `!==`, `>`, `<`, `>=`, `<=`
   ```js
   5 == "5";  // true (compara valor)
   5 === "5"; // false (compara tipo e valor)
   ```

3. **Lógicos**  
   `&&`, `||`, `!`
   ```js
   let maior = idade >= 18 && ativo === true;
   ```

---

## 6. Estruturas condicionais

```js
let idade = 20;

if (idade >= 18) {
  console.log("Maior de idade");
} else if (idade >= 12) {
  console.log("Adolescente");
} else {
  console.log("Criança");
}
```

Ternário:
```js
let acesso = idade >= 18 ? "Permitido" : "Negado";
```

---

## 7. Estruturas de repetição

### For
```js
for (let i = 0; i < 5; i++) {
  console.log(i);
}
```

### While
```js
let contador = 0;
while (contador < 5) {
  console.log(contador);
  contador++;
}
```

### For...of
```js
let frutas = ["maçã", "banana", "uva"];
for (let fruta of frutas) {
  console.log(fruta);
}
```

---

## 8. Funções

### Função tradicional
```js
function saudacao() {
  console.log("Bem-vindo!");
}
```

### Função com parâmetros e retorno
```js
function soma(a, b) {
  return a + b;
}
```

### Arrow Function
```js
const multiplica = (a, b) => a * b;
```

---

## 9. Arrays e objetos

### Arrays
```js
let frutas = ["maçã", "banana", "laranja"];
frutas.push("morango");  // adiciona
frutas.pop();            // remove o último
console.log(frutas.length); // tamanho
```

### Objetos
```js
let pessoa = {
  nome: "Ana",
  idade: 30,
  saudacao() {
    console.log(`Olá, meu nome é ${this.nome}`);
  }
};
pessoa.saudacao();
```

---

## 10. Boas práticas e dicas

- Prefira `let` e `const` em vez de `var`.  
- Nomeie variáveis e funções de forma descritiva.  
- Sempre use `===` ao comparar valores.  
- Evite códigos repetidos; use funções.  
- Use `console.log()` para depurar.  
- Organize seu código em módulos (quando possível).  

---

## 11. Exercícios propostos

1. Crie um programa que receba um nome e exiba “Olá, [nome]!”.  
2. Crie uma função que some dois números.  
3. Faça um contador que vá de 1 a 10.  
4. Crie um objeto representando uma pessoa e exiba seus dados.  
5. Faça um programa que pergunte a idade e diga se o usuário é maior ou menor de idade.

---

## 12. Fontes recomendadas

- [Documentação oficial - MDN Web Docs](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript)
- [W3Schools - JavaScript](https://www.w3schools.com/js/)
- [Curso em Vídeo - JavaScript](https://youtube.com/playlist?list=PLHz_AreHm4dlsK3Nr9GVvXCbpQyHQl1o1)
- [JavaScript.info](https://javascript.info/)
- [FreeCodeCamp - JavaScript Basics](https://www.freecodecamp.org/learn/javascript-algorithms-and-data-structures/)

---

### Créditos

- Apostila desenvolvida por [@imnikollasdev](https://github.com/imnikollasdev)
- Projeto: **DevKickStart**

---

> *Fim da apostila de JavaScript - Módulo introdutório*
