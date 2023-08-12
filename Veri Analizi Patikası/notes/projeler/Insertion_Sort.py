# 1. Soru [22,27,16,2,18,6] -> Insertion Sort

- 22 > 27 zaten sıralı dolayısıyla yer değiştirmez.
22, 27, 16, 2, 18, 6

- 27 > 16 olduğundan yer değiştirirler.
22, 16, 27*, 2, 18, 6 
Solundaki sayılarla karşılaştıracağımız için burada işlem henüz bitmedi.
22 > 16 dolayısıyla:
16, 22, 27*, 2, 18, 6 

- 27 > 2 olduğundan yer değiştirirler
16, 22, 2, 27*, 18, 6
22 > 2
16, 2, 22, 27*, 18, 6
ve 16 > 2 olduğundan
2, 16, 22, 27*, 18, 6

- 18 sayısını kıyaslamaya devam ediyoruz.
27 > 18 olduğudan
2, 16, 22, 18, 27*, 6
22 > 18 olduğundan
2, 16, 18, 22, 27*, 6
16 < 18 olduğundan yer değişikliği olmaz.

- Son elemanı kıyaslamaya geçiyoruz.
27 > 6:
2, 16, 18, 22, 6, 27*
22 > 6:
2, 16, 18, 6, 22, 27*
18 > 6:
2, 16, 6, 18, 22, 27*
16 > 6:
2, 6, 16, 18, 22, 17*
2 < 6 yani yer değişikliği yok.

Algoritma tamamlandı ve dizinin son hali: [2, 6, 16, 18, 22, 27]

# Soru-2 Big-O gösterimini yazınız.

Insertion Sort'un çalışma mantığı şu şekildedir:
Algoritma, listenin sıralı kısmını adım adım büyütürken, her elemanı sıralı kısmın içine yerleştirir.
Her elemanı sıralı kısma yerleştirirken, bu elemanın doğru pozisyonunu bulmak için sıralı kısmı tarar. 
Bu işlem her eleman için yapılır ve eleman sayısı arttıkça taranan sıralı kısım da artar. 
Bu nedenle, en kötü durumda (örneğin, tersten sıralı bir liste) her elemanı yerine yerleştirmek 
için sıralı kısımın tamamını tararız ve bu durumun karmaşıklığı O(n^2) olur.

# Soru-3:
# Time Complexity: Dizi sıralandıktan sonra 18 sayısı aşağıdaki case'lerden hangisinin kapsamına girer?

# Average case: Aradığımız sayının ortada olması
# Worst case: Aradığımız sayının sonda olması
# Best case: Aradığımız sayının dizinin en başında olması.

Average case: Aradığımız sayının ortada olması

# Soru-4: 
# [7,3,5,8,2,9,4,15,6] dizisinin Selection Sort'a göre ilk 4 adımını yazınız.

Selection Sort, bir dizi içerisindeki elemanları genellikle küçükten büyüğe doğru 
sıralayan bir sıralama algoritmasıdır. 
Temel mantığı, her adımda dizideki en küçük elemanı bulup, onu sıralanmış bölümün sonuna yerleştirmektir.

- Dizideki en küçük eleman bulunup baştaki sayı ile değiştirilir:
2* 3, 5, 8, 7, 9, 4, 15, 6

- Kalanlar arasından en küçük bulunur. Burada en küçük 3 olduğu için ve başta olduğu için
değişiklik yok
2, 3* 5, 8, 7, 9, 4, 15, 6

- En küçük eleman 4 dolayısıyla 5 ile yer değiştirir:
2, 3, 4* 8, 7, 9, 5, 15, 6

- En küçük eleman 5 ile 8 sayısı yer değiştirir:
2, 3, 4, 5* 7, 9, 8, 15, 6