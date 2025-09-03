# Melhorias pro fastjson-db #

## Sistema de Hashing ##

Para facilitar criação e armazenamento de senhas

## Sistema para Textos Longos ##

Tipo TEXT type do SQLite

## Importação Correta de Foreign Key ##

Por enquanto tem que importar assim:

```py
from fastjson-db.foreignkey import ForeignKey
```

O que é desagradável considerando que ForeignKey é o único módulo naquele arquivo.

## Nullable e Unique ##

Garantir novos fields (nullable e unique, pra evitar que tenham dois usuários com mesmo nome por exemplo)
