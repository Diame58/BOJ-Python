# [Silver I] Ten - 23247 

[문제 링크](https://www.acmicpc.net/problem/23247) 

### 성능 요약

메모리: 113392 KB, 시간: 312 ms

### 분류

브루트포스 알고리즘, 누적 합

### 제출 일자

2025년 10월 8일 21:11:38

### 문제 설명

<p>A real estate company IC is managing a rectangular section of land. The section is divided into $mn$ segments in $m \times n$ matrix shape, where the number of rows and that of columns are $m$ and $n$, respectively. Each segment has its own price as a positive integer. IC wants to sell a rectangular subsection of the land, but the price of the subsection should be ten. The price of a subsection is simply the sum of the prices of the segments in the subsection. Since there can be several such subsections, IC wants to identify the number of candidate subsections to sell. Write a program to help IC, counting the number of candidate subsections of the land.</p>

<p>For example, the prices of segments of the land having $5 \times 7$ segments are given as follows:</p>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/51bd1cc5-373e-4aa0-a8f8-ed208e043047/-/preview/" style="width: 355px; height: 124px;"></p>

<p>We can find four candidate subsections to sell marked by rectangles: the first one consists of four segments in the first and the second rows spanning over from the second to the third columns, the second, six segments in the second and the third rows spanning over from the third to the fifth columns, the third, two segments in the first row spanning over from the fifth to the sixth columns, and the fourth, three segments in the seventh column spanning over from the third to the fifth rows. Therefore, your program should report four for the above input.</p>

### 입력 

 <p>Your program is to read from standard input. The input starts with two positive integers $m$ and $n$ ($1 \le m, n \le 300$), denoting the dimensions of the land, which are given separated by a space. Each of the following $m$ lines contains $n$ positive integers $p_{ij}$ representing the prices of the segments of the $i$-th row of the land ($1 \le i \le m$, $1 \le j \le n$, and $1 \le p_{ij} \le 10$). The prices are also separated by a space.</p>

### 출력 

 <p>Your program is to write to standard output. Print exactly one line containing an integer representing the number of rectangular subsections with the price of ten.</p>

