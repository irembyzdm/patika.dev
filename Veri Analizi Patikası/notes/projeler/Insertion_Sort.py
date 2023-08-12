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