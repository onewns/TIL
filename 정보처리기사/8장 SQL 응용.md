# 8장 SQL 응용



## Section 072 C SQL - DDL



## Section 073 C SQL - DCL



## Section 074 B SQL - DML(Data Manipulation Language)

> 저장된 데이터를 실질적으로 관리하는데 사용되는 언어



### 삽입문(INSERT INTO~)

> 기본 테이블에 새로운 튜플을 삽일할 때 사용

```sql
INSERT INTO 테이블명([속성명1, 속성명2])
VALUES (데이터1, 데이터2);
```

- 대응하는 속성과 데이터는 개수와 데이터 유형이 일치해야 함
- 기본 테이블의 모든 속성을 사용할 때는 속성명을 생략 가능
- SELECT문을 사용하여 다른 테이블의 검색결과를 삽입 가능



### 삭제문(DELETE FROM~)

> 기본 테이블에 있는 튜플들 중에서 특정 튜플(행)을 삭제할 때 사용

```sql
DELETE
FROM 테이블명
[WHERE 조건]; #모든레코드 삭제시 WHERE절 생략
```

- 모든 레코드를 삭제하더라고 테이블 구조는 남아있음 => DROP과의 차이점



### 갱신문(UPDATE ~ SET ~)

> 특정 튜플의 내용을 변경할 때 사용

```sql
UPDATE 테이블명
SET 속성명 = 데이터 , 속성명 = 데이터, 
[WHERE 조건];
```



### 기출 따라잡기

| 번호 | 내답                                                         | 정답                                                         | 비고                                                         |
| ---- | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 1    | INSERT INTO '학생' <br />VALUES (<br />98170823, <br />'한국산',<br /> 3,<br /> '경영학개론', <br />'?-1234-1234'<br />); | INSERT INTO 학생<br />VALUES (<br />98170823, <br />'한국산',<br /> 3,<br /> '경영학개론', <br />'?-1234-1234'<br />); | 테이블에는 '' 붙이는거 아님                                  |
| 2    | DELETE FROM '학생'                                           | DELETE FROM 학생<br />WHERE 이름 = 'scott';                  | 속성명은 '' 붙이는거 아님                                    |
| 3    | SET WHERE                                                    |                                                              |                                                              |
| 4    | FROM '학과번호' =                                            | SET 학과번호 LIKE                                            | 속성명은 '' 붙이는거 아님<br />% 같은거 쓸떄는 LIKE<br />UPDATE 테이블<br />SET 속성명 = 데이터<br />WHERE 조건 |
| 5    | INSERT INTO '기획부'<br />SELECT ['성명', '경력', '주소', '기본급'] FROM '사원' <br />WHERE '부서' = '기획' | INSERT INTO 기획부('성명', '경력', '주소', '기본급') <br />SELECT 성명, 경력, 주소, 기본급<br />FROM 사원<br />WHERE 부서 = '기획' |                                                              |



## Section 075, 076 A DML - SELECT - 1, 2

```sql
SELECT [PREDICATE] [테이블명.]속성명 [AS 별칭]
[,그룹합수(속성명) [AS 별칭]]
[, Window 함수 OVER (PARTITION BY 속성명1, 속성명2,
					ORDER BY 속성명3, 속성명4 )]
FROM 테이블명1, 테이블명2, 
[WHERE 조건]
[GROUP BY 속성명, 속성명]
[HAVING 조건]
[ORDER BY 속성명 [ASC | DESC]];
```

### SELECT절

- PREDICATE : 불러올 튜플 수를 제한할 명령어를 기술
  - ALL : 모든 튜플을 검색할 때 지정, 주로 생략
  - DISTINCT : 중복된 튜플이 있으면 그 중 첫번쨰 한 개만 검색
  - DISTINCTROW : 중복된 튜플을 제거하고 한 개만 검색, 선택된 속성의 값이 아닌 튜플 전체를 대상
- 속성명: 검색하여 불러올 속성 또는 속성을 이용한 수식을 지정
  - 모든 속성 지정시에는 *
  - 두 개 이상의 테이블을 대상으로 검색 시 에는 테이블명.속성명 으로 표현
