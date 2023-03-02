import theater_module
theater_module.price(3) # 3명이서 영화보러 갔을때 가격
theater_module.price_morning(4) # 4명이서 조조 영화보러 갔을때 가격
theater_module.price_soldier(2) # 군인 2명이서 영화보러 갔을때 가격

import theater_module as mv
mv.price(3) # 3명이서 영화보러 갔을때 가격
mv.price_morning(4) # 4명이서 조조 영화보러 갔을때 가격
mv.price_soldier(2) # 군인 2명이서 영화보러 갔을때 가격

from theater_module import*
price(3)
price_morning(4)
price_soldier(2)

from theater_module import price, price_soldier #가져다 쓰고 싶은 함수만 가지고 올 수 있음
price(3)
price_soldier(2)