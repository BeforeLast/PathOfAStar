# A* Pathing
> Implementasi Algoritma A* untuk Menentukan Lintasan Terpendek

## Table of contents
* [General info](#general-info)
* [Setup](#setup)
* [Features](#features)
* [Status](#status)
* [Author](#author)

## General info
Algoritma A* adalah algoritma yang mencari jalur dalam suatu graf dengan diberikannya node awal dan node tujuan. Algoritma ini akan menghasilkan jalur terdekat yang dihitung berdasarkan _cost_ yang diimplementasi dengan rumus _f(n) = g(n) + h(n)_ dengan _g(n)_ adalah jarak dari node awal sampai node ke n dan _h(n)_ adalah perkiraan jarak dari node ke n sampai node tujuan.

## Setup
1. Pastikan semua library eksternal sudah terinstall, yang meliputi _Flask_
2. Pindah ke direktori src dari project ini
3. Masukkan perintah <code>python main.py</code> ke terminal
4. Tunggu sampai _Flask_ selesai berjalan dan buka link _localhost_ yang muncul
5. Pada halaman web, ketik nama dari test file yang akan digunakan, seperti _test1.txt_
6. Pilih nama lokasi awal dan tujuan dari dropdown yang telah ada
7. Klik tombol _Find Route_
8. Jalur yang dihitung dengan Algoritma A* akan muncul ditandai dengan garis hijau

## Features
Berikut adalah fitur-fitur yang terdapat dalam program.
* Menampilkan graf diberikannya file input eksternal
* Mencari jalur dengan algoritma A* dari suatu graf
* Menampilkan jalur, beserta jarak totalnya, ke layar

## Status
Project is: _finished_

## Author
Christopher Chandrasaputra - 13519074
Billy Julius - 13519094