- AS : 속성 및 연산의 이름을 다른 제목으로 표시하기 위해 사용



### 그룹함수

- GROUP BY 절에 지정된 그룹별로 속성의 값을 집계할 함수를 기술

  | 종류                   | 기능                                                         |
  | ---------------------- | ------------------------------------------------------------ |
  | COUNT(속성명)          | 그룹별 튜플 수를 구하는 함수                                 |
  | SUM(속성명)            | 그룹별로 함계를 구하는 함수                                  |
  | AVG()                  |                                                              |
  | MAX()                  |                                                              |
  | MIN()                  |                                                              |
  | STDDEV(속성명)         | 그룹별 표준편차를 구하는 함수                                |
  | VARIANCE(속성명)       | 그룹별 분산을 구하는 함수                                    |
  | ROLLUP(속성명, 속성명) | 인수로 주어진 속성을 대상으로 그룹별 소계를 하는 함수<br />속성의 개수가 n개 이면 n+1레벨까지 하위에서 상위 순으로 데이터 집계 |
  | CUBE(속성명, 속성명)   | ROLLUP과 유사한 형태이나 인수로 주어진 속성을 대상으로 모든 조합의 그룹별 소계를 구함<br />상위 레벨에서 하위 레벨 순으로 데이터가 집계 |



### WINDOW 함수

- GROUP BY 절을 이용하지 않고 속성의 값을 집계할 함수를 기술

  - PARTITION BY: WINDOW함수가 적용될 범위로 사용할 속성을 지정

  - ORDER BY: PARTITION 안에서 정렬 기준으로 사용할 속성을 지정

    | 종류         | 기능                                                         |
    | ------------ | ------------------------------------------------------------ |
    | ROW_NUMBER() | 윈도우별로 각 레코드에 대한 일련 번호를 반환                 |
    | RANK()       | 윈도우별로 순위를 반환하며, 공동 순위를 반영                 |
    | DENSE_RANK() | 윈도우별로 순위를 반환하며, 공동 순위를 무시하고 순위를 부여함 |



### FROM 절

- 질의에 의해 검색될 데이터들을 포함하는 테이블 명을 기술



### WHERE 절 

- 검색할 조건을 기술

- 조건 연산자

  - 비교 연산자
    - **`=, <>`** : 같다, 같지 않다.
    - **`>, <`**: 크다 , 작다
    - **`>=, <=`**: 크거나 같다, 작거나 같다
  - 논리 연산자 : NOT, AND, OR
  - LIKE 연산자 : 대표 문자를 이용해 지정된 속성의 값이 문자 패턴과 일치하는 튜플을 검색하기 위해 사용
    - **`%`** : 모든 문자를 대표함
    - **`_`** : 문자 하나를 대표함
    - **`#`** : 숫자 하나를 대표함

- 연산자 우선순위

  | 종류        | 연산자              | 우선순위                          |
  | ----------- | ------------------- | --------------------------------- |
  | 산술 연산자 | X , /, + , -        | 왼쪽에서 오른쪽으로 갈수록 낮아짐 |
  | 관계 연산자 | =, <>, >, >=, <, <= | 모두 같음                         |
  | 논리 연산자 | NOT, AND, OR        | 왼쪽에서 오른쪽으로 갈수록 낮아짐 |



##### 하위 질의

> 조건절에 주어진 질의를 먼저 수행하여 그 검색 결과를 조건절의 피연산자로 사용



### GROUP BY절

- 특정 속성을 기준으로 그룹화하여 검색할 때 사용, 일반적으로 그룹함수와 함께 사용



### HAVING절

- GROUP BY와 함께 사용되며, 그룹에 대한 조건을 지정



### ORDER BY 절

- 특정 속성을 기준으로 정렬하여 검색할 때 사용
- 속성명 : 정렬의 기준이 되는 속성명을 기술
- ASC | DESC : 오름차순, 내림차순 지정  생략시 => ASC





### 075 기출 따라잡기

