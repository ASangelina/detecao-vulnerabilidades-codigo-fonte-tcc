# Métricas de CK e sua Utilidade na Identificação de Código Vulnerável

## Métricas de CK

1. **CBO (Coupling Between Object classes)**: Mede o número de classes às quais uma classe está acoplada. Um alto acoplamento indica que a classe depende de muitas outras classes.

2. **CBO Modified**: Similar ao CBO, mas com algumas modificações específicas na forma de cálculo.

3. **Fan-In**: Número de outras classes que dependem dos métodos desta classe. Mede a reutilização de métodos.

4. **Fan-Out**: Número de outras classes de que a classe depende. Reflete o grau de dependência externa.

5. **WMC (Weighted Methods per Class)**: Soma dos pesos de todos os métodos de uma classe. Normalmente, o peso é a complexidade ciclomática de cada método.

6. **DIT (Depth of Inheritance Tree)**: Mede a profundidade da árvore de herança. Quanto maior a DIT, maior a complexidade da herança.

7. **NOC (Number of Children)**: Número de classes filhas que herdam da classe. Alto NOC indica maior reutilização de classe e maior responsabilidade.

8. **RFC (Response For a Class)**: Número de métodos que podem ser potencialmente executados em resposta a uma mensagem recebida por um objeto desta classe.

9. **LCOM (Lack of Cohesion of Methods)**: Mede a falta de coesão dos métodos de uma classe. Altos valores indicam que a classe realiza muitas operações não relacionadas.

10. **LCOM\***: Variante do LCOM, ajustada para lidar melhor com algumas situações específicas de coesão.

11. **TCC (Tight Class Cohesion)**: Mede a coesão de uma classe como a razão entre o número de pares de métodos que compartilham atributos e o número total de pares de métodos.

12. **LCC (Loose Class Cohesion)**: Variante da coesão da classe que mede uma forma mais relaxada de coesão em comparação ao TCC.

13. **totalMethodsQty**: Número total de métodos na classe.

14. **staticMethodsQty**: Número de métodos estáticos na classe.

15. **publicMethodsQty**: Número de métodos públicos na classe.

16. **privateMethodsQty**: Número de métodos privados na classe.

17. **protectedMethodsQty**: Número de métodos protegidos na classe.

18. **defaultMethodsQty**: Número de métodos com visibilidade de pacote (default) na classe.

19. **visibleMethodsQty**: Número de métodos visíveis (públicos ou protegidos) na classe.

20. **abstractMethodsQty**: Número de métodos abstratos na classe.

21. **finalMethodsQty**: Número de métodos finais na classe.

22. **synchronizedMethodsQty**: Número de métodos sincronizados na classe.

23. **totalFieldsQty**: Número total de campos na classe.

24. **staticFieldsQty**: Número de campos estáticos na classe.

25. **publicFieldsQty**: Número de campos públicos na classe.

26. **privateFieldsQty**: Número de campos privados na classe.

27. **protectedFieldsQty**: Número de campos protegidos na classe.

28. **defaultFieldsQty**: Número de campos com visibilidade de pacote (default) na classe.

29. **finalFieldsQty**: Número de campos finais na classe.

30. **synchronizedFieldsQty**: Número de campos sincronizados na classe.

31. **nosi (Number of Static Invocations)**: Número de invocações estáticas realizadas pela classe.

32. **loc (Lines of Code)**: Número de linhas de código da classe.

33. **returnQty**: Número de instruções de retorno na classe.

34. **loopQty**: Número de loops (for, while, etc.) na classe.

35. **comparisonsQty**: Número de operações de comparação (==, !=, etc.) na classe.

36. **tryCatchQty**: Número de blocos try-catch na classe.

37. **parenthesizedExpsQty**: Número de expressões entre parênteses na classe.

38. **stringLiteralsQty**: Número de literais de string na classe.

39. **numbersQty**: Número de literais numéricos na classe.

40. **assignmentsQty**: Número de instruções de atribuição na classe.

41. **mathOperationsQty**: Número de operações matemáticas (+, -, *, /, etc.) na classe.

42. **variablesQty**: Número de variáveis declaradas na classe.

43. **maxNestedBlocksQty**: Profundidade máxima de blocos aninhados na classe.

44. **anonymousClassesQty**: Número de classes anônimas na classe.

45. **innerClassesQty**: Número de classes internas na classe.

46. **lambdasQty**: Número de expressões lambda na classe.

47. **uniqueWordsQty**: Número de palavras únicas usadas na classe.

48. **modifiers**: Modificadores de classe (public, private, etc.).

49. **logStatementsQty**: Número de instruções de log na classe.

## Utilidade para Identificação de Código Vulnerável

- **CBO**: Código com alto acoplamento tende a ser mais difícil de manter e mais propenso a erros.
- **WMC**: Classes com muitos métodos ou métodos complexos são mais difíceis de entender e testar, o que pode levar a vulnerabilidades.
- **DIT**: Uma profundidade de herança maior pode aumentar a complexidade e a probabilidade de erros de implementação.
- **RFC**: Um alto número de métodos potencialmente executáveis pode indicar maior
