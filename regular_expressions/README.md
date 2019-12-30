### REGEX 

## What is regular expressions 

    Це символи які відображають текстовий шаблон і дозволяють нам
    порівнювати, шукати і заміняти текст
 
## Where we could find it 

    Мови програмування
    Текстові редактори
    Утиліти для терміналу
    Мобільні аплікухи
    
    
## Flags

    global -> знаходить всі входження тексту
    case sensitive -> великі і маленькі букви еквівалентні
    multiline ->
    
    
## Literal Characters

    Raw text
    
    
## Metacharacters

    . -> любий символ
     
## Escaping 

    \ -> використовується для того, щоб нівелювати дію метасимволу
    
## Characters

    \t -> таб
    \n -> перенос строки

    \d ->  всі цифри
    \w -> всі букви цифри і '_'
    \s -> пробіли, знаки табуляції, перенос строки
    
    \D -> не цифра
    \W -> не буква не цифра не '_'
    \S -> не символ табуляції, не перенос строки, не пробіл.
    
## Ranges 

    [] -> любий символ в любому порядку з наведених в скобках
    [ - ] -> можна вказати рендж між символами
        [a-z][1-9]
    Negation
    [^a] -> любий символ крім а

## Repetitions 

    * -> Люба кількість
    ? -> Або 0 або 1
    + -> Принаймні 1
    {n} -> Рівно n символів
    {0,} -> 0 і більше
    {n, m} -> від n до m
    
## Grouping 
    () -> обєднання кількох символів в один обєкт, який можна порахувати 
        recognize or unrecognize this is a question
        (un)?recognize
        
## Alternation

    | -> Або або (еквівалентно до правила OR в Python)
        super|market
        super(market|bowl)
        
        supermarket should has superbowl inside
        
        
## Anchors

    ^ ->  Початок строки
    $ ->  Кінець строки
    \b ->  Має знаходитися в кінці строки або на початку
    \B ->  Не Має знаходитися на початку чи в кінці строки
    
    
## Backreferences / Capturing
 
    \1 -> Має відповідати першій групі яка була знайдена в тексті
    (a|b) \1
    
    (?:name) -> ігнорувати групу входження символів name
    (?=,) -> шукати тільки входження груп які закінчуються на `,`
    
## Useful links

Регулярні вирази. Як їх використовувати в Python
https://www.educative.io/edpresso/how-to-use-regex-in-python?affiliate_id=5082902844932096&utm_source=google&utm_medium=cpc&utm_campaign=platform2&utm_content=ad-1-dynamic&gclid=CjwKCAjw8-LnBRAyEiwA6eUMGubDs_KNWp_g0IgAqT0W-z-1U1hF1slwob0Bfa7mF-ulIA5rTLmBOBoCmrIQAvD_BwE

Набір задачок для того, щоб себе перевірити
https://www.hackerrank.com/challenges/matching-anything-but-new-line/problem

Онлайн консоль для запуску регулярних виразів
https://regex101.com/

Символи групування
https://www.rexegg.com/regex-quickstart.html
https://docs.microsoft.com/en-us/dotnet/standard/base-types/regular-expression-language-quick-reference

Кросворд regex для тренування і фану
https://regexcrossword.com/