# -*- coding: utf-8 -*-

# @Time    : 2021/9/3 9:23 下午 
# @Author  : cyq
# @File    : Mobiles.py
import random


class Mobiles:
    l = ['18888888888', '15012345678', '17354309484', '15066666666', '15055555555', '15500000001',
         '15500000004', '15500000005', '18500000001', '18500000002', '18500000003', '18500000004',
         '18500000005', '18500000006', '18500000007', '13500000001', '13500000002', '13500000003',
         '13500000004', '13500000006', '13500000007', '13500000008', '13500000009', '13500000010',
         '15511111111', '15522222222', '15533333333', '15533333334', '13600000001', '13600000003',
         '13600000002', '13600000005', '13600000006', '13600000007', '13600000008', '13600000009',
         '13600000010', '13600000011', '13600000012', '18800000001', '18800000002', '18800000003',
         '18800000004', '18800000005', '18800000006', '18800000007', '18800000008', '18800000009',
         '13600000004', '13600000013', '13600000014', '13600000015', '13600000016', '13600000017',
         '13600000018', '13600000019', '13600000020', '13600000021', '13600000022', '13600000023',
         '13600000024', '13600000025', '13600000026', '13600000027', '13600000028', '13600000029',
         '13600000030', '13600000031', '13600000032', '13600000033', '13600000034', '13600000035',
         '13600000036', '13600000037', '13600000038', '13600000039', '13600000040']

    def get_one(self):
        a = random.choice(self.l)
        return a