| 번호 | 내답                                                         | 정답                                                         | 비고        |
| ---- | ------------------------------------------------------------ | ------------------------------------------------------------ | ----------- |
| 1    | 기말성적 DESC                                                | 기말성적 DESC, 중간성적 (ASC)                                |             |
| 2    | SELECT 학번,이름 FROM 학생<br />WHERE 학년 In(3,4);          | SELECT 학번, 이름<br />FROM 학생<br />WHERE 학년 IN (3,4);   |             |
| 3    | SELECT 이름 FROM Shop<br />WHERE id = (SELECT DISTINCT shopid FROM staff WHERE id = 10); | SELECT DISTINCT name<br />FROM Shop<br />WHERE id IN (SELECT shopid FROM Staff WHER id = 10); |             |
| 4    | SELECT name FROM Product<br />WHERE price = 'NULL'<br />ORDER BY name; | SELECT name<br />FROM Product<br />WHERE price IS NULL<br />ORDER BY name; |             |
| 5    | SELECT pid FROM Sale<br />WHERE psale >= 10 AND psale <= 20; | SELECT pid<br />FROM Sale<br />WHERE psale BETWEEN 10 AND 20; | 틀린건 아님 |
| 6    | SELECT 학생정보.학번, 학생정보.이름, 결제.결제여부<br />FROM  학생정보, 결제<br />WHERE | SELECT 학생정보.학번,이름,결제여부<br />FROM 학생정보, 신청정보, 결제<br />WHERE 학생정보.학번 = 신청정보.학번<br />AND 신청정보.신청번호 = 결제.신청번호<br />AND 신청과목 = 'OpenGL' |             |
| 7    | SELECT DISTINCTROW 과목 FROM 학생<br />WHERE 학년 >= 3 AND 점수 >= 80; | SELECT DISTINCT 과목<br />FROM 학생<br />WHERE 학년 >= 3 AND 점수 >= 80; |             |
| 8    | 연락번호 <> 'Null'                                           | 연락번호 IS NOT NULL                                         |             |
| 9    | 1: SELECT ID, NAME FROM CUSTOMER;<br />2: SELECT DISTINCTROW GRADE FROM CUSTOMER;<br />3: SELECT * FROM CUSTOMER ORDER BY ID DESC;<br />4: SELECT NAME FROM CUSTOMER WHERE AGE = 'NULL';<br />5: SELECT NAME FROM CUSTOMER WHERE AGE <> 'NULL'; | 2: SELECT DISTINCT GRADE FROM CUSTOMER;<br />4: SELECT NAME FROM CUSTOMER WHERE AGE IS NULL<br />5: SELECT NAME FROM CUSTOMER WHERE AGE IS NOT NULL<br /> |             |



### 076 기출 따라잡기

| 번호 | 내답                                                         | 정답                                                         | 비고 |
| ---- | ------------------------------------------------------------ | ------------------------------------------------------------ | ---- |
| 1    | SELECT 이름, 전공, 신청과목<br />FROM 학생정보, 신청정보<br />GROUP BY (이름, 전공, 신청과목)<br />WHERE 테이블.학번 = 신청정보.학번 <br />AND신청과목 = 'Java'<br />HAVING 전공 = '컴퓨터공학' | SELECT 이름, 전공, 신청과목<br />FROM 학생정보, 신청정보<br />WHERE 학생정보.학번 = 신청정보.학번<br />                 AND 신청과목 = 'Java'<br />GROUP BY 이름, 전공, 신청과목<br />HAVING 전공 = '컴퓨터공학' |      |
| 2    | SELECT 결제여부, COUNT(*) AS '학생수'<br />FROM 결제<br />GROUP BY 결제여부 |                                                              |      |
| 3    | SELECT SUM(psale)<br />FROM Sale<br />GROUP BY psale<br />WHERE pid IN (<br />SELECT id FROM Product WHERE name LIKE USB%); | SELECT SUM(psale)<br />FROM Sale<br />WHERE pid IN (<br />SELECT id FROM Product WHERE name LIKE 'USB%'); |      |
| 4    | 1: 매출액 > 1000<br />2: 소속도시<br />3: 3                  |                                                              |      |
| 5    | 1: 장학내역<br />2: 장학금<br />3: 'NUM'                     | 1: 장학내역<br />2: 장학금<br />3: NUM                       |      |
| 6    | 1: 학과<br />2: 장학내역<br />3: SUM(장학금)                 |                                                              |      |

