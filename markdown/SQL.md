#  SQL

## SELECT

```
SELECT 列名称 FROM 表名称
```

```
SELECT * FROM 表名称
```

## SELECT DISTINCT

```
SELECT DISTINCT 列名称 FROM 表名称
```

结果中去除重复的

## WHERE

```
SELECT 列名称 FROM 表名称 WHERE 列 运算符 值
```

| 运算符     | 描述     |
| ------- | ------ |
| =       | 等于     |
| <>      | 不等于    |
| >       | 大于     |
| <       | 小于     |
| >=      | 大于等于   |
| <=      | 小于等于   |
| BETWEEN | 在某个范围内 |
| LIKE    | 搜索某种模式 |

```
SELECT * FROM Persons WHERE City='Beijing'
```

```
SELECT * FROM Persons WHERE Year>1965
```

## AND & OR

```
SELECT * FROM Persons WHERE FirstName='Thomas' AND LastName='Carter'
```

```
SELECT * FROM Persons WHERE (FirstName='Thomas' OR FirstName='William') AND LastName='Carter'
```

## ORDER BY

```
SELECT Company, OrderNumber FROM Orders ORDER BY Company
```

结果以Company升序显示

```
SELECT Company, OrderNumber FROM Orders ORDER BY Company, OrderNumber
```

结果以Company升序显示，在Company相同时以OrderNumber升序显示

```
SELECT Company, OrderNumber FROM Orders ORDER BY Company DESC, OrderNumber ASC
```

DESC逆序，ASC正序

## INSERT INTO

```
INSERT INTO 表名称 VALUES (值1, 值2,....)
```

```
INSERT INTO table_name (列1, 列2,...) VALUES (值1, 值2,....)
```

## Update 

```
UPDATE 表名称 SET 列名称 = 新值 WHERE 列名称 = 某值
```

更新某一行中的一个列
```
UPDATE Person SET FirstName = 'Fred' WHERE LastName = 'Wilson' 
```
更新某一行中的若干列

```
UPDATE Person SET Address = 'Zhongshan 23', City = 'Nanjing'
WHERE LastName = 'Wilson'
```

## DELETE 

```
DELETE FROM 表名称 WHERE 列名称 = 值
```

删除某行

```
DELETE FROM Person WHERE LastName = 'Wilson' 
```

删除所有行

```
DELETE FROM table_name
DELETE * FROM table_name
```

## TOP 

并非所有的数据库系统都支持 TOP 子句。

MySQL 

```
SELECT column_name(s)
FROM table_name
LIMIT number
```

```
SELECT *
FROM Persons
LIMIT 5
```

## LIKE 

```
SELECT column_name(s)
FROM table_name
WHERE column_name LIKE pattern
```

## 原始的表 (用在例子中的)：

Persons 表:

| Id   | LastName | FirstName | Address        | City     |
| ---- | -------- | --------- | -------------- | -------- |
| 1    | Adams    | John      | Oxford Street  | London   |
| 2    | Bush     | George    | Fifth Avenue   | New York |
| 3    | Carter   | Thomas    | Changan Street | Beijing  |

## LIKE 操作符实例

**例子 1**

现在，我们希望从上面的 "Persons" 表中选取居住在以 "N" 开始的城市里的人：

我们可以使用下面的 SELECT 语句：

```
SELECT * FROM Persons
WHERE City LIKE 'N%'
```

提示："%" 可用于定义通配符（模式中缺少的字母）。

结果集：

| Id   | LastName | FirstName | Address      | City     |
| ---- | -------- | --------- | ------------ | -------- |
| 2    | Bush     | George    | Fifth Avenue | New York |

**例子 2**

接下来，我们希望从 "Persons" 表中选取居住在以 "g" 结尾的城市里的人：

我们可以使用下面的 SELECT 语句：

```
SELECT * FROM Persons
WHERE City LIKE '%g'
```

结果集：

| Id   | LastName | FirstName | Address        | City    |
| ---- | -------- | --------- | -------------- | ------- |
| 3    | Carter   | Thomas    | Changan Street | Beijing |

**例子 3**

接下来，我们希望从 "Persons" 表中选取居住在包含 "lon" 的城市里的人：

我们可以使用下面的 SELECT 语句：

```
SELECT * FROM Persons
WHERE City LIKE '%lon%'
```

结果集：

| Id   | LastName | FirstName | Address       | City   |
| ---- | -------- | --------- | ------------- | ------ |
| 1    | Adams    | John      | Oxford Street | London |

**例子 4**

通过使用 NOT 关键字，我们可以从 "Persons" 表中选取居住在*不包含* "lon" 的城市里的人：

我们可以使用下面的 SELECT 语句：

```
SELECT * FROM Persons
WHERE City NOT LIKE '%lon%'
```

结果集：

| Id   | LastName | FirstName | Address        | City     |
| ---- | -------- | --------- | -------------- | -------- |
| 2    | Bush     | George    | Fifth Avenue   | New York |
| 3    | Carter   | Thomas    | Changan Street | Beijing  |

| 通配符                      | 描述            |
| ------------------------ | ------------- |
| %                        | 替代一个或多个字符     |
| _                        | 仅替代一个字符       |
| [charlist]               | 字符列中的任何单一字符   |
| [^charlist]或者[!charlist] | 不在字符列中的任何单一字符 |

从上面的 "Persons" 表中选取居住的城市以 "A" 或 "L" 或 "N" 开头的人：

```
SELECT * FROM Persons
WHERE City LIKE '[ALN]%'
```

从上面的 "Persons" 表中选取居住的城市*不以* "A" 或 "L" 或 "N" 开头的人：

```
SELECT * FROM Persons
WHERE City LIKE '[!ALN]%'
```

## IN 

```
SELECT column_name(s)
FROM table_name
WHERE column_name IN (value1,value2,...)
```

希望从表中选取姓氏为 Adams 和 Carter 的人：

```
SELECT * FROM Persons
WHERE LastName IN ('Adams','Carter')
```

## BETWEEN 

```
SELECT column_name(s)
FROM table_name
WHERE column_name
BETWEEN value1 AND value2
```

以字母顺序显示介于 "Adams"（包括）和 "Carter"（不包括）之间的人，请使用下面的 SQL：

```
SELECT * FROM Persons
WHERE LastName
BETWEEN 'Adams' AND 'Carter'
```

不同的数据库对 BETWEEN...AND 操作符的处理方式是有差异的。某些数据库会列出介于 "Adams" 和 "Carter" 之间的人，但不包括 "Adams" 和 "Carter" ；某些数据库会列出介于 "Adams" 和 "Carter" 之间并包括 "Adams" 和 "Carter" 的人；而另一些数据库会列出介于 "Adams" 和 "Carter" 之间的人，包括 "Adams" ，但不包括 "Carter" 。

## Alias（别名）

表的 SQL Alias 语法

```
SELECT column_name(s)
FROM table_name
AS alias_name
```

列的 SQL Alias 语法

```
SELECT column_name AS alias_name
FROM table_name
```