# Apostila: Curso Introdutório de Java

> Esta apostila faz parte do projeto **DevKickStart** e tem como objetivo ensinar os conceitos básicos da linguagem Java para iniciantes. Aqui você encontrará teoria detalhada, exemplos comentados, práticas e exercícios que te ajudarão a iniciar sua jornada na programação orientada a objetos.

---

## Índice

- [Apostila: Curso Introdutório de Java](#apostila-curso-introdutório-de-java)
  - [Índice](#índice)
  - [1. Introdução ao Java](#1-introdução-ao-java)
  - [2. Instalação e configuração do ambiente](#2-instalação-e-configuração-do-ambiente)
    - [Passo 1: Baixar o Java](#passo-1-baixar-o-java)
    - [Passo 2: Verificar a instalação](#passo-2-verificar-a-instalação)
    - [Passo 3: Escolher uma IDE](#passo-3-escolher-uma-ide)
  - [3. Primeiros passos com Java](#3-primeiros-passos-com-java)
    - [Seu primeiro programa](#seu-primeiro-programa)
    - [Executando o programa:](#executando-o-programa)
  - [4. Tipos de dados](#4-tipos-de-dados)
    - [Tipos primitivos](#tipos-primitivos)
  - [5. Variáveis e operadores](#5-variáveis-e-operadores)
    - [Variáveis](#variáveis)
    - [Operadores](#operadores)
  - [6. Estruturas condicionais](#6-estruturas-condicionais)
    - [Switch](#switch)
  - [7. Estruturas de repetição](#7-estruturas-de-repetição)
    - [For](#for)
    - [While](#while)
    - [Do...While](#dowhile)
  - [8. Métodos (funções em Java)](#8-métodos-funções-em-java)
    - [Método sem retorno](#método-sem-retorno)
    - [Método com retorno e parâmetros](#método-com-retorno-e-parâmetros)
    - [Chamando métodos](#chamando-métodos)
  - [9. Classes e objetos](#9-classes-e-objetos)
    - [Classe](#classe)
    - [Criando objetos](#criando-objetos)
  - [10. Boas práticas e dicas](#10-boas-práticas-e-dicas)
  - [11. Exercícios propostos](#11-exercícios-propostos)
  - [12. Fontes recomendadas](#12-fontes-recomendadas)
    - [Créditos](#créditos)

---

## 1. Introdução ao Java

O **Java** é uma linguagem de programação **orientada a objetos**, criada pela **Sun Microsystems** em 1995 (hoje pertencente à Oracle).  
É uma linguagem **compilada e interpretada**, conhecida por seu lema:

> “**Escreva uma vez, execute em qualquer lugar**.”

Isso é possível porque o Java usa a **JVM (Java Virtual Machine)**, que permite executar o mesmo código em diferentes sistemas operacionais.

Java é usado em:

- Desenvolvimento **Web** (Spring, Jakarta EE)
- Aplicações **Desktop**
- **Android**
- Sistemas corporativos
- **Back-end** e **microserviços**

---

## 2. Instalação e configuração do ambiente

### Passo 1: Baixar o Java
Acesse o site oficial da Oracle:  
👉 [https://www.oracle.com/java/technologies/downloads/](https://www.oracle.com/java/technologies/downloads/)

Baixe e instale o **JDK (Java Development Kit)**.

### Passo 2: Verificar a instalação
Abra o terminal e digite:

```bash
java -version
```

Saída esperada:
```
java version "17.0.10"
```

### Passo 3: Escolher uma IDE
- **VS Code** → leve e fácil de usar  
- **IntelliJ IDEA** → IDE mais completa para Java  
- **Eclipse** → tradicional e popular no ensino  

---

## 3. Primeiros passos com Java

### Seu primeiro programa

Crie um arquivo `HelloWorld.java`:

```java
public class HelloWorld {
    public static void main(String[] args) {
        System.out.println("Olá, mundo!");
    }
}
```

### Executando o programa:

```bash
javac HelloWorld.java   # Compila o código
java HelloWorld         # Executa o programa
```

Explicação:
- `javac` → compilador Java (gera o bytecode `.class`)
- `java` → executa o bytecode na JVM

---

## 4. Tipos de dados

Java é **fortemente tipada**, ou seja, toda variável precisa declarar seu tipo.

### Tipos primitivos

| Tipo     | Tamanho | Exemplo     |
|-----------|----------|-------------|
| `byte`    | 1 byte   | -128 a 127  |
| `short`   | 2 bytes  | -32.768 a 32.767 |
| `int`     | 4 bytes  | 10, 200, 5000 |
| `long`    | 8 bytes  | 1000000000L |
| `float`   | 4 bytes  | 3.14f |
| `double`  | 8 bytes  | 3.14159 |
| `char`    | 2 bytes  | 'A' |
| `boolean` | 1 bit    | true / false |

Exemplo:

```java
int idade = 21;
double altura = 1.75;
char genero = 'M';
boolean ativo = true;
```

---

## 5. Variáveis e operadores

### Variáveis

```java
String nome = "Nikollas";
int ano = 2025;
```

### Operadores

**Aritméticos:**  
`+`, `-`, `*`, `/`, `%`

```java
int a = 10;
int b = 5;
System.out.println(a + b); // 15
```

**Relacionais:**  
`==`, `!=`, `>`, `<`, `>=`, `<=`

**Lógicos:**  
`&&`, `||`, `!`

```java
boolean maiorDeIdade = idade >= 18 && ativo;
```

---

## 6. Estruturas condicionais

```java
int idade = 17;

if (idade >= 18) {
    System.out.println("Maior de idade");
} else {
    System.out.println("Menor de idade");
}
```

### Switch
```java
int dia = 3;
switch (dia) {
    case 1 -> System.out.println("Domingo");
    case 2 -> System.out.println("Segunda");
    default -> System.out.println("Outro dia");
}
```

---

## 7. Estruturas de repetição

### For
```java
for (int i = 0; i < 5; i++) {
    System.out.println(i);
}
```

### While
```java
int i = 0;
while (i < 5) {
    System.out.println(i);
    i++;
}
```

### Do...While
```java
int x = 0;
do {
    System.out.println(x);
    x++;
} while (x < 3);
```

---

## 8. Métodos (funções em Java)

### Método sem retorno
```java
public static void saudacao() {
    System.out.println("Bem-vindo!");
}
```

### Método com retorno e parâmetros
```java
public static int somar(int a, int b) {
    return a + b;
}
```

### Chamando métodos
```java
int resultado = somar(5, 3);
System.out.println(resultado);
```

---

## 9. Classes e objetos

### Classe
```java
public class Pessoa {
    String nome;
    int idade;

    void apresentar() {
        System.out.println("Olá, meu nome é " + nome + " e tenho " + idade + " anos.");
    }
}
```

### Criando objetos
```java
public class Main {
    public static void main(String[] args) {
        Pessoa p1 = new Pessoa();
        p1.nome = "Ana";
        p1.idade = 22;
        p1.apresentar();
    }
}
```

---

## 10. Boas práticas e dicas

- Nomeie classes com inicial maiúscula (`Pessoa`, `Carro`)  
- Métodos e variáveis com inicial minúscula (`andar()`, `velocidade`)  
- Sempre use **nomes significativos**  
- Comente partes importantes do código  
- Separe código em métodos e classes pequenas  

---

## 11. Exercícios propostos

1. Crie um programa que exiba “Olá, Java!”.  
2. Faça um programa que leia dois números e exiba a soma.  
3. Crie uma classe `Carro` com atributos `modelo`, `ano` e um método `exibirInfo()`.  
4. Escreva um programa que verifique se um número é par ou ímpar.  
5. Crie uma função que calcule o fatorial de um número.  

---

## 12. Fontes recomendadas

- [Documentação Oficial da Oracle](https://docs.oracle.com/en/java/)
- [W3Schools - Java](https://www.w3schools.com/java/)
- [Curso em Vídeo - Java POO](https://youtube.com/playlist?list=PLHz_AreHm4dmGuLII3tsvryMMD7VgcT7x)
- [DevMedia - Fundamentos de Java](https://www.devmedia.com.br/)
- [GeeksForGeeks - Java Basics](https://www.geeksforgeeks.org/java/)

---

### Créditos

- Apostila desenvolvida por [@imnikollasdev](https://github.com/imnikollasdev)
- Projeto: **DevKickStart**

---

> *Fim da apostila de Java - Módulo introdutório*
